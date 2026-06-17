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
last_catchup: 2026-06-17T07:28:54Z
---

## Status

- Stage: live — prop-firm B-book, low-spread pricing model in production.
- Integration: live — Fintokei MT5 via Compass on `fintokei-ln-*`, YourBourse FIX connector being set up. CLIENT_PRICE_LDN distribution.
- Relationship: active — Kate Stagg / Rory King client-facing; Adam (Fintokei) primary client-side contact.

## Recent issues

> [open] 2026-06-16 — New model pricing question: setup fee vs monthly cost, unanswered
> Kate Stagg (Mahi) asked in #internal-fintokei whether to charge for a new model for Fintokei — they previously got one set up at no cost as a goodwill gesture. Kate's suggestion: one-off setup fee, no monthly cost (unusual commercial structure). No reply yet. [question](https://mahifx.slack.com/archives/C08R694QVNX/p1781610571053819)

> [open] 2026-06-16 — BMSL timezone deploy requested via Zendesk #23102
> Kate Stagg (Mahi) raised a Zendesk ticket for a BMSL timezone deploy for Fintokei. [ticket](https://mahifx.zendesk.com/agent/tickets/23102) [internal note](https://mahifx.slack.com/archives/C08R694QVNX/p1781610590423249)

> [resolved] 2026-06-15 — Slippage complaint: account 6032915, 6 simultaneous fills on 2026-06-14 ~22:00 UTC
> Pau (Fintokei) raised a complaint that one of 6 simultaneously-filled positions for FintokeiMT5C_6032915 received significantly higher slippage. Rory King (Mahi) acknowledged and investigated. Cameron Hughes (Mahi) explained: FINTOKEI market spreads blew out briefly, causing Mahi's pricing model to defensively widen in response, and the trade came in on that wider published spread. Pau reacted with `:thankyou:`. [complaint](https://mahifx.slack.com/archives/C08QWKFARDL/p1781524010061899) [CH explanation](https://mahifx.slack.com/archives/C08QWKFARDL/p1781524666634919)

> [resolved] 2026-05-29 — MT5 build 5830 server update: Mahi confirms no gateway impact
> Jan asked in #mahi-fintokei whether Fintokei's planned weekend update of MT5 servers to build 5830 would cause issues to the gateway. Rory King (Mahi) confirmed no issues expected on Mahi's side. Jan thanked and acknowledged. [question](https://mahifx.slack.com/archives/C08QWKFARDL/p1780059694047829) [Rory confirms OK](https://mahifx.slack.com/archives/C08QWKFARDL/p1780060200072389)

> [open] 2026-05-25 — MT4 bridge update causes trade rejections; rollback done, root cause unconfirmed
> Adam (@fintokei) raised a <!channel> alert at 02:00 BST: trades being rejected by the MahiFXMT4Bridge before reaching Compass after a weekend bridge update — clients unable to close positions or delete pending orders (example: account 30145252, 176.97 lots BUY JP225). Isaac Dann (Mahi) investigated, requested MT4 logs (248MB log provided), and proposed rollback + setting `UNIFIED REQUEST IDS=N` in the MT4 EB plugin. Adam rolled back and set the flag, but confirmed `UNIFIED REQUEST IDS` was already set to `N`, meaning the config change was not the cause. Isaac noted a dev review is still needed to confirm root cause. Status at 02:46 BST: rollback done, partial traffic flowing, full resolution unconfirmed. [alert](https://mahifx.slack.com/archives/C08QWKFARDL/p1779670858863209) [rollback thread](https://mahifx.slack.com/archives/C08QWKFARDL/p1779672373610029) [dev review flagged](https://mahifx.slack.com/archives/C08QWKFARDL/p1779673574470809)

> [open] 2026-04-16 — `fintokei-ln-trading-1` mysql volume at 90%
> Cameron flagged in #internal-fintokei (2026-04-16 16:41 BST): archiver retention defaults left in place on `PROD_LIVE_CLIENTDB`, top tables (EnrichedTradeOutputSummary 89GB, HouseOrder 84GB, HOUSE1PositionHistory 67GB) growing fast. LVM has ~1.26TB free so growing the volume buys time, but real fix is archiver overrides matching Funding Pips (POSITION_HISTORY 365→3 days, ORDER_HISTORY 365→30 days). Estimated ~2 weeks until full at current rate. https://mahifx.pagerduty.com/incidents/Q114Z685M3X0C1

> [resolved] 2026-05-11 — Nathan Burch asks if SYNAPSE_MT5_UAT_BACKUP & SYNAPSE_MT5_UAT FIX connections should be live
> Nathan queried in #internal-fintokei whether these UAT FIX connections were supposed to be connected. Maten Rehimi confirmed same day they are expected to be down. [permalink](https://mahifx.slack.com/archives/C08R694QVNX/p1778468805865709)

> [resolved] 2026-05-18 — new MT5 demo group `FNTKCONTZRJPY` added to MAHI
> Jan requested addition of demo group `demo\\AXSE Prop\\Fintokei\\FNTKCONTZRJPY` (ZRJPY product) on 2026-05-12; Kate acknowledged and confirmed completed by 2026-05-18. [request](https://mahifx.slack.com/archives/C08QWKFARDL/p1778580729147629) [confirmed](https://mahifx.slack.com/archives/C08QWKFARDL/p1779110385964649)

> [resolved] 2026-05-05 — client-side "Jan" reports position close failure on account 6027381
> Jan reached out via #mahi-fintokei reporting an issue closing positions 28614965 and 28618336 on account 6027381, attaching a journal screenshot (UTC+3 timezone). Kate Stagg acknowledged and Will Denny followed up at 16:33 confirming the trades show as filled in Compass. Jan replied 2026-05-06 confirming they resolved it internally. [permalink](https://mahifx.slack.com/archives/C08QWKFARDL/p1777988138576279) [Will Denny follow-up](https://mahifx.slack.com/archives/C08QWKFARDL/p1777995236877329)

## Notable topics

