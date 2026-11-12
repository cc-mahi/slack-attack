---
slug: pepperstone
aliases: [pepperstone-crypto, pepperstone-cfd]
refs:
  vibepulse: [../VibePulse/.claude/clients/pepperstone.yaml, ../VibePulse/.claude/clients/pepperstone-crypto.yaml]
  billing: ../MahiProduct/data/billing/clients.json     # entry: pepperstone
  hosts: ../MahiProduct/data/client-hosts.json          # entries: pepperstone, pepperstone-cfd, pepperstone-crypto
  wiki: ../MahiProduct/wiki/clients/pepperstone.md
channels:
  internal-pepperstone: C033K2P0RPT
  mahi-pepperstone-vnd: C06AR8MT8NT
contacts:
  - {name: "Stephen Hendrie", role: "exchange/product lead; main FX+crypto counterpart"}
  - {name: "Marianna Konstantinidi (MK)", role: "trading ops, CFD/crypto config, CFD licence sponsor"}
  - {name: "Reece Singh", role: "ops/counterparty admin; classification, YPs"}
  - {name: "Ruby Wang", role: "OZ/exchange trading ops"}
  - {name: "Diego Arranz", role: "CFD ops, OZ config, IP whitelisting"}
  - {name: "Mariapaz Bobadilla", role: "OZ; pricing/reject queries", confidence: low}
  - {name: "Gabriel Bignon", role: "YP/arb queries, failover breaks", confidence: low}
  - {name: "Tom Smith", role: "tech/ops: DB/IP requests (not Tom Williams)", confidence: low}
  - {name: "Sebastian Andrews", role: "DB access", confidence: low}
  - {name: "Georgios Voulgaropoulos", role: "OZ network", confidence: low}
  - {name: "Saemi Kim", role: "pricing config", confidence: low}
  - {name: "Sam Dammers", role: "security", confidence: low}
  - {name: "Tom Williams", role: "COO since 2026-08"}
last_catchup: 2026-11-12T08:16:18Z
status: active
---

## Now
Crypto env upgrade: London done, NY started 2026-11-05 night; spot backup trader (propTraderPolarisBackup1) awaits Pepperstone approval. Classification uploads live on crypto; 78 of Reece's 116 arbers missing from the B-book list (answer owed). New 2026-11-12: JPX/Nifty/copper perps requested; XAU gap and delayed fills at the CPI release explained (indicative pricing plus OZ-hub queueing); Barclays adapters repurposed for UBS via Wedbush.
Owed: ASXAUD open check (Isaac), CPI kill-switch explanation to Diego, 26D-Toxic whitelist answer, perp hedging cost agreement (-870 $/M), US DST check, MK's BTC 5/7 spread numbers. CFD licence steps to USD 45k/month; procurement contests the USD 1,500 day rate.

## Streams

### xau-cpi-price-gap — XAUUSD pricing gap and delayed fills at the 2026-11-10 CPI release
status: open · since: 2026-11-11 · last: 2026-11-12
State: Mariapaz asked why XAUUSD had no pricing 13:30:01-13:30:06Z on 2026-11-10. Rory: IG and Velocity cancelled XAUUSD-F quotes at the CPI release. Nathan's fuller cause: all three gold MWMS benchmark LPs (ISPRIME, FINALTO, INVAST26) stopped quoting, the pricer went indicative, and the continuity-pool fallback uses the same three LPs. A 5-6s fill delay was execution-report queueing between London and the NY OZ hub (latency 70 to 230-300ms), not the engine (558ms).
Next: Pepperstone to respond; continuity pool shares the MWMS benchmark LPs (not yet raised).
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794416974543159 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794446900688329?thread_ts=1794416974.543159&cid=C06AR8MT8NT

### barclays-adapters — Barclays maker adapters offboarded; UBS via Wedbush coming
status: open · since: 2026-11-11 · last: 2026-11-12
State: Georgios (2026-11-11) said the Barclays_NY and Barclays_LD maker adapters are disabled and will be offboarded. Taker adapters Mahi_NY_A_Barclays and Mahi_LD_A_Barclays stay but get renamed to Mahi_NY_A_UBS_Wed and Mahi_LD_A_UBS_Wed for a new UBS-via-Wedbush maker; timing to follow.
Next: Pepperstone to give timing; Mahi (Daria/Shyam) to update session and config names when renamed.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794404269481209 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794470635568689?thread_ts=1794404269.481209&cid=C06AR8MT8NT

### cfd-session-spreads — CFD custom sessions, BMSL timezone overrides and thin layers
status: open · since: 2026-11-09 · last: 2026-11-09
State: MK (2026-11-09) saw ASXAUD spreads go wider than 2 at the 22:50Z open: the custom session window started late. Isaac moved its start to 09:30 Sydney, effective after the 22:00Z daily-break restart (gateway sessions reconnect once, per region); he will check the open and confirm. On benchmarkMinimumSpreadLogicParameters Isaac says only CUSTOM2 should apply: the CUSTOM1 timetables were deleted, so outside CUSTOM2 BMSL falls back to the non-override parameters. MK also reports a deeper G30EUR layer missing from the model and broken Compass audit history.
Next: Isaac to confirm the ASXAUD open after tonight's restart; Mahi (Rory) to look at G30EUR and audit history.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794221476797189 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794223748709639?thread_ts=1794223748.709639&cid=C06AR8MT8NT

### cfd-depth-cap — CATTLEUSD 96k trade break: spread layers and distributed quantity cap
status: open · since: 2026-10-29 · last: 2026-11-09
State: A 96k CATTLEUSD trade broke ("Internalisation Quantity greater than Published"): spread table gave 40k, channel cap limited the book to 70k. Ruby added six layers on NY and LD; Nathan raised depth to 100k. On 2026-11-03 a 97k cattle trade was cancelled twice as "EXPIRED" and failed over; MK called it thin book liquidity and asked Cameron Hughes to double cattle quantities (agreed). On 2026-11-09 a client could not close Cocoa (TP "Expired", then a 1-lot market close "No execution"): Isaac saw no such orders, only cancels for 16 Cocoa against a book publishing one layer of 10; MK bumped it to 30 contracts.
Next: Cameron Hughes to double the cattle quantities as MK asked; Gabriel to confirm his question is answered; check other thin commodity books for single-layer depth.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793234694691149 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794238253178849?thread_ts=1794238253.178849&cid=C06AR8MT8NT

### arb-list-gap — 78 of 116 latency arbers missing from the B-book dynamic arb list
status: open · since: 2026-11-05 · last: 2026-11-06
State: Reece listed 116 latency arbers (YTD) but only 38 are in the NY B Book arbitrageurs list, leaving 78 uncaught. Daria said London capacity permitting today, otherwise Monday (2026-11-09); no reply seen in channel yet.
Next: Mahi (Daria/London team) to explain why 78 are not picked up and reply to Reece by Monday at the latest.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793857304268939 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793942588498509?thread_ts=1793857304.268939&cid=C06AR8MT8NT

### nfp-value-add — NFP value-add draft for Pepperstone, figures corrected
status: open · since: 2026-11-06 · last: 2026-11-11
State: Isaac (2026-11-11): XAUUSD 12:00-17:00Z B Book FI $229.2k on ~$9.1B (25.1 $/M), over half at the 13:30 release; LR $21.0k (2.3 $/M). Will noted Daria sent the QBR to Pepperstone's senior contacts. Will's client message on the 2026-11-06 NFP was corrected (figures were overstated ~3x): gold 674M, LR 4.3k (6.4 $/M); BTC 2.0M, skew ~677 $/M, LR 46 $/M. FX skew was slightly negative (LDN -1.9k), left out; Will wants a skew-health look. MK never received the earlier value-add report; to be emailed to Tom and Tammas after Monday's review.
Next: Will/Daria to review on Monday 2026-11-09 with the corrected figures, send to Tom and Tammas; skew-health check on the negative FX skew.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1793976769629449 https://mahifx.slack.com/archives/C033K2P0RPT/p1794397891032079

### classification-upload — Pepperstone's own counterparty classification upload (SOW #5)
status: open · since: 2026-05-19 · last: 2026-11-06
State: Live on crypto as of 2026-11-06 (26.4 went on overnight): Pepperstone can upload up to three counterparty lists that appear in Compass as UPLOAD1-3; Reece's 116-account test list loads hourly into the A Book's UPLOAD1 (NYC only, since London backgroundJobs has no books configured). FX and CFD are on 26.4 but have no download config yet.
Next: Ask Pepperstone whether each platform gets its own list; add the FX and CFD download config on request; Liam to confirm the SOW is issued.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1779146841798919 https://mahifx.slack.com/archives/C033K2P0RPT/p1793972837891119

### perps-pricing — Perp instruments: pricing, hedging cost, new perps
status: open · since: 2026-06-26 · last: 2026-11-12
State: Isaac finds perp hedging costly: clients paid +$37.3k spread (+135 $/M on $276M) against -$32.0k hedging (-870 $/M, about $8k a month), and proposes taking all perps except XAUUSD-PERP out of the hedger. Stephen asked for Nikkei 225 and Nifty 50 perps; Shyam proposed JPXUSD-PERP and I50USD-PERP mirroring NDXUSD-PERP, Nifty priced off the Goldi perp feed alone. MK added more perp markets to the HRP connection 2026-11-06 and Isaac added the instruments. On 2026-11-12 Saif confirmed Pepperstone subscribed and asked for JPXUSD-PERP and I50USD-PERP (min size 0.1) plus new XCUUSD-PERP copper (0.01); Shyam raised CHG-2611-N66J for 22:00Z on 11-12 to subscribe Nikkei and Nifty to Goldi prices. XAGUSD-PERP still unlaunched.
Next: Isaac to raise hedger removal with Stephen/MK and compare beta vs prod at the next funding basis adjustment; Shyam to apply CHG-2611-N66J and answer Saif on the copper name; Pepperstone to launch XAGUSD-PERP.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1793788289609159 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794442777531499

### a-book-client-risk — Client losing A-book money, accounts trading both books
status: open · since: 2026-11-06 · last: 2026-11-06
State: Stephen (2026-11-06): client 51506969 cost the A book -$8k while flat on the day; he will broker them meanwhile. Daria: A gained almost $5k from them earlier and aggregate yield looks good; review mid next week. Stephen found two other B-book accounts trading the same way and is cleaning up.
Next: Daria to review the counterparty mid next week; Pepperstone cleaning up the related accounts.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793929253708569 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793936446011299?thread_ts=1793929253.708569&cid=C06AR8MT8NT

### crypto-a-book-arb — Crypto A-book dynamic arb classifying too harshly; realtime detection
status: open · since: 2026-10-29 · last: 2026-11-05
State: Crypto A-book dynamic arb classified too harshly (633 accounts in sims, 2026-10-29); Stephen chose Light: Shyam set the 7-day and 30-minute bad checks to -$5/M, list reset to 193. Realtime arb detection ($1M, 50 fills, worse than -$50/M over a rolling hour) was tightened live 2026-11-05 03:36-03:48Z (CHG-2611-092T).
Next: Isaac to review crypto skew sizing and weekend setting.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792355023754729?thread_ts=1792355023.754729&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C033K2P0RPT/p1793851009921779

### polaris-migration — Spot crypto moving from Modulus to Polaris (SOW)
status: open · since: 2026-08-21 · last: 2026-11-05
State: Modulus dropped 2026-08-21; Liam wants an SOW (none seen). The 2026-10-23 cutover (CHG-2610-T16F) put propTraderPolaris1 on London. London rebooted twice 2026-10-25; Stephen asked for a backup and urgent alerting. On 2026-11-05 Daria said propTraderPolarisBackup1 in NY should be ready to switch on and asked Pepperstone to approve.
Next: Mahi to set up alerting; Daria to switch on the backup trader if Pepperstone confirm; Liam to scope the SOW; Arun to raise NYC OZ failover packet loss with Beeks if it persists; find why London rebooted (NOCINT-854295).
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1787289556446609 https://mahifx.slack.com/archives/C033K2P0RPT/p1793856168156919

### crypto-env-upgrade — Crypto environment upgrade, blocked on spot backup trader
status: open · since: 2026-10-22 · last: 2026-11-05
State: Held 2026-10-23 on pre-check conflicts (riskPath, indicative-pricing execution, ZD 23682). Shyam proposed region-by-region upgrades; Stephen called the missing spot backup a blocker (see polaris-migration). The London crypto env upgrade completed 2026-11-05 23:14Z and Shyam started NY (completion not yet seen).
Next: Shyam to confirm NY upgrade completion; Isaac to answer on internalising at the continuity price.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792665503647569 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793920459251039

### cfd-equities — Pepperstone CFD equities to be priced by Mahi
status: open · since: 2026-11-03 · last: 2026-11-04
State: After the 2026-11-03 quarterly call MK asked which equities Mahi covers; Isaac: anything Pepperstone supplies market data for, most traded first. MK sent ~45 US names (24h and standard variants are separate instruments); Isaac shared a symbol-map CSV. Nathan is ready to set them up and needs quantity definitions, spreads and LPs.
Next: MK to confirm coverage/symbol map, supply market data and the quantity/spread/LP parameters; Nathan/Isaac to set up the instruments in the CFD environment.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793699237499969 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793825895651279

### cfd-licence-fee — CFD licence fee step-up at month 4 and quarterly review prep
status: open · since: 2026-10-19 · last: 2026-11-03
State: The Global Quarterly Steering ran 2026-11-03; Will ran /meeting-ingest (outcomes not yet in Slack). The CFD licence enters month 4, when the addendum fee uplift moves from USD 30k to USD 45k a month; Nicole will annotate the invoice. Andrew wanted the review to remind Pepperstone of it (Bonnie to raise); not visible whether it was.
Next: Check the meeting notes for whether the fee step-up and open QBR checks (hero-moment links, FX/CFD cross-region failover) were covered; Mahi to raise the fee step-up before the next invoice if not.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1792425618470259 https://mahifx.slack.com/archives/C033K2P0RPT/p1793697818244769

### gateway-cpi-reject — NY gateway kill switch trips on data events (CPI, FOMC)
status: open · since: 2026-10-14 · last: 2026-11-03
State: Tripped 2026-11-03 13:48Z with no data event: the LDN failover price session dropped as a slow consumer and the NYC kill switch fired. Isaac: no rejects/cancels, failover in ~200ms; blamed on the cross-region WAN (routing being improved). Earlier trips: 10-14 CPI, 10-28 FOMC, 11-01. Daria (10-29): failover drops should not trip it.
Next: Mahi (Rory/Nathan) owes Diego the CPI kill-switch explanation and LD delay; Mahi to decide on configurable/failover-exempt kill-switch alert levels; Isaac to improve inter-region routing and re-investigate if it recurs.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1791997243862479 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793716420353649?thread_ts=1793713751.906079&cid=C06AR8MT8NT

### echo-cfd-ld-parties — LD parties not visible in the CFD Echo
status: open · since: 2026-11-03 · last: 2026-11-03
State: MK sees LD parties in FX and crypto NYC Echo but not CFD; Isaac is looking at a setting. CHG-2611-0Z3D undid the 2026-11-02 multicast change.
Next: Isaac to apply the CFD Echo setting;
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793723922411939 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793724158099669?thread_ts=1793723922.411939&cid=C06AR8MT8NT

### fx-xag-nop-limit — Inventory hedger blocked on XAGUSD per-market NOP limits
status: open · since: 2026-10-23 · last: 2026-11-02
State: On 2026-11-02 (00:00Z) Stephen asked for current NOP on ISP, Finalto and Invast, thinking all were maxed and blocking XAG hedging. Nathan replied the XAGUSD inventory-hedger risk level is USD 1.6M and current risk -1.41M, so the hedger was inside limits; Stephen sees USD 1.8M and will reconcile.
Next: Stephen to reconcile positions and adjust limits;
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792722843067479 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793579076774179

### dst-sunday-check — US DST change: confirm no pricing/execution breaks
status: open · since: 2026-10-29 · last: 2026-11-01
State: Diego asked on 2026-10-29 for confirmation that US DST on Sunday (2026-11-01) causes no pricing or execution breaks; Shyam expected none. On 2026-11-01 Georgios said Pepperstone's server timezone moved to GMT+2 and asked Mahi to update sessions; Daria: Compass named-timezone sessions should follow DST. Change need unconfirmed.
Next: Daria/Shyam to check session settings against GMT+2 and confirm to Diego.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793250276577629 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793564093291219?thread_ts=1793525397.111909&cid=C06AR8MT8NT

### fx-a-book-hedging — FX A-book metals hedging, LP limits and prime-broker positions
status: open · since: 2026-09-14 · last: 2026-10-29
State: Since 2026-09-18 metals hedge via Finalto and Invast with per-LP backstops. On 10-26 MK asked how an ISPRIME XAUUSD position arose despite LPR rules; Kate loosened metals LPR conditions, On 10-28 Daria added immediate LPR rules and delayed the $5k-VaR clearance 5s. On 2026-10-29 MK asked for further A-book hedger changes to keep XAU risk always close to 0 (excess risk currently).
Next: Daria/Kate to answer MK on holding XAU near zero and review the loosened LPR conditions.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793272154618899

### cfd-pricing-feeds — CFD feed gaps, reference-market changes and indicative alerts
status: open · since: 2026-09-22 · last: 2026-10-29
State: USDCLP gap (2026-09-22) is QRT-side; Pepperstone to raise with OneZero. IG fallback for the IG-feed latency exploit live 2026-10-27 (CHG-2610-4GVE); clean fallback at next cash close unchecked. Ten indices went to Velocity primary; VELOCITY_LDN does not price JPXJPY. Pepperstone cannot see Custom2 timezone times; OOH update was due 1 Nov.
Next: Shyam to raise visibility of timezone overrides with dev; Reece to check whether VELOCITY_LDN should stream JPXJPY; Isaac/Shyam to do the OOH timetable update on 1 Nov; Isaac to confirm IG fallback at next cash close; Pepperstone to chase OneZero on USDCLP.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1790096194336949 https://mahifx.slack.com/archives/C033K2P0RPT/p1793274530228519

### open-failover-breaks — Trades failing over to the internal maker at the open
status: open · since: 2026-10-27 · last: 2026-10-27
State: Gabriel is investigating breaks tied to failover trades: a coffee close at Monday's open reached the hub 1ms after IG's first tick, before Mahi's price arrived, so it failed over. Isaac: Mahi cannot stream earlier; longer last look would not help. Gabriel will look at other fixes.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793118304272449?thread_ts=1793118304.272449&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1793125987953359?thread_ts=1793118304.272449&cid=C06AR8MT8NT

### toxic-pool-failover — Toxic client internalised after failover to LD, request for hard 26D whitelist
status: open · since: 2026-10-26 · last: 2026-10-26
State: 2026-10-26: a client on the A-China>Broker 26D Toxic Pool rules traded EURCAD and, apparently after a brief failover to LD, was internalised, leaving 26D positions to trade out. He asked whether such clients can be whitelisted as 26D-Toxic 100% of the time so open and close are both captured. Shyam replied that Mahi will check and revert.
Next: Mahi (Shyam) to answer Stephen on a no-exceptions 26D-Toxic whitelist and why the failover internalised.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792988548313129?thread_ts=1792988548.313129&cid=C06AR8MT8NT

### dev-day-rate — Pepperstone procurement challenges the USD 1,500 SOW day rate
status: open · since: 2026-10-22 · last: 2026-10-22
State: Procurement (Lisa) objected to the SOW day rate moving from USD 1,000 to 1,500. Liam: 1,000 since Nov 2021, SOW #4 agreed at 1,250 with Stephen. Bonnie's draft (1,250 for 12 months then 1,500) not seen sent.
Next: Bonnie to send/revise the reply to Lisa; Liam to review the draft.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1792657103153339 https://mahifx.slack.com/archives/C033K2P0RPT/p1792688981792389

### crypto-hedging — Crypto spot hedger tuning and LP de-prioritisation
status: open · since: 2026-07-13 · last: 2026-10-20
State: 2026-10-19 XAUT/SOL opposite positions traced to merged per-LP LPR rules; Isaac restored per-market rules for non-XBT/XET pairs. 2026-10-20: Stephen said XAUT/PAXG hedging has no cost benefit.
Next: Stephen to decide whether to drop XAUT/PAXG from SI hedging; Diego to get HRP's answer on the PEP-LD4_Q feed now tagged HRP-2 (Mahi's HRP_LDN mapping is HRP-Agg, so London gets no HRP data since 2026-10-18), then Shyam to update the mapping.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1783981698651339 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792414394365519?thread_ts=1792414394.365519&cid=C06AR8MT8NT

### data-access — Pepperstone DB, S3/Athena access and IP whitelists
status: open · since: 2026-06-29 · last: 2026-10-20
State: Still open: Sebastian Andrews' DB access (2026-09-15) fails on TCP 3306 from Cloudflare WARP despite whitelisted IPs; last chased 09-28. Also open: James White's trade_id outliers, Reece's S3 backfill.
Next: Mahi to answer Sebastian, James and Reece.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1782731133990719 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792460410497769?thread_ts=1792460410.497769&cid=C06AR8MT8NT

### crypto-yield-psm — Crypto yields down; PSM scoping for XBTUSD/XETUSD
status: open · since: 2026-10-06 · last: 2026-11-11
State: Crypto spread yield fell to ~USD 200/M (350-450 before). Isaac proposed PSM (MK agreed 10-08); verification under way. On 2026-11-11 MK (forwarded by Isaac) asked for expected numbers on a bitcoin spread with a 5 minimum headline, averaging about 7, widening sized for maximum revenue.
Next: Isaac to produce MK's BTC 5/7 expected numbers; Isaac to finish engine verification (5 variants on 8 and 11 Oct flow) and send MK PnL/spread numbers for PSM fully active / defensive only / 10% widening.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1791285982179839 https://mahifx.slack.com/archives/C033K2P0RPT/p1794414193198939

### fi-skew-tuning — FI/skew/LR sizing and signals across FX, CFD and metals
status: open · since: 2026-08-18 · last: 2026-10-14
State: On 2026-10-14 Isaac moved FX majors to IFM-based benchmark adjustments; MK approved promoting HSIHKD, JPXJPY, XAUUSD-F and NDXUSD to the price signal (2026-10-08, monitoring);
Next: Nathan to report on promoted CFD skew performance.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787060801310749 https://mahifx.slack.com/archives/C033K2P0RPT/p1791992133214739

### cfd-hedging — CFD inventory hedger rejections, LP liquidity and risk controls
status: open · since: 2026-07-27 · last: 2026-10-13
State: The CFD inventory hedger keeps hitting LP limits: NG1 clips reject on 26Degrees; NG1 hedging stopped 08-06 when the trigger rose USD 2M to 3M.
Next: Reece to ask Invast/OZ whether NG1 depth is capped and whether the book can show remaining depth; Mahi to decide NG1 trigger appetite (USD 3M vs 2M) and the hedge venue review.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1785164826669399 https://mahifx.slack.com/archives/C06AR8MT8NT/p1791898246094219

### normalisation-mid — Model mid diverging from the normalisation market
status: watching · since: 2026-11-05 · last: 2026-11-06
State: Tom Williams (2026-11-05) asked about bringing the model mid closer to the normalisation market (CL1USD-PERP). Daria: divergence is basis changing over the look-back; a shorter window tracks better. Tom sees no issue.
Next: Daria to answer Tom's compute and slow-market question if he wants to pursue it.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793922940079729 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793943588875729?thread_ts=1793922940.079729&cid=C06AR8MT8NT

### fx-si-sims — FX B-book SI/inventory sims for Pepperstone
status: watching · since: 2026-08-27 · last: 2026-09-22
State: Nathan's SI/inventory sims went to Stephen 2026-09-22; he is convinced pure B-booking is wrong, but the USD 200M prime-broker credit limit is exceeded by every simulated method. Quiet since.
Next: Nathan to rework artefacts toward risk within the USD 200M limit; Stephen to send exact credit numbers.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787786333971199 https://mahifx.slack.com/archives/C033K2P0RPT/p1790046562048089

### margin-exploit-throttle — New-account margin exploits and order throttling
status: watching · since: 2026-07-30 · last: 2026-09-14
State: Diego asked for symbol-level throttling (2026-08-31); Stephen promised more exploiting accounts (2026-09-14). Daria: the 150 orders/1000ms throttle cannot be scoped to new accounts or symbols without a dev change; MK's NZDUSD override request looks unanswered.
Next: Mahi to answer MK on a timezone/NZDUSD-scoped throttle override (and raise the dev change); Stephen to send accounts.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1788172536055649 https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619

### xau-spreads-toxic — XAUUSD spread algorithm and toxic gold flow
status: watching · since: 2026-08-13 · last: 2026-09-14
State: Shyam proposed a PSM-style XAUUSD spread algo (cap 18pt) that Stephen broadly liked (2026-08-24); on 2026-09-14 he was taking it back internally (16c average next month); QQ EA detection is live and Pepperstone want its benefit quantified.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619

### perp-hedge-cost — Perp hedging costs and removing perps from the hedger
status: closed · since: 2026-11-04 · last: 2026-11-04 · closed: 2026-11-09
State: merged into perps-pricing.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1793788289609159

### new-index-perps — Nikkei 225 and Nifty 50 perps in the crypto environment
status: closed · since: 2026-11-03 · last: 2026-11-04 · closed: 2026-11-09
State: merged into perps-pricing.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793744841444769

### crypto-limit-nofill — XBTUSD client limit not filled despite pool price through it
status: closed · since: 2026-10-29 · last: 2026-10-29 · closed: 2026-10-30
State: Limit sat inside the continuity price after the $100/M markup; Reece accepted.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793263578250659

### roll-arb — Roll-time arbitrage on FX majors and Mahi's defensive LR/widening
status: closed · since: 2026-07-17 · last: 2026-10-27 · closed: 2026-11-04
State: Roll LR on all majors cut NZDUSD roll volume 87%; Stephen said wide USDCAD Finalto prices are deliberate (2026-10-27). Owed: Shyam to show Stephen's team the roll LR set-up.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793134266443239?thread_ts=1793125676.700959&cid=C06AR8MT8NT

### compass-264-release — Compass 26.4 upgrade of FX and CFD over the weekend
status: closed · since: 2026-10-23 · last: 2026-10-23 · closed: 2026-10-29
State: Applied to FX and CFD 24-25 Oct; no further issues.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792772169235949

### crypto-btc-arb — XBTUSD skew arbers hitting crypto pricing
status: closed · since: 2026-10-18 · last: 2026-10-20 · closed: 2026-10-30
State: merged into crypto-a-book-arb.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792467208123369?thread_ts=1792464616.833879&cid=C06AR8MT8NT

### hrp-ld-md — HRP market data missing in London after tag change
status: closed · since: 2026-10-18 · last: 2026-10-19 · closed: 2026-11-04
State: merged into crypto-hedging.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792362092980019?thread_ts=1792362092.980019&cid=C06AR8MT8NT

### arb-classification — Dynamic arb classification false positives and realtime detection
status: closed · since: 2026-07-27 · last: 2026-09-02 · closed: 2026-11-02
State: B-book arber list cut from ~700 to ~39 CPs by 2026-09-02; no activity since; assumed resolved.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1788388750800949

### findings-athena-creds — Findings routine lacks Athena access
status: closed · since: 2026-09-01 · last: 2026-09-01 · closed: 2026-11-02
State: No Athena credentials for the ring-fenced account, so cfd findings ran config-only; no activity since 2026-09-01; assumed resolved.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1788284401790649

### dax-rejects — DAX rejections reported by Pepperstone
status: closed · since: 2026-11-08 · last: 2026-11-09 · closed: 2026-11-09
State: Ruby reported many DAX rejections (2026-11-08 23:39Z). Nathan found pricing fine in Compass but no orders arriving; Pepperstone found the root cause on their side and orders flowed again by 00:25Z.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794181193136569 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794183987860399?thread_ts=1794181193.136569&cid=C06AR8MT8NT

### cfd-ld-admin-traffic — Traffic problem on Pepperstone's LD admin server
status: closed · since: 2026-11-02 · last: 2026-11-02 · closed: 2026-11-09
State: merged into echo-cfd-ld-parties.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793615743428549

### infra-resilience — Crypto server reboots, failover sessions and patching
status: closed · since: 2026-08-09 · last: 2026-10-23 · closed: 2026-11-10
State: merged into polaris-migration.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1786319051125299 https://mahifx.slack.com/archives/C033K2P0RPT/p1792767468812089

## Arc
- 2021 — first negotiation failed; ~3 months free goodwill work
- 2023-07-31 — Pepperstone board approves including CFDs
- 2023-12-21 — 3-year MSA signed (MFXEcho + Compass + Pulse, FX and metals)
- 2024-04 — Compass live in production for FX MM
- 2025-07-16 — 3rd Addendum: term to 2028-07-16, no termination for convenience
- 2025-Q4 — Modulus crypto exchange live with 6 AUD pairs
- 2026-Q1 — CFD licence signed; crypto SI profitable every week of 2026
- 2026-07-22 — CFD desk live (NY and LDN)
- 2026-08 — Tom Williams promoted to COO; Stephen Hendrie becomes main counterpart
- 2026-08-21 — Rob Bowen leaves Pepperstone; Pepperstone drops Modulus for spot crypto
