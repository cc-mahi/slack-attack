---
slug: velocity
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/velocity.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: velocity
  hosts: ../MahiProduct/data/client-hosts.json          # entry: velocity
  wiki: ../MahiProduct/wiki/clients/velocity.md
channels:
  internal-velocity: CPDS0M2KF
  mahi-velocity: C05NB72AGR2
contacts:
  - {name: "Dan Beale", role: "Velocity client ops: feeds, spreads, KAU/crosses, LP hedging, yield profiles; daily counterpart"}
  - {name: "Jackson March", role: "Velocity (Singapore hours): API creds/hedge accounts, whitelists, LP testing"}
  - {name: "Richard Holman", role: "Velocity principal: pricing/hedging policy, commercial terms, prospect flow"}
  - {name: "Russell Hewson", role: "Velocity: sim data requests, Echo login"}
  - {name: "Liv Mottershead", role: "Velocity, joined Richard's team 2026-07", confidence: low}
last_catchup: 2026-11-20T08:19:14Z
status: active
---
## Now
11-18/19 1034 off Prem and gold book healthier (client flow +$21/M at 1s, up $43/M since Monday); Mahi proposed a phased FX rollout to Richard (Celer tags on A feed, GBPJPY wants client details) and answered client 122's Prem-width complaint with network benchmarks. KAMA added to the Prem roll benchmark to stop 60-95c gold widening at 21:00 UTC; a 861 sale on 11-19 cost ~$600 when hedge orders to KAMA cancelled.
11-16 1034 moved off Prem to A (13 exemptions remain, Will C wants them off), auto broker/arb classification and defensive LR live-ish; FX SI on 25 tags waiting on Richard.
11-11 internal review: hedging loses 57% of round trips; commercials: volume-banded fee, contract draft with Will C then client CFO.

## Streams

### hedging-pnl-turnaround — PnL bleed, hedge speed and spreads
status: open · since: 2026-08-24 · last: 2026-11-20
State: 11-20 Nathan's read of the 11-19 CP 861 loss (about $585): the hedger did not try other LPs although it can route to 12, because KAMA showed the best bid each time; DYNAMIC-DONTBBOOK (fires 500ms after the trade, 5s to close) went back to KAMA six times, all rejected (gold -$2), then DELAYED-VARCLEARANCE held off selling for most of 25s on the OR-IMI-IMS pull-away signal (gold -$2.50) and filled at the bottom; even so, other routing would still have lost $140-335. He proposes a stand-down after the pull-away signal clears, backtested first, plus a safety cap on how long the rule can hold off. 11-19 05:30 UTC CP 861 sold 100 oz into a falling market (position 4 oz short to 96 long), the hedger's six KAMA sell orders all cancelled while gold fell $5, then sold at 3729.95 locking in about a $600 loss (Will asked if other LPs were tried). 11-18 Will C: gold book up $43/M since Monday and 1034 off gives hold times 147s median (was 49s), hedged share 65% (was 97%), hedge cost $15/M vs $17/M; Denny asked to add KAMA to the benchmarkSpreadMarkets of the XAUUSD CLIENT_PRICE_LDN roll rule, as Prem gold widens from 9c to ~62c at 21:00 UTC because the benchmark omits KAMA (sim: 67c to 41c published); tightens only, no change record; the 23:00 roll was not simmed, and the 21:00 UTC start and 2.5x multiplier are open. 11-17 Denny removed Jump as prioritised primary market on XAUUSD CLIENT_PRICE_LDN (skew on Jump's price created arb); watching skew PnL. Will C: up $22/M that day. 11-13 XAU hybrid hedging reworked (10:07-12:05Z) and explained to the client: fast-hedge rules now wait for a hold (500ms to 1s) and act only above 1x max VaR; old FASTHEDGE and the 1034 non-ZZ set deleted; toxic flow still hedged within 100-500ms; BACKSTOP only above 5x max VaR; illiquid sessions (Twilight, Roll, Singapore Monday) clear above 10% max VaR at once. Softest XAU flow goes to the SI book; Mahi tracks hedge cost and held-risk PnL for a week and will share a read-out. 11-12 Dan said XAU PnL negative and hedging too quick. 11-11 Will C review of 12 Oct-11 Nov XAUUSD hybrid hedges: 57% lose, about -$47k on 640k oz; clients trade with short-term momentum, holding 30s would cost more, so slower hedging is not the fix; losses concentrated in 1133, 1034Z58D791CF, 911, 1107, 1120. 11-05 call with Richard and Dan: KAU own book, SI on softer classifications, faster hedging; CHG-2611-P6RM cut XAU hedging to 5 fast rules; 2 minute SI live on B-book classified XAU flow. Bleed began late Aug; dynamicOrderSpeedScaling 1.0 to 0.1 on 10-12 stabilised PnL.
Next: Denny: verify tonight's roll spread at ~40c. Nathan: dig into the 861 hedge failure Monday, backtest a post-signal stand-down and a hold-off cap, and look at rerouting rejected KAMA hedges to other LPs. Will C: hedge cost and held-risk PnL read-out to the client after the week; tiering talk with Richard. Will C/Denny: sim momentum lean on the price for 1133, 1034Z58D791CF, 911, 1107, 1120. Mahi: monitor the 2 minute SI and the 5-rule XAU hedging, NZ watch overnight book, size a higher-risk backstop (~300oz). Will D: PnL-by-price analysis for the interest feed.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1787575981397189 https://mahifx.slack.com/archives/C05NB72AGR2/p1792421041345839 https://mahifx.slack.com/archives/CPDS0M2KF/p1795147464771659 https://mahifx.slack.com/archives/CPDS0M2KF/p1795147889489229


### tag-exec-routing — Turn off worst 1034 tags, EXEC channel for toxic flow
status: open · since: 2026-10-15 · last: 2026-11-18
State: 11-18 Will C: since turning off 1034 PnL is up $3.1k, and classified counterparty LR will now apply to signal-follow and broker flow (Denny, 11:33). 11-17 Will C (internal) is pushing Richard to turn 1034 off completely: Richard asked whether A can cope, Will said yes with classification-based execution (worse execution, then complaints); Will estimates about 80 hours of Mahi time on 1034 since September (65-95, six people) with flow unprofitable at any setting (-$13.6k at 1m on Prem, -$17.0k on A since 12 Oct), and the client does not want automation. Richard (08:54) said Mahi can enable auto-classification for 1034 on A and tell him once live. Edgewater (the 1034 firm, now off) asked Will for a demo. Dan added 1032 to the A feed for EURUSD and GBPUSD (09:27). 11-16 1034 came off Prem: Will C called it systematic tag-rotating flow (relentless, worst week yet); Dan blacklisted all 1034 tags except 13 (Denny, 11:43), then moved 1034 to the A feed (13:33). Will C told Dan the 13 exemptions should also come off Prem (about 45 new gold tags a week, 12 new tags tried Prem in 30 minutes) and is taking a client-safe version to Richard (flying; call requested). Will C also explained Dan's tripled volume (Zendesk 23850): unfiltered view counts our book once plus the drop copy twice, real 1034 gold is about $145M; 1034 on A is -$31/M at 30s and -$26/M at 1m since 12 Oct, and the client confirmed (15:23) auto-classification may go live for 1034 on A. Denny's plan (16:45): tags classified every 5-18 min once over 5 trades and $1k volume; a tag failing the broker bad check (yield decay beyond $10/M at 500ms/1s, $20/M at 5s/10s, $40/M at 30s) is broker/arb classified and rejected permanently; arb and broker reject rules built; defensive counterparty LR promoted above XAU-All (30k/s and 80k/s). Will C separately flagged 1009Z tags on gold A (churn like 1034, toxicity unproven, $48M in 6 days), to re-check at about $200M and not raise as rotation. Dan also asked for what-if markouts on blacklisted flow; Denny will check. 11-13 six 1034Z tags arbing Prem blacklisted. 11-09/10 1120 (Prem, live 28 Oct) rejected on the A_CLIENTS_PREMIUM rule at Denny's ask, client not told; Richard: communicate rather than reject everything; 385-tag blacklist in. 10-29 PnL drop from tags 1107 and 861; 1107 to be split out as 1034* was. 10-20/21 strategy with Richard: turn off worst tags, route signal-follow/broker flow to a prem EXEC channel at a worse price (EXEC not live).
Next: Will C: Richard call on removing the 13 Prem exemptions; tell Dan when 1034 auto-classification is live on A; re-check 1009Z at ~$200M. Denny: answer Dan on rejected-flow what-if markouts; verify 1034 blacklist and the new reject rules work; alerts and pre-warning to clients. Will C/Dan: settle whether 1120 stays rejected and what is told to that client. Mahi: enable the premium EXEC list and verify routing; split 1107 tags out like 1034*. Client: tag removal up the broker chain, review the tag spreadsheet, confirm XAUUSD sends subtags.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1792407215108419 https://mahifx.slack.com/archives/C05NB72AGR2/p1794841400895339 https://mahifx.slack.com/archives/CPDS0M2KF/p1794906861410419 https://mahifx.slack.com/archives/CPDS0M2KF/p1794994624050549


### fx-si-sims — FX systematic internalisation to offset gold
status: open · since: 2026-11-11 · last: 2026-11-19
State: 11-19 Richard sent the FX tag overview: of 16 tags 8 are possible (50587, 811, 50528, 573, 1032, 361, 772) and 8 are not (deliverable clients, internal accounts, and a couple of Mahi hedging accounts); Dan then enabled 1032 and 573. 11-18 Will C/Denny proposed to Richard a phased FX rollout with sign-off per step (target spreads per instrument, agree tags and simulated yield profiles, then compare live to sim); phase one is EURUSD, AUDUSD, GBPUSD plus the 13 Nov SI tags (only one on so far; Dan: most are internal accounts, some Sydney being asked). A_CLIENTS FX feed is used for SI FX with MWMS and BMSL overnight (Denny). Dan added tag 573 to EURUSD (16:33). Richard asked for GBPJPY on Prem; Mahi wants client, size, sessions and history first (no GBPJPY flow in three months). 11-17 Denny moved Compass B-book classified EURUSD, GBPUSD and AUDUSD flow (currently 1044) into a 5 minute SI to start (10:31); Dan added 1032 to the A feed for EURUSD and GBPUSD (09:27). Will C (internal) wants SI FX nudged along as the path to PnL; Richard said most of those tags are not easy to implement. 11-16 Will C asked Dan which tags cannot switch, to re-verify first (the 19 chosen FX accounts: +$30/M at fill, +$39/M at 4m on ~$2bn, 10 Aug-10 Nov). 11-13 Denny proposed 25 tags across EURUSD, GBPUSD and AUDUSD get FX pricing on the A feed for SI (trades must arrive down A, not Prem); Will C had a 5 minute SI ready; Kate: config set, only risk splitting 0 to 100% remains. 11-12 CHG-2611-RJV7: FX SI for 32 soft tags, 1-minute hold then SI hedger. 11-11 Will C (internal): no reason to be gold-only as terms go volume-based; profitable FX systematic internalisation on picked tags offsets the loss-leading 9c Prem feed; Denny to cherry-pick tags and run SI sims.
Next: Client (Richard): target spreads per FX instrument, GBPJPY client/size/history. Client (Dan): list which tags cannot switch and which are being set up. Mahi: re-verify that list. Client (Richard): say when to switch the tags on, confirm tag format. Mahi (Kate): set risk splitting to 100% on go-ahead. Denny: FX SI sim results on chosen tags and instruments; watch the 32-tag SI after the change.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1794410361294419 https://mahifx.slack.com/archives/C05NB72AGR2/p1794907664664659 https://mahifx.slack.com/archives/C05NB72AGR2/p1795095019559479


### flow-onboarding — Prospect datasets, new tags and tob size requests
status: open · since: 2026-08-21 · last: 2026-11-18
State: 11-18 Celer select clients switched on the A feed (FX only; Prem tag 1067, A tag 1068, expect 1068; Zendesk 23854); Denny asked for FX majors only, Dan's subscriptions trimmed to 9 pairs after one tag traded USDZAR to the street. Live yield profiles to be compared with the simulation. 11-16 Dan sent updated data for the Celer clients and said feeds are ready for 'this environment'; Will C told Dan Mahi will now score each dataset at its actual tradable spread net of hedge to 8m, check tag turnover and cross-tag overlap, re-check at one and two weeks live, and give a Prem, A or not-yet call. 11-11 re-run of the prospect dataset (30/06-25/09/26, transact times already UTC): Denny says inception yield mean +$85.15/M, std $166.12/M, with a time shift giving 30x the std, so time and side are right and the decaying yield is as in other datasets; Dan (10:35) says the report shows inception yield $125.85, not $85.15, and posted a screenshot; unanswered. Internally Will C: of 26 datasets Velocity sent since Nov 2025 only 1 confirmed live (tag 1120, 93 days), so ~4% conversion. 11-05 Denny (internal): 98.3% of the Velocity sim dataset matches FinPrime's Jul-Sep XAU export (Zendesk 23560, 23665); keep internal. 11-03 Dan posted six contra tags (2346, 92, 2461, 3726, 3714, 2925) for the A feed; no Mahi reply seen. 10-26 TF Global dataset lacks UTC timestamps and trade ID; re-export requested. Hantec asked for 500oz TOB (09-16); decision not yet communicated.
Next: Denny: compare Celer live yield profiles vs sim. Mahi: answer Dan on $125.85 vs $85.15. Client: which dataset maps to which tag, whether 1034/371/372/367/1090 gave data. Mahi: assess the six contra tags for A feed. Client: re-send TF Global export with UTC timestamps. Mahi: reply on the 500oz TOB request; run SB1 FX sim.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787309743078989 https://mahifx.slack.com/archives/C05NB72AGR2/p1792062011672689 https://mahifx.slack.com/archives/C05NB72AGR2/p1794299892652179 https://mahifx.slack.com/archives/C05NB72AGR2/p1795003275692639


### prem-spread-bench — Client 122 says Prem is wider than its other LPs
status: open · since: 2026-11-18 · last: 2026-11-18
State: 11-18 Dan asked for average spreads by timezone because Prem client 122 (FX and XAU) says Mahi is much wider than its other LPs (brokers, unnamed). Denny shared the spread-analysis view; Will C replied: Prem gold median 9.3c London/NY, 12.8c Asia; EURUSD/GBPUSD/USDCAD 0.1 pip London/NY, 0.7-1.1 pips Asia; tighter than the network median and bottom quartile, 122 gold pays ~$10/M at fill and is -$80/M a minute later, so Asia is the area to tidy. Dan does not want LD/NY changed.
Next: Mahi: tidy Asia Prem spreads. Dan: have 122 name instrument, session and size compared.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1794992741084519 https://mahifx.slack.com/archives/C05NB72AGR2/p1795010715703219


### client-tooling — Access, reports and self-serve requests
status: open · since: 2026-08-19 · last: 2026-11-17
State: 11-17 Liam asked whether the Velocity dashboard is working better, to close Zendesk 23803; Denny: config now loads in a few seconds, a definite improvement. 11-16 CHG-2611-T123 posted for Denny: correct outage-damaged yield profiles in Pulse/Athena, 09:00-10:00Z. 11-13 Beeks faulty LD4 link switched off (CHG-2611-TCZ4, NOCINT-860378), one path left. 11-12 Dan asked for automated hourly PnL emails (Denny to enquire); Jackson asked for XAU tick data over CPI via Price Forensics. 11-10/09 Dan hit a yield-profile share error; Richard asked for blacklisted-tag info: classifications live in Compass automation page (CSV download); Dan asked for lookbacks today/1d/1w/WTD/MTD/28d/1m/3m/6m, yield-profile filters and ClientId in yield profiles. 11-07 admin server replacement done (CHG-2611-JBJV); MySQL replica rebuild and S3 allowlist removal remain. 11-06 Dan's second markouts set and sub tag column request unanswered. 10-14 Dan asked for LP average spreads by timezone.
Next: Liam: close Zendesk 23803 if dashboard stays fine. Denny: classification lookback options and ClientId column; answer on hourly PnL email. Mahi: average LP spreads by timezone for Dan; answer on sub-tag column and Dan's second markouts set. Inald: Beeks reclaim of old admin box.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787118553763069 https://mahifx.slack.com/archives/C05NB72AGR2/p1792064490877339 https://mahifx.slack.com/archives/CPDS0M2KF/p1794816834091839 https://mahifx.slack.com/archives/CPDS0M2KF/p1794913394258619


### metals-break-firm — Gold firm in the metals break off ZZ alone
status: open · since: 2026-11-08 · last: 2026-11-09
State: 11-08 22:31 UTC CP 460 sold 71 oz XAUUSD at 4070.49 into a firm price during the metals break: ZZ streamed firm ticks while every other gold LP was indicative, making the price firm off ZZ alone; hedges to ZZ did not fill, so CLIENTS_NET held 71 oz until the 23:00 reopen (~$400 loss). Shyam found ZZ does this in every weekday break and A_CLIENTS_PREMIUM was tradeable on each weekday since 26 Oct (this was the only trade). Fix: force indicative timetable on metals over 17:00-18:00 NY; /price-availability-health extended to flag client prices firm while the market is closed (trial 2-8 Nov found this plus gaps at other clients). Client was told in mahi-velocity 11-08 23:46; no reply yet.
Next: Shyam: follow up the other-client gaps found by the trial run.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1794181586979739 https://mahifx.slack.com/archives/CPDS0M2KF/p1794187744710969


### premium-skew-lean — Skew on big premium tickets (slicers)
status: open · since: 2026-10-22 · last: 2026-11-05
State: 11-05 Will C reviewing Premium yield profiles ('this flow is shite'), floated an SI on Premium and a 2 minute hold. 11-04 Will C: FM-BIG-100k-30s had the best backtest returns; Denny bounced pricerB1/2 and pricer1/2 to add FM-BIG-100k-30s on LDN, LDNNYC, NYC, SNG, SNGLDN timezones (not SNGMON, ROLL, TWILIGHT) after first starting an FM-BIG-100k-120s signal with 2c skew on A_CLIENTS (B_LDN) and holding off. Will C found VEL AGG_1 is an aggregate of premium bank skews with no leakage but unusable in pricing. A price-variation-health finding that flow-signal arb is not excluded was queried by Isaac (likely missing most FM-T-0-* signals, arb classification odd; to check). Earlier: premium flow comes in streaks (same client's next ticket goes the same way 73-83% after a $200k+ one), mostly one client slicing (1034 tags); LR cannot capture it (97% of premium orders are limit IoC with zero slack). Engine tests: IFMS-B +$0.7/M (includes zero), FM-BIG +$8/M on follow-ups (thin).
Next: Will C: watch FM-BIG-100k-30s live, decide on SI for Premium. Isaac: check whether FM-T-0-* signals are missing from the arb exclusion.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1792656425258739 https://mahifx.slack.com/archives/CPDS0M2KF/p1793794830996489 https://mahifx.slack.com/archives/CPDS0M2KF/p1793865227704789


### kau-kilo-gold — XAU/Kilogram (KAUUSD) pricing and hedge
status: open · since: 2026-08-25 · last: 2026-11-05
State: 11-05 after the client call Denny moved KAU into a separate book with its own hedger (to keep it out of the SI book), bounced the reporting/risk processes to pick up the new books, and Dan's KAU test trade passed (13:34 UTC). Priced at fixed 32.15 x XAU; 3kg TOB on A feed. Hedge lands 32.14 (0.01oz residual below min clip); Mahi changed VaR gate, client accepted. Ops signed off 09-18, client rolled out 09-21.
Next: Client: spread protections for KAU; Mahi confirm 32.15 hedge behaviour on the new book.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787642723388769 https://mahifx.slack.com/archives/C05NB72AGR2/p1790778810519969 https://mahifx.slack.com/archives/C05NB72AGR2/p1793885687336439


### prem-a-feed — Prem and A feed spreads, fills, LR
status: open · since: 2026-08-26 · last: 2026-11-04
State: 11-04 Dan chased the XAG PREM request; Denny asked why TOB should go 1000 to 5000, Dan said most LPs quote 5k TOB (about $250k notional); Denny will sim PnL first as most XAG volume hits the 4k second tier, whose width is in line with LPs. 11-03 Dan asked to amend XAGUSD core on PREM (drop the 1k layer, 5k to 0.0012); Rory said Mahi will look. 11-02 Daria set clientOrders.validation.validatePriceIncrement to false (CHG-2611-MRV4) so off-step limit orders no longer reject with INVALID_INCREMENT, prompted by CP 460 sending XAUUSD at 3dp against 2dp quotes; quotes unchanged. 10-28 Richard called gold exceptionally wide (Kama 22c, prem over $1) and the config overly defensive; Isaac: Prem's twilight/roll minimum follows the tightest benchmark LP and LMAX's TOB cut dropped it; agreed a multiple of 9c as starting point, Isaac ready to apply (add Kama to benchmark, twilight 1.2x-2.5x). Earlier: Richard holds Prem at 9c base (flow dries up beyond 12); A-feed fill rate 57% MTD vs 75% target (09).
Next: Denny: sim the XAGUSD PREM TOB/layer change and answer. Isaac: add Kama to Prem benchmark and set twilight multiple (client may raise LMAX TOB change with LMAX). Mahi: decide on dropping Kama from A's twilight/roll MWMS benchmark; client to say how tight Prem should be. Will D: check the temporary volatility widening and bring prem back to 9c. (3dp item resolved 11-02: see State.)
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787744856529959 https://mahifx.slack.com/archives/C05NB72AGR2/p1793134646597689 https://mahifx.slack.com/archives/C05NB72AGR2/p1793179982245099 https://mahifx.slack.com/archives/C05NB72AGR2/p1793787152502249


### commercial-terms — Move from PnL share to volume-banded fee
status: open · since: 2026-09-09 · last: 2026-11-03
State: 11-02 Will C said Tim (client CFO) is finally back and asked Nicole to draft the contract for the new terms; 11-03 Nicole posted a draft Compass Services Agreement, noting the options make it a little complicated. INV-1039 netting dispute paid 09-14. 10-01 meeting: agreed to drop PnL share for a volume-banded long-term deal; 10-06 Richard accepted terms: 12-month $15k + $2.00/$1.50/$1.25 per M tiers, $20k minimum (3-month rolling $17.5k + higher tiers). Velocity CEO backs the long-term commitment.
Next: Will C to review Nicole's draft, then send to client CFO (Tim) for sign-off and new 12-month contracts; client wants consultation before Asia widening (SLAs).
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1788953874786009 https://mahifx.slack.com/archives/CPDS0M2KF/p1790847451087629 https://mahifx.slack.com/archives/CPDS0M2KF/p1791298648881549 https://mahifx.slack.com/archives/CPDS0M2KF/p1793614039432379


### aud-dkk-synthetic — Synthetic AUDDKK cross as a favour
status: open · since: 2026-10-28 · last: 2026-11-02
State: 11-02 client (Jackson) saw no AUD/DKK on A or Prem; Daria found AUDDKK was produced in the model but missing from the distribution market, added it, restart scheduled for EOD. 10-28/29 Richard asked for a synthetic AUD/DKK as a favour (no flow expected); triangulated in the model, Denny bounced pricer1/2 for AUDDKK and USDDKK.
Next: Mahi: confirm AUDDKK prices after the EOD restart. Client: subscribe and say if the price needs adjusting.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1793199398168089 https://mahifx.slack.com/archives/C05NB72AGR2/p1793298225682449 https://mahifx.slack.com/archives/C05NB72AGR2/p1793596439286539


### cfd-expansion — CFD / index instruments (J40, Z40, new CFD list)
status: open · since: 2026-08-19 · last: 2026-10-30
State: 10-30 Cameron H forwarded a broker (Bryan Seegers) asking for feedback on Velocity's indices liquidity, saying its fair values are often off market; Cameron suggested using it to win Velocity more business and tell them Mahi helped; Will C will pick it up (delicate). 08-19 IG FIX timeout dropped Velocity's bridge; policy: confirm positions before re-enabling the hedger. Z40 hedging fixed after a 10-02 NFP loss. Client supplied pricing for CNI/DJI/GDI/USO/UKO and a 28-instrument CFD list; 21 of 28 have drop copies; yield profiles generate (10-15). riskPathCsv MD throttle 10-13 had distorted CFD yields.
Next: Will C: handle the indices fair-value feedback request. Drop copies missing for AEXEUR, DJFUSD, DXFEUR, JPUUSD, NDFUSD, S30SGD, SPFUSD.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787147771318879 https://mahifx.slack.com/archives/CPDS0M2KF/p1790947414363299 https://mahifx.slack.com/archives/C05NB72AGR2/p1792574647919929 https://mahifx.slack.com/archives/CPDS0M2KF/p1793355961117979


### last-look-slack — Last-look retry and passing client slack back
status: open · since: 2026-10-26 · last: 2026-10-29
State: 10-29 Richard questioned fill rate on tag 1133 (cancels shown in Echo, XAUUSD); Denny: last look triggers the cancels, all the cancelled flow is sharp, so relaxing last look just accepts more of it; its fill rate is about 67%, average for the hedger. 10-26 Richard queried a trade rejected then instantly refilled; Denny: the first order was cancelled by last look, the retry was repriced to our TOB and passed. Richard then said Velocity had stopped passing slack (client-side limit) to Mahi because it was not improving them, asked whether that is resolved and whether to resume; Denny will check execution settings and revert.
Next: Mahi (Denny): answer on whether slack can be passed again.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1793032599037739 https://mahifx.slack.com/archives/C05NB72AGR2/p1793033048353429 https://mahifx.slack.com/archives/C05NB72AGR2/p1793290667230129


### gold-depth-ladder — Tight gold TOB, charge for size, per-session skew
status: open · since: 2026-10-23 · last: 2026-10-23
State: Andrew M proposes (internal only) keeping the tight XAUUSD TOB for the first clip and laddering depth so bigger tickets fill wider on VWAP, instead of widening the Prem TOB; Will C's 20 Oct analysis has the 9c Prem channel below hedge cost, with losses in identifiable tags. Jul-Sep half-spread paid on 20-100oz equals the network median, >100oz well above it; about $330k a quarter per +10 $/M on the 20-100oz band if flow stays. FinPrime prospect figures stay internal; any Velocity-facing version uses network bands only. Second lever is a per-counterparty/FIX-session flow-momentum skew variant being built in the SkewValueAdd sim, with Velocity a live candidate. Figures are Athena-based, not yet Compass-linked.
Next: Mahi: size a depth ladder on Velocity's own flow in sim; score per-session skew once built.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1792771031124009


### db-pro — Deutsche Bank Limit Pro passive hedging via Reactive
status: open · since: 2026-08-18 · last: 2026-10-22
State: 10-22 DB cancels for subceeding minimum notional forced the hedge minimum order up to $100k (Richard: DB Pro minimum is 10oz); the cancels tripped the Reactive switch again and LimitPro not-permissioned rejects returned; Denny re-enabled DB_PRO and awaits Reactive. 10-20 passive hedging retried: first rejects were 'Exceeded maximum price precision' (3dp sent, DB takes 2dp); after Denny changed to 2dp, rejects became 'LimitPro not permissioned for account VELOCITY_ALGO'. Richard says permission was disabled after the dp issues and Reactive are switching it back on; Denny turned DB_PRO off until resolved and sees no passive trades. Test trades succeeded 08-24, drop copy via Xenfin live. 10-01 adding DB_PRO as an XAUUSD execution market crashed hybridHedger1; reverted, setup not finished. Shared Reactive cross-connect in LD4 costs GBP 100/month; on-charge question to Nicole 08-18 unanswered.
Next: Reactive: re-enable LimitPro permission; Mahi: re-enable DB_PRO and confirm passive trades; Nicole: on-charge/addendum answer.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787049402059669 https://mahifx.slack.com/archives/C05NB72AGR2/p1790081928596799 https://mahifx.slack.com/archives/C05NB72AGR2/p1792494641397569 https://mahifx.slack.com/archives/C05NB72AGR2/p1792668512445189


### interest-feed — Interest-only (risk-reducing) C feed
status: watching · since: 2026-08-18 · last: 2026-10-20
State: Downgraded to watching 2026-11-20 (no activity since 10-20). 10-20 Will C wants to check whether the fills are actually risk-decreasing; Denny posted an analysis artifact. Live 08-18 with riskAdjustedFirmQty. Fill rate rose ~15% to ~92% (09-22). Mahi analysis (09-29): 97.7% of fills reduce risk but are -$30/M at 1m; counterparty 1100 machine-guns 1-10ms bursts and is 99% of added risk; exec rule split, channel LR and cap added, still ~12oz/day risk-increasing fills and the hedger races the feed. Will C wants it off; base spread widened 20 to 30, now no fills. Client wants it kept but priced correctly.
Next: Will D: data-backed PnL effect at different price levels; fix hedger-vs-interest race.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1787071381197089 https://mahifx.slack.com/archives/CPDS0M2KF/p1790693863681659 https://mahifx.slack.com/archives/CPDS0M2KF/p1792060203147839 https://mahifx.slack.com/archives/CPDS0M2KF/p1792480630454159


### hedge-lps — Hedging LP set (Argamon, Virtu, ZZ, Kama, others)
status: watching · since: 2026-08-26 · last: 2026-10-15
State: Downgraded to watching 2026-11-16 (no activity since 10-15). Argamon in hedging from 08-27, ZZ added with tag-1034 blacklist (09-02), SGX/Edgewater added. Argamon fill rate ~15% so removed 09-18, restored 09-22. Virtu (to replace Kama) still being configured by the client; NWM Morgan Stanley test 09-29 then held off. Kama routes to its institutional channel since 10-02; Argamon and Kama widened to 20-24c TOB 10-06. Ref-mid LP set re-chosen 10-07. 10-15 client asked to cut ~16 price layers on hedge LP sessions; Will D agreed to cut to 5.
Next: Mahi: apply 5-layer cut on hedge sessions. Client: Virtu ready-to-test notice; decision on VELBINT099HS (left live). Mahi: move hedge weight off Kama where possible.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787725457576859 https://mahifx.slack.com/archives/C05NB72AGR2/p1789653498837279 https://mahifx.slack.com/archives/C05NB72AGR2/p1792079679596159


### hedger-reliability — Hedger switched off or crashing
status: watching · since: 2026-09-04 · last: 2026-10-01
State: 09-04 hybrid hedger left off after KAU testing into NFP (arb flat; gold +$3.2k by luck); Will C: never leave hedgers off into news. Liam/Justin proposed UI safeguards (MahiProduct PR 67 draft). 09-11 hybridHedger1 died repeatedly on unacked orders to Argamon/XTX/Kama; 10-01 crashed after DB_PRO market add.
Next: Mahi: hedger-off reminder safeguards (PR 67); investigate unacked-order crashes.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1788525147002129 https://mahifx.slack.com/archives/CPDS0M2KF/p1790871377514399

## Arc
- 2026-01-06 — Contract signed (re-papered 12 Jan), Compass + Echo pilot, $20k minimum plus 50% PnL share
- 2026-02-26 — Go-live
- 2026-04-29 — Premium channel rolled out for first tags, repeated tuning
- 2026-06-09 — Prem feed fill-rate crisis (45%)
- 2026-06-25 — CFD contract-change intent confirmed
- 2026-08-18 — Interest-only C feed live
- 2026-09-18 — KAUUSD signed off by client ops
- 2026-10-06 — Client accepts volume-banded terms replacing PnL share
