---
slug: atc
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/atc.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: atc
  hosts: ../MahiProduct/data/client-hosts.json          # entry: atc
  wiki: ../MahiProduct/wiki/clients/atc-brokers.md
channels:
  internal-atc: C046RNF64VD
  mahi-atc: C04AZM0LPMH
  internal-atc-prop: C0AQ3PVTX6D
contacts:
  - {name: David Manoukian, role: "ATC trading/sales lead (Dave M); raises execution and depth issues in #mahi-atc"}
  - {name: Malik Khan, role: "ATC ops/back office; LP and connectivity contact, owns UAT and whitelisting requests"}
last_catchup: 2026-10-27T07:20:02Z
status: active
---
## Now
ATC is a matched-principal broker in a build phase: prop firm launch (own MT5/bridge), a Britannia prime arrangement for triangulation-arb flow, and a Seychelles entity migration.
Biggest live risk is the FCA/compliance finding that non-USD P&L legs in Compass leave real unhedged LP exposure; the fix is a weekend flatten and reimport to USD.
Compass moved to 26.4 on the 10-10/11 weekend, which switched on PSM widening/tightening overlays for ATC pricing. Volumes are well down on early 2026; ATC is sensitive to spreads, depth and fill quality on gold.
On 2026-10-26 the Malik call was joined by an ATC compliance contact working with auditors, who is pressing on why Mahi-held LP cross positions (NZD etc.) dwarf client trades; Andrew treats it as an escalation. Malik also wants futures, XAU futures and crypto setups.

## Streams

### lp-cross-positions — legacy cross positions at Finalto and auditor questions
status: open · since: 2026-10-26 · last: 2026-10-26
State: ATC's compliance contact, working with auditors, is not satisfied that Mahi-held positions (NZD crosses etc.) are far larger than client trades while ATC is a matched principal at FCA level; Malik escalated on 10-26 and Andrew raised it as higher priority, with regulators following up the position rec. Will's investigation found the Finalto crosses are legacy brokered inventory built Sep 2023 to Sep 2024 by brokering rules (whale rule, Dynamic Broker Toxic FX and Metals) plus LP switching and manual moves, never unwound because hedgers only trade USD pairs; NZDJPY is about 36M, the NZD crosses are 8-13x recent client volume, and gross $304.5M nets to about $96M with the same open risk. Five broker setups in the LDN config still send crosses to Finalto. Dave's claims of out-of-loop adjustments may cause divergence.
Next: Stop brokering crosses; net the dead pairs into USD pairs at Finalto (Will: close the longs/shorts at minimum); pull the Oct 2023 and 2026-06-25 import files for auditors; Mahi to answer the auditors' original questions (Andrew asked Malik for them).
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1793025346402589 https://mahifx.slack.com/archives/C046RNF64VD/p1793038694725539

### xbt-phantom-position — XBTUSD and DOW CFD positions differ from ATC's own rec
status: open · since: 2026-10-26 · last: 2026-10-26
State: ATC's own rec flagged CFD differences on 2026-10-26: XBTUSD is flat on ATC's side and at Finalto while Compass shows 64 client and LP side, and DOW is about 0.5 on the client side versus 1.77 in Compass (not netted to Velocity correctly). Dave asked why Compass shows a position that does not exist at Finalto; Cameron Hughes said it is likely trading outside Compass (manual close-outs or failover routing) and Compass needs position updates, being worked with Malik. CFDs hedge 1-1 with the inbound instrument.
Next: Malik to confirm exact client positions to book; Mahi to adjust Compass positions.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1793023106101569 https://mahifx.slack.com/archives/C04AZM0LPMH/p1793023353198839 https://mahifx.slack.com/archives/C046RNF64VD/p1793027080083249

### futures-crypto-ask — futures, XAU futures symbol and crypto setup
status: open · since: 2026-10-26 · last: 2026-10-26
State: After a pre-call with Malik, Andrew noted ATC is courting basis traders in futures, wants a crypto setup (with its own LP), and G7 futures quoted as CFDs; Andrew wants an XAU futures symbol added. Mahi also needs ATC client and LP positions ingested into Compass for reconciliation and swap calcs; a swap inventory skew CSV is owed to ATC. Mahi is looking for other firms quoting G7 futures as CFDs (Amana was named as having CMC, Jump, IG, GCEX).
Next: Mahi to send swap inventory skew CSV and ingest ATC positions; scope the XAU futures symbol and crypto setup.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1793009406477699 https://mahifx.slack.com/archives/C046RNF64VD/p1793033858681609

### beeks-ld-incident — Beeks LD networking incident, ATC failover
status: open · since: 2026-10-16 · last: 2026-10-16
State: On 2026-10-16 a networking incident in the Beeks-hosted LD environment hit ATC's connectivity; Dave reported connection issues on the spotex MT5 order and price sessions. Mahi asked ATC to switch to failover, saw recovery signs, and at ~12:07 BST Liam said it was safe to switch back (no official Beeks confirmation yet) and later that the issue was reported resolved. Malik asked whether failback is automatic; Liam said it depends on ATC's failover setup.
Next: Beeks root-cause / official confirmation; confirm ATC failed back and sessions are healthy.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1792143086471619 https://mahifx.slack.com/archives/C04AZM0LPMH/p1792150199815879

### prop-launch — ATC Prop firm: servers, rules, go-live
status: open · since: 2026-08-05 · last: 2026-10-14
State: Go-live plan of record and programme rules are filed in MahiProduct (agreed at the 2026-08-19 meeting); ATC runs its own prop bridge and MT5 install, Mahi supplies the Beeks server and Compass (atc-prop-ln). Conformance passed 2026-09-11, prop FIX creds (qualifying and funded) sent, and Malik asked for prod IPs to be whitelisted on 2026-09-30 (proptrading and brokerage). Open commercial item: ATC's in-house prop CRM resale as a white-label bundled with Mahi liquidity needs written sub-licence agreement and a pricing steer (Andrew/Will, alongside the Seychelles addendum). Jack's 2026-10-08 email asking what API data Mahi wants for anti-predatory safeguards has had no reply for 6 days.
Next: Cameron Hughes to send Jack a holding reply and then the API data list; Andrew/Will to give commercial steer on CRM sub-licensing; confirm drawdown calc mechanics with ATC.
Refs: https://mahifx.slack.com/archives/C0AQ3PVTX6D/p1787125125063369 https://mahifx.slack.com/archives/C0AQ3PVTX6D/p1787210584953589 https://mahifx.slack.com/archives/C0AQ3PVTX6D/p1791963840973209

### client-exec-incidents — pricing and fill incidents reported by Dave M
status: open · since: 2026-08-11 · last: 2026-10-13
State: Recurring client-reported issues: skew floors distorting EURUSD/USDCHF/GBPUSD (08-11; Daria fixed config, Will took a fleet-wide skew review, ATC's historical-data cleanup request never actioned); silver fills outside market range (08-19, root cause a brokered-LR feedback loop after Finalto pulled its bid, Zendesk 23372); SPX/NDX stopped ticking for ~1h20 on 09-17/18 (internal messaging reset) and NDX orders expired on 09-18 because a backup market-data aggregation process stopped carrying NDX (bounced; root cause still to investigate). On 2026-10-13 Dave reported account 27072570 orders not filling; Nathan found no rejects or cancels in Compass and no further reply.
Next: Mahi owes root-cause for the NDX aggregation stall and the 09-17 publishing stall; confirm with Dave whether 27072570 is resolved; historical data cleanup request from 08-12 still open.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1786480031117319 https://mahifx.slack.com/archives/C046RNF64VD/p1787568429179159 https://mahifx.slack.com/archives/C04AZM0LPMH/p1789749067038009 https://mahifx.slack.com/archives/C04AZM0LPMH/p1791915479144599

### xau-depth-ladder — gold depth question for a prospective large client
status: open · since: 2026-10-13 · last: 2026-10-21
State: Dave noticed XAUUSD levels 3-5 showing identical bid/ask while preparing for a large prospect. Cameron Hughes explained the ladder is floored at the average Finalto+Velocity spread (about 70c at 1.6k oz) so deeper levels repeat the price until the 80c base spread at 12.6k; clients see the repeated tiers merged into one ~7k band. Mahi publishes 12.6k oz per side but only about 3k oz is backed by firm LP depth, so a 5k order is chipped away rather than cleared at once. Dave confirmed he will rely on those numbers. Separately Dave asked about a client's trading style (trade logs from Malik) and Cameron said that analysis is still in progress.
On 2026-10-21 Dave again needed to show XAUUSD depth to a client and reported it invisible for days; Rory King saw normal depth on Mahi's side and suggested a hard refresh, which did not help, but removing and re-adding the symbol fixed it (client-side display issue, resolved).
Next: Cameron Hughes owes the trading-style analysis; Dave to decide whether to widen the 1.6k/3.6k/7.6k base spreads above the LP floor or drop the floor.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1791902732632709 https://mahifx.slack.com/archives/C04AZM0LPMH/p1791907572332459 https://mahifx.slack.com/archives/C04AZM0LPMH/p1792590024121469

### pnl-currency-rec — non-USD P&L legs and LP position reconciliation
status: open · since: 2026-07-09 · last: 2026-10-26
State: Compass books realised P&L in the counter currency, so cross flow (AUDNZD, GBPNZD etc.) leaves non-USD P&L balances (about 21.7m NZD) that the hedger treats as risk and hedges at the LPs. Finalto and ATC cash are USD-only, so those LP positions (about $12m short NZD, $4.5m long JPY) are real exposure with no client trade behind them; ATC's compliance officer flagged this to auditors and the FCA on 2026-10-01 and has accepted the mechanism. Agreed fix is converting P&L legs to USD in Compass as a weekend flatten and reimport (duplicate trade-position rows from the NY-to-LDN move, Zendesk 23171, still need cleaning), then a currency-level rec with ATC. On 10-08 Malik asked for a systematic conversion to limit spread cost; Liam laid out the three P&L models (Compass, Finalto, MetaQuotes) that disagree. On 09-22 Cameron Hughes confirmed no net per-asset risk between ATC and LPs. On 2026-10-26 Andrew said the technical gap is known and CPS is fixing it but a HPS fix may be brought forward; the July USD adjustment was never done (NZD residual about 30.9m on 09-29, JPY 637m) and a counter-currency to USD or deposit currency conversion is needed. Andrew also called the swap risk on a book meant to be zero "crazy".
Next: Cameron Hughes to revert to Malik with a full-rec plan and schedule the weekend flatten/reimport (Daria, Liam); build the ongoing currency-level rec.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1783567793838579 https://mahifx.slack.com/archives/C046RNF64VD/p1790850531938759 https://mahifx.slack.com/archives/C046RNF64VD/p1791463861287519 https://mahifx.slack.com/archives/C046RNF64VD/p1793028994527199

### britannia-triangle-arb — Britannia prime connectivity and triangulation arb flow
status: open · since: 2026-09-15 · last: 2026-10-08
State: Dave's clients may send high-volume triangular-arb flow, to be distributed across LPs under ATC's Britannia PB setup; preferred design is a separate FIX session per LP, with Spotex possibly supplying an LP panel. Britannia approved ATC's account 2026-10-01, Malik supplied creds and product mappings, and fixOrders4/fixMarketData4 were bounced on 10-05; waiting on Britannia whitelisting. On the 10-08 call Malik worried that competitor spreads and commission (about 15c and $7/lot) are too low to compete once Britannia costs are included. Mahi still needs representative arb trade data and proof of arb for account 27072550.
Next: Cameron Hughes to model ATC's proposed spreads by volume tier with Britannia costs; Britannia WL; arb trade data and write-up for Dave and compliance.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1789485221018859 https://mahifx.slack.com/archives/C046RNF64VD/p1789660746314299 https://mahifx.slack.com/archives/C046RNF64VD/p1791214089857239 https://mahifx.slack.com/archives/C046RNF64VD/p1791463861287519

### velocity-depth-cap — Velocity data load
status: open · since: 2026-10-05 · last: 2026-10-05
State: Velocity complained about ATC's market-data consumption (up to 30 layers per instrument). Cameron Hughes agreed to cap the depth request at 10 on both Velocity logins (main and BVI; Velocity only sends 5 levels so pricing is unaffected) after an EOD restart, and noted that roughly 935 symbols per login is likely the bigger load. Malik will contact Velocity; no confirmation the cap or any symbol trim was applied.
Next: Malik to relay Velocity's response and any symbols to drop; Cameron Hughes to confirm the cap is live.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1791190471362809 https://mahifx.slack.com/archives/C04AZM0LPMH/p1791215001177869

### fxcm-connection — FXCM logon rejects and failed auto-restarts
status: watching · since: 2026-06-04 · last: 2026-09-23
State: No activity since 2026-09-23; downgraded to watching. FXCM session is up but auto-restarts after weekend restarts keep failing and need a manual restart (still true 2026-09-23). Logon rejects began Sunday 2026-08-16 (Daria's question on 08-17 about `user not recognised or password incorrect` got no reply), likely a credential change; FXCM also wanted to publish only TOB to ATC. ATC said they would raise it with FXCM and had not as of 08-19; Malik reportedly tired of the issue and may leave Britannia to handle it.
Next: Malik owes the FXCM follow-up; Cameron Hughes sent a chaser 08-19.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1786947960799679 https://mahifx.slack.com/archives/C0AQ3PVTX6D/p1787127331818279 https://mahifx.slack.com/archives/C046RNF64VD/p1790183042306349

### compass-26-4 — Compass 26.3 to 26.4 upgrade
status: watching · since: 2026-10-08 · last: 2026-10-13
State: ATC staged 26.4 on 10-09 and went live at the weekend restart (client notified in #mahi-atc). Because ATC sets neither `adjustmentSignalParametersForWidening` nor `...ForTightening`, prices now widen/tighten one increment on PSM-W/PSM-T signals (Liam decided to let it go ahead). `arbHedger1` failed to start on the first RC and was fixed (precheck success). A dashboard-component deploy also hit ATC on 10-13. No client-reported regression yet.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1791483329972859 https://mahifx.slack.com/archives/C04AZM0LPMH/p1791543785439449 https://mahifx.slack.com/archives/C046RNF64VD/p1791866234975939

### seychelles-uat — Seychelles entity, dev connections and UAT feed
status: watching · since: 2026-05-19 · last: 2026-10-26
State: Seychelles (SC) infrastructure is live (SC channel, books, hedgers) with BVI-only LP routing; on the 2026-09-16 call Malik said ATC wants to move from UK plus SC connections to SC only, and ATC's dev team needs connections to both servers (two new sessions for ATC Broker). UAT feed/server restarts are a recurring ask from Malik and Dave (09-02, 09-14, 09-21, 09-28, 10-07, 10-12, 10-19, 10-26; Liam turned it on 10-26 but Dave said at 17:42 it was still not live, and Cameron Copland confirmed it working at 18:24, Dave acked); the realistic gateway moved to 9012/9013 on 09-14 so ATC needed re-whitelisting and port changes. SC monitoring was toggled off in August pending connections.
Next: Mahi to create the two dev connections; re-enable SC monitoring when connections are expected.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1782992990487589 https://mahifx.slack.com/archives/C046RNF64VD/p1789563271953519 https://mahifx.slack.com/archives/C04AZM0LPMH/p1792427565099679 https://mahifx.slack.com/archives/C04AZM0LPMH/p1793036534440469

### xau-hedging — gold hedging and P&L bleed
status: watching · since: 2026-05-27 · last: 2026-10-08
State: SHI/FAU hedging was merged into XAUUSD at Finalto (June) with covariance fixes, and XAU spread/BMSL/hedger tuning continued through the summer. Recent P&L drops were mostly false or transient: -$1k on 09-14 when Finalto rejects slowed risk clearing after $10M XAU trades; a ~$4k drop on 10-08 from bad final Velocity ticks into the roll that recovered. Malik wants to cut dependence on Finalto, and Velocity usage is deliberately limited to avoid large opposite positions.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1779890363013439 https://mahifx.slack.com/archives/C046RNF64VD/p1789360531094629 https://mahifx.slack.com/archives/C046RNF64VD/p1791499053655529

### monthly-pnl-report — monthly P&L report for Jack
status: watching · since: 2026-06-07 · last: 2026-10-01
State: Jack Manoukian wants the P&L report alongside each invoice; August was requested 2026-09-12 (Bonnie asked if it could be sent proactively) and September was posted unprompted by Cameron Hughes on 10-01. Jack also asked for April client and LP trade CSVs by POP (delivered 09-17); end-April Finalto-only open positions were unavailable as that data has only been persisted since late June.
Next: October report due start of November.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1780865571965479 https://mahifx.slack.com/archives/C04AZM0LPMH/p1789217003836759 https://mahifx.slack.com/archives/C04AZM0LPMH/p1790852829281389

### cfd-arb-execution — CFD arbitrageur execution rules
status: watching · since: 2026-09-21 · last: 2026-09-23
State: CFD arbitrageur execution was turned off 2026-09-21 after two of Dave's clients complained (mostly intentional flow; he wants good relationships and whitelisting by daily check). On 09-22 rules were restored with 10 $/M additional slippage instead of 50 at Dave and Jack's request, and a riskPathCFD benchmarkNormalised override fixed negative-spread yield profiles that had fed false arb classifications; the old CFD arb bot list was cleared on 09-23 and yields improved.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1790005631153139 https://mahifx.slack.com/archives/C046RNF64VD/p1790088439159019 https://mahifx.slack.com/archives/C046RNF64VD/p1790154076347849

### cfd-hedger-off-rca — CFD hedger book left OFF for 5h
status: watching · since: 2026-08-28 · last: 2026-08-30
State: CFD_PRAXIS_HEDGING_HYBRID was switched OFF in the GUI at 03:57 UTC on 08-28 during config work and not re-enabled; G30EUR risk built (about -$2k) and PD alerts were resolved twice with the book still off. RCA filed (P2); proposed actions are alerts that only resolve when state matches expected, mandatory comments on GUI book-state changes, and Daria's push to bump MXC-66 Sustained VaR Alerting. No recorded implementation.
Next: Mahi to decide and implement the preventive actions.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1787907463800669 https://mahifx.slack.com/archives/C046RNF64VD/p1788127946167719

### lr-martingale — liquidity refresh policy for martingale masters
status: closed · since: 2026-05-27 · last: 2026-08-25 · closed: 2026-10-26
State: No activity since 2026-08-25; assumed resolved. Martingale masters (27072402, 27072435, 27072473) sit on a No-LR profile as a deliberate temporary measure while a "timer-LR" / 50ms speed-hump design is worked out (never defined in Slack). The 2026-08-25 LR health check found LR earning $4.01/M inside ATC's band; the one gap (SHIUSD taking zero LR) was fixed by adding SHI alongside XAU in the counterparty and global profiles. David flagged the clients may scale to $30-50M.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1779895485904019 https://mahifx.slack.com/archives/C046RNF64VD/p1782819193766359 https://mahifx.slack.com/archives/C046RNF64VD/p1787677959034359

## Arc
- 2026-05-13 — SI disabled after losing every month Feb-May; volumes down sharply, ATC under financial stress
- 2026-06-04 — SHI/FAU hedging merged into XAUUSD at Finalto; covariance fixed 2026-06-11
- 2026-06-23 — Seychelles entity structure confirmed; SC flow hedges to BVI LPs only
- 2026-06-30 — Seychelles Compass channel, books and hedgers deployed
- 2026-07-05 — full outage after weekend restart (bad LIQUIDITY_POOL_SC config); fixed same day
- 2026-08-19 — prop go-live plan agreed with Jack and Malik
- 2026-09-15 — Britannia PB and triangulation-arb discussions begin
- 2026-10-01 — ATC compliance flags non-USD LP positions to auditors/FCA
- 2026-10-26 — auditors/compliance press ATC on LP cross positions; Mahi traces them to legacy brokered inventory from 2023-24
- 2026-10-09 — Compass upgraded 26.3 to 26.4 at weekend restart
