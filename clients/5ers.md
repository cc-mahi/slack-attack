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
last_catchup: 2026-10-16T07:05:25Z
status: active
---
## Now
Funded flow runs through the YourBourse X-Connect (since 2026-08-17/25). The 2026-09-25 NIC-degradation incident is fixed on the optic, but the server still runs on the backup NIC; the move back to primary was pushed to a later weekend (window TBC) and Beeks still owes an answer on the unexplained 09-28 reboot. Funded XC limit-order cancels are mostly cured (YB set SEND_ORIGINAL_REQUEST_PRICE=TRUE 2026-10-09, fills ~99%); 5ers agreed 10-13 to market orders but YB says MT5 is already market and the remaining limits come from the Trade Server flow, so it awaits confirmation. Demo flow on Compass is stalled on 5ers' reluctance to pay the extra fee.

## Streams

### xc-order-cancels — Funded XC limit-order cancels and rejects
status: open · since: 2026-09-11 · last: 2026-10-13
State: YB reprices client limit orders at the bridge off its own TOB (SEND_ORIGINAL_REQUEST_PRICE defaults to false), so Mahi's LR/Mid Distance Check cancelled them as off market (YB-flagged 2026-09-09 XAUUSD IOCs, LIQUIDITY_VIOLATION; acct 11207 looping GBPUSD limits from 2026-10-08, also classified arbitrageur so on continuity-pool pricing; up to half of orders cancelled 7-9 Oct, 64-85%/h worst, fills 48-69%). Linos approved the change 2026-10-09; YB set SEND_ORIGINAL_REQUEST_PRICE=TRUE and restarted the LM that evening (Shyam only announced it internally 10-11). Fills were ~99% on 12-13 Oct; ~0.5% still cancelled off market (100-300/day, 8 accounts). Kate asked YB 10-12 for market orders (40=1) and keep the flag TRUE; Andreas agreed 10-13 ("proceed as you suggested"); YB's 10-13 reply says MT5 flow is already market, including triggered TP/limits, and the remaining 40=2 limits come from the 5ers Trade Server flow, asking for confirmation; YB ticket stays open until the order type is agreed. Andrew Morgan (internal) backs market orders and asked for off-market tracking. Isaac moved Mid Distance Check negative on Custom 2 / toxic / B Book rules 2026-09-16 after USDJPY closes were rejected (Will told Linos 09-22 it was fixed).
Next: Kate/5ers to answer YB's 10-13 question (Trade Server flow to market) and YB to action it; keep SEND_ORIGINAL_REQUEST_PRICE=TRUE meanwhile.
Refs: https://mahifx.slack.com/archives/C0AUF6LBZ0Q/p1789122645463079 https://mahifx.slack.com/archives/C0AUF6LBZ0Q/p1791905136357879 https://mahifx.slack.com/archives/C0AUF6LBZ0Q/p1791892394986009 https://mahifx.slack.com/archives/C079M09MGGP/p1791891409913529

### nic-degradation-0925 — 2026-09-25 stale pricing + cTrader drop, Beeks NIC
status: open · since: 2026-09-25 · last: 2026-10-09
State: 2026-09-25 5ers saw delayed prices / extreme slippage on MT5 via the XC and cTrader dropped; cause was a degraded optic on 5ers-ln-trading-1's primary NIC (Beeks). Beeks' manual failover to the backup NIC left the box unreachable ~38 min (backup switchport never had VLANs; cTrader has no failover at 5ers). On 2026-09-28 the server rebooted mid-flow while Beeks were on the console: Mahi's logs show a SIGINT (Ctrl-Alt-Del) from a Beeks console session (beeksadmin, tty1) and no Mahi user action, but Beeks deny it and have not yet answered the reboot / why-degradation-wasn't-flagged questions (NOCINT-848378; Gavin's 10-02 reply on NOCINT-847123 was unhelpful and Inald re-asked). That day Mahi briefly sat idle believing it was blocked on Beeks' logical change for the primary; Beeks said the backup is fine to use, so flow resumed on it. 5ers moved funded flow to B-book from 09-25 and returned to Mahi 2026-09-29; incident report sent 09-29, committing only to better latency monitoring and earlier provider detection. Optic replaced 09-26 and clean since; server still on the backup NIC. The switch to primary (Sat 10 Oct, agreed by Andreas 10-05) was rescheduled on 10-09 to "next weekend" (~17 Oct), window TBC (CHG-2610-B5YC). Arun's post-change check script is on the server (links, errors/drops, pings, named sessions up); Beeks to fail back to the backup if it fails; Yaniv wants post-change monitoring.
Next: Beeks to confirm the new window (tickets NOCINT-847123, 848128, 848378) and answer the reboot/late-detection questions; Kate to re-confirm timing with 5ers; Arun to brief Beeks on the script and record the change via /change-record.
Refs: https://mahifx.slack.com/archives/C07AQJS4E80/p1790343904474559 https://mahifx.slack.com/archives/C07AQJS4E80/p1791206464396519 https://mahifx.slack.com/archives/C079M09MGGP/p1791385218922749 https://mahifx.slack.com/archives/C079M09MGGP/p1791558129864319

### stock-cfd-request — New stock CFD instruments (~55 tickers)
status: open · since: 2026-09-29 · last: 2026-09-29
State: Andreas asked whether Mahi can price a list of ~55 US/EU single stocks (AAPL, TSLA, NVDA, etc). Kate said Mahi does not price all of them; Andreas noted 5ers gets these from B2B and Mahi may source from there, and Kate agreed but said some backend work is needed to add the instruments and she is checking feasibility. No further update seen.
Next: Kate to revert on feasibility.
Refs: https://mahifx.slack.com/archives/C07AQJS4E80/p1790672163941279 https://mahifx.slack.com/archives/C07AQJS4E80/p1790691730847859

### fx-spread-tuning — FX spread widening / zero-spread requests
status: watching · since: 2026-08-20 · last: 2026-09-15
State: Fast-markets multiplier raised to 1.3 for CFDs and metals (2026-08-20). Andreas questioned ~130-170 point FX spikes around the 20:59-22:00Z daily rollover (2026-09-10); Rory explained it is LP feed widening with a cap in place and offered a lower multiplier. On 2026-09-14 5ers asked for EURUSD/GBPUSD/USDJPY at 0; Kate set base spread 0, cTrader briefly showed negative spreads (5ers-side markdown, fixed), and Yaron confirmed it looked good 2026-09-15. YB later noted 72-93% zero-spread ticks on those pairs.
Refs: https://mahifx.slack.com/archives/C07AQJS4E80/p1787221538992459 https://mahifx.slack.com/archives/C07AQJS4E80/p1789466160780809

### xc-funded-migration — XC cleanup after funded flow cutover
status: watching · since: 2026-07-07 · last: 2026-09-08
State: XC delivered 2026-07-28 after YB delays; funded flow moved 2026-08-17 and all funded (incl. TradingView after the counterparty-tag fix, YB now sends account id in tag 448) routed via XC by 2026-08-25. On 2026-08-28 Kate found the XC flow had run on the catch-all ruleset for two weeks (no classification) with no measured cost; fixed (v35) and classification added to CATCHALL. On 08-25 YB found cTrader/UAT/MT5 DEV sessions still on the Mahi LP; MT5 DEV and UAT were repointed to the XC (cTrader on YB unused per Andreas), and on 09-08 YB confirmed MT5 Main and MT5 Exp use the XC prices while MT5 TSG uses match prime. Old MT5 gateways were set up as 5ers' failovers; Kate leaned to decommission them and asked YB (08-25) to retire the 5ers-Funded-YB-MT5 Orders/Prices connections, but YB never confirmed retirement and Kate flagged a billing risk if removing the gateways reduces fees (billing structure never agreed). 2026-08-26 cTrader flow, missing for weeks, was routed back to Compass after Andreas found a fault on their side.
Next: confirm YB retired the old MT5 connections and decide on decommissioning the MT5 gateways after the billing check.
Refs: https://mahifx.slack.com/archives/C079M09MGGP/p1783426138434659 https://mahifx.slack.com/archives/C079M09MGGP/p1786959572664399 https://mahifx.slack.com/archives/C079M09MGGP/p1787565915372879 https://mahifx.slack.com/archives/C0AUF6LBZ0Q/p1788879639154749

### xc-demo-flow — Moving demo/grad flow onto the XC
status: watching · since: 2026-07-29 · last: 2026-08-28
State: Main reason for the XC push was demo flow, but Yaniv (2026-08-25 call) is reluctant to pay the additional ~$35k for demo flow while already using Mahi pricing and executing mostly on TOB. Kate offered an ROI sim. Yaniv also asked for latency/performance metrics; Kate's 08-28 view is fill ratio (99.6-99.9% vs 93-96% on the old MT5 path) and flat skew PnL, and plans to share only after two clean weeks under the LIVE ruleset. YB_DEMO_CLIENTS already added to the DEMO ruleset. Billing context (internal, 08-24): there is no bridge line item; Compass fees are discounted ~50% permanently, and Kate wants the billing structure confirmed since fees were discounted for lack of demo flow.
Next: (watching, no Slack activity since 2026-08-28) Kate to run the ROI sim and send Yaniv fill ratio / rejections once two clean weeks exist (could be due now).
Refs: https://mahifx.slack.com/archives/C079M09MGGP/p1785317110665399 https://mahifx.slack.com/archives/C079M09MGGP/p1787663051652619 https://mahifx.slack.com/archives/C079M09MGGP/p1787926196028439

### yb-mt5-feed-filters — XPDUSD / ESXEUR / BTCEUR feed stops
status: closed · since: 2026-09-04 · last: 2026-09-04 · closed: 2026-10-15
State: Feeds stopped on 5ers' MT5 because their YourBourse discard-filtration (500 points) dropped a large gap quote; Mahi confirmed it was streaming. Linos widened the XPDUSD discard filter from 500 to 2000 points (feed back); ESXEUR was fixed by a gateway restart and BTCEUR by a filter adjustment; Linos confirmed resolved 2026-09-04.
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
