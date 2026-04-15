# Pricing Test Rules — NPSC Crack Kit

Use this with `pricing_test_tracker.csv`.

## Rule Set
1. Start launch at **₹299**.
2. Keep price at ₹299 for the first **20 paid buyers** or until **23:59 IST on 2026-05-31**, whichever comes first.
3. From buyer 21 onward, set price to **₹499**.
4. Update the tracker after every payment to avoid pricing mismatch in DMs/posts.
5. Keep urgency ethical and factual (milestone/deadline based), never shame-based.

## Price Switch Checklist (must be YES before switch)
- [ ] Buyer number is 21+ or deadline trigger is reached.
- [ ] Last 7-day reply rate is stable (no major collapse).
- [ ] Last 7-day qualified lead rate is stable.
- [ ] Last 7-day close rate is stable.
- [ ] Offer + DM scripts are aligned to current price messaging.
- [ ] `active_price_point` updated across listing, DM scripts, and tracker.

## Rollback Criteria (after switch to ₹499)
If either condition happens, rollback to ₹299 for a 7-day stabilization cycle, then re-test:
1. 3-day close rate drops by **30%+** vs pre-switch baseline, OR
2. 5-day revenue/day drops by **20%+** vs pre-switch baseline.

Rollback actions:
- Freeze new copy changes except one controlled test at a time.
- Log rollback reason in `experiment_registry.csv` and weekly dashboard.
- Re-run switch checklist before attempting next price bump.

## Operational Notes
- `buyer_number_running` is the control field for price switch.
- Always copy the current active price into outreach replies.
- Review conversion rates separately for:
  - ₹299 cohort (buyers 1–20)
  - ₹499 cohort (buyers 21+)
