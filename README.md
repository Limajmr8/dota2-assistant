# NPSC Rank Accelerator - Ops Repository

Operational workspace for building and selling the **NPSC Rank Accelerator System**.

> Note: this repository was previously initialized under the `dota2-assistant` name but is now maintained as an NPSC prep + commercialization workspace; legacy name references may still appear in branch/history metadata.

This repo is organized to run one clear loop:
1. produce/maintain exam-prep assets,
2. package them into a clean PDF,
3. execute daily lead-gen + follow-up,
4. make weekly KPI-driven optimization decisions.

## Quick start

### 1) Run PDF quality gate, then build compiled kit PDF
1. Complete checklist in `pdf_build_quality_gate.md`.
2. Run:
```bash
python build_npsc_pdf.py
```
Output:
- `NPSC_Crack_Kit.pdf`

### 2) Start operations
Use these files in order:
- `npsc_product_readme.md`
- `first_money_7_14_days_operating_pack.md`
- `gumroad_listing_setup.md`
- `facebook_posting_queue.md`
- `daily_revenue_ops_tracker.csv`
- `daily_revenue_ops_tracker_schema.md`
- `weekly_kpi_dashboard.md`
- `experiment_registry.csv`

## Repository map

### Core product content
- `npsc_260_questions.md`
- `npsc_study_strategy.md`
- `npsc_chatgpt_quiz_prompts.md`
- `npsc_product_readme.md`

### Commercialization + growth system
- `npsc_marketing_plan.md`
- `first_money_7_14_days_operating_pack.md`
- `instagram_reels_viral_deployment.md`
- `profit_game_plan_30_days.md`
- `pricing_test_rules.md`
- `pricing_test_tracker.csv`
- `gumroad_listing_setup.md`
- `facebook_posting_queue.md`
- `daily_revenue_ops_tracker.csv`
- `daily_revenue_ops_tracker_schema.md`
- `weekly_kpi_dashboard.md`
- `experiment_registry.csv`
- `pdf_build_quality_gate.md`

### Team handoff artifacts
- `HANDOFF_CLAUDE_COWORK.md`
- `EXEC_SUMMARY_FOR_CLAUDE.txt`
- `OPERATOR_COMMAND_CENTER.md`

## Weekly operating cadence
- **Daily:** execute posting + DM follow-ups, log every lead/event.
- **Weekly:** review only the 5 North Star KPIs in `weekly_kpi_dashboard.md`, cut low-performing actions, scale top-converting actions.
- **Milestone-based pricing:** keep intro price until threshold is hit, then move to next price tier per `pricing_test_rules.md`.

## Non-negotiables
- Keep messaging ethical and proof-first.
- Keep decisions data-based (from tracker + dashboard), not intuition-only.
- Keep listing copy, post hooks, and DM scripts consistent with one promise.
- Route hook/script changes through `experiment_registry.csv`.
