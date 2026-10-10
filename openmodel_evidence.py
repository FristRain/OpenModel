"""Minimal opt-in evidence integrity core; no tool execution or hidden authority."""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Any, Literal

Confidence = Literal["observed", "derived", "inferred"]
Authority = Literal["source", "runtime", "test", "human-report", "analyst-inference"]

def canonical(data: Any) -> str:
    return json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False)

def seal(data: dict[str, Any]) -> dict[str, Any]:
    """Validate JSON, detach caller-owned references, and assign content-addressed identity."""
    snapshot = json.loads(canonical(data))
    if not isinstance(snapshot, dict):
        raise ValueError("Evidence must be an object")
    required = {"subject", "revision", "provider", "operation", "result", "confidence", "authority", "limitations"}
    if not required.issubset(snapshot):
        raise ValueError("Missing evidence fields: " + ", ".join(sorted(required - snapshot.keys())))
    if snapshot["confidence"] not in ("observed", "derived", "inferred"):
        raise ValueError("Unknown confidence")
    if snapshot["authority"] not in ("source", "runtime", "test", "human-report", "analyst-inference"):
        raise ValueError("Unknown authority")
    if not all(isinstance(snapshot[k], str) and snapshot[k] for k in ("subject", "revision", "provider", "operation")):
        raise ValueError("Subject, revision, provider and operation must be nonempty strings")
    if not isinstance(snapshot["limitations"], list) or not all(isinstance(x, str) for x in snapshot["limitations"]):
        raise ValueError("Limitations must be a list of strings")
    if "evidence_id" in snapshot:
        raise ValueError("Use verify() for externally supplied evidence")
    digest = hashlib.sha256(("OpenModel Evidence v1\0" + canonical(snapshot)).encode("utf-8")).hexdigest()
    return {"evidence_id": "ev_" + digest, **snapshot}

def verify(record: dict[str, Any]) -> dict[str, Any]:
    snapshot = json.loads(canonical(record))
    identity = snapshot.pop("evidence_id", None)
    if not isinstance(identity, str) or seal(snapshot)["evidence_id"] != identity:
        raise ValueError("Evidence identity mismatch")
    return {"evidence_id": identity, **snapshot}

@dataclass
class EvidenceLedger:
    """Session-local, copy-in/copy-out, idempotent store. Not a durable database."""
    _records: dict[str, str] = field(default_factory=dict)

    def add(self, record: dict[str, Any]) -> str:
        validated = verify(record)
        identity = validated["evidence_id"]
        payload = canonical(validated)
        if identity in self._records and self._records[identity] != payload:
            raise ValueError("Conflicting evidence")
        self._records[identity] = payload
        return identity

    def get(self, identity: str) -> dict[str, Any] | None:
        value = self._records.get(identity)
        return json.loads(value) if value is not None else None

    def export(self) -> list[dict[str, Any]]:
        return [json.loads(self._records[k]) for k in sorted(self._records)]

@dataclass(frozen=True)
class Claim:
    text: str
    evidence_ids: tuple[str, ...]
    falsifier: str
    scope: str

@dataclass(frozen=True)
class Verification:
    level: Literal["static", "unit", "integration", "representative-runtime", "production"]
    passed: bool
    can_express_failure: bool
    evidence_ids: tuple[str, ...]

def assess(claim: Claim, verification: Verification, ledger: EvidenceLedger) -> tuple[str, tuple[str, ...]]:
    """Return eligibility of the *stated* claim, not an automatic permission to deploy."""
    unknowns: list[str] = []
    if not claim.text or not claim.scope or not claim.falsifier:
        unknowns.append("Claim needs a scope and falsifier")
    if not claim.evidence_ids:
        unknowns.append("Claim has no supporting evidence")
    for identity in (*claim.evidence_ids, *verification.evidence_ids):
        if ledger.get(identity) is None:
            unknowns.append("Missing evidence reference: " + identity)
    if not verification.can_express_failure:
        unknowns.append("T0 failure expressibility not established")
    if not verification.passed:
        unknowns.append("Verification did not pass")
    if not verification.evidence_ids:
        unknowns.append("No verification evidence")
    return ("supported" if not unknowns else "unverified", tuple(dict.fromkeys(unknowns)))
