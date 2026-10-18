# ShopClose Architecture

## Architectural objective
Provide a deterministic, auditable control plane for reviewing discrepancies between technician service documentation and recorded invoice items.

ShopClose identifies candidates. It does not determine financial truth independently.

## Current implementation

`Synthetic job JSON → FastAPI → keyword matching → review response`

This is a synchronous, in-memory proof of concept.

## Target local architecture

```text
                 UNTRUSTED INPUT
              Jobber / CSV / Fixtures
                        |
                        v
                 Input validation
                        |
                        v
              Normalized Job Snapshot
                        |
                        v
              Evidence extraction
                        |
                        v
           Deterministic comparison rules
                        |
                        v
               Candidate findings
                        |
                        v
                SQLite evidence ledger
                        |
                        v
                Human review queue
                        |
               +--------+---------+
               |        |         |
           Confirm   Dismiss   More info
               |
               v
          Audit receipt only
```

The system must not write back to billing records without a separately designed and authorized future capability.

## Components

### API — `app/main.py`
Accepts validated inputs, exposes review results, and eventually manages review/decision endpoints.

### Domain models — `app/models.py` (planned)
Typed contracts for normalized jobs, invoice items, findings, decisions, and evidence.

### Detection engine — `app/gatekeeper.py`
Finds supported discrepancies between recorded service work and billable items.

Rules should be deterministic, versioned, and testable.

### Ledger — `app/ledger.py` (planned)
Persists review snapshots, findings, decision events, source fingerprints, and timestamps.

Use SQLite transactions and uniqueness constraints. Never overwrite prior evidence to accommodate new findings.

### FSM adapter — `app/integrations/jobber.py` (planned)
Handles authorized provider-specific event and API contracts. Converts provider-specific records into normalized ShopClose models.

### Notification adapter — `app/integrations/telegram.py` (planned)
Notifies authorized reviewers without granting invoice modification authority.

## Trust boundaries
1. External FSMs and imported files are untrusted sources, even when authenticated.
2. A validated JSON schema proves structure, not factual accuracy.
3. AI output is a proposal, never authorization or evidence of execution.
4. A human decision is recorded separately from the original evidence.
5. A confirmed review does not prove money was recovered.
6. Financial recovery requires independent billing or payment evidence.

## Reliability
- Use input fingerprints and rule versions for idempotency.
- Preserve conflicting records rather than silently choosing one.
- Use explicit lifecycle states.
- Make duplicate events safe.
- Fail visibly when required source information is absent.
- Do not claim that a review or external action succeeded until a durable receipt exists.

## Technology
- Python 3.12
- FastAPI and Pydantic
- SQLite for the local MVP
- pytest and HTTP test clients
- Optional local Ollama or remote models for non-authoritative extraction
- Future documented FSM APIs

PostgreSQL, Redis, cloud queues, and browser agents are not baseline requirements.

## Security posture
Development runs on loopback only. No production deployment, authentication, or customer-data processing is authorized by this document.

See `SECURITY.md`.
