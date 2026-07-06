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
  - {name: "Todd Hodges", role: "TOT internal contact; onboarded Jan 2026 alongside Priojit for Compass product training", confidence: low}
  - {name: "Arjie", role: "MatchTrader operations contact at TOT", confidence: low}
last_catchup: 2026-07-06T07:09:21Z
---

## Status

- **Stage:** live, post-pilot; billing renegotiated Oct 2025 to $10,000/mo base + $1.00/account (Challenge + Funded)
- **Integration:** CTrader live Jul 1 2025; MT5 live ~Aug 2025; MatchTrader live Sep 15 2025; TradeLocker pending (contact lost, no ETA as of Oct 2025)
- **Relationship:** strong; weekly calls; Matt engaged and expanding; brokerage expansion discussion opened Mar 2026 (retail FX under Comoros licence, same playbook as ACG)

## Recent issues

> [resolved] 2026-07-01 — Pricing incident (Finalto/MAHI_LP_5) at ~07:43 BST; LP removed 2026-07-02
> Cameron Hughes flagged in #internal-toponetrader that the same pricing feedback loop incident seen at Infinox also hit TOT at ~07:43 BST, caused by MAHI_LP_5 (Finalto). On 2026-07-02, Liam confirmed MAHI_LP_5 is the Finalto LP from Infinox and recommended swapping it out given the feeds are untrusted; Cameron Hughes confirmed it had been removed from price formation and bounced the pricers. No client-facing communication in #mahi-toponetraders. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1782927073351899) [resolution](https://mahifx.slack.com/archives/C08TG143F4L/p1782991925017169)

> [resolved] 2026-06-01 — MatchTrader account 10408: 1.7 lot (170 XBT) order rejected; TOB depth raised
> Arjie raised that account 10408 on MatchTrader could not place a 1.7 lot position despite sufficient margin. Cameron Hughes diagnosed the order size (170 XBT) exceeded Mahi's published TOB depth; he raised the TOB tiers and imported new tiers. Arjie confirmed the large orders were being accepted by 11:03 BST; resolved same morning. [permalink](https://mahifx.slack.com/archives/C08U853T684/p1780303004735039)

> [open] 2026-05-28 — ETHUSD/XETUSD LIMIT order rejections due to 3dp pricing precision
> Isaac Dann flagged in #mahi-toponetraders that TOT is submitting ETHUSD/XETUSD LIMIT orders with 3 decimal place precision; Mahi prices and executes ETHUSD at 2dp, causing rejections. Pattern traced to mostly one counterparty. No resolution or thread replies yet as of run time. [permalink](https://mahifx.slack.com/archives/C08U853T684/p1779942346326859)

> [resolved] 2026-05-19 — BTCUSD slippage complaint; expected VWAP fill behaviour
> Arjie (TOT MatchTrader ops contact) raised a concern about a trader account 19099 (demoTOTusd-B1 group) experiencing 5–10 pip slippage on BTCUSD vs the TOB price. Nathan Burch investigated and confirmed the 65 BTC sell consumed 5 liquidity layers, producing a VWAP fill of $76,944.91 vs TOB $76,992.22 — correct behaviour. Arjie acknowledged and confirmed resolved. [permalink](https://mahifx.slack.com/archives/C08U853T684/p1779154129412389)

> [resolved] 2026-05-11 — Crypto FI skew P&L reporting bug (XBTUSD/XETUSD)
> XAUUSD yield alert (-$4,932 on Funded FX) triggered a deeper look; Cameron Hughes identified a separate FI bug: `PRICINGBENCHMARKMIDLIFETIMEPNL` on the `_CRYPTO_CLIENTS` book dropped ~-$8.7k at 15:49:05 UTC 2026-05-10 with no fill, and FI cumsums for XBTUSD froze — broken risk-reporting pipeline for crypto books. ZD ticket #22959 raised; an older fix (ZD#20890) identified as deployable. Daria updated `signalReturnBenchmarkMarketSelectors` for XBTUSD and XETUSD on 2026-05-12 and marked ticket solved. Root cause: 3 large trades around 15:46–15:47 UTC where model mid moved faster than reference mids, causing negative skew P&L. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1778555635853379)

> [resolved] 2026-05-11 — XAUUSD Funded FX yield alert (-$4,932); false alarm
> Automated ESCALATE alert on Top One Trader Funded FX · XAUUSD · -$4,932. Cameron Hughes reviewed, confirmed reporting error (one massive off-market trade distorting the yield profile). Echo showed no real P&L issue. No client impact. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1778493874264169)

> [open] 2026-03-19 — Brokerage expansion discussion
> Will Carter had introductory call with Matt Morris. TOT wants to use their Comoros FX licence to launch a retail brokerage, marketing to prop clients — full outsourced dealing desk discussed, same model as ACG. Follow-up call scheduled Monday 23 March. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1773937053278899)

> [resolved] 2026-01-02–06 — Crypto expansion to MatchTrader
> Lars requested all crypto symbols activated on MatchTrader (same list as MT5). Target launch Wednesday Jan 7. Testing on Jan 6 showed only BTC/ETH visible; Cameron Hughes worked through symbol configs and decimal place issues with Shane and Lars; all 34 crypto instruments confirmed active and testable by Jan 7. [permalink](https://mahifx.slack.com/archives/C08U853T684/p1767370386895999)

> [open] 2025-10-22 — TradeLocker integration stalled
> Ivan Juren left TradeLocker. Liam Cordelle chasing new contact (Kristijan) for re-engagement. Implementation was reportedly "far along" per a Sep 18 email from TL, but no progress since. No ETA. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1761145850804539)

## Notable topics

- 2025-11-05 — Matt's business metrics strong: avg weekly sales $24k (up from ~$4k), payout ratio 35% (trending down), consistency rule effective. Planning separate Top One Crypto site. [permalink](https://mahifx.slack.com/archives/C08TG143F4L/p1762360910675469)
