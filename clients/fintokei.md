---
slug: fintokei
refs:
  vibepulse: ../VibePulse/.claude/clients/fintokei.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: fintokei
  hosts: ../MahiProduct/data/client-hosts.json          # entry: fintokei
  wiki: null                                             # ../MahiProduct/wiki/clients/fintokei.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Jan", role: "Fintokei support/ops contact", confidence: low}
last_catchup: 2026-07-03T07:20:15Z
---

## Status

- Stage: live — prop-firm B-book, low-spread pricing model in production.
- Integration: live — Fintokei MT5 via Compass on `fintokei-ln-*`, YourBourse FIX connector being set up. CLIENT_PRICE_LDN distribution.
- Relationship: active — Kate Stagg / Rory King client-facing; Adam (Fintokei) primary client-side contact.

## Recent issues

> [open] 2026-06-30 — New model CLIENT_PRICE_LSB_LDN set up for review; Fintokei to subscribe post-weekend restarts
> Kate Stagg posted in #internal-fintokei that the new pricing model CLIENT_PRICE_LSB_LDN is set up and ready for review. Fintokei will subscribe with suffix `_t` following their weekend server restarts. Commercial pricing question on this model (setup fee vs monthly cost) remains unresolved per 2026-06-16 entry. [permalink](https://mahifx.slack.com/archives/C08R694QVNX/p1782815433338759)

> [open] 2026-06-16 — New model pricing question: setup fee vs monthly cost, unanswered
> Kate Stagg (Mahi) asked in #internal-fintokei whether to charge for a new model for Fintokei — they previously got one set up at no cost as a goodwill gesture. Kate's suggestion: one-off setup fee, no monthly cost (unusual commercial structure). Billing-impact scan (2026-06-17) flagged: no setup fee provision in current per-user contract; Daria to confirm whether as-is or needs addendum. No resolution yet. [question](https://mahifx.slack.com/archives/C08R694QVNX/p1781610571053819)

> [open] 2026-06-16 — BMSL timezone deploy requested via Zendesk #23102
> Kate Stagg (Mahi) raised a Zendesk ticket for a BMSL timezone deploy for Fintokei. Feature = per-TradingTimeZone overrides on pricing.benchmarkMinimumSpread (commit 66192190, in release/26.3). Triaged P3 Dev: Fintokei pricer needs upgrading to release/26.3 before this can be applied; same feature in flight for Velocity (#23080). [ticket](https://mahifx.zendesk.com/agent/tickets/23102) [internal note](https://mahifx.slack.com/archives/C08R694QVNX/p1781610590423249)

> [resolved] 2026-06-25 — XAUUSD price drop complaint: clients query 2026-06-24 12:25:02–03 UTC move
> Jan (Fintokei) posted in #mahi-fintokei asking Mahi to verify whether a sharp XAUUSD price drop at 2026-06-24 12:25:02–03 UTC was a genuine market move or a platform issue, citing multiple client complaints. Kate Stagg investigated and confirmed genuine market move (~4032 to ~4020), sharing an Echo ToB screenshot. Jan thanked and closed. [complaint](https://mahifx.slack.com/archives/C08QWKFARDL/p1782378741888539) [Kate response](https://mahifx.slack.com/archives/C08QWKFARDL/p1782379413206499)

> [resolved] 2026-06-15 — Slippage complaint: account 6032915, 6 simultaneous fills on 2026-06-14 ~22:00 UTC
> Pau (Fintokei) raised a complaint that one of 6 simultaneously-filled positions for FintokeiMT5C_6032915 received significantly higher slippage. Rory King (Mahi) acknowledged and investigated. Cameron Hughes (Mahi) explained: FINTOKEI market spreads blew out briefly, causing Mahi's pricing model to defensively widen in response, and the trade came in on that wider published spread. Pau reacted with `:thankyou:`. [complaint](https://mahifx.slack.com/archives/C08QWKFARDL/p1781524010061899) [CH explanation](https://mahifx.slack.com/archives/C08QWKFARDL/p1781524666634919)

> [resolved] 2026-05-29 — MT5 build 5830 server update: Mahi confirms no gateway impact
> Jan asked in #mahi-fintokei whether Fintokei's planned weekend update of MT5 servers to build 5830 would cause issues to the gateway. Rory King (Mahi) confirmed no issues expected on Mahi's side. Jan thanked and acknowledged. [question](https://mahifx.slack.com/archives/C08QWKFARDL/p1780059694047829) [Rory confirms OK](https://mahifx.slack.com/archives/C08QWKFARDL/p1780060200072389)

> [resolved] 2026-05-25 — MT4 bridge update causes trade rejections; root cause confirmed MTB-391 reserveUUID leak
> Adam (@fintokei) raised a <!channel> alert at 02:00 BST: trades being rejected by the MahiFXMT4Bridge before reaching Compass after a weekend bridge update — clients unable to close positions or delete pending orders (example: account 30145252, 176.97 lots BUY JP225). Isaac Dann (Mahi) investigated, proposed rollback + `UNIFIED REQUEST IDS=N`; Adam rolled back but confirmed flag was already `N`. Root cause confirmed 2026-05-26 by Andrew Morgan (Mahi): MTB-391 — reserveUUID leak in `MT4ExecutionBridge.cpp:263-267` caused exhaustion under load. RCA: `docs/ops/incidents/2026-05-25-fintokei-mtb391-reserveuuid-leak/rca.md`. [alert](https://mahifx.slack.com/archives/C08QWKFARDL/p1779670858863209) [rollback thread](https://mahifx.slack.com/archives/C08QWKFARDL/p1779672373610029) [dev review flagged](https://mahifx.slack.com/archives/C08QWKFARDL/p1779673574470809) [RCA](https://mahifx.slack.com/archives/C015A0QBV2N/p1779802448548119)

> [open] 2026-04-16 — `fintokei-ln-trading-1` mysql volume at 90%
> Cameron flagged in #internal-fintokei (2026-04-16 16:41 BST): archiver retention defaults left in place on `PROD_LIVE_CLIENTDB`, top tables (EnrichedTradeOutputSummary 89GB, HouseOrder 84GB, HOUSE1PositionHistory 67GB) growing fast. LVM has ~1.26TB free so growing the volume buys time, but real fix is archiver overrides matching Funding Pips (POSITION_HISTORY 365→3 days, ORDER_HISTORY 365→30 days). Estimated ~2 weeks until full at current rate. https://mahifx.pagerduty.com/incidents/Q114Z685M3X0C1

> [resolved] 2026-05-11 — Nathan Burch asks if SYNAPSE_MT5_UAT_BACKUP & SYNAPSE_MT5_UAT FIX connections should be live
> Nathan queried in #internal-fintokei whether these UAT FIX connections were supposed to be connected. Maten Rehimi confirmed same day they are expected to be down. [permalink](https://mahifx.slack.com/archives/C08R694QVNX/p1778468805865709)

> [resolved] 2026-05-18 — new MT5 demo group `FNTKCONTZRJPY` added to MAHI
> Jan requested addition of demo group `demo\\AXSE Prop\\Fintokei\\FNTKCONTZRJPY` (ZRJPY product) on 2026-05-12; Kate acknowledged and confirmed completed by 2026-05-18. [request](https://mahifx.slack.com/archives/C08QWKFARDL/p1778580729147629) [confirmed](https://mahifx.slack.com/archives/C08QWKFARDL/p1779110385964649)

> [resolved] 2026-05-05 — client-side "Jan" reports position close failure on account 6027381
> Jan reached out via #mahi-fintokei reporting an issue closing positions 28614965 and 28618336 on account 6027381, attaching a journal screenshot (UTC+3 timezone). Kate Stagg acknowledged and Will Denny followed up at 16:33 confirming the trades show as filled in Compass. Jan replied 2026-05-06 confirming they resolved it internally. [permalink](https://mahifx.slack.com/archives/C08QWKFARDL/p1777988138576279) [Will Denny follow-up](https://mahifx.slack.com/archives/C08QWKFARDL/p1777995236877329)

> [open] 2025-12-02 — Adam (Fintokei) unable to see live pricing in Compass
> Adam raised in #mahi-fintokei that he couldn't see live pricing in Compass. Bonnie (Mahi) acknowledged and said she was checking. No resolution confirmed in thread. [report](https://mahifx.slack.com/archives/C08QWKFARDL/p1764682062781469)

> [resolved] 2025-11-10 — Pau (Fintokei) reports orders cancelled with "Liquidity violation"
> Pau raised an issue where orders were cancelled with a "Liquidity violation" message. Kate Stagg (Mahi) investigated and identified the cause as the "Mid Distance Check" — the price had moved at the time of the order, triggering the protection. [report](https://mahifx.slack.com/archives/C08QWKFARDL/p1762789306265089)

> [resolved] 2025-11-06 — Graphite disk full on fintokei server
> Flagged in #internal-fintokei: Graphite disk full. Andrew Morgan (Mahi) deleted Signals stats (not mid diff pnl) to free space; Liam Cordelle resized the disk. Resolved same day. [disk full](https://mahifx.slack.com/archives/C08R694QVNX/p1762439401659699) [deleting stats](https://mahifx.slack.com/archives/C08R694QVNX/p1762439520375309)

> [watching] 2025-07-08 — LR disabled per client request; still very low utilisation as of early 2026
> LR fully disabled per Fintokei's request on ~2025-07-08 due to slippage-sensitive client base. Global LR applied gently from 2025-07-15. As of Feb 2026 Daria (Mahi) flagged LR PnL still very low (~$5.9k on 58.9B volume, ~$0.1/M); Kate Stagg said she'd discuss with Roman (Fintokei) in March 2026 whether to include LR in published price. No resolution confirmed. [LR apply](https://mahifx.slack.com/archives/C08R694QVNX/p1752589418837899) [Feb 2026 flag](https://mahifx.slack.com/archives/C08R694QVNX/p1770762875006809) [Mar 2026 follow-up](https://mahifx.slack.com/archives/C08R694QVNX/p1773318229000979)

## Notable topics

- **2026-06-24 — pricerLSB1/2 added to infra** — Kate Stagg noted infra deploying to add `pricerLSB1/2` to the Fintokei stack, setting up in preparation for alerting. Dashboard restarted shortly after. Routine topology addition; no client impact flagged. [infra deploy](https://mahifx.slack.com/archives/C08R694QVNX/p1782298252000339)

- **Weekly FI PnL snapshots** — Kate Stagg started posting weekly FI PnL snapshots in #mahi-fintokei from ~2025-11-24, running ~$310–313k/week (~$5/M). [first snapshot](https://mahifx.slack.com/archives/C08QWKFARDL/p1764004819102009)

- **Crypto addendum executed** — crypto addendum fully executed 2025-09-02, live from start of that week. [confirmed](https://mahifx.slack.com/archives/C08R694QVNX/p1756813051563939)

- **Beeks admin server recurring outages (mid-2025)** — recurring NIC / connectivity outages on Beeks admin server escalated to Beeks company owner Gordon. NICs replaced weekend of ~2025-07-05; resolved mid-July 2025. [escalation](https://mahifx.slack.com/archives/C08R694QVNX/p1751447125404229)

