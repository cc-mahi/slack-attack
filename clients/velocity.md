---
slug: velocity
refs:
  vibepulse: ../VibePulse/.claude/clients/velocity.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: velocity
  hosts: ../MahiProduct/data/client-hosts.json          # entry: velocity
  wiki: null                                             # ../MahiProduct/wiki/clients/velocity.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Dan", role: "client ops — yield profile / Echo lookups", confidence: low}
last_catchup: 2026-04-27T09:35:00Z
---

## Recent issues

> [open] 2026-04-23 — Xenfin (XF) CSV upload latency — moving to once-daily uploads
> Dan couldn't see yield profiles for counterparties 1009 / 851 in Echo. Daria diagnosed: Echo's counterparty field uses the obfuscated client ID (in `cpty_anon` column of the XF CSVs). Morning huddle (Will, Cameron Hughes, William Denny) agreed Mahi moves to once-a-day upload of all Xenfin CSVs until Xenfin fixes the latency. Will put a fix in for XF CSV lag — 60-min trade-to-yield-profile lag now (vs prior EOD). [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1776927890282329)

## Notable topics

- 2026-04-23 — Huddle action items (recap): (1) once-daily Xenfin CSV upload; (2) VT working on hedge liquidity + cautious bank skew (can't be aggressive or it's lost); (3) Mahi to add pricing for XAU crosses + other majors (low-hanging fruit); (4) look at reducing XAU TOB; (5) VT has more prospect data to upload. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1776936723214169)
- 2026-04-23 — XAU triangulated crosses added (XAU/{AUD,CHF,CNH,EUR,GBP,JPY,NZD,SGD}); pricers + dashGW bounced. Action item #3 from huddle. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1776954962207129)
- 2026-04-23 — VEL000951 on-prem per chat. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1776936286728029)
