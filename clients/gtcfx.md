---
slug: gtcfx
aliases: [gtc-global-trade-capital]                       # MahiProduct billing slug
refs:
  vibepulse: null                                          # no ../VibePulse/.claude/clients/gtcfx.yaml yet
  billing: ../MahiProduct/data/billing/clients.json        # entry: gtc-global-trade-capital
  hosts: ../MahiProduct/data/client-hosts.json             # entry: gtcfx (s3Slug GTCFX; LDN)
  wiki: ../MahiProduct/wiki/clients/gtcfx.md
  onboarding: ../MahiProduct/data/onboarding/gtcfx.json    # stage tracker
channels:
  internal-gtcfx: C0AKAPLU78W
  mahi-gtcfx: C0AKRP8C049
contacts:
  - {name: Manglai, role: "GTC - main day-to-day counterpart; decides which symbols/servers move to Mahi and when"}
  - {name: Marios Lysandrou, role: "GTC - connectivity/ops; requests new OZ/Centroid/HRP sessions, reports rejects and disconnects"}
  - {name: Antreas Florentzou, role: "GTC - ops/trading; pricing controls, tag moves between A/B book, OZ session times"}
  - {name: John (Jun Yang), role: "GTC - raises pricing-quality issues (XAG quote jumps); has Compass access", confidence: low}
  - {name: Ralich, role: "OneZero - waived OZ per-million fees on GTCFX flow to Mahi; David Cooney's contact", confidence: low}
  - {name: Lochlan, role: "OneZero - internal-only escalation route if OZ fee/support talks stall; not to be shared with GTC", confidence: low}
last_catchup: 2026-11-25T08:12:31Z
status: active
---
## Now
GTC is live and ramping: FX majors/crosses, XAGUSD and XAUUSD (MT5 Live2 switched 11-09) route to Mahi over 7 OneZero hubs, plus PXM and Centroid, with an A Book account live since 2026-10-06 (HRP-only hedging).
Main risk is load and stability: cent flow drives ticket rates, and the stream overflow (Zendesk 23796) crashed signalProcess1 (skew flat since 11-05) and riskReportingExtended (5 times on 11-16; Compass PR 81 may be needed).
24/7 XAU is the priority: hosting/DR plan (AWS second set, Fabric/Megaport questions) and a new 250k tier are being scoped; GTC asked 11-16 about tXAUUSD gaps on Sat 11-14. NFP gold result (LR/skew/PSM flat) still needs an owner. On 11-23 gateway 2 rejected ~70 XAU orders at the open (queue limit raised; nine-gateway restart 22:00 UTC tonight, CHG-2611-D8ZS awaiting approval). On 11-25 the trading-1 MySQL disk filled again (4th purge in 5 days, refills in ~12h), killing hedger/risk processes and causing a 02:50-03:20 UTC XAU price gap GTC has asked about. GTC is also asking OneZero to pass SL/TP info for no-slippage execution. GTC reported an MT server issue 11-19 and Mahi's analytics plugins there are stopped pending the all clear.

## Streams

### infra-disk-alerting — Trading-server disk, replica and alert hygiene
status: open · since: 2026-08-10 · last: 2026-11-25
State: vg03-mysql extended repeatedly (trading-1/2 +200G on 09-10; trading-2 +50G on 09-30 with no more room in the vg, ZD 23574); a slow manual replica restore (10-01) was killed 10-02, the slave was back by 10-05, and nightly backup was switched off with bigger buffer pools (CHG 10-14). The OneZero analytics drop copy (analyticsFixServerOZ1) was removed on trading-1 on 2026-10-05 for load reduction (revert commit to restore). The `mysql_optimize_enable=false` question from 2026-08-10 never got a reply. On 2026-10-29 CHG-2610-XJSN (Cameron Copland responsible) freed 550G on the DB master by emptying an unused table, window 11:00-11:30Z, approved by Liam. On 2026-11-13 Arun saw the B_CLIENTS_LDN USD rounding drift behind the tradePositionInconsistent PagerDuty alert again and proposed an Open adjustment of -0.14829 for review.
On 2026-11-20 CHG-2611-0M5R (Daria Horton) purged DB binary logs before the DB disk filled (executed 05:44Z, verified and closed 08:06Z). Also queued: CHG-2611-3XQ0 (Liam, self-approved) adds a Java4Shell stopgap JVM flag live at the weekend reboots (Sat 21 Nov 00:00 to Sun 22 Nov 12:00Z), and CHG-2611-N1P3 raises the order request persistence buffer 256 to 2048 on all gateways, Sat 21 Nov 15:20-16:00Z, awaiting approval.
On 2026-11-25 the MySQL volume on trading-1 hit 0% free at 02:40 UTC and DB writes stopped until Daria purged binary logs about 03:20; arbHedger1 and riskReportingExtended1 OOMed and pricerWknd1 died, automatic restarts failed and all were back ~03:23. Shyam purged again (207G free, 88%); binary logs grow ~11 GB/hour so it refills in ~12 hours, the trading-2 replica is also growing, and neither VG has room to extend (71G trading-1, 24G trading-2). Fourth purge in five days (Zendesk 23911).
Next: a durable fix for DB growth (binlog retention/sizing, volume extension) before the next fill; someone to answer the mysql_optimize_enable question.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1790734299323199 https://mahifx.slack.com/archives/C0AKAPLU78W/p1790870773608959 https://mahifx.slack.com/archives/C0AKAPLU78W/p1795587506259939

### restart-pricing-gaps — Restart windows, pricing cut-offs and S3 data latency
status: open · since: 2026-11-11 · last: 2026-11-25
State: Restarts are Sat 10:05-10:40 NY plus central source restart Sunday 01:00 UTC; the 22:00 UTC EOD restart adds gateway capacity and pricer failovers can gap a single-sourced feed. S3 MarketData lands in 15-minute batches (15-20 min delay). tXAUUSD went indicative Sat 14 Nov to early Sunday from an over-conservative weekend safeguard after a big gold move (likely the Sanity Check node, Will's backtest to confirm); weekend gold settings still being tuned. 11-20: non-23/5 sources (HRP_ARG, HRP_MEX) set to XAUUSD 01:01-23:58 UTC+2 Mon-Fri to stop roll-hour pricing. 11-24 Stefanos asked what Client_Price_WKND_ldn does on a weekend cut-off (21 Nov ~09:33, 3s; MFXPulse showed CLIENT_PRICE); Isaac checking, says it would not send the stale CLIENT_PRICE_LDN. 11-25 Stefanos reported no XAUUSD prices ~02:50-03:20 UTC; Shyam said a data issue is being investigated, matching the trading-1 MySQL disk fill (see infra-disk-alerting).
Next: Isaac to answer the WKND cut-off question; Shyam to report back on the 02:50-03:20 XAU gap; Isaac (out this week, back after) to fix the weekend gold safeguard settings; Will's backtest to confirm the Sanity Check node cause; Rory to look at specific instances on request; check the 22-23 roll-hour pricing after the weekend restart applies the new HRP sessions.
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1794402600953049 https://mahifx.slack.com/archives/C0AKRP8C049/p1794907764858049 https://mahifx.slack.com/archives/C0AKRP8C049/p1795588646851709

### sltp-execution — Stop-loss/take-profit orders from OneZero without slippage
status: open · since: 2026-11-24 · last: 2026-11-24
State: On the 2026-11-24 call GTC said it is asking OneZero to pass stop-loss and take-profit info so Mahi can execute those orders without slippage (probably no last look at the touch, maybe no LR). Isaac proposed the cleaner route of a trigger type on the order: Mahi already reads custom FIX tag 9249 on new orders (6 = stop loss, 7 = take profit), so OZ populating it avoids changing the counterparty tag; he also wants open/close flagged, and asked whether GTC accepts cancel-and-retry of the limit price when the market passes through without trading, and what fill ratios are expected (he and Andrew warn it can give undeserved positive slippage; Andrew thinks it is doomed unless clients are deserving). Manglai agreed and asked for the latest FIX spec to pass to OneZero; Liam said to ask him to have OZ email support.
Next: Manglai to get OZ to email support; Mahi to provide FIX spec/answers on 9249, open/close and fill-ratio expectations.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1795518584012859 https://mahifx.slack.com/archives/C0AKAPLU78W/p1795530609096189

### xau247-ha-hosting — 24/7 XAU extra servers, DR and weekend hosting
status: open · since: 2026-11-10 · last: 2026-11-24
State: Plan (Isaac 11-11, Andrew agreed): hot/hot with a secondary set in AWS ($5-8k/month, unverified), primaries on the Beeks cluster; Equinix Private Cloud the alternative. GTC has 9 connections (7 OZ hubs, PXM, Centroid), so 18 secondary session pairs, whitelisting and bridge failover are needed. Andrew wants a written failover/weekend release plan before costing; Isaac's draft to Manglai asks GTC to ask OneZero, PrimeXM and Centroid about Fabric (Megaport an alternative) and which MT servers sit behind each hub. Beeks answers (Martyna) outstanding. 11-23: XAUUSD_24_7 subscribable from EOD, tXAUUSD to be discontinued once GTC confirms. 11-24 call: GTC asked to own the AWS hosting; Liam favours a flat no and suggests GTC ask OneZero for dedicated AWS connectivity (Fabric/Megaport or cross-connect, hosted connection at Equinix LD5).
Next: Liam/Dev to confirm the answer on GTC-owned hosting; GTC to confirm the switch to XAUUSD_24_7; GTC (Manglai) to answer the Fabric and MT-server questions; Isaac to finish the DR/release plan and send quote; Beeks (Martyna) to revert.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1794306401214489 https://mahifx.slack.com/archives/C0AKRP8C049/p1794309472636159 https://mahifx.slack.com/archives/C0AKAPLU78W/p1794560779618239 https://mahifx.slack.com/archives/C0AKAPLU78W/p1795518584012859

### mt-analytics-plugin — GTC MT server issue and Mahi analytics plugins
status: open · since: 2026-11-19 · last: 2026-11-23
State: On 2026-11-19 Manglai reported an issue on a GTC MT server with a screenshot and an unfamiliar source IP 170.75.204.2, and asked Mahi to advise on it. Liam said it looked like a Beeks IP not allocated to Mahi (Mahi's only direct MT connectivity is 18.130.191.84 in AWS, otherwise via bridge providers), but stopped Mahi's analytics services/plugins on the MT windows server as a precaution and asked if it helped. Manglai said John will confirm; no confirmation seen. On 2026-11-23 Isaac noticed the MT servers (analytics plugins) were off; Daria had stopped them too in case of DB back-pressure, and Isaac said it is probably fine to leave them off.
Next: decide whether the analytics plugins stay off for good; GTC (John) to confirm the MT issue cleared.
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1795106224602519 https://mahifx.slack.com/archives/C0AKAPLU78W/p1795106769889399 https://mahifx.slack.com/archives/C0AKAPLU78W/p1795426069406989

### dist-gateway-capacity — Distribution gateway load from cent/small-ticket flow
status: open · since: 2026-09-09 · last: 2026-11-23
State: B_CLIENTS is ~6% of XAU notional but 16-20% of tickets; cent flow on small-ticket servers drives load. Latency cancels (09-21/22) led to gateways 6-8, a raised unexpected-fill-latency ceiling and dist9 (10-14); OZ-5 latency fix via CHG-2610-4FG5 (10-24). OZ-6/OZ-7 ready for cent flow (11-10), capacity added at the 22:00 UTC break; Isaac asked GTC to move one MT server at a time. Andrew is fixing the ZD 23796 scaling problem. 11-20 Marios said GTC was moving XAUUSD off OZ-2. 11-23 clientDistributionGateway2 rejected ~70 XAU orders (full inbound queue, 01:25-02:49 UTC); Daria raised the queue 1024 to 2048 live and staged for 22:00 UTC CHG-2611-VR3K (gateway 2 CEP threads 2 to 5) and CHG-2611-D8ZS (revert persistence buffer to 256, needs eng approval); all nine gateways restart so every GTCFX session drops once. Root cause with dev on ZD 23899.
Next: eng approval for CHG-2611-D8ZS and the 22:00 UTC restart on 23 Nov; dev root cause on ZD 23899; GTC to say which MT server moves to OZ-6/OZ-7 first; GTC to confirm the rebalance across gateways (Isaac to chase); Mahi to compare 1 hour of OZ1 vs OZ7 ticks (binlogs) and explain the differences; dev review of latency cancels requested 2026-09-28.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1790591684124349 https://mahifx.slack.com/archives/C0AKRP8C049/p1790567720885579 https://mahifx.slack.com/archives/C0AKRP8C049/p1794316873730009 https://mahifx.slack.com/archives/C0AKAPLU78W/p1795405562905789

### commercial-value — Pilot value case and billing
status: open · since: 2026-08-19 · last: 2026-11-20
State: Isaac's 09-09 estimate: at 2.5 $/M LR and 4 $/M FI on XAU alone, billing reaches ~200k/month by January (4M value-add on ~650B/month XAU). Call KPIs (09-29): skew PnL on XAU, toxic HFT on A Book, 24/7 crypto uptime; upsell is 24/7 XAUUSD. OZ's fee waiver (quiet) stands. 11-10/11-11: for 24/7 GTC is quoted hosting at cost (AWS), a $3k/month cluster-management fee, a 24/7 support fee and a new 250k/month tier above 5m value-add on the 3-month lookback (current: base 100k, 3m 150k, 4m 200k); needs a contract amendment. 11-16/17: GTC's bill slipped; GTC believes it is paid (24-hour payment rule) and Bonnie is sending their reply to billing. Will posted the October value-add report and email draft for Isaac to sign off. 11-20 weekly value-add to GTC: $1.58M on $151.3B (10.5 $/M), almost all XAUUSD (FI $1.03M, LR $0.54M); XAGUSD FI positive 3 weeks.
Next: billing to reconcile GTC's payment claim with Bonnie's forwarded reply; Isaac to sign off the October value-add report/email; Isaac to present the tier to GTC and send the quote once the Fabric answers, AWS figure and DR plan are in.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1788950931799769 https://mahifx.slack.com/archives/C0AKAPLU78W/p1790674407124919 https://mahifx.slack.com/archives/C0AKAPLU78W/p1794917700995739 https://mahifx.slack.com/archives/C0AKRP8C049/p1795191012115729

### signalprocess-crash — Skew flatline and signalProcess1 crashing
status: open · since: 2026-11-06 · last: 2026-11-16
State: Isaac saw skew flatlining since 18:00 on 2026-11-05 and found signalProcess1 had died with no PagerDuty alert; it looks to have been crashing repeatedly, and two PagerDuty incidents followed (16:27 UTC). Likely related to the weak skew on NFP (see nfp-gold-review). Root cause is the stream overflow tracked in Zendesk 23796; the 1M queue flag was applied to signalProcess1 only. On 2026-11-16 Shyam reported riskReportingExtended crashing 5 times between 01:02 and 01:45 UTC on the same overflow: it is still on the 23 Oct build without the fm-throttle fix that bounds the queue, so Compass PR 81 may need deploying here.
Next: decide on deploying Compass PR 81 (https://github.com/MahiFX/Compass/pull/81) to riskReportingExtended; add a PagerDuty alert for signalProcess1.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1793978437571839 https://mahifx.slack.com/archives/C0AKAPLU78W/p1794797723158549

### pricing-skew-tuning — Skew, spread and last-look tuning
status: open · since: 2026-08-19 · last: 2026-11-12
State: Skew config tuned repeatedly (XAG ceilings, IFMS leg removed 10-07, arb protection and cross spreads). Controls: opening-window last look (800ms XAU, 400-500ms others), indicative XAU around the open, 8 cent min TOB, MAHI_BENCHMARK_LDN added after the 09-19 XAU blowout; SWIFT out of arb protection (10-15); wide-spread suppression extended to the custom execution timezone. XAG spikes (10-20) came from price formation swapping FINALTO/SWIFT; GTC to choose XAG reference markets. 10-26 FX spikes: Isaac cut FX skew (majors 0.1, crosses 0.2 flat), FX skew $3.60/M that month. 11-11 XAU spikes traced to a crossed market in central formation; production formation to move into GTC's own Compass. 11-12 XAUUSD skew added ~$734k (~$5.60/M) on B-book 5-12 Nov; Stefanos accepted Kate's explanation of a 10:56 saw pattern.
Next: Isaac to return with skew-improvement options incl. predictive spread modulation and give GTC before/after values; GTC to send tick data from both hubs for 23:55-00:15 their time so Isaac can confirm the OZ vs OZ-3 spread difference; Rory checking the 10-12 FX spike report; GTC to pick the XAG reference markets (Shyam will change and restart on request).
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1788911767407019 https://mahifx.slack.com/archives/C0AKRP8C049/p1794486366653579

### flow-rollout — Symbol and server migration to Mahi
status: open · since: 2026-08-17 · last: 2026-11-09
State: EURGBP moved 2026-08-17, then rolling in batches through 2026-10-05 (all FX majors/crosses, B Book). XAGUSD routed 2026-09-03 and XAUUSD 2026-09-10 with more servers added 09-16, 10-05 and 10-08 (mt4 live2); on 2026-10-23 Manglai moved XAUUSD mt5 live1 execution to Mahi and Isaac is monitoring. On 2026-10-27 Isaac pressed GTC to switch MT5 Live 2 (October FI PnL $897,145 at 7.76 $/M on executed flow so far; Live 2 would have added ~$2.22M on 285.69B). Its drop copy to Mahi stopped 10-28 16:10 UTC; no reply recorded. On 2026-11-09 Antreas said GTC will switch XAUUSD from MT5 Live2 to Mahi and asked for confirmation; Isaac confirmed; Antreas then posted "Done pls monitor" (08:19 UTC), so the XAUUSD switch from MT5 Live2 is done and Mahi is monitoring. Remaining: cent accounts on small-ticket servers, indices (GTC worried about primary benchmark feed dropouts), crypto. Priorities per the 2026-09-24 Expo meeting: fix OZ hub drops, A Book with hedging, B Book via OZ, crypto, then 24/7 XAU.
Next: Mahi to monitor the now-live XAUUSD MT5 Live2 flow; GTC picks the next server/day; weekly call 2026-10-13 notes remaining checks (24/7 connection 5, FX pair spikiness, HRP Jane Street).
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1786977281687209 https://mahifx.slack.com/archives/C0AKRP8C049/p1793286194434769 https://mahifx.slack.com/archives/C0AKRP8C049/p1794212384937039

### nfp-gold-review — NFP result: LR, skew and PSM flat on gold
status: open · since: 2026-11-06 · last: 2026-11-06
State: Will Carter reviewed the 2026-11-06 NFP release (13:30-13:33 UTC) on B_CLIENTS_LDN: other clients made money on the same engine, GTCFX did not. Corrected figures (first post overstated volume ~4x): $105M, $98M of it XAUUSD, LR $343 at $3.3/M (same as the hour before, not scaled to the event), skew -$295 (about -$2.8/M), PSM $52 with nothing firing on gold despite being wired on 11 instruments. Gold ran as ~46k fills in three minutes at ~$2.1k each, so LR and skew settings may not be scaled for flow this fine. Will's actions: find why LR did not scale on gold, sim a stronger or adaptive skew on the release before changing anything, check whether gold is in PSM scope. No owner assigned in thread.
Next: owner needed for lr-health-check, skew-health-check and psm-health-check follow-ups.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1793977971609499 https://mahifx.slack.com/archives/C0AKAPLU78W/p1793980111840819

### crypto-24x7 — Crypto onboarding and 24/7 sessions
status: open · since: 2026-09-15 · last: 2026-11-03
State: Crypto is next after gold; GTC's core BTC/ETH LP is Binance (pricing only). The HRP Route28 connection is established (10-15). cryptoMarketData1 fails because Binance returns HTTP 451 for the Beeks IP range; preferred fix (Liam, Isaac) is subscribing from mc-apnortheast-1 and proxying to mahi-central-ln via Fabric, Beeks egress ticket as fallback. GTC switched OZ sessions to 24/7 on 10-16 (Mahi applied 10-17 after OZ and PXM logouts and a sequence re-sync). After the 10-20 call 24/7 XAU is the priority and crypto deprioritised; GTC enabled XAUUSD_24_7 from PXM (10-25) and Kate confirmed the tXAUUSD subscription on OZ-7 (10-28). On 11-03 Stefanos reported ~$2 mid spikes on the 24/7 XAU symbol; Isaac found none in Mahi's binlogs, blamed a 09:45 safety-check cut-out and a ~$2 basis between GTC's GMG stream and Mahi's, and asked GTC to check what picks up GMG; Stefanos is reviewing.
Next: GTC (Stefanos) to find the source of the spikes and explain the basis; Mahi to subscribe to the PXM XAUUSD_24_7 feed and the OZ-4 tXAUUSD stream; Mahi to roll 24/7 tXAUUSD to the other streams; crypto (deprioritised): get mc-apnortheast-1 consuming Binance and proxied to mahi-central-ln (Beeks egress ticket is the fallback); GTC to confirm session changes on PXM and Centroid.
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1791975353055319 https://mahifx.slack.com/archives/C0AKRP8C049/p1792053281436189 https://mahifx.slack.com/archives/C0AKRP8C049/p1792147010645739 https://mahifx.slack.com/archives/C0AKRP8C049/p1793702429610309

### hedging-a-book — A Book go-live, STP rules and hedging structure
status: open · since: 2026-10-05 · last: 2026-10-27
State: A Book live 2026-10-06 on one account, hedging via HRP markets only (Finalto/Swift still the two LPs in the hedger market, reason to be confirmed). 10-12: flow from tag 52146947 was internalised though GTC expected STP to HRP; Mahi closed 267oz and booked a 2100oz position adjustment at HRP_MEX 4177.43; two more tags switched to STP (resolved). Kate: wait for Mahi to confirm STP whitelisting before routing a tag. 10-14 hedge split ask (A 30% / B 70%): a portion of flow can go to a hedged book by counterparty or instrument; hybridHedgerSI1/arbHedgerSI1 exist. SWIFT XCUUSD prices per 100-unit lots. 10-27 Bruce's A Book group showed as B Book in Compass; only drop copies were received, so flow must route via GTC-A-Orders-* sessions; Bruce then said disregard.
Next: GTC (Bruce) to route that A Book group down A Book order sessions; the separate hedged book for the large VIP client (tag 56020001, 100 lots to start, Swift/CBCX) is being configured via the PXM stream (see pxm-xau-counterparty); GTC to give the test-account counterparty (asked 2026-10-15); agree the hedge-percentage setup with GTC; Swift to fix XCUUSD unit (Swift removed from reference markets 10-06, request logged on the wiki 10-12).
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1791202994256859 https://mahifx.slack.com/archives/C0AKRP8C049/p1793124148219949

### pxm-xau-counterparty — XAUUSD via PXM xcore sessions, counterparty tag
status: watching · since: 2026-10-16 · last: 2026-10-20
State: GTC tested XAUUSD from its PXM xcore A and B order sessions on 2026-10-16; test trades arrived tagged ABOOK because the PXM bridge sends the Parties block with PartyRole 452=1 (Executing Firm) where Mahi reads PartyRole 3 (Client ID), so orders fill but cannot be attributed. On 2026-10-19 Antreas asked to route XAUUSD from GTC-A-Orders-PXM to Swift only; Isaac explained A Book routing is per distribution channel, not per connection, and suggested a separate PXM trading account tag with an execution rule to a Swift-only pool. Manglai confirmed it is the separate large-client setup (hedged on its own book, starting at 100 lots / 50m); the VIP client tag is 56020001 (sent as 16_71_56020001) and Isaac added it to config. Isaac put a workaround in for the ABOOK tag; the proper counterparty fix needs the EOD restart. A further test from 16_71_50001 on 2026-10-20 looked correct on Mahi's side.
Next (no activity since 2026-10-20, downgraded to watching): GTC to change the PXM bridge to send the counterparty with 452=3; Mahi to confirm the EOD fix and drop the workaround; GTC to retest with the VIP tag.
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1792140498426039 https://mahifx.slack.com/archives/C0AKRP8C049/p1792479999175029

### oz-hub-connectivity — OneZero hub sessions, disconnects and tags
status: watching · since: 2026-08-17 · last: 2026-10-17
State: GTC keeps adding OZ hubs because OZ fears it cannot handle their trade rate (7th hub requested 2026-10-09, in progress). Recurring session problems: OZ-2/OZ-3/OZ-4 hub drop-outs and "Session time ended" logouts (fixed by aligning all OZ sessions to Sun 17:00-Fri 17:30 NYT; OZ-4 outage 22-24 Sep fixed by a hub bridge restart), missing counterparty tags on OZ-4 (2026-09-08) and OZ PTR sessions disconnecting (2026-10-06, Mahi switched PTR analytics off). New-hub sessions needed whitelisting plus a cross-connect with several delays: OZ-6 (requested 2026-09-23) needed a Beeks NAT/routing change and was last pointed at the new ports on 10-06 with no confirmation in thread; OZ-7 (requested 10-09) details were sent 2026-10-14 and GTC acknowledged 10-15; after the 24/7 session-time fix on 2026-10-17 all sessions including GTC-A-Orders-OZ-7 were reported connected. Downgraded to watching 2026-11-17 (no activity for 31d; OZ-6/OZ-7 now carry cent flow per dist-gateway-capacity).
Next: GTC to confirm OZ-6 working; GTC weekly call is the forum.
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1786969418265589 https://mahifx.slack.com/archives/C0AKRP8C049/p1792228566542629

### riskpath-stability — riskPath stalls, OOM crash-loops and yield-profile gaps
status: watching · since: 2026-09-02 · last: 2026-10-15
State: riskPath OOM crash-looped on an unbounded analytics map (fix cherry-picked to release/26.3, process split across low-latency nodes). Yield profiles were missing ~31% of XAU fills (9 Sep) and classifier queries overloaded it (classification off for A and drop-copy profiles since 09-11); YPs not persisted to Pulse 09-24 (ZD 23547). A "riskPath stall and overflow-crash fix" behind two flags (CHG-2610-MBV3) was self-approved by Liam and rescheduled on 2026-10-15 from 14:00-15:00Z to 12:15-14:45Z; no completion message seen yet; downgraded to watching on 2026-11-16 (no activity for 32d), with the live stream-overflow crashes now tracked in signalprocess-crash.
Next: Isaac/Liam to confirm the 10-15 deploy landed; re-enable classification on A/drop copy once safe.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1788309377675289 https://mahifx.slack.com/archives/C0AKAPLU78W/p1792065637260039

### compass-client-support — GTC's use of Compass, Echo and Pulse
status: watching · since: 2026-08-17 · last: 2026-10-13
State: Weekly Tuesday 10:00 UK call set up 2026-08-17. GTC asks about order CSV export in USD (fixed in the 25 Aug dashboard deploy), MT4/MT5 servers missing from yield profiles, price-forensics limits and classifier tag export. Pulse creds and spec passed to Manglai 2026-10-13 (Zendesk 23640).
Next: none outstanding.
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1787663421577319 https://mahifx.slack.com/archives/C0AKRP8C049/p1791901914330729

## Arc
- 2026-07-14 - A Book first; B Book held pending OZ per-million fee
- 2026-07-28 - OZ waives per-million fees on GTCFX flow (quiet; precedent for joint OZ clients)
- 2026-08-12 - AUDUSD B Book live
- 2026-08-17 - EURGBP moved; weekly Tuesday call agreed
- 2026-08-28 - NZDUSD, USDJPY, USDCHF moved; EURUSD followed 08-31
- 2026-09-03 - XAGUSD routed to Mahi
- 2026-09-10 - XAUUSD routed to Mahi (more servers 09-16, 10-05, 10-08)
- 2026-09-24 - Expo meeting with Manglai fixes the roadmap
- 2026-10-06 - A Book live on one account, HRP-only hedging
