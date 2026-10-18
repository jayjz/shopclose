---
name: deterministic-control-plane
description: Architect and write production Python, FastAPI, PostgreSQL/SQLite, Playwright, Docker, and cloud-agent control planes. Use when writing backend code, database schemas, webhook routers, browser automation scripts, Cursor Cloud Agent specs, or Grok Bot task definitions. Enforces idempotency, "Read Widely, Write Rarely" boundaries, SHA-256 evidence contracts, and 50th-run failure pre-mortems.
---

# Deterministic Control Plane & Agent Architecture

Use this skill whenever designing system topologies or writing executable code that coordinates local scripts, databases, and autonomous browser/coding agents.

## 1. Core Architectural Laws ("The Why")
- **Law 1: Never Put an LLM Between Two APIs When a Typed Function Works.** If the input and output schemas are bounded, use deterministic Python + Pydantic. Reserve LLM/GUI agents strictly for unstructured visuals, dirty text, or API-less legacy portals.
- **Law 2: Read Widely, Write Rarely.** Autonomous agents (Grok Bot, Cursor Cloud Agents) have permission to read, extract, classify, and stage proposals. Deterministic Python validates evidence. A human authorizes irreversible external writes (sending proposals, mutating live accounting/FSM records, merging to `main`).
- **Law 3: Shared-VM Isolation Boundary.** All Grok Bots under one seat share a single cloud computer and filesystem. Never mix personal financial credentials with client portal sessions on the same VM.

## 2. Mandatory State Machine & Evidence Contract
Every automated workflow must persist state in an external durable ledger (PostgreSQL/SQLite) outside the agent's memory using this exact state progression:

[discovered] --> [proposed] --> [approved] --> [executed] --> [verified]
|                                            |
+--> [rejected / failed (terminal/retry)] <--+


Every run record must enforce idempotency (`source_id` + `workflow_version`) and log:
- `run_id` (UUID), `executor` (`python_playwright` | `grok_bot` | `cursor_agent` | `local_ollama`), `artifact_hash` (`sha256`), `evidence_refs` (screenshots/raw JSON paths), `validation_passed` (bool), `human_intervention_seconds` (int), `approval_state`, `write_receipt`, and `incremental_cost_usd`.

## 3. 50th-Run Failure Pre-Mortem (Mandatory Check)
Before finalizing any scraper, webhook, or agent loop, explicitly identify and code a guard against what will break on **Run #50**:
- *GUI/Browser Agents:* ASP.NET `__VIEWSTATE` expiration, pagination infinite loops (guard: abort if Row 1 ID on Page $N$ == Page $N-1$), shadow DOM clipping, or modal popups.
- *Coding Agents:* Context-window bloat crossing the 200K/256K token 2x billing cliff via lockfiles or stack traces (guard: strict `.cursorignore` + max 3 pytest retry cap).
- *Webhooks:* Duplicate delivery retries causing double-writes (guard: database unique constraint on idempotency key).

## 4. Required Output Format
- **Topology Diagram:** Compact ASCII or Mermaid diagram showing the boundary between Untrusted External Input, Deterministic Validator, Durable Ledger, and Human Approval Gate.
- **Production Code:** Clean, typed Python 3.12+ / FastAPI / SQL code with Pydantic v2 validation and explicit error states—never stubbed pseudo-code when real implementation is requested.