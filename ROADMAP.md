# ShopClose Roadmap

**Status:** Early local prototype  
**Product hypothesis:** HVAC contractors lose administrative time and may miss legitimate charges because service documentation and billing records are inconsistent.

## M0 — Local proof of concept

**Status:** Verified manually, pending repository-level re-verification.

Delivered:
- FastAPI application
- `GET /health`
- `POST /review`
- Keyword-based potential omission detection
- Two synthetic job fixtures
- Four passing pytest tests
- Successful local HTTP request identifying a possible refrigerant omission

Limitations:
- No persistence or authentication
- No FSM integration
- No human decision recording
- No model/serial extraction
- No semantic understanding or financial recovery proof

## M1 — Evidence foundation

**Priority:** P0

Implement:
- Typed job, invoice, finding, and review contracts
- Evidence excerpts and rule identifiers
- Explicit uncertainty and exception handling
- SQLite persistence
- Idempotent review creation
- Immutable decision receipts
- Read-only review queue

Acceptance:
- At least 20 meaningful automated tests
- Identical review input plus rule version is idempotent
- Changed input produces a new snapshot review
- Restart preserves records
- Negated or diagnostic-only notes do not produce confident omission claims
- Review decisions are attributable and auditable
- Existing working API behavior remains compatible or has documented migration

## M2 — Office review experience

**Priority:** P0

Implement:
- Minimal review interface or Telegram notification workflow
- Evidence-first presentation
- Confirm, dismiss, and request-information decisions
- Decision history
- Clear distinction between candidate and verified omission

Acceptance:
- Human can resolve a review without modifying an invoice
- No unauthorized state transitions
- Duplicated notifications cannot create duplicated decisions
- Review evidence can be retrieved and explained

## M3 — FSM integration

**Priority:** P1; gated by customer demand

Start with one supported integration, likely Jobber.

Implement:
- Authorized development/test environment
- API scope verification
- Webhook signature and event validation where supported
- Event deduplication
- Asynchronous data retrieval
- Normalization into ShopClose contracts
- Retry, rate-limit, and failure handling

Acceptance:
- One supported event processed end-to-end
- No real customer data in test fixtures
- Errors and incomplete API responses are explicit
- No invoice mutations

## M4 — Contractor pilot

**Priority:** P0 commercial validation

Target:
- Interview five relevant contractors
- Obtain authorized historical records from at least one
- Evaluate 20 or more representative historical jobs where feasible
- Compare candidate findings against human-reviewed ground truth
- Quantify actual administrative time and confirmed invoice corrections
- Offer a paid, narrowly scoped pilot

No revenue outcome is assumed.

## M5 — Commercial hardening

**Priority:** Conditional

Only after a paid pilot demonstrates value:
- Authentication and tenant isolation
- Retention and deletion controls
- Production deployment and monitoring
- Per-customer access controls
- Billing and support processes
- Contractual data-processing terms

## Explicit non-goals
- Replacing ServiceTitan, Jobber, Housecall Pro, or BuildOps
- Autonomous invoicing
- Automated warranty submissions in the initial product
- Full HVAC estimating or dispatch optimization
- Unsupported supplier-portal scraping
- Requiring Grok Bot or a large-model subscription

## Release gates
A milestone is complete only when implementation, automated verification, and relevant manual evidence agree.
