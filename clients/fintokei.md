---
slug: fintokei
refs:
  vibepulse: ../VibePulse/.claude/clients/fintokei.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: fintokei
  hosts: ../MahiProduct/data/client-hosts.json          # entry: fintokei
  wiki: null                                             # ../MahiProduct/wiki/clients/fintokei.md (not yet)
channels_override: null
key_people_overrides: []
last_catchup: 2026-05-05T07:28:27Z
---

## Status

- Stage: live — prop-firm B-book, low-spread pricing model in production.
- Integration: live — Fintokei MT5 via Compass on `fintokei-ln-*`, YourBourse FIX connector being set up. CLIENT_PRICE_LDN distribution.
- Relationship: active — Kate Stagg / Rory King client-facing; Adam (Fintokei) primary client-side contact.

## Recent issues

> [open] 2026-04-16 — `fintokei-ln-trading-1` mysql volume at 90%
> Cameron flagged in #internal-fintokei (2026-04-16 16:41 BST): archiver retention defaults left in place on `PROD_LIVE_CLIENTDB`, top tables (EnrichedTradeOutputSummary 89GB, HouseOrder 84GB, HOUSE1PositionHistory 67GB) growing fast. LVM has ~1.26TB free so growing the volume buys time, but real fix is archiver overrides matching Funding Pips (POSITION_HISTORY 365→3 days, ORDER_HISTORY 365→30 days). Estimated ~2 weeks until full at current rate. https://mahifx.pagerduty.com/incidents/Q114Z685M3X0C1

## Notable topics
