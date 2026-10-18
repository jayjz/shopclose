# ShopClose — Architecture Decision Log

## ADR-001 — Integrate with existing FSM software
**Status:** Accepted product direction  
**Date:** 2026-10-18

**Context:** Contractors already use platforms providing dispatch, invoicing, and customer management.

**Decision:** Build exception detection around existing operational systems rather than replacing them.

**Why:** Lower switching costs and implementation complexity. The customer retains their existing system of record.

**Tradeoff:** Integrations can be limited by API access, subscriptions, and vendor-specific contracts.

## ADR-002 — Evidence-backed findings, not autonomous billing
**Status:** Accepted  
**Date:** 2026-10-18

**Decision:** Findings are provisional until independently reviewed.

**Why:** Technician notes alone cannot establish whether a material is billable or omitted.

**Consequence:** The product must show supporting evidence, uncertainty, and applicable exceptions.

## ADR-003 — Local-first Python/FastAPI
**Status:** Implemented in the initial prototype  
**Date:** 2026-10-18

**Decision:** Begin with Python, FastAPI, Pydantic, and pytest.

**Why:** Rapid iteration, simple validation, low cost, and compatibility with the planned integration and extraction stack.

**Consequence:** The initial service is not production-ready.

## ADR-004 — SQLite before PostgreSQL
**Status:** Proposed for M1  
**Date:** 2026-10-18

**Decision:** Use SQLite for durable local review records.

**Why:** Local persistence does not initially require database servers or cloud infrastructure.

**Migration trigger:** Multiple tenants, distributed workers, high concurrency, or demonstrated operational needs.

## ADR-005 — AI is an extractor, not an authority
**Status:** Accepted design principle  
**Date:** 2026-10-18

**Decision:** AI may propose classifications and extract equipment data, but cannot independently authorize charges or external submissions.

**Why:** Model output can be plausible without being correct.

**Consequence:** Validation, evidence references, and human approvals remain separate from inference.

## ADR-006 — One commercially testable wedge
**Status:** Accepted initial strategy  
**Date:** 2026-10-18

**Decision:** Prioritize note-to-invoice reconciliation before warranty, rebate, or supplier-pricebook automation.

**Why:** The first workflow can be tested without privileged portal credentials and has a directly observable buyer problem.

**Consequence:** Broader automation is deferred until pilot evidence demonstrates demand.

## ADR-007 — Human-review state transitions
**Status:** Proposed for M1  
**Date:** 2026-10-18

**Decision:** Implement explicit review and decision states, idempotent input handling, and immutable receipts.

**Why:** Prevent duplicate or contradictory actions and preserve accountability.

**Consequence:** More implementation effort than a stateless classifier, justified before handling real operations.

## ADR-008 — No mandatory agent orchestration
**Status:** Accepted design principle  
**Date:** 2026-10-18

**Decision:** Do not require Grok Bot, local LLM inference, multiple agents, or cloud orchestration for the baseline.

**Why:** Deterministic validation should not depend on unnecessary model inference, quotas, browser sessions, or network availability.

**Revisit when:** A demonstrated customer workflow requires capabilities simpler tools cannot reliably provide.