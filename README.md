# LUMEN — Pricing & Go-to-Market Case — ATELIA × ESCP Starter Kit

> This repo is your starting point. Codex should read this README first.

## How to Get Started

This repo is a **template**: click **Fork** (top right), not "Use this template." Fork keeps your copy linked back to the original — that's what lets ATELIA automatically find every team's work, without anyone needing to send a link.

Once you've forked it, add your teammates as collaborators (Settings → Collaborators on your fork), and leave the visibility as **Public** — don't switch it to Private, or we lose access to your work.

## The Brief

The full brief is in `LUMEN_Case_Brief.md` (and a formatted version in `LUMEN_Case_Brief.pdf`). The data is in the `data/` folder, documented in `data/README_data.md`.

## Data quality gate

Before Codex or an analyst uses any CSV, run `python3 scripts/audit_data_quality.py` and read [`DATA_QUALITY_REPORT.md`](DATA_QUALITY_REPORT.md). The rules in [`data/AGENTS.md`](data/AGENTS.md) apply automatically to Codex work inside `data/`; the human-readable workflow is in [`DATA_WORKFLOW.md`](DATA_WORKFLOW.md). Names and email values must never be used or reproduced, and files not marked **Direct use: Yes** require the documented cleaning or privacy review first.

One-sentence summary: LUMEN, a functional beverage brand, has to decide **price, positioning, and launch channel(s)** to enter the German market — with no real German sales data (LUMEN isn't there yet), and a real trade-off between the CMO (premium positioning) and the CFO (fast return on investment).

## Rule #1 — Prompt Logging Is Automatic

This repo includes an `AGENTS.md` file, which Codex reads automatically at the start of every task — you don't need to open or edit it. The first time you talk to Codex in a new conversation, it will ask for your **student ID**. Answer it, and from then on Codex logs every prompt you send it — automatically, verbatim — into `prompts/<your-id>/session-*.md`, without you doing anything else.

**You don't fill this in by hand.** Your only job is to make sure that log file gets committed along with your code changes — Codex writes it, but you still need to include it when your pull request is created and merged. If a pull request only has code changes and no updated log file, that's a sign something didn't get logged.

Why we're doing this: it's not to monitor you. It's what lets us understand, at the end, how you reasoned — not just what you produced. A good result reached with a clear prompt from the start isn't scored the same as a good result reached after fifteen random attempts.

## Rule #2 — Before You Code, Ask Yourself These Questions

Check each box in this README as you go — not at the end, while you're working:

- [ ] **Data**: what data will your tool actually handle? Is any of it sensitive (personal data, company customer data)? `data/customer_survey.csv` has name/email columns — did you use them in your tool? If yes, how did you protect/anonymize them? If no, why did you choose not to expose them? (A team that never touches these columns should still be able to answer — "we chose not to use them" is a valid answer.)
- [ ] **API keys**: if your tool calls an external API (weather, or anything else), where is the key stored? Never hardcoded in a file committed to GitHub. (A valid answer: "we didn't use any external API.")
- [ ] **Deployment**: if you deployed a live demo, does any endpoint or response return raw, unfiltered data (e.g. the full survey with name/email) to any visitor?
- [ ] **Files generated along the way**: if your tool (or Codex) created new files derived from the provided data, did you think about whether they should be committed to the repo or not?
- [ ] **Storage**: if you're keeping any data, in what structure, and why that choice over another?
- [ ] **Robustness**: what happens if the user gives an empty, inconsistent, or unexpected input?
- [ ] **Explainability**: can you explain to someone non-technical why your tool does what it does?
- [ ] **Business relevance**: does your prototype actually answer the problem posed in the brief, or is it an interesting technical build that's off-target?

These questions aren't here to slow you down — they're part of what's being evaluated. A thoughtful answer to one of them is worth more than an extra feature nobody asked for.

## What We Expect at the End

- A prototype that works, even partially, on the LUMEN case
- Your prompt log (`prompts/<your-id>/session-*.md`) committed and up to date
- A short paragraph below, written in business language (not technical), explaining what you did and why
- A live URL (Vercel or similar) if you deployed it — not required to still get credit, but expected if you did

## Our Approach

The final website is a role-based decision hub: each contribution has its own page, while the landing page keeps the team's Germany recommendation coherent. The integration analysis starts with a transparent simulator rather than an unexplained answer, and the Role 3 pricing cockpit compares the €1.79, €2.19, and €2.59 candidates using competitor positioning, stated customer thresholds, acceptance, and channel contribution margins. It recommends testing €2.19 and clearly labels observed facts, calculations, planning assumptions, and risks because LUMEN has no observed German sales history.

Open `price_simulator.html` in a browser to test the scenarios. The cockpit also supports blended channel mix, launch volume and budget inputs, acceptance sensitivity, marketing CAC/LTV benchmarks, city context, and competitor price references; its decision score is an explicitly illustrative 40% acceptance / 60% contribution weighting.

For the market, city, and timing work, we combined the illustrative German market split with anonymized, aggregated survey measures, then cross-checked the launch window against monthly demand seasonality, temperature, and the supplied competitor promotion history. The analysis labels observed facts, calculations, assumptions, and recommendations separately; customer names and email addresses were not used or exposed. See `analysis/market_city_timing_analysis.md` for the evidence and the tests required before scaling.
Open `index.html` for the team hub, `role-3-pricing.html` for the full pricing evidence, and `price_simulator.html` for the interactive launch-room prototype. The supporting pricing calculations and sources are documented in [`analysis/pricing_analysis.md`](analysis/pricing_analysis.md). Customer identity fields were not used or exposed, and the website does not call an external API or publish raw survey data.
