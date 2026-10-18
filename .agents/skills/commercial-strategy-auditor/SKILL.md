---
name: commercial-strategy-auditor
description: Audit unit economics, subscription vs. API tier arbitrage, B2B pricing models, market wedges, and competitive positioning using Porter's Five Forces, Game Theory, and Financial Statement Analysis. Use when pricing a service or SaaS, evaluating AI/cloud subscription tiers, choosing which customer segment to target, or writing a commercial pitch/ROI diagnostic. Do not use for pure syntax debugging or low-level code formatting.
---

# Commercial Strategy & Unit-Economics Auditor

Use this skill to evaluate whether a technical workflow, subscription tier, or product wedge is mathematically and commercially viable before writing production code.

## 1. Expected Inputs
- Proposed product/service scope, target customer profile (e.g., 5-to-30 truck HVAC contractor, engineering team), and pricing tiers.
- Compute/tool cost inputs: subscription multipliers, token rates ($/1M input, cached input, output), context-cliff thresholds (e.g., 200K token 2x rate jump), and human review time.

## 2. Ordered Analytical Workflow
1. **Unit-Economics & Break-Even Math:**
   - Calculate marginal cost per accepted run (including retries, tool calls, and human review seconds).
   - Compare fixed subscription pools against metered API execution (`cost_in_usd_ticks`) and local GPU execution ($0 marginal cost on RTX 4060).
2. **Porter's Five Forces Wedge Audit:**
   - *Supplier Power:* Are we dependent on a single LLM vendor, OEM portal, or closed API (e.g., ServiceTitan enterprise walls)?
   - *Buyer Power & Switching Costs:* Does this anchor into the buyer's daily cash-flow ledger so ripping it out hurts, or is it a "nice-to-have" lead list?
   - *Threat of Substitution:* Can the buyer solve this by flipping a native software toggle or hiring a $20/hr part-time admin?
3. **Game Theory & Mechanism Design:**
   - Identify every actor in the loop (Owner, Dispatcher, Field Tech, GC, Estimator).
   - Align incentives so the buyer sees **immediate recovered cash** (e.g., a 60-day historical "Profit Leak Audit") rather than paying for speculative future value.
4. **Financial Statement Mapping:**
   - Map value directly to **Gross Margin %** (catching unbilled materials/pricebook drift), **SG&A reduction** (displacing manual admin hours), or **Working Capital acceleration** (faster invoice/rebate collection).

## 3. Facts Not to Infer & Guardrails
- **DO NOT** invent market conversion rates, contractor revenue figures, or unverified vendor quota numbers. Where vendor pool sizes are opaque, express break-even thresholds algebraically as a function of measured baseline runs ($B$) and marginal top-up cost ($c$).
- **STOP** and recommend killing any product wedge where customer acquisition or human babysitting costs exceedVerified Contribution Margin.

## 4. Required Output Format
1. **Executive Verdict (1–2 sentences):** Invest, Pivot Wedge, or Kill, backed by the primary economic driver.
2. **Strategic Matrix:** Compact Markdown table covering Force/Incentive, Operational Reality, and Strategic Counter-Move.
3. **Break-Even Equation / Pricing Ladder:** Explicit math showing exact daily/weekly volume required for positive ROI.