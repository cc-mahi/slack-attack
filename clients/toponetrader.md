---
slug: toponetrader
refs:
  vibepulse: ../VibePulse/.claude/clients/toponetrader.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: toponetrader
  hosts: ../MahiProduct/data/client-hosts.json          # entry: toponetrader
  wiki: null                                             # ../MahiProduct/wiki/clients/toponetrader.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Matt Morris", role: "CEO, Top One Trader"}
  - {name: "Lars Aerts", role: "Operations / integration lead at TOT"}
  - {name: "Shane Kalichurn", role: "Operations; weekly payout reporting"}
  - {name: "Priojit", role: "TOT hire working closer with Compass (Jan 2026)", confidence: low}
  - {name: "Arjie", role: "MatchTrader operations contact at TOT", confidence: low}
last_catchup: 2026-05-07T07:34:06Z
---

## Status

- **Stage:** live, post-pilot; billing renegotiated Oct 2025 to $10,000/mo base + $1.00/account (Challenge + Funded)
- **Integration:** CTrader live Jul 1 2025; MT5 live ~Aug 2025; MatchTrader live Sep 15 2025; TradeLocker pending (contact lost, no ETA as of Oct 2025)
- **Relationship:** strong; weekly calls; Matt engaged and expanding; brokerage expansion discussion opened Mar 2026 (retail FX under Comoros licence, same playbook as ACG)

## Recent issues

> [open] 2026-03-19 — Brokerage expansion discussion
> Will Carter had introductory call with Matt Morris. TOT wants to use their Comoros FX licence to launch a retail brokerage, marketing to prop clients — full outsourced dealing desk discussed, same model as ACG. Follow-up call scheduled Monday 23 March. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1773937053278899)

> [open] 2026-01-02–06 — Crypto expansion to MatchTrader
> Lars requested all crypto symbols activated on MatchTrader (same list as MT5). Target launch Wednesday Jan 7. Testing on Jan 6 showed only BTC/ETH visible; other instruments not yet activated. No resolution confirmed in window. [permalink](https://mahifx.slack.com/archives/C08U853T684/p1767370386895999)

> [open] 2025-10-22 — TradeLocker integration stalled
> Ivan Juren left TradeLocker. Liam Cordelle chasing new contact (Kristijan) for re-engagement. Implementation was reportedly "far along" per a Sep 18 email from TL, but no progress since. No ETA. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1761145850804539)

> [resolved] 2025-09-26–10-01 — PropFirmMatch ranking; low-spread strategy agreed
> TOT ranking low on PropFirmMatch due to EURUSD/USDJPY/GBPUSD spreads. 2–3 week trial of significantly tightened spreads agreed and implemented Oct 1. Matt reported sales more than doubled in the first full week. [permalink](https://mahifx.slack.com/archives/C08U853T684/p1759168523485169)

> [resolved] 2025-09-05–21 — Commercial billing dispute settled; new model agreed
> Matt Morris requested removal of Mahi from challenge accounts (except Phase 2), citing $9,435 August bill. Internal defence prepared; call held Sep 8. Renegotiated to Option 3: $10,000/mo base + $1.00/account (Challenge and Funded), selected Oct 21. [permalink](https://mahifx.slack.com/archives/C08U853T684/p1757076448158819)

> [resolved] 2025-09-08–10 — Slippage complaints; LR and TOB loosened post-MatchTrader live
> Multiple client slippage complaints following MatchTrader go-live. Sep 8 call acknowledged. Resolved by reducing LR across the board and substantially increasing TOB quantities (XAUUSD 25k→160k, EURUSD/USDJPY/GBPUSD 100k→500k each). [permalink](https://mahifx.slack.com/archives/C08U853T684/p1757497415749449)

> [resolved] 2025-09-15 — MatchTrader live
> After months of delays (Axcera blocking, symbol mapping issues, CFD group-tag workaround), MatchTrader fully live routing all flow to Compass. Nearly half of TOT accounts on Match at launch. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1757951129738709)

> [resolved] 2025-07-30–09-15 — MatchTrader integration blocked by Axcera
> Match integration stalled because Axcera (TOT's operations handler) refused to configure feed changes. Shane eventually gave Cameron direct Match login credentials on Sep 5; Mahi worked around group-tag limitation; test trades confirmed; live Sep 15. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1753885546366869)

> [resolved] 2025-08-18–19 — MT5 spreads 300–400% wider than CTrader
> Per-group markups on MT5 were stacking on top of Mahi pricing. Identified and markups removed. Extensive recalibration followed (15+ pairs adjusted per Lars's specifications). [permalink](https://mahifx.slack.com/archives/C08U853T684/p1755589527448899)

> [resolved] 2025-07-09 — Qualifying fill rate low (62%); LR loosened
> Large EURUSD orders being cancelled due to LR throttling (another counterparty placed a 1M order beforehand). Daria loosened the channel LR from a tighter limit to 100k per 500ms. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1752104836601079)

> [resolved] 2025-07-01 — CTrader go-live
> After 5-week integration effort (Spotware NDA friction, alias mapping issues, test trade coordination), CTrader went live July 1 2025. Second ODI confirmed live same day. Full instrument expansion followed: FX Jul 1, Metals Jul 9, CFDs/Crypto Jul 14–15. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1751386893117689)

## Notable topics

- 2025-11-05 — Matt's business metrics strong: avg weekly sales $24k (up from ~$4k), payout ratio 35% (trending down), consistency rule effective. Planning separate Top One Crypto site. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1762360910675469)
- 2025-07-21 — AWS overload outage during high-tick event; too many data streams; Mio informed Lars and flagged to dev. [permalink](https://mahifx.slack.com/archives/C08U853T684/p1753094064708819)
