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
last_catchup: 2026-11-27T08:16:42Z
status: active
---
## Now
11-20: a hybrid-hedger position-ID miss (NY-ID positions) built large EURUSD/AUDUSD exposure and a Velocity margin call; flattened, hedger repointed to HOUSE, Zendesk 23880 for dev (Dave: "never ending issue").
ATC is a matched-principal broker in a build phase (prop launch, Britannia prime for triangulation-arb flow, Seychelles migration); volumes are well down and it is sensitive to gold spreads, depth and fills.
11-16: after Dave's large-order slippage complaint (orders filled against Finalto's thinner book under full STP), FX, metals and indices went back to internalisation; ATC will reconcile currency positions itself until the Seychelles move (~1 month).
Top risk: Mahi-held LP cross positions dwarfed client trades; auditors escalated 11-02, ATC self-reported to the FCA (~11-09/10), the ~USD 10m gap was explained as accumulated hedging P&L, and ~1m CHF stays unexplained. CFD hedgers stay off after the 11-10 SPX mishap (-$80.5k) pending the Compass rebase; 11-17 a DOW hedger was bounced and reconfigured to clear risk (made P&L, FCA concern).

## Streams

### seychelles-uat — Seychelles entity, dev connections and UAT feed
status: open · since: 2026-05-19 · last: 2026-11-24
State: On 2026-11-12 Dave reported no prices for index and energy CFDs on SC production; Nathan Burch found none of the instruments in LIQUIDITY_POOL_SC and added them with an EOD restart, but Dave still saw no prices on 11-13. Nathan had missed scheduling the clientDistributionGateway restart; after a weekend restart by 11-16 all index and energy CFDs price except F40EUR and JPXUSD, which Britannia rejects as invalid symbols (requested as FRA40 and JPXUSD); Mahi asked ATC to check Britannia's names for France 40 and Japan 225. Seychelles (SC) infrastructure is live (SC channel, books, hedgers) with BVI-only LP routing; on the 2026-09-16 call Malik said ATC wants to move from UK plus SC connections to SC only, and ATC's dev team needs connections to both servers (two new sessions for ATC Broker). UAT feed/server restarts are a recurring weekly ask from Malik and Dave (since 09-02, latest 11-24 evening when Malik asked for UAT prices to be started and Nathan brought the UAT server and Compass UAT online by 21:11 UTC; earlier 11-09/11-10, actioned by Rory/Daria); the UAT gateway moved to 9012/9013 on 09-14, needing re-whitelisting. On 11-02 the MT5 SC orders session (orders_mt5_sc) could not log on: MT5 resets FIX sequence numbers at 00:00 while Mahi's session runs Sun 20:00 to Fri 21:00 UTC; ATC asked to align.
Next: ATC (Dave/Malik) to get Britannia's symbol names for France 40 and Japan 225; Nathan to confirm pricing at market open; ATC to align orders_mt5_sc MT5 reset schedule with Sun 20:00-Fri 21:00 UTC; Mahi to create the two dev connections; re-enable SC monitoring when connections are expected.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1782992990487589 https://mahifx.slack.com/archives/C04AZM0LPMH/p1794790970454859 https://mahifx.slack.com/archives/C04AZM0LPMH/p1795552449593369

### velocity-ny-position-id — hybrid hedger built EURUSD/AUDUSD positions after NY-ID miss
status: open · since: 2026-11-20 · last: 2026-11-20
State: On 2026-11-20 ~02:06 UTC Velocity put ATC under margin call; Dave found 53M short EURUSD at Finalto and 20M long at Velocity (plus ~17M AUDUSD), the hedger sending orders to one LP without checking the opposite position at the other. Dave said "we can not have position buildups" and was disappointed. Daria stopped flow there and Nathan flattened EURUSD at Velocity (33.25M short at Finalto, flat Velocity) and AUDUSD (1M short Finalto, flat Velocity) by 03:13. Cause (Daria): after the NY-to-LDN migration older positions are stored under NY market IDs; the hybrid looks up positions by position ID, so with the hedger pointed at A_HOUSE it missed ~120m long EURUSD held under NY IDs, saw ATC short at Velocity and bought EURUSD there through the LPR rules. Daria switched the market position party back to HOUSE; the biggest remaining NY position is 4.2m AUDUSD and smaller ones are left to close via the hybrid. Zendesk 23880 raised for dev to fix how these positions are stored. The same pattern left GBPUSD 2.51M short at Velocity and long at Finalto on 11-20; with Malik's OK Rory turned hybridHedger1 and arbHedger1 off, bought 2,505,748 at Velocity and sold the same at Finalto at TOB, confirmed Velocity flat under HOUSE ~16:26 UTC and turned the hedgers back on; Malik confirmed plenty of margin at Velocity (Dave said it had been -20K the day before).
Next: Dev to fix NY-ID position storage (Zendesk 23880); confirm no remaining NY-ID positions; ATC to confirm NOP; Dave expects an LP-with-opposite-position routing rule.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1795140403241519 https://mahifx.slack.com/archives/C04AZM0LPMH/p1795143064229409 https://mahifx.slack.com/archives/C04AZM0LPMH/p1795192248961379

### britannia-triangle-arb — Britannia prime connectivity and triangulation arb flow
status: open · since: 2026-09-15 · last: 2026-11-25
State: Re-opened: live Britannia testing started 2026-11-09; on 11-10 Dave confirmed test account 28050001 (Seychelles side only) is mapped to Britannia, then saw Mahi apparently take the opposite side (open at the PB, flat on MT5): Daria found the counterparty on the orders was not in the broker execution rule so the trades were internalised and hedged, and added it so he can retry; Dave will test this week and next. Cameron Hughes also noted unexpected arb flow and put a broker rule above it. Dave's clients may send high-volume triangular-arb flow, to be distributed across LPs under ATC's Britannia PB setup; preferred design is a separate FIX session per LP, with Spotex possibly supplying an LP panel. Britannia approved ATC's account 2026-10-01, Malik supplied creds and product mappings, and fixOrders4/fixMarketData4 were bounced on 10-05; waiting on Britannia whitelisting. On the 10-08 call Malik worried that competitor spreads and commission (about 15c and $7/lot) are too low to compete once Britannia costs are included. On 11-09 Dave asked to test live trades on Britannia production; Cameron Hughes pointed the SC hedger at Britannia (stripping old FINALTO_BVI config), tested EURUSD and GBPUSD 1000 buy/sell via Compass, and Dave tested from MT5 on account 28050001: the first GTC order was rejected ("MFX does not accept GTC", only IOC/FOK, Rory said the rejection was not from Mahi), an IOC test filled but Dave saw no fill on the Britannia GUI. Dave then asked for that account to be brokered through to Britannia; Nathan created LIQUIDITY_POOL_BRITANNIA and a "Britannia broker test" execution profile on the SC and CATCHALL rules (11-10 02:34 UTC). Mahi still needs representative arb trade data and proof of arb for account 27072550. On 11-12 Dave asked for second PAMM test account 28050002 to be pointed at Britannia for all execution; Nathan Burch could not match it to a Compass counterparty ID (28050001 maps correctly, orders going straight to Britannia) and by 23:12 UTC inferred it is the new tag that traded 2 EURUSD 1,000 lots down the SC connection on 11-11, asking Dave to confirm before adding it to the SC execution rule. On 11-20 Dave started index tests in production on the new setup: a 0.1 US500 order on 28050001 got no fill because the Britannia SPXUSD quantity definition has min qty 1, so it was rejected internally (William Denny); Dave will retest with 1 on Monday 11-23, and the config needs changing if 0.1 is wanted. On 11-25 Dave tested US100 on 28050001 and got fills (25,141.52 entry, 25,146.36 exit) that differed from Britannia's GUI prices (25,140.77 and 25,148.02); Nathan found the SC/Britannia broker test execution profile had price improvement off, so favourable LP moves were kept by Mahi while worse ones passed through, and turned it on so client fills now equal Britannia's. Dave said this helps his testing before filters are added.
Next: Dave to retest US500 at qty 1 (was due 11-23; no result seen); Dave to confirm the 28050002 test trades (11-11 19:51 and 19:54 UTC) so Nathan can add it to the Britannia rule; Dave to confirm the test fill appears on the Britannia GUI; Cameron Hughes to model ATC's proposed spreads by volume tier with Britannia costs; Britannia WL; arb trade data and write-up for Dave and compliance.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1789485221018859 https://mahifx.slack.com/archives/C046RNF64VD/p1791214089857239 https://mahifx.slack.com/archives/C04AZM0LPMH/p1794340074134389 https://mahifx.slack.com/archives/C04AZM0LPMH/p1795643649870269

### beeks-firewall-reboot — Beeks firewall reboot maintenance window for ATC
status: open · since: 2026-11-19 · last: 2026-11-19
State: On 2026-11-19 Malik forwarded Beeks NOCINT-861756 (firewall reboot maintenance window, 15/11/2026 as stated) pending Beeks' CAB approval, and assumed Mahi handles ATC servers in the ecosystem except the MT5 server that ATC IT manages. Will told him that should be fine and asked Liam to confirm; Liam will speak to Will on 11-20.
Next: Liam/Will to confirm Mahi covers the window and Beeks CAB outcome.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1795110016057249 https://mahifx.slack.com/archives/C046RNF64VD/p1795110234856299

### spx-hedger-flatten — CFD hedger bought SPX at Velocity during flatten
status: open · since: 2026-11-10 · last: 2026-11-17
State: On 2026-11-10 ~15:30 UTC, while Cameron Hughes was flattening the CFD book via the GUI with the CFD hedger unexpectedly on, Compass CFD Praxis bought 3,168 SPX at Velocity against fake client positions (real exposure 137); Malik had Velocity undo them and it was sold back by 16:20 for a realised -$80.5k. The hedger was switched off at 16:37 and stays off overnight (residual ~-138 SPX and a few index lots unhedged unless Malik asks for a hand hedge before the roll). RCA and client report drafted for Will's sign-off; one RCA question on the 15:14 book switch is open. housePositionServer1 tradePositionInconsistent alerts fired every 5 min after the GUI flatten; CFD side resolved by Isaac, SI books still alert (Isaac, 11-11). Position corrections now go only through /position-adjustment-import with hedgers confirmed off; change records for the flattens, unwind and rule edits are owed retrospectively. On 2026-11-17 ~15:49 UTC Rory bounced hybridHedgerPraxis1 (trades to Velocity) after DOW risk would not clear: the hedger had dynamic speed scaling left at 0.001, reverted to 1; midStyle was switched from adaptive to execution markets and scaling raised to 100, and the DOW then hedged with a profit (Will: "we can say it was hedging", but another FCA headache); which change allowed it is still unclear. Will wants the CFD structure cleaned up (separate book per LP dates from before trade position tracking; rename hedging procs to hybridCFD1) as a long-term plan alongside running risk.
Next: Rory to establish whether midStyle or speed scaling cleared the DOW; Will to plan the CFD book/hedger rename; Will to sign off and send the client report to Malik by 09:00 11-11; Isaac to clear the SI-book alerts; CFD hedger back on only after the rebase; retrospective change records.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1794325120967939 https://mahifx.slack.com/archives/C046RNF64VD/p1794332098551479 https://mahifx.slack.com/archives/C046RNF64VD/p1794930550849329

### pnl-currency-rec — non-USD P&L legs and LP position reconciliation
status: open · since: 2026-07-09 · last: 2026-11-17
State: Compass books realised P&L in the counter currency, so cross flow (AUDNZD, GBPNZD etc.) leaves non-USD P&L balances (about 21.7m NZD) that the hedger treats as risk and hedges at the LPs. Finalto and ATC cash are USD-only, so those LP positions (about $12m short NZD, $4.5m long JPY) are real exposure with no client trade behind them; ATC's compliance officer flagged this to auditors and the FCA on 2026-10-01 and has accepted the mechanism. Agreed fix is converting P&L legs to USD in Compass as a weekend flatten and reimport (duplicate trade-position rows from the NY-to-LDN move, Zendesk 23171, still need cleaning), then a currency-level rec with ATC. On 10-08 Malik asked for a systematic conversion to limit spread cost; the three P&L models (Compass, Finalto, MetaQuotes) disagree. On 2026-10-26 Andrew said the technical gap is known and CPS is fixing it but a HPS fix may be brought forward; the July USD adjustment was never done (NZD residual about 30.9m on 09-29, JPY 637m) and a counter-currency to USD or deposit currency conversion is needed. On 2026-11-17 Will estimated ATC rec work at roughly 250-330 hours since Nov 2023 (120-180h of it on the currency/position issue since July) and said the aim is a currency rec that ends manual breaks rather than more one-off fixes.
Next: Cameron Hughes to revert to Malik with a full-rec plan and schedule the weekend flatten/reimport (Daria, Liam); build the ongoing currency-level rec.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1783567793838579 https://mahifx.slack.com/archives/C046RNF64VD/p1790850531938759 https://mahifx.slack.com/archives/C046RNF64VD/p1791463861287519 https://mahifx.slack.com/archives/C046RNF64VD/p1794907226788829

### client-exec-incidents — pricing and fill incidents reported by Dave M
status: open · since: 2026-08-11 · last: 2026-11-16
State: Recurring client-reported issues: skew floors distorting EURUSD/USDCHF/GBPUSD (08-11; Daria fixed config; ATC's historical-data cleanup request never actioned); silver fills outside range (08-19, brokered-LR feedback loop, Zendesk 23372); SPX/NDX stopped ticking ~1h20 on 09-17/18 and NDX orders expired 09-18 (backup aggregation process stopped carrying NDX; bounced, root cause open). On 2026-11-05 Dave flagged 27072570 as a $1M account that will deposit more if fills are clean; Cameron Hughes checked config and put custom rules on the account's tag to avoid bad fills, and Dave acked. On 2026-11-16 Dave emailed support and asked for a same-day answer on large-order slippage on both legs; Rory explained that since the 11-04 full-STP agreement (FX and metals brokered from 11-06, this account from 11-10) every order fills against Finalto's thinner book rather than the CLIENT_PRICE_LDN DOM, so a 6mio order walks several levels; Mahi was backtesting matching its pricing depth to Finalto's. That evening FX, metals and indices were switched back to internalisation after Malik's call with Daria, to protect client execution (see lp-cross-positions).
Next: Dave to confirm the slippage complaint is resolved by internalisation; Mahi owes root-cause for the NDX aggregation stall and the 09-17 publishing stall; watch 27072570 fills and any complaints; historical data cleanup request from 08-12 still open.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1786480031117319 https://mahifx.slack.com/archives/C046RNF64VD/p1787568429179159 https://mahifx.slack.com/archives/C04AZM0LPMH/p1793895619556529 https://mahifx.slack.com/archives/C04AZM0LPMH/p1794855820849239

### lp-cross-positions — legacy cross positions at Finalto and auditor questions
status: open · since: 2026-10-26 · last: 2026-11-16
State: ATC's compliance contact and auditors are not satisfied that Mahi-held positions (NZD crosses etc.) far exceed client trades while ATC is a matched principal at FCA level; Andrew treats it as an escalation and the auditor threatened (11-02) to go to the FCA. Finalto crosses are legacy brokered inventory (Sep 2023 to Sep 2024) never unwound because hedgers only trade USD pairs. Mahi built a recon artifact and compliance response pack (11-03) conceding NZD 24.43M (~$13.8m) as a real residual from P&L booking, not a trading decision. On 11-04 ATC was advised to self-report a matched-principal breach to the FCA; Mahi traded out the open Finalto exposure, ATC moved to brokering then full STP (execution rules from 11-06). Daria and Cameron Hughes' weekend rec left A_HOUSE aligned with ATC FX and metals by 11-09; ATC's rec script will diverge until SI books are sorted and HOUSE is re-aligned with A_HOUSE (Cameron Hughes).
On 11-09 all books except A and CFD were flat; Malik's rec found USDCHF off by 1.8m between Finalto and Velocity, and Daria and Shyam made final trades at 21:58 UTC before ATC's 22:00 self-report deadline; Malik confirmed CHF "off by 9300", though Daria says ~1m CHF is still unexplained (~700k price differences). On 11-10 Malik said ATC breached an FCA capital hard limit and self-reported, and compliance does not accept "we had a problem and fixed it". Will's plan was a Compass rebase (positions reset to Spotex and Finalto/Velocity statements, hedgers off, red change record), blocked on root cause (cross P&L booked in quote currency, or the migration position-ID issue). Malik's consultants see ~GBP 10.5m non-GBP exposure vs Compass GBP 5.2m; Will told Malik every non-USD currency reconciles and the ~USD 10m gap is accumulated hedging P&L with GBP translation risk. On 11-11 Jack accepted ("got it, close it"); David Cooney questioned why positive USD P&L breaches matched principal.
On 11-16 ATC switched back to internalisation after Dave's slippage complaint; FX, metals and indices were switched back that evening. Daria proposed ATC reconcile currency positions across Finalto, Velocity and Spotex and flag growing exposure (Malik agreed to build it; ends when ATC moves to Seychelles, ~a month away). Finalto swaps are now based on currency positions. Malik "supposedly" self-reported to the FCA on 11-15. Whether crosses are brokered or the pool feed published stays open. See velocity-ny-position-id for the 11-20 build-up.
Next: Malik to build the currency position rec and flag growing exposure; Daria to explain the remaining ~1m CHF gap; confirm whether the Compass rebase and its root-cause check still happen; ATC compliance verification; Will/Cameron Hughes to finish the response pack and get Andrew's OK; Mahi to present a close-the-gap plan for written ATC sign-off, agree Finalto's mark and fee, then ask Finalto to rebook; pull the Oct 2023 and 2026-06-25 import files for auditors.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1793025346402589 https://mahifx.slack.com/archives/C046RNF64VD/p1793634692520699 https://mahifx.slack.com/archives/C046RNF64VD/p1794383273171979 https://mahifx.slack.com/archives/C046RNF64VD/p1794865644760119

### futures-crypto-ask — futures, XAU futures symbol and crypto setup
status: open · since: 2026-10-26 · last: 2026-11-12
State: On 11-12 Dave sent a list of extra symbols to support; Nathan Burch replied all exist in Compass, EURCZK, EURHUF, USDCZK and USDILS are available now, and eight FX (CADSGD, CHFDKK, GBPCZK, GBPDKK, EURHKD, EURILS, GBPHKD, GBPTRY) and eight CFDs (SPA35, CN50, SWI20, USDX, TWN, XAUIDX, NATGAS, SG30) need an LP to stream them. On 10-29 Malik asked Andrew for a 15-20 min call because Dave wants to understand how Mahi works with futures instruments; Andrew was on holiday so Will took it with Dave (Andrew suggested demoing some contracts and asking for data). Will reported ATC is happy with the P/W framework used elsewhere, will talk again early next week if issues, and that the futures feeds would come through Britannia, with about a day to get the system ready after that. After a pre-call with Malik, Andrew noted ATC is courting basis traders in futures, wants a crypto setup (with its own LP), and G7 futures quoted as CFDs; Andrew wants an XAU futures symbol added. Mahi also needs ATC client and LP positions ingested into Compass for reconciliation and swap calcs; a swap inventory skew CSV is owed to ATC. Mahi is looking for other firms quoting G7 futures as CFDs (Amana was named as having CMC, Jump, IG, GCEX).
Next: Mahi to send swap inventory skew CSV and ingest ATC positions; scope the XAU futures symbol and crypto setup.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1793009406477699 https://mahifx.slack.com/archives/C046RNF64VD/p1793033858681609 https://mahifx.slack.com/archives/C046RNF64VD/p1793290830652219 https://mahifx.slack.com/archives/C04AZM0LPMH/p1794513373925249

### eurchf-arb-pnl-drop — EURCHF arb hit and P&L drop on 11-03
status: open · since: 2026-11-03 · last: 2026-11-03
State: On 2026-11-03 Will flagged a P&L drop at ~07:10 UTC and traced it to an arbitrageur hitting an EURCHF price (yield profiles and price forensics shared); the same account tried again but the following trades were cancelled. Will added a continuity-fee markup in the channel explorer for the SNGMON zone as a response.
Next: Watch whether EURCHF arbing recurs after the markup.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1793696634409629 https://mahifx.slack.com/archives/C046RNF64VD/p1793697495114959

### gold-position-mismatch — Compass vs ATC gold positions disagree
status: open · since: 2026-10-29 · last: 2026-10-29
State: On 10-29 Dave said ATC's gold positions do not match Compass, and that FAU shows zero open positions at ATC, Spotex and Finalto (no SHI at Finalto either). Compass shows net client positions XAU -280.9 and SHI 309.4; Cameron Hughes suspected client and LP positions diverged during a failover and said he is looking into it. Likely related to the xbt-phantom-position pattern of Compass holding positions that do not exist at the LP.
Next: Cameron Hughes to reconcile Compass XAU/FAU/SHI positions against ATC and Finalto and adjust Compass.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1793286377179559 https://mahifx.slack.com/archives/C04AZM0LPMH/p1793293226695989

### monthly-pnl-report — monthly P&L report for Jack
status: watching · since: 2026-06-07 · last: 2026-11-10
State: Jack Manoukian wants the P&L report alongside each invoice; August was requested 2026-09-12 (Bonnie asked if it could be sent proactively), September was posted unprompted by Cameron Hughes on 10-01, and October was requested by Jack and delivered by Cameron Hughes on 11-10. April trade CSVs were delivered 09-17.
Next: November report due start of December.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1780865571965479 https://mahifx.slack.com/archives/C04AZM0LPMH/p1789217003836759 https://mahifx.slack.com/archives/C04AZM0LPMH/p1794322207441799

### prop-launch — ATC Prop firm: servers, rules, go-live
status: watching · since: 2026-08-05 · last: 2026-10-14
State: Downgraded to watching 2026-11-16: no prop-channel activity since 2026-10-14, Jack's API-data email reply status unknown. Go-live plan of record and programme rules are filed in MahiProduct (agreed at the 2026-08-19 meeting); ATC runs its own prop bridge and MT5 install, Mahi supplies the Beeks server and Compass (atc-prop-ln). Conformance passed 2026-09-11, prop FIX creds (qualifying and funded) sent, and Malik asked for prod IPs to be whitelisted on 2026-09-30 (proptrading and brokerage). Open commercial item: ATC's in-house prop CRM resale as a white-label bundled with Mahi liquidity needs written sub-licence agreement and a pricing steer (Andrew/Will, alongside the Seychelles addendum). Jack's 2026-10-08 email asking what API data Mahi wants for anti-predatory safeguards has had no reply for 6 days.
Next: Cameron Hughes to send Jack a holding reply and then the API data list; Andrew/Will to give commercial steer on CRM sub-licensing; confirm drawdown calc mechanics with ATC.
Refs: https://mahifx.slack.com/archives/C0AQ3PVTX6D/p1787125125063369 https://mahifx.slack.com/archives/C0AQ3PVTX6D/p1787210584953589 https://mahifx.slack.com/archives/C0AQ3PVTX6D/p1791963840973209

### compass-26-4 — Compass 26.3 to 26.4 upgrade
status: watching · since: 2026-10-08 · last: 2026-10-13
State: ATC staged 26.4 on 10-09 and went live at the weekend restart (client notified in #mahi-atc). Because ATC sets neither `adjustmentSignalParametersForWidening` nor `...ForTightening`, prices now widen/tighten one increment on PSM-W/PSM-T signals (Liam decided to let it go ahead). `arbHedger1` failed to start on the first RC and was fixed (precheck success). A dashboard-component deploy also hit ATC on 10-13. No client-reported regression yet.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1791483329972859 https://mahifx.slack.com/archives/C04AZM0LPMH/p1791543785439449 https://mahifx.slack.com/archives/C046RNF64VD/p1791866234975939

### xau-hedging — gold hedging and P&L bleed
status: watching · since: 2026-05-27 · last: 2026-10-08
State: SHI/FAU hedging was merged into XAUUSD at Finalto (June) with covariance fixes, and XAU spread/BMSL/hedger tuning continued through the summer. Recent P&L drops were mostly false or transient: -$1k on 09-14 when Finalto rejects slowed risk clearing after $10M XAU trades; a ~$4k drop on 10-08 from bad final Velocity ticks into the roll that recovered. Malik wants to cut dependence on Finalto, and Velocity usage is deliberately limited to avoid large opposite positions.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1779890363013439 https://mahifx.slack.com/archives/C046RNF64VD/p1789360531094629 https://mahifx.slack.com/archives/C046RNF64VD/p1791499053655529

### velocity-depth-cap — Velocity data load
status: watching · since: 2026-10-05 · last: 2026-10-05
State: No activity since 2026-10-05; downgraded to watching. Velocity complained about ATC's market-data consumption (up to 30 layers per instrument). Cameron Hughes agreed to cap the depth request at 10 on both Velocity logins (main and BVI; Velocity only sends 5 levels so pricing is unaffected) after an EOD restart, and noted that roughly 935 symbols per login is likely the bigger load. Malik will contact Velocity; no confirmation the cap or any symbol trim was applied.
Next: Malik to relay Velocity's response and any symbols to drop; Cameron Hughes to confirm the cap is live.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1791190471362809 https://mahifx.slack.com/archives/C04AZM0LPMH/p1791215001177869

### xbt-phantom-position — XBTUSD and DOW CFD positions differ from ATC's own rec
status: closed · since: 2026-10-26 · last: 2026-10-26 · closed: 2026-11-26
State: No activity since 2026-10-26; assumed resolved (position rec work continues under lp-cross-positions and gold-position-mismatch). ATC's own rec flagged CFD differences on 2026-10-26: XBTUSD is flat on ATC's side and at Finalto while Compass shows 64 client and LP side, and DOW is about 0.5 on the client side versus 1.77 in Compass (not netted to Velocity correctly). Dave asked why Compass shows a position that does not exist at Finalto; Cameron Hughes said it is likely trading outside Compass (manual close-outs or failover routing) and Compass needs position updates, being worked with Malik. CFDs hedge 1-1 with the inbound instrument.
Next: Malik to confirm exact client positions to book; Mahi to adjust Compass positions.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1793023106101569 https://mahifx.slack.com/archives/C04AZM0LPMH/p1793023353198839 https://mahifx.slack.com/archives/C046RNF64VD/p1793027080083249

### xau-depth-ladder — gold depth question for a prospective large client
status: closed · since: 2026-10-13 · last: 2026-10-21 · closed: 2026-11-23
State: No activity since 2026-10-21; assumed resolved. XAUUSD ladder is floored at the LP spread (~3k oz firm depth behind 12.6k published); Dave relied on the numbers.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1791902732632709 https://mahifx.slack.com/archives/C04AZM0LPMH/p1791907572332459 https://mahifx.slack.com/archives/C04AZM0LPMH/p1792590024121469

### beeks-ld-incident — Beeks LD networking incident, ATC failover
status: closed · since: 2026-10-16 · last: 2026-10-16 · closed: 2026-11-16
State: No activity since 2026-10-16; assumed resolved. A Beeks LD networking incident hit ATC's spotex MT5 sessions; ATC failed over and Liam said it was safe to switch back around 12:07 BST.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1792143086471619 https://mahifx.slack.com/archives/C04AZM0LPMH/p1792150199815879

### fxcm-connection — FXCM logon rejects and failed auto-restarts
status: closed · since: 2026-06-04 · last: 2026-09-23 · closed: 2026-11-23
State: No activity since 2026-09-23; assumed resolved. FXCM logon rejects since 08-16 and failing post-restart auto-restarts were left with ATC to raise with FXCM.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1786947960799679 https://mahifx.slack.com/archives/C0AQ3PVTX6D/p1787127331818279 https://mahifx.slack.com/archives/C046RNF64VD/p1790183042306349

### cfd-arb-execution — CFD arbitrageur execution rules
status: closed · since: 2026-09-21 · last: 2026-09-23 · closed: 2026-11-23
State: No activity since 2026-09-23; assumed resolved. CFD arb rules restored 09-22 with 10 $/M extra slippage; benchmarkNormalised override fixed false arb classifications.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1790005631153139 https://mahifx.slack.com/archives/C046RNF64VD/p1790088439159019 https://mahifx.slack.com/archives/C046RNF64VD/p1790154076347849

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
