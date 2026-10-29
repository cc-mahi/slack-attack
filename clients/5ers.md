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
last_catchup: 2026-10-29T07:19:02Z
status: active
---
## Now
CHURN RISK: on the 2026-10-20 weekly call Yaniv said he wants to give 3 months' notice, citing the Beeks incidents ("two issues too many") and an unnamed rival offering skew/LR at under 50% of our fees with seamless failover; a C-level follow-up call with Yaniv is set for 2026-10-21 13:45 UK (he is away from 10-22 for ~a week) and Andrew has asked for a performance/comms review since Nov 2025. Funded flow runs through the YourBourse X-Connect; the NIC fix is done on the optic but the server is still on the backup NIC (move back to primary pending), and Beeks owes RCAs for the 09-28 reboot and the 10-16 London outage. Compass 26.4 release went out in the 10-23 to 10-25 weekend window (CHG-2610-VSHM); 57 single stocks are loaded but unpriced (needs a B2Broker feed). Funded XC limit-order cancels are mostly cured; demo flow on Compass is stalled on the fee.

## Streams

### churn-risk-1020 — Yaniv's notice threat and retention response
status: open · since: 2026-10-20 · last: 2026-10-27
State: 2026-10-27 plan (Kate, #internal-5ers): adaptive sized skew rolled out that day; single stocks are in the system and Kate will hunt the feed mappings to subscribe overnight; this week a funded pricing model (space being cleared on the box, set up by end of week for Yaniv's return) and weekend gold proxied. Andrew wants progress shared in the main channel as hero moments, asked for fresh value-add moments (Justin deployed a dashboard with value-add Findings and Price Forensics screens 10-27), and wants an MT5 price feed set up to consume the competitor (Kate: not priced at 5ers; Andrew: a manager account can feed it). Earlier: Internal retrospective 10-21 (Andrew, Kate, Will; huddle notes in #internal-5ers): Andrew's read is that 5ers will give 3 months' notice anyway and Mahi must make its case alongside the rival. Retention plan, one answer per negative point: make Mahi single-region rather than only single-server tolerant (Andrew: cover that cost out of our fee, after the Beeks account complaints), set up all asset classes (Kate/Andrew will add single stocks; Will asks to make more of taking on futures for free), set up weekend gold as an evaluation, and show a spike in value-add. Kate is writing a client-facing published version of the review; Andrew has an artifact with the full list and says this is the bar across all clients. Yaniv is away from 10-22 for about a week. Kate: the XC was the main blocker, then the extra demo price ($30k discounted) was; 5ers execute most flow on TOB because of MT depth settings, so they were executing on Mahi's skewed price. Demo flow earned $81.5M skew capture on $16.8tn ($4.86/M) over the same window, so they use our price without executing; Andrew wants to scope that into value-add and says the two-clients-one-pricing-model variation objection needs handling. Andrew will add running fully funded and graduate accounts in the system. Kate reported a bad 2026-10-20 call: a bad 2026-10-20 call: Yaniv is unhappy with Beeks (two issues too many, thousands of tickets and client refunds on 5ers' side; he had thought Beeks only touched the XC, Kate explained they host the trading servers) and wants to give 3 months' notice now so 5ers can trial a competitor inside the notice window and can still reverse. The rival (unnamed) offers skew and LR with "better architecture" at under 50% of our fees; Yaniv will share its test feedback. Kate told him Mahi is disappointed in Beeks and looking at other hosts, and wants a C-level follow-up, which Yaniv accepted for 10-21 13:45 (the weekly-call slot). Internally Andrew asked for an assessment of performance, reports/comms and added functionality since Nov 2025; noted Mahi earns about $6.3/M on gold (43% of XC volume) with room to improve; there is no adaptive sized skew or PSM on 5ers and classification is not used for client experience (Kate: no B-book classified flow, toxic gets harsher execution, catch-all takes the rest), and Kate will update the skew config. Andrew thinks the competitor may be Boltzmann (skew rev-share, no fixed fee) and wants new products and hero moments, though adaptive sized skew is "no point unless we coordinate around messaging". 5ers are still on release 26.3; 26.4 needs a weekend release (Justin), and Andrew asked Justin/Leonardo to deploy the latest dashboard.
Next: Kate to send the client-facing review and publish hero moments to the main channel; Justin/Kate to set up the funded pricing model and weekend-gold proxy before Yaniv returns; Andrew/Kate to set up an MT5 feed for the competitor; Andrew to feed in the funded/graduate point and scope the demo-flow value-add; plan single-region, all-asset-class and weekend-gold evaluation work; Justin to schedule the 26.4 weekend release; consider alternative hosting to Beeks. Outcome of the 10-21 13:45 call not seen in Slack.
Refs: https://mahifx.slack.com/archives/C079M09MGGP/p1792502905672309 https://mahifx.slack.com/archives/C079M09MGGP/p1792589201530159 https://mahifx.slack.com/archives/C079M09MGGP/p1793099110414249 https://mahifx.slack.com/archives/C079M09MGGP/p1793111560735969

### adaptive-skew-rollout — Adaptive sized skew rolled out
status: open · since: 2026-10-27 · last: 2026-10-27
State: Kate rolled out adaptive sized skew in 5ers' environment on 2026-10-27 and told the client: skew now scales with market speed (larger in fast markets, unchanged in quiet). Part of the retention plan; impact on the book to be reviewed over the coming weeks.
Next: Kate to review impact on the book and feed it into value-add.
Refs: https://mahifx.slack.com/archives/C07AQJS4E80/p1793124677300249 https://mahifx.slack.com/archives/C079M09MGGP/p1793099110414249

### stock-cfd-request — New stock CFD instruments (~57 tickers)
status: open · since: 2026-09-29 · last: 2026-10-27
State: Andreas asked for ~55 US/EU single stocks; they are now part of the retention offer. On 2026-10-23 Isaac loaded all 57 from his list into 5ers Compass as reference data (names-only import, one equity asset + one USD CFD per stock, e.g. AAPL/AAPLUSD; Mattel is MATTEL as MAT clashes with a crypto asset); he skipped a change record (Liam flagged it, bounce of systemNotificationProcessor2 was clean). Naming convention is under debate (Liam's Finotive pattern: asset AAPLx, instrument AAPL; Andrew wants ticker consistency checked against top retail sites). The blocker is price: B2Broker's 5ers session carries no stocks, so 5ers must confirm B2Broker can stream these names and their symbols. Isaac asked Andreas this 10-23; Andreas replied he must first discuss internally. Support is limited: no dividend, corporate-action or equity-news feed (a split means manual handling; only AAPL, AMZN, GOOGL, META, MSFT, NVDA, TSLA have econ-news drivers). Andrew wants a KB/upsell article and PDFs on stock capacity.
Update 2026-10-27: Kate said the stocks are in the system and she will look for symbol mappings herself to subscribe overnight, with a further update to 5ers due 10-28.
Next: Andreas to come back after internal discussion and ask B2Broker about the feed; Isaac to settle naming and map subscriptions/pricing once symbols are known.
Refs: https://mahifx.slack.com/archives/C07AQJS4E80/p1790672163941279 https://mahifx.slack.com/archives/C079M09MGGP/p1792757497794269 https://mahifx.slack.com/archives/C07AQJS4E80/p1792759023540679 https://mahifx.slack.com/archives/C079M09MGGP/p1793099110414249

### xc-demo-flow — Moving demo/grad flow onto the XC
status: open · since: 2026-07-29 · last: 2026-10-21
State: Main reason for the XC push was demo flow, but Yaniv (2026-08-25 call) is reluctant to pay the additional ~$35k for demo flow while already using Mahi pricing and executing mostly on TOB. Kate offered an ROI sim. Yaniv also asked for latency/performance metrics; Kate's 08-28 view is fill ratio (99.6-99.9% vs 93-96% on the old MT5 path) and flat skew PnL, and plans to share only after two clean weeks under the LIVE ruleset. YB_DEMO_CLIENTS already added to the DEMO ruleset. Billing context (internal, 08-24): there is no bridge line item; Compass fees are discounted ~50% permanently, and Kate wants the billing structure confirmed since fees were discounted for lack of demo flow.
Update 2026-10-21: the ROI sim is still owed (Andrew asked what the 'demo-flow payout sim' is) and is now part of the retention case; demo flow already runs on Mahi pricing and shows $4.86/M skew capture.
Next: Kate to run the ROI sim and send Yaniv fill ratio / rejections.
Refs: https://mahifx.slack.com/archives/C079M09MGGP/p1785317110665399 https://mahifx.slack.com/archives/C079M09MGGP/p1787663051652619 https://mahifx.slack.com/archives/C079M09MGGP/p1787926196028439 https://mahifx.slack.com/archives/C079M09MGGP/p1792581592949149

### beeks-ld-outage-1016 — 2026-10-16 Beeks London network outage
status: open · since: 2026-10-16 · last: 2026-10-16
State: Between ~10:10 and 11:35 UK on 2026-10-16 a network outage across Beeks' London campus intermittently dropped 5ers' sessions, causing rejections, 3s+ stale pricing and cTrader gaps (5ers' second such incident; Andreas objected to switching pricing/execution mid-session). Kate advised failover; cTrader has no alternate price source so she suggested adding a YourBourse failover for it. Stable from ~11:35, 5ers switched pricing and execution back to the XC at 13:50 UK and reported normal. YB flagged six stale FIX orders and two execution timeouts as possible unhedged exposure; Mahi (Kate) and YB both confirmed none reached Mahi's engine, so nothing was filled or unhedged.
Next: Beeks to deliver the full RCA, then Kate sends 5ers an incident report; 5ers to consider a cTrader price failover.
Refs: https://mahifx.slack.com/archives/C07AQJS4E80/p1792143475688329 https://mahifx.slack.com/archives/C07AQJS4E80/p1792152998534239 https://mahifx.slack.com/archives/C0AUF6LBZ0Q/p1792158852575859 https://mahifx.slack.com/archives/C07AQJS4E80/p1792155150067909

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

### fx-spread-tuning — FX spread widening / zero-spread requests
status: watching · since: 2026-08-20 · last: 2026-09-15
State: Fast-markets multiplier raised to 1.3 for CFDs and metals (2026-08-20). Andreas questioned ~130-170 point FX spikes around the 20:59-22:00Z daily rollover (2026-09-10); Rory explained it is LP feed widening with a cap in place and offered a lower multiplier. On 2026-09-14 5ers asked for EURUSD/GBPUSD/USDJPY at 0; Kate set base spread 0, cTrader briefly showed negative spreads (5ers-side markdown, fixed), and Yaron confirmed it looked good 2026-09-15. YB later noted 72-93% zero-spread ticks on those pairs.
Refs: https://mahifx.slack.com/archives/C07AQJS4E80/p1787221538992459 https://mahifx.slack.com/archives/C07AQJS4E80/p1789466160780809

### xc-funded-migration — XC cleanup after funded flow cutover
status: watching · since: 2026-07-07 · last: 2026-09-08
State: XC delivered 2026-07-28 after YB delays; funded flow moved 2026-08-17 and all funded (incl. TradingView after the counterparty-tag fix, YB now sends account id in tag 448) routed via XC by 2026-08-25. On 2026-08-28 Kate found the XC flow had run on the catch-all ruleset for two weeks (no classification) with no measured cost; fixed (v35) and classification added to CATCHALL. On 08-25 YB found cTrader/UAT/MT5 DEV sessions still on the Mahi LP; MT5 DEV and UAT were repointed to the XC (cTrader on YB unused per Andreas), and on 09-08 YB confirmed MT5 Main and MT5 Exp use the XC prices while MT5 TSG uses match prime. Old MT5 gateways were set up as 5ers' failovers; Kate leaned to decommission them and asked YB (08-25) to retire the 5ers-Funded-YB-MT5 Orders/Prices connections, but YB never confirmed retirement and Kate flagged a billing risk if removing the gateways reduces fees (billing structure never agreed). 2026-08-26 cTrader flow, missing for weeks, was routed back to Compass after Andreas found a fault on their side.
Next: confirm YB retired the old MT5 connections and decide on decommissioning the MT5 gateways after the billing check.
Refs: https://mahifx.slack.com/archives/C079M09MGGP/p1783426138434659 https://mahifx.slack.com/archives/C079M09MGGP/p1786959572664399 https://mahifx.slack.com/archives/C079M09MGGP/p1787565915372879 https://mahifx.slack.com/archives/C0AUF6LBZ0Q/p1788879639154749

### yb-mt5-feed-filters — XPDUSD / ESXEUR / BTCEUR feed stops
status: closed · since: 2026-09-04 · last: 2026-09-04 · closed: 2026-10-15
State: Feeds stopped on 5ers' MT5 because their YourBourse discard-filtration (500 points) dropped a large gap quote; Mahi confirmed it was streaming. Linos widened the XPDUSD discard filter from 500 to 2000 points (feed back); ESXEUR was fixed by a gateway restart and BTCEUR by a filter adjustment; Linos confirmed resolved 2026-09-04.
Refs: https://mahifx.slack.com/archives/C0AUF6LBZ0Q/p1788516970494359 https://mahifx.slack.com/archives/C07AQJS4E80/p1788529520937229

### usdchf-spike-1027 — USDCHF bad-price report
status: closed · since: 2026-10-27 · last: 2026-10-27 · closed: 2026-10-28
State: Andreas reported bad USDCHF pricing and a spike at 20:42 UTC+3 on 2026-10-27; Kate found Mahi distributing normal pricing, USDCHF untouched by that day's skew change, and the quote not originating from Mahi. Andreas concluded it was not Mahi's side and 5ers would handle it.
Refs: https://mahifx.slack.com/archives/C07AQJS4E80/p1793125044157899 https://mahifx.slack.com/archives/C07AQJS4E80/p1793127218839519

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
- 2026-10-20 — Yaniv signals intent to give 3 months' notice over Beeks incidents and a cheaper rival; C-level call set for 10-21
- 2026-10-27 — adaptive sized skew rolled out at 5ers as part of the retention plan
