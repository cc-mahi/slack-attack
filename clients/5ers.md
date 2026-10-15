---
slug: 5ers
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/5ers.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: 5ers
  hosts: ../MahiProduct/data/client-hosts.json          # entry: 5ers
  wiki: ../MahiProduct/wiki/clients/5ers.md
channels:
  internal-5ers: C079M09MGGP
  mahi-the-five-percenters: C07AQJS4E80
  5ers-mahi-yourbourse: C0AUF6LBZ0Q
contacts:
  - {name: "Andreas Michael", role: "5ers trading ops — main day-to-day contact (YourBourse bridge, spreads, instruments)", confidence: low}
  - {name: "Yaniv Elbaz", role: "5ers senior stakeholder — weekly calls, commercial", confidence: low}
  - {name: "Yaron Farjun", role: "5ers stakeholder — spreads / feed quality", confidence: low}
  - {name: "Linos Astreos", role: "5ers trading ops — MT5/YB bridge issues, instrument feeds", confidence: low}
  - {name: "Constantinos P", role: "5ers trading ops — pricing/execution checks", confidence: low}
  - {name: "Kirill Oleskevic", role: "YourBourse support — shared channel tickets", confidence: low}
  - {name: "Valter Timanov", role: "YourBourse — MT5 filtration / bridge diagnostics", confidence: low}
last_catchup: 2026-10-15T12:57:40Z
status: active
---
## Now
Funded flow runs through the YourBourse X-Connect (since 2026-08-17/25). The 2026-09-25 NIC-degradation incident is fixed on the optic, but the server still runs on the backup NIC; the move back to primary was pushed to a later weekend. Funded XC limit-order cancels are mostly cured (SEND_ORIGINAL_REQUEST_PRICE=TRUE, fills ~99%); a switch to market orders was agreed 2026-10-13. Demo flow on Compass is stalled on 5ers' reluctance to pay the extra fee.

## Streams

### xc-order-cancels — Funded XC limit-order cancels and rejects
status: open · since: 2026-09-11 · last: 2026-10-13
State: YB reprices client limit orders at the bridge off its own TOB, so LR/Mid Distance Check cancelled them as off market (YB-flagged 2026-09-09 XAUUSD IOCs; acct 11207 looping GBPUSD limits from 2026-10-08; fills fell to 48-69% on 7-9 Oct). YB set SEND_ORIGINAL_REQUEST_PRICE=TRUE (2026-10-11) and fills went to 99% on 12-13 Oct; ~0.5% still cancelled off market (100-300/day, 8 accounts). Andreas agreed (2026-10-12/13) to send all orders as market; YB says MT5 flow is already market (40=1) and the remaining limits (40=2) come from the 5ers Trade Server flow, asking for confirmation. Isaac also moved Mid Distance Check on Custom 2 / toxic / B Book rules negative on 2026-09-16 after USDJPY closes were rejected.
Next: 5ers/YB to confirm Trade Server flow switches to market orders; Kate to keep SEND_ORIGINAL_REQUEST_PRICE=TRUE until agreed.
Refs: https://mahifx.slack.com/archives/C0AUF6LBZ0Q/p1789122645463079 https://mahifx.slack.com/archives/C0AUF6LBZ0Q/p1791458258776889 https://mahifx.slack.com/archives/C079M09MGGP/p1791891409913529 https://mahifx.slack.com/archives/C079M09MGGP/p1791892556648959

### nic-degradation-0925 — 2026-09-25 stale pricing + cTrader drop, Beeks NIC
status: open · since: 2026-09-25 · last: 2026-10-07
State: 2026-09-25 5ers saw delayed prices / extreme slippage on MT5 via the XC; cause was a degraded optic on 5ers-ln-trading-1's primary NIC (Beeks). Beeks' manual failover to the backup NIC then dropped cTrader (backup switchport had no VLANs; cTrader has no failover at 5ers) and the box rebooted unprompted on 2026-09-28 (unexplained). 5ers moved funded flow to B-book/other pricing from 09-25 and returned to Mahi 2026-09-29; incident report sent 2026-09-29. Optic replaced 2026-09-26 and clean since; server still on the backup NIC. The planned switch to primary (Sat 10 Oct 21:00-22:00Z, agreed with Andreas) was rescheduled to "next weekend", exact window TBC. Arun wrote a post-change verification script.
Next: Beeks to confirm the new window (tickets NOCINT-847123, 848128, 848378); Kate to re-confirm timing with 5ers (Yaniv wants post-change monitoring).
Refs: https://mahifx.slack.com/archives/C07AQJS4E80/p1790343904474559 https://mahifx.slack.com/archives/C07AQJS4E80/p1791206464396519 https://mahifx.slack.com/archives/C079M09MGGP/p1791385218922749

### stock-cfd-request — New stock CFD instruments (~55 tickers)
status: open · since: 2026-09-29 · last: 2026-09-29
State: Andreas asked whether Mahi can price a list of US/EU single stocks (AAPL, TSLA, NVDA, etc). Kate said Mahi does not price all of them and will check whether they can be sourced. No answer seen since.
Next: Kate to revert on sourcing.
Refs: https://mahifx.slack.com/archives/C07AQJS4E80/p1790672163941279 https://mahifx.slack.com/archives/C07AQJS4E80/p1790674453347299

### fx-spread-tuning — FX spread widening / zero-spread requests
status: watching · since: 2026-08-20 · last: 2026-09-15
State: Fast-markets multiplier raised to 1.3 for CFDs and metals (2026-08-20). Andreas questioned ~130-170 point FX spikes around the 20:59-22:00Z daily rollover (2026-09-10); Rory explained it is LP feed widening with a cap in place and offered a lower multiplier. On 2026-09-14 5ers asked for EURUSD/GBPUSD/USDJPY at 0; Kate set base spread 0, cTrader briefly showed negative spreads (5ers-side markdown, fixed), and Yaron confirmed it looked good 2026-09-15. YB later noted 72-93% zero-spread ticks on those pairs.
Refs: https://mahifx.slack.com/archives/C07AQJS4E80/p1787221538992459 https://mahifx.slack.com/archives/C07AQJS4E80/p1789466160780809

### xc-demo-flow — Moving demo/grad flow onto the XC
status: watching · since: 2026-07-29 · last: 2026-08-28
State: Main reason for the XC push was demo flow, but Yaniv (2026-08-25 call) is reluctant to pay the additional ~$35k for demo flow while already using Mahi pricing and executing mostly on TOB. Kate offered an ROI sim. Yaniv also asked for latency/performance metrics; Kate's 08-28 view is fill ratio (99.6-99.9% vs 93-96% on the old MT5 path) and flat skew PnL, and plans to share only after two clean weeks under the LIVE ruleset. YB_DEMO_CLIENTS already added to the DEMO ruleset.
Next: (watching, no Slack activity since 2026-08-28) Kate to run the ROI sim and send Yaniv fill ratio / rejections once two clean weeks exist (could be due now).
Refs: https://mahifx.slack.com/archives/C079M09MGGP/p1785317110665399 https://mahifx.slack.com/archives/C079M09MGGP/p1787663051652619 https://mahifx.slack.com/archives/C079M09MGGP/p1787926196028439

### xc-funded-migration — XC cleanup after funded flow cutover
status: watching · since: 2026-07-07 · last: 2026-08-28
State: XC delivered 2026-07-28 after YB delays; funded flow moved 2026-08-17 and all funded (incl. TradingView after the counterparty-tag fix) routed via XC by 2026-08-25. On 2026-08-28 Kate found the XC flow had run on the catch-all ruleset for two weeks (no classification) with no measured cost; fixed (v35) and classification added to CATCHALL. Old MT5 gateways were set up as 5ers' failovers; Kate leaned to decommission them and asked YB/5ers to retire the non-XC connection. 2026-08-26 cTrader flow, missing for weeks, was routed back to Compass after Andreas found a fault on their side.
Next: confirm the old non-XC YB connection and MT5 gateways are retired.
Refs: https://mahifx.slack.com/archives/C079M09MGGP/p1783426138434659 https://mahifx.slack.com/archives/C079M09MGGP/p1786959572664399 https://mahifx.slack.com/archives/C079M09MGGP/p1787654688140719 https://mahifx.slack.com/archives/C079M09MGGP/p1787926196028439

### yb-mt5-feed-filters — XPDUSD / ESXEUR / BTCEUR feed stops
status: closed · since: 2026-09-04 · last: 2026-09-04 · closed: 2026-10-15
State: Feeds stopped on 5ers' MT5 because their YourBourse discard-filtration (500 points) dropped a large gap quote; Mahi confirmed it was streaming. Linos widened the filters and a gateway restart fixed ESXEUR/BTCEUR; resolved 2026-09-04.
Refs: https://mahifx.slack.com/archives/C0AUF6LBZ0Q/p1788516970494359 https://mahifx.slack.com/archives/C07AQJS4E80/p1788529520937229

## Arc
- 2026-04 — B2Broker weekend session breaks caused crypto/CFD indicative pricing; crypto and CFD feed enrichment deployed (04-30/05-01)
- 2026-04-28 — T4B to YourBourse demo flow migration complete
- 2026-05-19 — cTrader US-client cutoff from 06-01; 5ers moving to YB with TradingView front-end
- 2026-07-18 — crypto outage during Compass release (B2Broker normalisation reset)
- 2026-07-28 — cross-connect into LD4/LD6 delivered after weeks of YB delay
- 2026-08-11 — YB LON1 DDoS caused stale-FIX episodes (also 06-12, 07-03, 07-31)
- 2026-08-17 — funded flow switched to the XC; fully routed via XC by 08-25
- 2026-08-20 — Yaniv: 5ers have not bought a new broker (only TSG); new senior manager joining
- 2026-09-25 — Beeks NIC degradation incident; 5ers off Mahi pricing/execution until 09-29
