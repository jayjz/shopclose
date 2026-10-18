---
name: hvac-fsm-integrator
description: Design, audit, and debug HVAC Field Service Management (FSM) integrations, pricebook syncs, dataplate OCR pipelines, and warranty/rebate automations across Jobber, Housecall Pro, ServiceTitan, supply houses (FW Webb, Johnstone), and Mass Save/NHSaves portals. Use when the prompt involves contractor software workflows, technician mobile inputs, invoice margin leaks, equipment serial extraction, or Division 23 mechanical specs. Do not use for generic web scraping unrelated to contracting or field services.
---

# HVAC FSM & Operations Integrator

Use this skill to bridge the operational gap between field technicians, office dispatch/billing, supply house pricing, and manufacturer/utility portals.

## 1. Expected Inputs & Raw Artifacts
Start from raw operational artifacts rather than summarized assumptions:
- **FSM Payloads:** Raw Jobber GraphQL payloads, Housecall Pro/ServiceTitan REST webhooks (`job.completed`, `invoice.created`), or 60-day CSV job/invoice exports.
- **Field Media:** Smartphone photos of weathered condenser/air-handler rating plates (`Model`, `Serial`, `AHRI Ref`), and technician voice/text completion notes.
- **External Portals & Catalogs:** Distributor price sheets (FW Webb, Johnstone, Ferguson CSV/PDFs), Division 23 mechanical schedules (`M-001` to `M-601`), and Mass Save / NHSaves / OEM warranty forms.

## 2. Core Analytical & Game-Theory Rules ("The Why")
- **Incentive Compatibility (Principal-Agent Problem):** A technician at 4:30 PM optimizes for leaving the job site, not data entry. Any workflow requiring manual typing of 18-digit serial numbers or multi-screen checklists will fail via shirking. Shift tech input to **1 photo + 15-second voice note**; push structured extraction to Python + Vision APIs.
- **Avoid Native Commodity Syncs:** Never build custom code for native 1-click features (e.g., standard Jobber-to-QuickBooks Online invoice sync). Target the **Three Broken Bridges**:
  1. *Tech Note-to-Invoice Gatekeeper:* Flagging parts mentioned in free-text tech notes (refrigerant lbs, capacitors, contactors, filter driers, condensate pumps) missing from billed line items.
  2. *Supply House Pricebook Drift:* Reconciling live distributor tier pricing against stale flat-rate pricebooks.
  3. *Warranty & Rebate Staging:* Automating OEM warranty registration (60-day cliff) and Mass Save/NHSaves AHRI verification.

## 3. Ordered Execution Steps
1. **Classify Execution Surface:**
   - Documented FSM API available (Jobber GraphQL, HCP REST) -> Route to deterministic **Python/FastAPI**.
   - Legacy portal without API (OEM warranty, supply house login, Accela/ProjectDog plan room) -> Route to **Playwright** (if public/stable) or **Grok Bot Cloud VM** (if authenticated/dynamic DOM).
2. **Enforce Schema Normalization:** Map extracted entities into strict Pydantic models (`equipment_model`, `serial_number`, `ahri_ref`, `unbilled_parts_detected`, `margin_leak_usd`).
3. **Apply Stop & Escalation Conditions:**
   - **STOP** before submitting any live warranty registration, rebate application, or customer invoice mutation. Stage as `proposed` and require human approval.
   - **DO NOT INFER** missing serial numbers, AHRI references, or refrigerant weights if OCR confidence is low or the photo is clipped—flag status as `needs_tech_rephoto`.

## 4. Required Output Format
- **Architecture / Flow:** Compact Mermaid or ASCII sequence diagram showing `Trigger -> Extraction -> Validation -> Approval Gate -> Target System`.
- **Margin Impact Table:** Markdown table quantifying Technician Friction (Seconds), Failure Mode at Run 50, and Recovered Gross Margin ($/Job).