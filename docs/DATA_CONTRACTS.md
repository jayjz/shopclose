# ShopClose — Data Contracts

**Status:** Proposed M1 schema. Not yet implemented.

## Principles
- Preserve raw source snapshots and normalized interpretations separately.
- Schema validity does not establish factual truth.
- Every inference must reference source evidence.
- Every authority-bearing action requires an attributable identity.
- Review history must remain auditable.
- Unknown data is not equivalent to false or zero.

## 1. JobSnapshot

Required:
- `job_id`: External or synthetic job identifier
- `source_system`: `fixture`, `csv`, or an approved FSM provider
- `source_record_id`: Stable source identifier
- `technician_notes`: Original text
- `invoice_items`: List of InvoiceItem objects
- `captured_at`: UTC timestamp
- `schema_version`: Version identifier

Optional:
- `equipment`: Model, serial, manufacturer, source reference
- `source_event_id`: Provider event identifier
- `work_completed_at`: Source-reported completion time
- `external_references`: Authorized immutable source references

Missing values must remain missing rather than be generated.

## 2. InvoiceItem

Required:
- `line_id`: Stable line identifier within the snapshot
- `description`: Original billing description

Optional:
- `quantity`
- `unit_price`
- `amount`
- `sku`
- `billing_category`
- `pricebook_reference`

Use decimal-safe monetary representations, not binary floating point. Currency must be explicit when monetary values are present.

## 3. EvidenceReference

Required:
- `source_type`: `technician_note`, `invoice_line`, `equipment_record`, or `external_document`
- `source_id`
- `excerpt` or stable structured field reference

Optional:
- `start_offset`
- `end_offset`
- `content_hash`

Offsets must correspond to the preserved raw text.

## 4. Finding

Required:
- `finding_id`
- `rule_id`
- `rule_version`
- `category`
- `interpretation`
- `evidence_references`
- `review_required`: true

Allowed categories initially:
- `potential_material_omission`
- `possible_inclusion_exception`
- `insufficient_documentation`

A finding is not an invoice adjustment instruction.

## 5. Review

Required:
- `review_id`
- `job_id`
- `input_fingerprint`
- `rule_version`
- `created_at`
- `status`
- `findings`
- `snapshot_reference`

Suggested lifecycle:
- `pending`
- `needs_more_info`
- `confirmed`
- `dismissed`

A review with no findings may be recorded as `no_rule_flags`; that is not equivalent to "accurate invoice."

## 6. DecisionReceipt

Required:
- `decision_id`
- `review_id`
- `reviewer_id`
- `decision`
- `reason`
- `decided_at`
- `review_version`

Allowed decisions:
- `confirmed`
- `dismissed`
- `needs_more_info`

Reject blank reviewer identities. Dismissals require a reason.

Reviewer identity must eventually be derived from authenticated context rather than an arbitrary client-supplied string.

## 7. Idempotency
A proposed review idempotency key is:

`SHA256(canonical input snapshot + schema version + rule version)`

The canonicalization algorithm must be documented and covered by cross-process tests.

Repeated identical submissions return the existing review without duplicate decision records.

Changed inputs create distinct review snapshots.

## 8. Transitions
- New review → pending or no-rule-flags
- Pending → confirmed, dismissed, needs-more-info
- Needs-more-info → resolved through a separately recorded follow-up decision when new information is available
- Terminal decisions must not be silently overwritten
- Conflicting or unauthorized transitions must be rejected

## 9. API evolution

Currently implemented:
- `GET /health`
- `POST /review`

Proposed:
- `GET /reviews`
- `GET /reviews/{review_id}`
- `POST /reviews/{review_id}/decision`

Preserve initial response compatibility where practical. If a breaking change is necessary, document the migration and test it.

## 10. Privacy
Do not use identifiable customer records as public fixtures.

Review snapshots containing customer information must not be processed in an externally accessible deployment until authentication, authorization, encryption, retention, and deletion rules are implemented.