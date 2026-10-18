# ShopClose — Verification Contract

## Principle
A successful code change requires evidence proportional to its risk.

Documentation, type validation, and a passing build do not by themselves prove correct business behavior.

## Baseline commands

From the repository root, using the local Python environment:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Alternatively, with the environment activated:

```powershell
python -m pytest -q
```

Start the API:

```powershell
python -m uvicorn app.main:app --reload --host 127.0.0.1
```

Manual health check:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

## Previously observed baseline

On October 18, 2026:
- Four tests passed locally.
- A deprecation warning occurred in the FastAPI/Starlette test-client dependency.
- A real local HTTP request to `/review` returned a possible refrigerant omission from a synthetic job.

These are historical observations, not proof of the current repository's state. Re-run after importing the code.

## M1 automated test matrix

### Extraction and domain semantics
- Installed component with missing explicit invoice item
- Correctly invoiced installed component
- Diagnostic-only component mention
- Explicit negation
- Recommended but not completed work
- Warranty exception
- Flat-rate inclusion
- Multiple materials
- Missing notes
- Empty invoice
- Alternate terminology
- Conflicting service statements
- Unrecognized materials

### Persistence
- New review stored
- Duplicate input deduplicated
- Changed input creates new review
- SQLite survives process restart
- Concurrent identical submissions handled safely
- Failed transactions do not leave partial decisions

### Decisions
- Authorized valid decision
- Invalid decision rejected
- Missing reviewer rejected
- Conflicting terminal decision rejected
- Dismissal reason required
- Immutable decision receipt retrievable

The minimum M1 target is 20 meaningful automated tests; scenario coverage matters more than test count.

## Evaluation protocol
Use independently labeled HVAC job examples.

For each example, record:
- Original notes
- Original invoice
- Contractor-specific inclusion rules where known
- Expected candidate findings
- Human-adjudicated outcome
- False-positive and false-negative behavior

Report precision and recall with both numerator and denominator. Do not claim model accuracy from synthetic examples alone.

## Security tests
Before external deployment:
- Invalid and forged webhook inputs
- Unauthenticated access denied
- Cross-tenant access denied
- Secret redaction
- Injection-resistant handling of imported data
- Duplicate and replayed events
- Failed external API requests

## Reporting format
Each completed implementation report must include:
1. Files changed
2. Behavior added or modified
3. Tests and commands actually run
4. Observed results
5. Unverified assumptions
6. Outstanding risks

Never claim a business outcome from a passing technical test.

## Milestone completion
A milestone is complete only when its acceptance criteria are implemented, tested, and traceable to concrete evidence.