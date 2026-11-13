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
last_catchup: 2026-11-13T08:13:58Z
status: active
---
## Now
ATC is a matched-principal broker in a build phase (prop launch, Britannia prime for triangulation-arb flow, Seychelles migration); volumes are well down and it is sensitive to gold spreads, depth and fills.
Top risk: Mahi-held LP cross positions (NZD etc.) dwarf client trades; auditors/compliance escalated 11-02/03 and on 11-04 ATC was advised to self-report a matched-principal breach to the FCA.
11-10/11: USD gap explained to Malik/Jack as accumulated hedging P&L (~USD 10m, GBP translation risk); Compass rebase planned for 11-11 17:00 NY; an SPX hedger mishap (-$80.5k) on 11-10 left CFD hedgers off. Earlier response: Finalto exposure traded out, ATC on full STP, books flattened and ATC self-reported 11-09 evening after a last-minute CHF rec (~1m CHF still unexplained); live Britannia test trades started 11-09; gold positions mismatch (10-29) and Compass 26.4 PSM overlays also live.

## Streams

### britannia-triangle-arb — Britannia prime connectivity and triangulation arb flow
status: open · since: 2026-09-15 · last: 2026-11-12
State: Re-opened: live Britannia testing started 2026-11-09; on 11-10 Dave confirmed test account 28050001 (Seychelles side only) is mapped to Britannia, then saw Mahi apparently take the opposite side (open at the PB, flat on MT5): Daria found the counterparty on the orders was not in the broker execution rule so the trades were internalised and hedged, and added it so he can retry; Dave will test this week and next. Cameron Hughes also noted unexpected arb flow and put a broker rule above it. Dave's clients may send high-volume triangular-arb flow, to be distributed across LPs under ATC's Britannia PB setup; preferred design is a separate FIX session per LP, with Spotex possibly supplying an LP panel. Britannia approved ATC's account 2026-10-01, Malik supplied creds and product mappings, and fixOrders4/fixMarketData4 were bounced on 10-05; waiting on Britannia whitelisting. On the 10-08 call Malik worried that competitor spreads and commission (about 15c and $7/lot) are too low to compete once Britannia costs are included. On 11-09 Dave asked to test live trades on Britannia production; Cameron Hughes pointed the SC hedger at Britannia (stripping old FINALTO_BVI config), tested EURUSD and GBPUSD 1000 buy/sell via Compass, and Dave tested from MT5 on account 28050001: the first GTC order was rejected ("MFX does not accept GTC", only IOC/FOK, Rory said the rejection was not from Mahi), an IOC test filled but Dave saw no fill on the Britannia GUI. Dave then asked for that account to be brokered through to Britannia; Nathan created LIQUIDITY_POOL_BRITANNIA and a "Britannia broker test" execution profile on the SC and CATCHALL rules (11-10 02:34 UTC). Mahi still needs representative arb trade data and proof of arb for account 27072550. On 11-12 Dave asked for second PAMM test account 28050002 to be pointed at Britannia for all execution; Nathan Burch could not match it to a Compass counterparty ID (28050001 maps correctly, orders going straight to Britannia) and by 23:12 UTC inferred it is the new tag that traded 2 EURUSD 1,000 lots down the SC connection on 11-11, asking Dave to confirm before adding it to the SC execution rule.
Next: Dave to confirm the 28050002 test trades (11-11 19:51 and 19:54 UTC) so Nathan can add it to the Britannia rule; Dave to confirm the test fill appears on the Britannia GUI; Cameron Hughes to model ATC's proposed spreads by volume tier with Britannia costs; Britannia WL; arb trade data and write-up for Dave and compliance.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1789485221018859 https://mahifx.slack.com/archives/C046RNF64VD/p1791214089857239 https://mahifx.slack.com/archives/C04AZM0LPMH/p1794340074134389 https://mahifx.slack.com/archives/C04AZM0LPMH/p1794525133887599

### futures-crypto-ask — futures, XAU futures symbol and crypto setup
status: open · since: 2026-10-26 · last: 2026-11-12
State: On 11-12 Dave sent a list of extra symbols to support; Nathan Burch replied all exist in Compass, EURCZK, EURHUF, USDCZK and USDILS are available now, and eight FX (CADSGD, CHFDKK, GBPCZK, GBPDKK, EURHKD, EURILS, GBPHKD, GBPTRY) and eight CFDs (SPA35, CN50, SWI20, USDX, TWN, XAUIDX, NATGAS, SG30) need an LP to stream them. On 10-29 Malik asked Andrew for a 15-20 min call because Dave wants to understand how Mahi works with futures instruments; Andrew was on holiday so Will took it with Dave (Andrew suggested demoing some contracts and asking for data). Will reported ATC is happy with the P/W framework used elsewhere, will talk again early next week if issues, and that the futures feeds would come through Britannia, with about a day to get the system ready after that. After a pre-call with Malik, Andrew noted ATC is courting basis traders in futures, wants a crypto setup (with its own LP), and G7 futures quoted as CFDs; Andrew wants an XAU futures symbol added. Mahi also needs ATC client and LP positions ingested into Compass for reconciliation and swap calcs; a swap inventory skew CSV is owed to ATC. Mahi is looking for other firms quoting G7 futures as CFDs (Amana was named as having CMC, Jump, IG, GCEX).
Next: Mahi to send swap inventory skew CSV and ingest ATC positions; scope the XAU futures symbol and crypto setup.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1793009406477699 https://mahifx.slack.com/archives/C046RNF64VD/p1793033858681609 https://mahifx.slack.com/archives/C046RNF64VD/p1793290830652219 https://mahifx.slack.com/archives/C04AZM0LPMH/p1794513373925249

### seychelles-uat — Seychelles entity, dev connections and UAT feed
status: open · since: 2026-05-19 · last: 2026-11-12
State: On 2026-11-12 Dave reported no prices for index and energy CFDs on SC production; Nathan Burch found none of the instruments in LIQUIDITY_POOL_SC (the channel's core price selector) so nothing was published, and will add them with a pool restart scheduled for EOD. Seychelles (SC) infrastructure is live (SC channel, books, hedgers) with BVI-only LP routing; on the 2026-09-16 call Malik said ATC wants to move from UK plus SC connections to SC only, and ATC's dev team needs connections to both servers (two new sessions for ATC Broker). UAT feed/server restarts are a recurring ask from Malik and Dave (09-02, 09-14, 09-21, 09-28, 10-07, 10-12, 10-19, 10-26, 11-02, 11-10 (Malik, Rory actioned); on 11-09 Dave asked again at 19:54 UTC; 11-02 Dave asked at 04:57 UTC and Daria started it by 05:05, Dave acked); the realistic gateway moved to 9012/9013 on 09-14 so ATC needed re-whitelisting and port changes. SC monitoring was toggled off in August pending connections. On 2026-11-02 Daria reported the MT5 SC orders session (orders_mt5_sc) could not log on from 00:00 UTC: MT5 reset FIX sequence numbers at 00:00 while Mahi's session runs Sunday 20:00 to Friday 21:00 UTC; ATC asked to align the MT5 side to the weekly schedule; Cameron Hughes forwarded it internally and Malik and Patrick were looking into it by 14:23 UTC.
Next: Nathan to add the CFDs to LIQUIDITY_POOL_SC at the EOD pool restart and confirm to Dave; ATC to align orders_mt5_sc MT5 reset schedule with Sun 20:00-Fri 21:00 UTC; Mahi to create the two dev connections; re-enable SC monitoring when connections are expected.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1782992990487589 https://mahifx.slack.com/archives/C04AZM0LPMH/p1793582879361799 https://mahifx.slack.com/archives/C04AZM0LPMH/p1794316877201149 https://mahifx.slack.com/archives/C04AZM0LPMH/p1794512686696149

### lp-cross-positions — legacy cross positions at Finalto and auditor questions
status: open · since: 2026-10-26 · last: 2026-11-11
State: ATC's compliance contact and auditors are not satisfied that Mahi-held positions (NZD crosses etc.) far exceed client trades while ATC is a matched principal at FCA level; Andrew treats it as an escalation and the auditor threatened (11-02) to go to the FCA. Finalto crosses are legacy brokered inventory (Sep 2023 to Sep 2024) never unwound because hedgers only trade USD pairs. Mahi built a recon artifact and a compliance response pack (11-03) conceding the NZD 24.43M (~$13.8m) as a real residual created by P&L booking, not a trading decision; Compass cannot know when LP balances auto-convert to USD. On 11-04 ATC was advised to self-report a matched-principal breach to the FCA; Mahi traded out the open Finalto exposure overnight (small loss, Malik fine), and ATC moved to brokering and then full STP. Daria and Cameron Hughes' weekend full rec (flatten, import ATC's actual positions) left A_HOUSE aligned with ATC FX and metals by 11-09 01:49 UTC. On 2026-11-06 Cameron Hughes created broker execution rules so all non-arb FX, metals and CFD flow is brokered until Britannia is onboard (ahead of NFP). ATC's reconciliation script will still show divergences until the SI book positions are sorted and HOUSE is re-aligned with A_HOUSE (Cameron Hughes to pick up); ATC was told in #mahi-atc.
On 2026-11-09 the SI book and then all books except A and CFD were flat (Cameron Hughes), ATC switched to full STP, and the plan is compliance verification, report to the FCA, then Britannia. Malik's rec the same evening found USDCHF off by 1.8m between Finalto and Velocity; Daria and Shyam made final trades at 21:58 UTC to beat ATC's 22:00 self-report deadline, Malik confirmed CHF "off by 9300", and opposite Finalto/Velocity positions plus small HSI/DOW positions with no client side were closed. Daria's working theory (10-Nov) is that ~700k of the CHF gap was price differences (adjustment used 0.82051, Spotex likely 0.7966, matching the NY USDCHF position price); about 1m is still unexplained, update due by EOD 11-10. Future recs should use both trade and currency positions with prices.
On 2026-11-10 Malik said ATC breached an FCA capital hard limit and had to self-report that day, and that compliance still sees mismatches and does not accept "we had a problem and fixed it". Will's 10 Nov open-issues list puts a Compass rebase at the Wed 11 Nov 17:00 NY cut (22:00 UK; reset client positions to Spotex and Finalto/Velocity to statements, hedgers off, red change record with a second checker, confirm to Malik by 23:30), with root cause blocking it: whether cross P&L is still booked in the quote currency and hedged at the LP, or the server-migration position-ID issue (45 TradePositions-vs-Positions errors). Malik's consultants say ATC carries about GBP 10.5m of non-GBP (mostly USD) exposure because GBP is its currency of account; Compass sees about GBP 5.2m. Andrew's Pulse read (unverified) shows roughly $11-14m of realised P&L sitting as USD balance with no trade behind it, and he proposed a per-currency rec (Spotex vs Compass client vs Compass LP vs LP statements). By the evening Will told Malik every non-USD currency reconciles and the ~USD 10m difference is accumulated hedging P&L with GBP translation risk (Malik: "phew"); Cameron Hughes' timeline records Compass converting P&L to USD as the 12-10 fix and Will floated GBP P&L reporting as a large roadmap item. The same night Jack asked how to close the USD gap; Daria noted it cannot be netted into GBP and that closing and reopening positions to realise P&L would cost spread. On 11-11 Will said Jack had accepted the explanation ("got it, close it") and wanted a call with Malik that morning to close the matter; David Cooney questioned why positive USD P&L breaches matched principal.
Next: Daria to explain the remaining ~1m CHF gap; confirm the Wed 17:00 NY rebase, its root-cause check and change record; call with Malik/Jack on 11-11 to close the USD point; ATC compliance verification and FCA report; Malik's brokering decision (now full STP); Will/Cameron Hughes to finish the response pack placeholders and get Andrew's OK on Q4; Mahi to present a close-the-gap plan and set up regular divergence meetings; Malik to supply LP statements and swap sheets; Mahi to present the plan to ATC and obtain written sign-off, agree Finalto's mark and fee, then ask Finalto to rebook; Andrew to sign off the history section; pull the Oct 2023 and 2026-06-25 import files for auditors.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1793025346402589 https://mahifx.slack.com/archives/C046RNF64VD/p1793634692520699 https://mahifx.slack.com/archives/C046RNF64VD/p1793817981496309 https://mahifx.slack.com/archives/C046RNF64VD/p1794383273171979

### spx-hedger-flatten — CFD hedger bought SPX at Velocity during flatten
status: open · since: 2026-11-10 · last: 2026-11-10
State: On 2026-11-10 ~15:30 UTC, while Cameron Hughes was flattening the CFD book via the GUI with the CFD hedger unexpectedly on, Compass CFD Praxis bought 3,168 SPX at Velocity against fake client positions (real exposure 137); Malik had Velocity undo them and it was sold back by 16:20 for a realised -$80.5k. The hedger was switched off at 16:37 and stays off overnight (residual ~-138 SPX and a few index lots unhedged unless Malik asks for a hand hedge before the roll). RCA and client report are drafted, client report to Will for sign-off then Malik by 09:00 Wed 11 Nov; one RCA question on the 15:14 book switch is open. Arun separately reported housePositionServer1 tradePositionInconsistent alerts firing every 5 min since the GUI flatten of currency positions zeroed balances Daria had realigned; the CFD side was resolved by Isaac but the SI books still alert and Isaac was handed it on 11-11. Position corrections now go only through /position-adjustment-import with hedgers confirmed off; change records for the flattens, unwind and rule edits are owed retrospectively.
Next: Will to sign off and send the client report to Malik by 09:00 11-11; Isaac to clear the SI-book alerts; CFD hedger back on only after the rebase; retrospective change records.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1794325120967939 https://mahifx.slack.com/archives/C046RNF64VD/p1794332098551479 https://mahifx.slack.com/archives/C046RNF64VD/p1794333405355459

### client-exec-incidents — pricing and fill incidents reported by Dave M
status: open · since: 2026-08-11 · last: 2026-11-05
State: Recurring client-reported issues: skew floors distorting EURUSD/USDCHF/GBPUSD (08-11; Daria fixed config, Will took a fleet-wide skew review, ATC's historical-data cleanup request never actioned); silver fills outside market range (08-19, root cause a brokered-LR feedback loop after Finalto pulled its bid, Zendesk 23372); SPX/NDX stopped ticking for ~1h20 on 09-17/18 (internal messaging reset) and NDX orders expired on 09-18 because a backup market-data aggregation process stopped carrying NDX (bounced; root cause still to investigate). On 2026-10-13 Dave reported account 27072570 orders not filling; Nathan found no rejects or cancels in Compass and no further reply. On 2026-11-05 Dave flagged 27072570 as a $1M account that will deposit more if fills are clean; Cameron Hughes checked config and put custom rules on the account's tag to avoid bad fills, and Dave acked.
Next: Mahi owes root-cause for the NDX aggregation stall and the 09-17 publishing stall; watch 27072570 fills and any complaints; historical data cleanup request from 08-12 still open.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1786480031117319 https://mahifx.slack.com/archives/C046RNF64VD/p1787568429179159 https://mahifx.slack.com/archives/C04AZM0LPMH/p1789749067038009 https://mahifx.slack.com/archives/C04AZM0LPMH/p1793895619556529

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

### xbt-phantom-position — XBTUSD and DOW CFD positions differ from ATC's own rec
status: open · since: 2026-10-26 · last: 2026-10-26
State: ATC's own rec flagged CFD differences on 2026-10-26: XBTUSD is flat on ATC's side and at Finalto while Compass shows 64 client and LP side, and DOW is about 0.5 on the client side versus 1.77 in Compass (not netted to Velocity correctly). Dave asked why Compass shows a position that does not exist at Finalto; Cameron Hughes said it is likely trading outside Compass (manual close-outs or failover routing) and Compass needs position updates, being worked with Malik. CFDs hedge 1-1 with the inbound instrument.
Next: Malik to confirm exact client positions to book; Mahi to adjust Compass positions.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1793023106101569 https://mahifx.slack.com/archives/C04AZM0LPMH/p1793023353198839 https://mahifx.slack.com/archives/C046RNF64VD/p1793027080083249

### pnl-currency-rec — non-USD P&L legs and LP position reconciliation
status: open · since: 2026-07-09 · last: 2026-10-26
State: Compass books realised P&L in the counter currency, so cross flow (AUDNZD, GBPNZD etc.) leaves non-USD P&L balances (about 21.7m NZD) that the hedger treats as risk and hedges at the LPs. Finalto and ATC cash are USD-only, so those LP positions (about $12m short NZD, $4.5m long JPY) are real exposure with no client trade behind them; ATC's compliance officer flagged this to auditors and the FCA on 2026-10-01 and has accepted the mechanism. Agreed fix is converting P&L legs to USD in Compass as a weekend flatten and reimport (duplicate trade-position rows from the NY-to-LDN move, Zendesk 23171, still need cleaning), then a currency-level rec with ATC. On 10-08 Malik asked for a systematic conversion to limit spread cost; Liam laid out the three P&L models (Compass, Finalto, MetaQuotes) that disagree. On 09-22 Cameron Hughes confirmed no net per-asset risk between ATC and LPs. On 2026-10-26 Andrew said the technical gap is known and CPS is fixing it but a HPS fix may be brought forward; the July USD adjustment was never done (NZD residual about 30.9m on 09-29, JPY 637m) and a counter-currency to USD or deposit currency conversion is needed. Andrew also called the swap risk on a book meant to be zero "crazy".
Next: Cameron Hughes to revert to Malik with a full-rec plan and schedule the weekend flatten/reimport (Daria, Liam); build the ongoing currency-level rec.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1783567793838579 https://mahifx.slack.com/archives/C046RNF64VD/p1790850531938759 https://mahifx.slack.com/archives/C046RNF64VD/p1791463861287519 https://mahifx.slack.com/archives/C046RNF64VD/p1793028994527199

### xau-depth-ladder — gold depth question for a prospective large client
status: open · since: 2026-10-13 · last: 2026-10-21
State: Dave noticed XAUUSD levels 3-5 showing identical bid/ask while preparing for a large prospect. Cameron Hughes explained the ladder is floored at the average Finalto+Velocity spread (about 70c at 1.6k oz) so deeper levels repeat the price until the 80c base spread at 12.6k; clients see the repeated tiers merged into one ~7k band. Mahi publishes 12.6k oz per side but only about 3k oz is backed by firm LP depth, so a 5k order is chipped away rather than cleared at once. Dave confirmed he will rely on those numbers. Separately Dave asked about a client's trading style (trade logs from Malik) and Cameron said that analysis is still in progress.
On 2026-10-21 Dave again needed to show XAUUSD depth to a client and reported it invisible for days; Rory King saw normal depth on Mahi's side and suggested a hard refresh, which did not help, but removing and re-adding the symbol fixed it (client-side display issue, resolved).
Next: Cameron Hughes owes the trading-style analysis; Dave to decide whether to widen the 1.6k/3.6k/7.6k base spreads above the LP floor or drop the floor.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1791902732632709 https://mahifx.slack.com/archives/C04AZM0LPMH/p1791907572332459 https://mahifx.slack.com/archives/C04AZM0LPMH/p1792590024121469

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

### monthly-pnl-report — monthly P&L report for Jack
status: watching · since: 2026-06-07 · last: 2026-11-10
State: Jack Manoukian wants the P&L report alongside each invoice; August was requested 2026-09-12 (Bonnie asked if it could be sent proactively), September was posted unprompted by Cameron Hughes on 10-01, and October was requested by Jack and delivered by Cameron Hughes on 11-10. Jack also asked for April client and LP trade CSVs by POP (delivered 09-17); end-April Finalto-only open positions were unavailable as that data has only been persisted since late June.
Next: October report due start of November.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1780865571965479 https://mahifx.slack.com/archives/C04AZM0LPMH/p1789217003836759 https://mahifx.slack.com/archives/C04AZM0LPMH/p1794322207441799

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

### fxcm-connection — FXCM logon rejects and failed auto-restarts
status: watching · since: 2026-06-04 · last: 2026-09-23
State: No activity since 2026-09-23; downgraded to watching. FXCM session is up but auto-restarts after weekend restarts keep failing and need a manual restart (still true 2026-09-23). Logon rejects began Sunday 2026-08-16 (Daria's question on 08-17 about `user not recognised or password incorrect` got no reply), likely a credential change; FXCM also wanted to publish only TOB to ATC. ATC said they would raise it with FXCM and had not as of 08-19; Malik reportedly tired of the issue and may leave Britannia to handle it.
Next: Malik owes the FXCM follow-up; Cameron Hughes sent a chaser 08-19.
Refs: https://mahifx.slack.com/archives/C04AZM0LPMH/p1786947960799679 https://mahifx.slack.com/archives/C0AQ3PVTX6D/p1787127331818279 https://mahifx.slack.com/archives/C046RNF64VD/p1790183042306349

### cfd-arb-execution — CFD arbitrageur execution rules
status: watching · since: 2026-09-21 · last: 2026-09-23
State: CFD arbitrageur execution was turned off 2026-09-21 after two of Dave's clients complained (mostly intentional flow; he wants good relationships and whitelisting by daily check). On 09-22 rules were restored with 10 $/M additional slippage instead of 50 at Dave and Jack's request, and a riskPathCFD benchmarkNormalised override fixed negative-spread yield profiles that had fed false arb classifications; the old CFD arb bot list was cleared on 09-23 and yields improved.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1790005631153139 https://mahifx.slack.com/archives/C046RNF64VD/p1790088439159019 https://mahifx.slack.com/archives/C046RNF64VD/p1790154076347849

### cfd-hedger-off-rca — CFD hedger book left OFF for 5h
status: closed · since: 2026-08-28 · last: 2026-08-30 · closed: 2026-10-30
State: No activity since 2026-08-30; assumed resolved. CFD_PRAXIS_HEDGING_HYBRID was switched OFF in the GUI at 03:57 UTC on 08-28 during config work and not re-enabled; G30EUR risk built (about -$2k) and PD alerts were resolved twice with the book still off. RCA filed (P2); proposed actions are alerts that only resolve when state matches expected, mandatory comments on GUI book-state changes, and Daria's push to bump MXC-66 Sustained VaR Alerting. No recorded implementation.
Refs: https://mahifx.slack.com/archives/C046RNF64VD/p1787907463800669 https://mahifx.slack.com/archives/C046RNF64VD/p1788127946167719

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
