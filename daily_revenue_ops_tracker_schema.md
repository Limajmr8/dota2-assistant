# Daily Revenue Ops Tracker — Field Definitions

Use with: `daily_revenue_ops_tracker.csv`

## Standard vocab (required)
- `channel`: `Instagram-Reels` | `Instagram-Stories` | `WhatsApp-DM` | `Other`
- `activity_type`: `Reel` | `DM` | `Followup` | `Story` | `Close` | `Upsell`
- `hook_angle`: `Confidence` | `Speed` | `Affordability` | `Clarity` | `Proof` | `Urgency-Ethical` | `Risk-Reversal` | `Bundle-Value` | `Other`
- `active_price_point`: `299` | `499`

## Column-by-column definitions
1. `date`
   - What counts: Calendar day of logged activity.
   - When to log: Every row, same day.
   - Format: `YYYY-MM-DD`.

2. `channel`
   - What counts: Primary source channel for the activity.
   - When to log: Every row.
   - Allowed values: Standard vocab only.

3. `hook_angle`
   - What counts: Core messaging angle used in post/DM.
   - When to log: Every row.
   - Allowed values: Standard vocab only.

4. `cta_source_keyword`
   - What counts: CTA keyword/source identifier used to attribute Reel→DM→Sale path.
   - When to log: Every row with outbound content or inbound lead.
   - Format: short token (examples: `DM-START`, `REEL-C1`, `STORY-QZ1`).

5. `activity_type`
   - What counts: Primary activity executed.
   - When to log: Every row.
   - Allowed values: Standard vocab only.

6. `reels_posted`
   - What counts: Number of Reels posted that day.
   - When to log: End of day.
   - Allowed values: integer `>= 0`.

7. `reel_views`
   - What counts: Total Reel views for that day’s tracked content.
   - When to log: End of day snapshot.
   - Allowed values: integer `>= 0`.

8. `replies_count`
   - What counts: New inbound replies tied to tracked CTA/content.
   - When to log: Real-time or end-of-day batch.
   - Allowed values: integer `>= 0`.

9. `leads_contacted`
   - What counts: New qualified DMs started by you.
   - When to log: As executed.
   - Allowed values: integer `>= 0`.

10. `conversations_started`
    - What counts: Leads that moved from contact to active two-way chat.
    - When to log: As status changes.
    - Allowed values: integer `>= 0`.

11. `qualified_leads`
    - What counts: Leads meeting your buy-intent/fit criteria.
    - When to log: As status changes.
    - Allowed values: integer `>= 0`.

12. `followup_d0`
    - What counts: Same-day follow-ups sent.
    - When to log: As executed.
    - Allowed values: integer `>= 0`.

13. `followup_d1`
    - What counts: Day-1 follow-ups sent.
    - When to log: As executed.
    - Allowed values: integer `>= 0`.

14. `followup_d3`
    - What counts: Day-3 follow-ups sent.
    - When to log: As executed.
    - Allowed values: integer `>= 0`.

15. `followup_d5`
    - What counts: Day-5 follow-ups sent.
    - When to log: As executed.
    - Allowed values: integer `>= 0`.

16. `sales_count`
    - What counts: Core offer sales closed that day.
    - When to log: Immediately after payment confirmation.
    - Allowed values: integer `>= 0`.

17. `cash_collected_inr`
    - What counts: Cash-in recorded for the day.
    - When to log: Immediately after payment confirmation.
    - Allowed values: integer/number `>= 0`.

18. `revenue_inr`
    - What counts: Total recognized revenue for the day (core + upsell).
    - When to log: End of day reconciliation.
    - Allowed values: integer/number `>= 0`.

19. `active_price_point`
    - What counts: Live listed price used for that day’s selling window.
    - When to log: Every row.
    - Allowed values: `299` or `499`.

20. `upsell_sales`
    - What counts: Number of upsells closed that day.
    - When to log: Immediately after payment confirmation.
    - Allowed values: integer `>= 0`.

21. `best_message_variant`
    - What counts: Best-performing script/DM variant ID for the day.
    - When to log: End of day.
    - Format: short ID (examples: `VAR-A`, `VAR-B2`).

22. `notes`
    - What counts: Critical context (objections, anomalies, proof links).
    - When to log: As needed.
    - Format: short free text.
