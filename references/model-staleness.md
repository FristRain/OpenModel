# Model staleness

An explanation can have been correct and no longer apply. Check when an old issue, incident, comment, user report, or previous agent answer conflicts with current evidence.

## Evidence boundary

Record the model's original scope/time if available. Compare current source revision, configuration/feature flags, deployed version, and active request/job path. Missing deployment identity remains unknown.

Trace the actual call path and timing boundary. A background-job API name does not prove asynchronous execution; an alternate path or configuration may still execute inline. Genuinely background work may still compete for resources without directly blocking the request.

## Update precisely

Old claim: "Artifact generation blocks the request."

- Current source enqueues generation: this weakens the claim **for that code path**.
- Matching deployment and a correlated trace show the response precedes generation: downgrade direct blocking for those requests.
- Resource contention remains possible and requires different measurements.
- Unknown deployment: do not announce production is fixed.

Record old → current explanation; revision/path/evidence; remaining unknown; next action. Preserve the old explanation as historical context, not present truth. Do not reimplement a fix already active.

Stop once the disputed premise is resolved enough for the next decision. Do not audit all history or assume every old incident is stale.
