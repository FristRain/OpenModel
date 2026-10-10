"""Tests for evidence integrity; not a behavioral agent benchmark."""
import unittest

from openmodel_evidence import Claim, EvidenceLedger, Verification, assess, seal, verify


def sample():
    return {
        "subject": "source-file-sha256:demo",
        "revision": "commit:demo",
        "provider": "unit-test",
        "operation": "inspect",
        "result": {"latency_ms": 640},
        "confidence": "observed",
        "authority": "test",
        "limitations": ["fixture only"],
    }


class EvidenceTests(unittest.TestCase):
    def test_deterministic_id(self):
        self.assertEqual(seal(sample()), seal(dict(reversed(list(sample().items())))))

    def test_tampering_rejected(self):
        record = seal(sample())
        record["result"]["latency_ms"] = 0
        with self.assertRaises(ValueError):
            verify(record)

    def test_snapshot_isolated_from_mutation(self):
        record = seal(sample())
        ledger = EvidenceLedger()
        identity = ledger.add(record)
        record["result"]["latency_ms"] = -1
        self.assertEqual(ledger.get(identity)["result"]["latency_ms"], 640)
        got = ledger.get(identity)
        got["result"]["latency_ms"] = -2
        self.assertEqual(ledger.get(identity)["result"]["latency_ms"], 640)

    def test_missing_reference_blocks_support(self):
        ledger = EvidenceLedger()
        claim = Claim("serialization bottleneck", ("ev_missing",), "serial time negligible", "fixture")
        check = Verification("unit", True, True, ("ev_missing",))
        status, reasons = assess(claim, check, ledger)
        self.assertEqual(status, "unverified")
        self.assertTrue(any("Missing evidence" in x for x in reasons))

    def test_mock_cannot_verify_real_incident(self):
        ledger = EvidenceLedger()
        identity = ledger.add(seal(sample()))
        claim = Claim("race fixed", (identity,), "race persists under concurrency", "production")
        check = Verification("unit", True, False, (identity,))
        self.assertEqual(assess(claim, check, ledger)[0], "unverified")

    def test_verified_narrow_claim(self):
        ledger = EvidenceLedger()
        identity = ledger.add(seal(sample()))
        claim = Claim("fixture contains 640ms", (identity,), "fixture contains other value", "fixture")
        check = Verification("unit", True, True, (identity,))
        self.assertEqual(assess(claim, check, ledger)[0], "supported")

    def test_nonfinite_not_allowed(self):
        source = sample()
        source["result"] = {"value": float("nan")}
        with self.assertRaises(ValueError):
            seal(source)


if __name__ == "__main__":
    unittest.main()
