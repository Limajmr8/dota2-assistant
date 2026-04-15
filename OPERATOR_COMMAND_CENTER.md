# Operator Command Center (Daily + Weekly)

Use this as the execution source-of-truth for running the NPSC system without guesswork.

Primary copy-paste scripts and operating assets:
- `first_money_7_14_days_operating_pack.md`

## Daily scoreboard targets
Track in: `daily_revenue_ops_tracker.csv`

Minimum daily actions:
- Publish 1 Instagram Reel (single-channel sprint mode)
- Start 10 new qualified DMs
- Complete D0/D1/D3/D5 follow-ups for all open leads
- Log all outcomes (reply, objection, close, no-response)

## Daily sequence (15–45 min blocks)
1. **Offer consistency check (5 min)**
   - Ensure today’s hook aligns with promise in `npsc_product_readme.md`.
2. **Distribution (15 min)**
   - Publish post/Reel + CTA (DM keyword / link).
3. **Lead handling (20 min)**
   - First response under 1 hour when possible.
   - Move warm leads to close flow same day.
4. **Follow-up batch (20 min)**
   - Run D1, D3, D5 messages.
5. **Data logging (10 min)**
   - Update tracker immediately after each interaction.
   - Use allowed vocab from `daily_revenue_ops_tracker_schema.md`.

## Weekly KPI review ritual (45–60 min)
Use: `weekly_kpi_dashboard.md`

Decision filter (mandatory):
- Use only these 5 KPIs: reply rate, qualified lead rate, close rate, AOV, revenue/day.
- Every weekly decision must map to one of the 5 KPIs only.

Decisions:
- Cut bottom 20% activities.
- Double top 20% activities.
- Update listing or DM copy only where data supports it and test is logged in `experiment_registry.csv`.

## Trigger rules
- If reply rate drops for 3 days: rotate hook angle immediately.
- If Reel hold rate drops for 3 days: rewrite first 2-second hook format.
- If closes stall but replies are high: tighten offer clarity + risk reversal.
- If lead volume is high but AOV is low: strengthen bundle framing and upsell path.
- If milestone threshold is reached: apply next pricing tier per `pricing_test_rules.md`.

## Single command reference
Rebuild product PDF any time source content changes:
1. Complete `pdf_build_quality_gate.md`
2. Run:
```bash
python ./build_npsc_pdf.py
```
