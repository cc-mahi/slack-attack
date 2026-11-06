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
last_catchup: 2026-11-06T08:14:23Z
status: active
---

## Now
Crypto env upgrade under way: London done, NY started 2026-11-05 night; backup spot trader (propTraderPolarisBackup1) still awaiting Pepperstone approval. Crypto A-book arb on Light plus realtime detection live; 78 of Reece's 116 arbers missing from the B-book list (answer due by Monday); A-book client 51506969 under review.
Owed: CPI kill-switch explanation to Diego, 26D-Toxic whitelist answer, perp hedging cost agreement (-870 $/M), US DST session check. CFD equities and Nikkei/Nifty perps onboarding after the 2026-11-03 steering; CFD licence steps to USD 45k/month; procurement contests the USD 1,500 day rate.

## Streams

### arb-list-gap — 78 of 116 latency arbers missing from the B-book dynamic arb list
status: open · since: 2026-11-05 · last: 2026-11-06
State: Reece (2026-11-05) listed 116 clients he classifies as latency arbers (YTD data) but only 38 are in the NY B Book arbitrageurs automated list, leaving 78 uncaught, and asked what he is missing. Daria said Mahi will look; Reece chased 2026-11-06 and Daria replied she will see if the London team has capacity today, otherwise Monday (2026-11-09).
Next: Mahi (Daria/London team) to explain why 78 are not picked up and reply to Reece by Monday at the latest.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793857304268939 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793942588498509?thread_ts=1793857304.268939&cid=C06AR8MT8NT

### a-book-client-risk — Client losing A-book money, accounts trading both books
status: open · since: 2026-11-06 · last: 2026-11-06
State: Stephen (2026-11-06) flagged client 51506969 costing the A book -$8k while flat on the day and said he would broker them meanwhile. Daria: the A book gained almost $5k from them earlier and aggregate yield looks good (flow fell to about -$6k in 30s); review mid next week. Stephen found two other B-book accounts trading the same way, believes the client is moving the market with A-book trades complementing the B-book (possibly hitting other brokers), and is cleaning up; he thinks short-term risk on A is dangerous.
Next: Daria to review the counterparty mid next week; Pepperstone cleaning up the related accounts.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793929253708569 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793936446011299?thread_ts=1793929253.708569&cid=C06AR8MT8NT

### normalisation-mid — Model mid diverging from the normalisation market
status: watching · since: 2026-11-05 · last: 2026-11-06
State: Tom Williams (2026-11-05) asked how feasible it is to bring the model mid closer to the normalisation market (CL1USD-PERP example), noting basis never quite returns to the Goldi rate. Daria: divergence is basis changing over the look-back; shortening the basis window would track the current basis better. Tom sees no issue, only asked, and wonders about the compute cost or normalising to a slower market if shortened.
Next: Daria to answer Tom's compute and slow-market question if he wants to pursue it.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793922940079729 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793943588875729?thread_ts=1793922940.079729&cid=C06AR8MT8NT

### crypto-a-book-arb — Crypto A-book dynamic arb classifying too harshly; realtime detection
status: open · since: 2026-10-29 · last: 2026-11-05
State: Reece (2026-10-29) said the crypto A-book dynamic arb classifies far too harshly; Stephen (10-30) reported more complaints and asked for a quick fix or whitelists; sims showed 633 accounts listed. Stephen chose Light: Shyam set the 7-day and 30-minute bad checks to -$5/M and reset the list to 193 problem accounts. Stephen also agreed to realtime arb detection ($1M, 50 fills, worse than -$50/M over a rolling hour); it was tightened live 2026-11-05 03:36-03:48Z (CHG-2611-092T).
Next: Isaac to review crypto skew sizing and weekend setting.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792355023754729?thread_ts=1792355023.754729&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1793330613302529?thread_ts=1793262497.615879&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C033K2P0RPT/p1793851009921779

### polaris-migration — Spot crypto moving from Modulus to Polaris (SOW)
status: open · since: 2026-08-21 · last: 2026-11-05
State: Modulus dropped 2026-08-21; Liam wants an SOW (none seen yet). The 2026-10-23 cutover (CHG-2610-T16F) put propTraderPolaris1 on London; the old prop traders are decommissioned. The London crypto server rebooted twice on 2026-10-25 night after the RAM upgrade, taking propTraderPolaris1 down; Stephen asked for a NY/LD backup so maintenance has no downtime, plus alerting urgently. On 2026-11-05 Daria said propTraderPolarisBackup1 in NY should be ready to switch on (quoting no tighter than the LDN trader) and asked Pepperstone to approve.
Next: Mahi to set up alerting; Daria to switch on the backup trader if Pepperstone confirm and review tomorrow; Liam to scope the SOW.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1787289556446609 https://mahifx.slack.com/archives/C033K2P0RPT/p1792968665134069 https://mahifx.slack.com/archives/C033K2P0RPT/p1793856168156919

### crypto-env-upgrade — Crypto environment upgrade, blocked on spot backup trader
status: open · since: 2026-10-22 · last: 2026-11-05
State: Held 2026-10-23 on pre-check conflicts (riskPath, indicative-pricing execution, ZD 23682). On 2026-11-05 Shyam asked to upgrade crypto region by region (20-30 min down each, same version as FX and CFD); Stephen first agreed, then called it a blocker because spot has no backup and the exchange pricing would die. Daria expects the backup up that afternoon; it should be ready to switch on in NY (see polaris-migration). The London crypto env upgrade completed 2026-11-05 23:14Z and Shyam started NY (completion not yet seen).
Next: Shyam to confirm NY upgrade completion; Isaac to answer on internalising at the continuity price when indicative.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792665503647569 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793841602522829?thread_ts=1793839204.236169&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1793920459251039

### perp-hedge-cost — Perp hedging costs and removing perps from the hedger
status: open · since: 2026-11-04 · last: 2026-11-04
State: Isaac (internal, 2026-11-04) finds perp hedging costly: clients paid +$37.3k spread (+135 $/M on $276M) but hedging cost -$32.0k on $36.8M hedged (-870 $/M, about $8k a month). Proposes taking all perps except XAUUSD-PERP out of the hedger; needs Pepperstone's agreement.
Next: Isaac to raise with Stephen/MK.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1793788289609159

### new-index-perps — Nikkei 225 and Nifty 50 perps in the crypto environment
status: open · since: 2026-11-03 · last: 2026-11-04
State: Stephen asked (2026-11-03 22:27Z) to add Nikkei 225 and Nifty 50 to the perp range in the crypto environment. Shyam proposed JPXUSD-PERP and I50USD-PERP (both USC-quoted per Stephen), mirroring NDXUSD-PERP settings for now. Nifty has no spot feed and would price off the Goldi perp feed alone, like KR200.
Next: Stephen to send the Goldi symbols per index (like NAS100-PERP / KR200-PERP) and confirm min/max settings; Shyam to build once received.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793744841444769 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793753070673649?thread_ts=1793744841.444769&cid=C06AR8MT8NT

### cfd-equities — Pepperstone CFD equities to be priced by Mahi
status: open · since: 2026-11-03 · last: 2026-11-04
State: Nathan (2026-11-04) said Mahi is ready to set them up in the CFD environment and asked for quantity definitions, spreads, LPs and other parameters, pointing at the spreadsheet used for the earlier CFD setup. After the 2026-11-03 quarterly call MK asked which equities Mahi covers; Isaac said anything Pepperstone supplies market data for, starting with their most traded. MK sent ~45 US names, mixing 24h and standard variants (separate instruments; Mahi can do both). Isaac shared a symbol-map CSV for symbol clashes.
Next: MK to confirm coverage/symbol map, supply market data and the quantity/spread/LP parameters; Nathan/Isaac to set up the instruments in the CFD environment.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793699237499969 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793717811643899?thread_ts=1793699237.499969&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1793825895651279

### cfd-licence-fee — CFD licence fee step-up at month 4 and quarterly review prep
status: open · since: 2026-10-19 · last: 2026-11-03
State: The Global Quarterly Steering ran Tuesday 2026-11-03 08:00 GMT; Will posted the Gemini notes and ran /meeting-ingest (outcomes not yet in Slack). The CFD licence enters month 4, when the addendum fee uplift moves from USD 30k to USD 45k a month; Nicole will annotate the invoice. Andrew wanted the review to remind Pepperstone of it (Bonnie to raise); not visible whether it was.
Next: Check the meeting notes for whether the fee step-up and open QBR checks (hero-moment links, FX/CFD cross-region failover) were covered; Mahi to raise the fee step-up before the next invoice if not.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1792425618470259 https://mahifx.slack.com/archives/C033K2P0RPT/p1793676457572049 https://mahifx.slack.com/archives/C033K2P0RPT/p1793697818244769

### gateway-cpi-reject — NY gateway kill switch trips on data events (CPI, FOMC)
status: open · since: 2026-10-14 · last: 2026-11-03
State: It tripped again 2026-11-03 13:48Z with no data event: the LDN B-book failover price session (NYC backup feed) dropped as a slow consumer and the NYC distribution kill switch fired. Isaac: no rejects/cancels, bridge failed over in ~200ms, ~1,450 fills traded on London failover sessions; blamed on the cross-region WAN (routing being improved). Earlier trips: 2026-10-14 CPI print (Last Look latency spike; XAUUSD SYSTEM_CLOSED rejects; Mahi owes Diego a log-backed explanation and the ~20s LD price delay), 2026-10-28 FOMC, 2026-11-01 FX. Daria (10-29) argues failover-session drops should not trip it and asks about configurable per-connection alert levels.
Next: Mahi (Rory/Nathan) owes Diego the CPI kill-switch explanation and LD delay; Mahi to decide on configurable/failover-exempt kill-switch alert levels; Isaac to improve inter-region routing and re-investigate if it recurs.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1791997243862479 https://mahifx.slack.com/archives/C033K2P0RPT/p1793570018752399 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793716420353649?thread_ts=1793713751.906079&cid=C06AR8MT8NT

### cfd-depth-cap — CATTLEUSD 96k trade break: spread layers and distributed quantity cap
status: open · since: 2026-10-29 · last: 2026-11-03
State: A 96k CATTLEUSD trade broke overnight ("Internalisation Quantity greater than Published"): the spread table gave only 40k and the channel cap (visible quantity 350 x normal quantity 200) limited the book to 70k. Pepperstone (Ruby) added six layers on NY and LD (25k top of book, 15k each behind); Nathan raised CATTLEUSD's depth to 100k (live; the same client's 97k close later traded through Compass). On 2026-11-03 Gabriel asked why a 97k cattle trade was cancelled twice as "EXPIRED" and failed over (80k + 17k); MK called it too little book liquidity and asked Cameron Hughes to double cattle quantities (he agreed). 
Next: Cameron Hughes to double the cattle quantities as MK asked; Gabriel to confirm his question is answered.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793234694691149 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793739369648469?thread_ts=1793730944.380609&cid=C06AR8MT8NT

### echo-cfd-ld-parties — LD parties not visible in the CFD Echo
status: open · since: 2026-11-03 · last: 2026-11-03
State: MK sees the LD parties in the FX and crypto NYC Echo views but not the CFD one and asked for the same so she need not toggle environments; Isaac said a setting exists and is looking into it.
Next: Isaac to apply the setting for the CFD Echo.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793723922411939 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793724158099669?thread_ts=1793723922.411939&cid=C06AR8MT8NT

### cfd-ld-admin-traffic — Traffic problem on Pepperstone's LD admin server
status: open · since: 2026-11-02 · last: 2026-11-02
State: MK reported alerts on CFD prices on 2026-11-02 (no reply seen); Liam told her traffic to the LD admin server has issues, no trading impact, possibly spurious alerting. CHG-2611-0Z3D (2026-11-02 22:00-23:00Z) undoes Saturday's multicast change to restore admin feeds.
Next: Mahi to confirm to MK the admin feeds are restored after CHG-2611-0Z3D.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793615743428549 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793615787469419 https://mahifx.slack.com/archives/C0C1UHPLZPF/p1793646949124589

### fx-xag-nop-limit — Inventory hedger blocked on XAGUSD per-market NOP limits
status: open · since: 2026-10-23 · last: 2026-11-02
State: On 2026-11-02 (00:00Z) Stephen asked for current NOP on ISP, Finalto and Invast, thinking all were maxed and blocking XAG hedging. Nathan replied the XAGUSD inventory-hedger risk level is USD 1.6M and current risk -1.41M, so the hedger was inside limits; Stephen sees USD 1.8M on his side and will reconcile.
Next: Stephen to reconcile positions and adjust limits;
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792722843067479 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793577548415299 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793579076774179

### dst-sunday-check — US DST change: confirm no pricing/execution breaks
status: open · since: 2026-10-29 · last: 2026-11-01
State: Diego asked on 2026-10-29 for confirmation that US DST on Sunday (2026-11-01) causes no pricing or execution breaks; Shyam expected none. On 2026-11-01 Georgios said Pepperstone's server timezone moved to GMT+2 and asked Mahi to update sessions; Daria: Compass named-timezone sessions should follow DST. Unconfirmed whether a change is needed.
Next: Daria/Shyam to check session settings against GMT+2 and confirm to Diego.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793250276577629 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793525397111909 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793564093291219?thread_ts=1793525397.111909&cid=C06AR8MT8NT

### fx-a-book-hedging — FX A-book metals hedging, LP limits and prime-broker positions
status: open · since: 2026-09-14 · last: 2026-10-29
State: Since 2026-09-18 Mahi hedges metals via Finalto and Invast (PB LPs are off the table) with per-LP backstops. On 2026-10-26 MK asked how an ISPRIME XAUUSD position arose despite LPR rules and wants metals LPR rules at top priority; Kate loosened metals LPR conditions, Reece traded down positions (10-27). On 2026-10-28 Daria delayed the $5k-VaR clearance rule 5s and added immediate LPR rules so they hedge first. On 2026-10-29 MK asked for further A-book hedger changes to keep XAU risk always close to 0 (excess risk currently).
Next: Daria/Kate to answer MK on holding XAU near zero and review the loosened LPR conditions.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793272154618899

### cfd-pricing-feeds — CFD feed gaps, reference-market changes and indicative alerts
status: open · since: 2026-09-22 · last: 2026-10-29
State: USDCLP gap (2026-09-22) is QRT-side; Pepperstone to raise with OneZero. IG-feed latency exploitation (2026-10-16): CHG-2610-4GVE IG fallback live 2026-10-27; clean fallback at next cash close still to check. Ten indices went to Velocity as primary; VELOCITY_LDN does not price JPXJPY. Out-of-hours timezone update follows 1 Nov with US DST end; on 2026-10-25 Pepperstone said they cannot see the Custom2 timezone times (tradingTimeTable.timezoneOverrides).
Next: Shyam to raise visibility of timezone overrides with dev; Reece to check whether VELOCITY_LDN should stream JPXJPY; Isaac/Shyam to do the OOH timetable update on 1 Nov; Isaac to confirm IG fallback at next cash close; Pepperstone to chase OneZero/QRT on USDCLP.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1790096194336949 https://mahifx.slack.com/archives/C033K2P0RPT/p1792581335519849?thread_ts=1792581335.519849&cid=C033K2P0RPT https://mahifx.slack.com/archives/C033K2P0RPT/p1793274530228519

### open-failover-breaks — Trades failing over to the internal maker at the open
status: open · since: 2026-10-27 · last: 2026-10-27
State: Gabriel is investigating breaks tied to failover trades: a coffee close at Monday's open reached the hub 1ms after IG's first tick, before Mahi's price arrived, so it failed over. Isaac says Mahi cannot stream earlier and a longer last look would not help. Gabriel will look at other fixes.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793118304272449?thread_ts=1793118304.272449&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1793125987953359?thread_ts=1793118304.272449&cid=C06AR8MT8NT

### toxic-pool-failover — Toxic client internalised after failover to LD, request for hard 26D whitelist
status: open · since: 2026-10-26 · last: 2026-10-26
State: On 2026-10-26 Stephen reported a client on the A-China>Broker 26D Toxic Pool rules traded EURCAD and, apparently after a brief failover to LD, was internalised, leaving 26D positions to trade out. He asked whether such clients can be whitelisted as 26D-Toxic 100% of the time so open and close are both captured. Shyam replied that Mahi will check and revert.
Next: Mahi (Shyam) to answer Stephen on a no-exceptions 26D-Toxic whitelist and why the failover internalised.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792988548313129?thread_ts=1792988548.313129&cid=C06AR8MT8NT

### infra-resilience — Crypto server reboots, failover sessions and patching
status: open · since: 2026-08-09 · last: 2026-10-23
State: NYC OZ failover sessions flapped every 7-8 min from TCP retransmits (2026-10-05); the London crypto server rebooted twice on 2026-10-25 after a Beeks RAM upgrade (NOCINT-854295; see polaris-migration).
Next: Arun to raise the packet loss with Beeks if it persists; Mahi to find why the London server rebooted twice on 2026-10-25.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1786319051125299 https://mahifx.slack.com/archives/C033K2P0RPT/p1792767468812089

### dev-day-rate — Pepperstone procurement challenges the USD 1,500 SOW day rate
status: open · since: 2026-10-22 · last: 2026-10-22
State: Procurement (Lisa) objected to the SOW day rate moving from USD 1,000 to 1,500 and proposed a rate card, volume tiers and a lower base. Liam: 1,000 since Nov 2021, SOW #4 agreed at 1,250 with Stephen. Bonnie drafted a reply (1,250 for 12 months then 1,500; not seen sent).
Next: Bonnie to send/revise the reply to Lisa; Liam to review the draft.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1792657103153339 https://mahifx.slack.com/archives/C033K2P0RPT/p1792688981792389

### crypto-hedging — Crypto spot hedger tuning and LP de-prioritisation
status: open · since: 2026-07-13 · last: 2026-10-20
State: On 2026-10-19 XAUT/SOL opposite positions traced to merged per-LP LPR rules; Isaac restored per-market LPR rules for non-XBT/XET pairs and cut LPR delays. 2026-10-20: Stephen said XAUT/PAXG hedging has no cost benefit.
Next: Stephen to decide whether to drop XAUT/PAXG from SI hedging; Diego to get HRP's answer on the PEP-LD4_Q feed now tagged HRP-2 (Mahi's HRP_LDN mapping is HRP-Agg, so London gets no HRP data since 2026-10-18), then Shyam to update the mapping.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1783981698651339 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792414394365519?thread_ts=1792414394.365519&cid=C06AR8MT8NT

### data-access — Pepperstone DB, S3/Athena access and IP whitelists
status: open · since: 2026-06-29 · last: 2026-10-20
State: Still open: Sebastian Andrews' DB access (2026-09-15) fails on TCP 3306 from Cloudflare WARP despite whitelisted IPs; last chased 09-28. Also James White's trade_id outliers, Reece's S3 backfill question.
Next: Mahi to answer Sebastian, James and Reece.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1782731133990719 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792460410497769?thread_ts=1792460410.497769&cid=C06AR8MT8NT

### perps-pricing — Perp instruments: pricing, rollover and KRX
status: open · since: 2026-06-26 · last: 2026-10-20
State: Binance removed from non-XAUUSD perp references (2026-09-20). Brent rollover basis-jump fix deployed 2026-09-30 (off on beta to compare). KRXUSD-PERP replaced KRXKRW-PERP on 2026-10-07; 2dp-vs-1dp price rejects fixed 2026-10-20. XAGUSD-PERP still unlaunched.
Next: Isaac to compare beta vs prod at the next funding basis adjustment; Pepperstone to launch XAGUSD-PERP.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1782431997282909 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792481789618939

### crypto-yield-psm — Crypto yields down; PSM scoping for XBTUSD/XETUSD
status: open · since: 2026-10-06 · last: 2026-10-15
State: Crypto spread yield fell to ~USD 200/M versus 350-450 historically. Isaac proposed PSM (MK agreed 2026-10-08); engine verification under way.
Next: Isaac to finish engine verification (5 variants on 8 and 11 Oct flow) and send MK PnL/spread numbers for PSM fully active / defensive only / 10% widening.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1791285982179839 https://mahifx.slack.com/archives/C033K2P0RPT/p1792068068772829

### fi-skew-tuning — FI/skew/LR sizing and signals across FX, CFD and metals
status: open · since: 2026-08-18 · last: 2026-10-14
State: On 2026-10-14 Isaac moved FX majors to IFM-based benchmark adjustments. On CFD, MK approved promoting HSIHKD, JPXJPY, XAUUSD-F and NDXUSD to the price signal (2026-10-08, monitoring);
Next: Nathan to report on promoted CFD skew performance.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787060801310749 https://mahifx.slack.com/archives/C033K2P0RPT/p1791992133214739

### classification-upload — Pepperstone's own counterparty classification upload (SOW)
status: open · since: 2026-05-19 · last: 2026-10-13
State: MK/Reece have asked since May for an automated S3 upload of their external classifications. On 2026-10-13 Liam said MK has resurfaced and that Mahi will wrap the existing S3-based implementation in the SOW Pepperstone are expecting, aiming to be paid for it.
Next: Liam to issue the SOW.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1779146841798919 https://mahifx.slack.com/archives/C033K2P0RPT/p1791904949863369

### cfd-hedging — CFD inventory hedger rejections, LP liquidity and risk controls
status: open · since: 2026-07-27 · last: 2026-10-13
State: The CFD inventory hedger keeps hitting LP limits: Velocity cancelled 241/250 HSTHKD hedges (2026-09-11). NG1 clips reject on 26Degrees (to 10-13); NG1 hedging stopped 2026-08-06 when the trigger rose USD 2M to 3M.
Next: Reece to ask Invast/OZ whether NG1 depth is capped and whether the book can show remaining depth; Mahi to decide NG1 trigger appetite (USD 3M vs 2M) and the hedge venue review.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1785164826669399 https://mahifx.slack.com/archives/C06AR8MT8NT/p1791898246094219

### fx-si-sims — FX B-book SI/inventory sims for Pepperstone
status: watching · since: 2026-08-27 · last: 2026-09-22
State: Nathan's SI/inventory sims (asked 2026-08-27) went to Stephen 2026-09-22; he is convinced pure B-booking is wrong, but his constraint is the prime-broker credit limit (USD 200M), which every simulated method exceeds. Watching: quiet since 2026-09-22; the XAG NOP issue shows the same constraint.
Next: Nathan to rework artefacts toward risk within the USD 200M limit; Stephen to send exact credit numbers.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787786333971199 https://mahifx.slack.com/archives/C033K2P0RPT/p1790046562048089

### margin-exploit-throttle — New-account margin exploits and order throttling
status: watching · since: 2026-07-30 · last: 2026-09-14
State:  Diego asked for symbol-level throttling (2026-08-31); Stephen promised more exploiting accounts (2026-09-14). Daria: the 150 orders/1000ms per-counterparty throttle cannot be scoped to new accounts or symbols without a dev change; MK's per-timezone / NZDUSD override request looks unanswered.
Next: Mahi to answer MK on a timezone/NZDUSD-scoped throttle override (and raise the dev change); Stephen to send accounts.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1788172536055649 https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619

### xau-spreads-toxic — XAUUSD spread algorithm and toxic gold flow
status: watching · since: 2026-08-13 · last: 2026-09-14
State: Shyam proposed a PSM-style XAUUSD spread algo (cap 18pt) that Stephen broadly liked (2026-08-24); on 2026-09-14 he was taking it back internally (16c average next month); QQ EA detection is live and Pepperstone want its benefit quantified.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619

### crypto-limit-nofill — XBTUSD client limit not filled despite pool price through it
status: closed · since: 2026-10-29 · last: 2026-10-29 · closed: 2026-10-30
State: Limit sat inside the continuity price once the $100/M markup applied to dynamic-arb executions; Reece accepted.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793263578250659

### positions-mismatch-alert — TradePositions vs Positions mismatch alert after weekend upgrade
status: closed · since: 2026-10-26 · last: 2026-10-27 · closed: 2026-10-27
State: Small HKD mismatch alert after the weekend upgrade; Shyam booked an adjustment 2026-10-27.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793004200709869?thread_ts=1793004200.709869&cid=C06AR8MT8NT

### roll-arb — Roll-time arbitrage on FX majors and Mahi's defensive LR/widening
status: closed · since: 2026-07-17 · last: 2026-10-27 · closed: 2026-11-04
State: Across-the-board roll LR on all majors (tightened 2026-10-19, agreed with Stephen) cut NZDUSD roll volume 87%; on 2026-10-27 Stephen said wide USDCAD Finalto prices are deliberate and Gabriel closed the thread. Only owed: Shyam to show Stephen's team the roll LR set-up.
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
State: B-book arber list cut from ~700 to ~39 problem CPs by 2026-09-02 after tighter badCheck and realtime detection; no activity since 2026-09-03; assumed resolved (A-book variant lives in crypto-a-book-arb).
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1788388750800949

### findings-athena-creds — Findings routine lacks Athena access
status: closed · since: 2026-09-01 · last: 2026-09-01 · closed: 2026-11-02
State: No Athena credentials for the ring-fenced account, so cfd findings ran config-only; no activity since 2026-09-01; assumed resolved.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1788284401790649

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
