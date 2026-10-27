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
  - {name: "Stephen Hendrie", role: "Pepperstone exchange/product lead; main FX+crypto counterpart, joined steer co 2026-07"}
  - {name: "Marianna Konstantinidi (MK)", role: "Pepperstone trading ops, CFD/crypto config requests, CFD licence sponsor"}
  - {name: "Reece Singh", role: "Pepperstone ops/counterparty admin; classification, YPs, hedger rejections"}
  - {name: "Ruby Wang", role: "Pepperstone OZ/exchange trading ops"}
  - {name: "Diego Arranz", role: "Pepperstone CFD ops, OZ config, IP whitelisting"}
  - {name: "Mariapaz Bobadilla", role: "Pepperstone OZ; pricing/reject queries", confidence: low}
  - {name: "Gabriel Bignon", role: "Pepperstone; yield-profile and arb-classification queries", confidence: low}
  - {name: "Tom Smith", role: "Pepperstone tech/ops: DB/credentials/IP requests (distinct from Tom Williams, COO)", confidence: low}
  - {name: "Sebastian Andrews", role: "Pepperstone; DB access and cancelled-order queries", confidence: low}
  - {name: "James White", role: "Pepperstone data; joins Mahi data to OneZero by trade_id", confidence: low}
  - {name: "Georgios Voulgaropoulos", role: "Pepperstone OZ network/infrastructure", confidence: low}
  - {name: "Saemi Kim", role: "Pepperstone; pricing config changes 2026-10", confidence: low}
  - {name: "Sam Dammers", role: "Pepperstone security/Cloudflare IP policy", confidence: low}
  - {name: "Tom Williams", role: "Pepperstone COO since 2026-08"}
last_catchup: 2026-10-27T07:20:34Z
status: active
---

## Now
Polaris (spot crypto) cut over 2026-10-23, but the London crypto server rebooted twice on 2026-10-25 and Stephen wants a backup prop trader and alerting urgently; he also wants a hard 26D-Toxic whitelist after an internalised failover (2026-10-26). Metals hedging is squeezed on LP margin (LPR rules loosened 2026-10-26, positions to be traded down). Also live: roll arb, XBTUSD skew arbers, CPI-print incident response owed to Diego, FX/CFD on 26.4. CFD licence steps to USD 45k/month; procurement contests the USD 1,500 dev day rate (Mahi counter: 1,250).

## Streams

### fx-a-book-hedging — FX A-book metals hedging, LP limits and prime-broker positions
status: open · since: 2026-09-14 · last: 2026-10-26
State: PB LPs are off the table for metals; since 2026-09-17/18 Mahi hedges metals via Finalto and Invast with per-LP backstop logic and round-robin over look-alike tags (agreed by Stephen and MK); the 2026-09-28 XAG short at ISP was a Pepperstone-side break. On 2026-10-26 Reece saw hedging still executing with Invast (no reply seen), and MK asked how an ISPRIME XAUUSD position arose despite LPR rules. Kate: LPR rules sold to ISPRIME, which mostly had the cheapest offer and weakest bid, so Mahi buys there and sells to Finalto/Invast. MK wants metals LPR rules at highest priority as Pepperstone are margin-squeezed at the LPs; Kate loosened the metals LPR spread conditions and relaxed the spread quantile predicates (bouncing hybridHedgerNYC1), to review over a day or so, and offered to manually trade down the positions (MK said yes). MK's SCB-LP query on exotics (USDHUF) was Pepperstone's incomplete USD-only switch cleanup (SCB, not POP), no Mahi change.
Next: Mahi (Kate) to manually trade down the metals positions, review the loosened LPR conditions and answer Reece on Invast hedging.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793032160128729?thread_ts=1793031944.392429&cid=C06AR8MT8NT

### toxic-pool-failover — Toxic client internalised after failover to LD, request for hard 26D whitelist
status: open · since: 2026-10-26 · last: 2026-10-26
State: On 2026-10-26 Stephen reported a client on the A-China>Broker 26D Toxic Pool rules traded EURCAD and, apparently after a brief failover to LD, was internalised, leaving 26D positions to trade out. He asked whether such clients can be whitelisted as 26D-Toxic 100% of the time so open and close are both captured. Shyam replied that Mahi will check and revert.
Next: Mahi (Shyam) to answer Stephen on a no-exceptions 26D-Toxic whitelist and why the failover internalised.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792988548313129?thread_ts=1792988548.313129&cid=C06AR8MT8NT

### compass-264-release — Compass 26.4 upgrade of FX and CFD over the weekend
status: open · since: 2026-10-23 · last: 2026-10-23
State: Leonardo told Pepperstone on 2026-10-23 that the FX and CFD Compass environments (not crypto) get 26.4 over the 24-25 Oct weekend, live at each host's weekly reboot, with monitoring over the open. Outcome not yet seen in channel.
Next: Mahi to confirm any 26.4 issues.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792772169235949

### dev-day-rate — Pepperstone procurement challenges the USD 1,500 SOW day rate
status: open · since: 2026-10-22 · last: 2026-10-22
State: Pepperstone procurement (Lisa) objected to the SOW day rate moving from USD 1,000 to 1,500 and proposed a written rate card (fixed 12 months, 90 days' notice), volume tiers, and a lower base rate. Liam's background: rate held at 1,000 since Nov 2021 (about 8.8%/yr), SOW #4 was agreed at 1,250 with Stephen, quotes are lean, and Modulus was built free; he thinks 1,500 was a bit sharp and suggested 6-12 months at 1,250. Bonnie drafted a reply (hold 1,250 for 12 months then 1,500, written rate card, no volume tiers); not yet sent as far as seen.
Next: Bonnie to send/revise the reply to Lisa; Liam to review the draft.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1792657103153339 https://mahifx.slack.com/archives/C033K2P0RPT/p1792688981792389

### fx-xag-nop-limit — Inventory hedger blocked on XAGUSD per-market NOP limits
status: open · since: 2026-10-23 · last: 2026-10-23
State: On 2026-10-23 Nathan flagged the FX inventory book (hybridHedgerInvNY1) short about 89k oz XAGUSD (~USD 4.8M) against a USD 1.6M inventory risk level. The hedger could not buy because Finalto, Invast and ISPrime NY were all over the USD 20M per-market NOP high watermark in Compass (Compass shows each long in XAGUSD), so only NOP-reducing trades are allowed. Stephen says Pepperstone's own snapshot including B-book hedges is net long, XAU/XAG opposing positions across markets are the problem, and LPs are under pressure on XAU; he will loosen limits on Finalto for now and expects to keep tinkering while hedges are high.
Next: Stephen to loosen Finalto NOP limits and revisit; Mahi to help if asked.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792722843067479 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792723876829419

### crypto-env-upgrade — Crypto environment upgrade in APAC window, held on pre-check conflicts
status: open · since: 2026-10-22 · last: 2026-10-23
State: Liam asked on 2026-10-22 to upgrade the crypto environment in the next APAC session (both regions, NZ hours); Diego approved (MK deferred). Shyam prepared it but held the deploy on 2026-10-23 after pre-checks showed riskPath not coming back up and odd indicative-pricing execution behaviour (ZD 23682), and asked Isaac whether internalising on the continuity pool price while indicative (e.g. perps at weekends) is acceptable.
Next: Isaac to answer on internalising at the continuity price when indicative; Shyam to review the pre-check conflicts and reschedule.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792665503647569 https://mahifx.slack.com/archives/C033K2P0RPT/p1792721043650659

### polaris-migration — Spot crypto moving from Modulus to Polaris (SOW)
status: open · since: 2026-08-21 · last: 2026-10-25
State: Pepperstone is dropping Modulus for spot crypto (2026-08-21); Liam wants an SOW with an added-days clause or monthly exchange-MM fee. Polaris sessions and a 26.3 build were staged in London 2026-10-19-22. On 2026-10-23 Liam self-approved the cutover (CHG-2610-T16F): a new process propTraderPolaris1 on London trades Polaris and all three old prop traders are decommissioned. Arun then asked for propTraderPolaris1 to be turned back on once Polaris fixed their issue. The London crypto server was rebooted twice on 2026-10-25 night (after the Saturday RAM upgrade), taking propTraderPolaris1 down twice; Stephen complained the prop trader was off again and asked for a NY/LD backup so maintenance has no downtime, plus alerting urgently. Shyam asked internally whether a backup like the old setup can be built. No SOW seen yet.
Next: Mahi to set up a backup/failover for propTraderPolaris1 and alerting; Liam to scope the SOW.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1787289556446609 https://mahifx.slack.com/archives/C033K2P0RPT/p1792638948097249 https://mahifx.slack.com/archives/C033K2P0RPT/p1792964887567969 https://mahifx.slack.com/archives/C033K2P0RPT/p1792968665134069

### cfd-pricing-feeds — CFD feed gaps, reference-market changes and indicative alerts
status: open · since: 2026-09-22 · last: 2026-10-25
State: USDCLP gap (2026-09-22) is QRT-side; Pepperstone to raise with OneZero, MK disabled NAPN and USDCLP meanwhile. On 2026-10-15 MK asked to move the primary reference on ten indices to Velocity ahead of extended hours at the DST change. On 2026-10-16 MK flagged clients exploiting latency on the IG feed (known, IG fixing; no other LP prices UKOUSD/USOUSD, so no backup); Isaac proposed a proxied cash-partner mid as primary with IG as fallback; MK agreed to beta, pending a proxy restart. The out-of-hours timezone update follows on 1 Nov with US DST end. On 2026-10-22 Isaac corrected a Nikkei backup rule scoped for LDN but not NYC and started an audit; VELOCITY_LDN does not price JPXJPY (only NYC). On 2026-10-23 Isaac confirmed the ten indices go to Velocity as primary for pricing and hedging in LDN and NYC before Sunday's open; Shyam executed it Saturday (CHG-2610-GF87). Stephen asked whether Mahi "jumped the gun"; Shyam pointed to Pepperstone's own request. On 2026-10-25 Stephen asked where Custom2 timezone times are defined: Shyam pointed to tradingTimeTable.timezoneOverrides, Stephen and Tom Williams said Pepperstone cannot see those keys, and Shyam will ask dev whether they can be made visible. MK also asked for an @here tag on channel alerts (2026-10-23); William agreed.
Next: Shyam to raise visibility of timezone overrides with dev; Reece to check whether VELOCITY_LDN should stream JPXJPY; Isaac/Shyam to do the OOH timetable update on 1 Nov; Isaac to prepare the proxied-mid IG fallback for beta; Pepperstone to chase OneZero/QRT on USDCLP.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1790096194336949 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792155095799099?thread_ts=1792155095.799099&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C033K2P0RPT/p1792581335519849?thread_ts=1792581335.519849&cid=C033K2P0RPT https://mahifx.slack.com/archives/C06AR8MT8NT/p1792969809909669?thread_ts=1792969809.909669&cid=C06AR8MT8NT

### cfd-licence-fee — CFD licence fee step-up at month 4 and quarterly review prep
status: open · since: 2026-10-19 · last: 2026-10-21
State: The CFD licence enters month 4, when the addendum fee uplift moves from USD 30k to USD 45k a month. Nicole will annotate the invoice. On 2026-10-21 Andrew suggested using the quarterly review with Pepperstone (in about two weeks) to remind them of the fee increase and show current value-add, plans and anything further Mahi can do; Bonnie is happy to raise it there and Will asked the team to get a system health review ready for it.
Next: Mahi team to prep the system health review and value-add summary for the quarterly (~early Nov); Mahi to raise the CFD fee step-up there or before the next invoice.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1792425618470259 https://mahifx.slack.com/archives/C033K2P0RPT/p1792573119829529

### infra-resilience — Crypto server reboots, failover sessions and patching
status: open · since: 2026-08-09 · last: 2026-10-23
State: Crypto server reboots (LDN Aug 29) moved infra patches to Monday windows with notice. On 2026-10-05 Arun found the NYC OZ failover MD/order sessions flapping every 7-8 minutes from TCP retransmits (primary healthy). Beeks had to power down the London crypto server, done over the weekend. It was scheduled as a RAM upgrade (NOCINT-854295, orders failing over to NY); the London server then rebooted twice on the night of 2026-10-25, taking propTraderPolaris1 down (see polaris-migration).
Next: Arun to raise the packet loss with Beeks if it persists; Mahi to find why the London server rebooted twice on 2026-10-25.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1786319051125299 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792489392693439 https://mahifx.slack.com/archives/C033K2P0RPT/p1792767468812089

### crypto-btc-arb — XBTUSD skew arbers hitting crypto pricing
status: open · since: 2026-10-18 · last: 2026-10-20
State: On 2026-10-18 Gabriel flagged ten accounts of one client (over USD 40M at about -55/M spread yield) hitting XBTUSD. Shyam says they were skew arbing, so negative spread yield is expected; the classifier had already marked most as arbers and he offered to whitelist them against rehabilitation, which Stephen accepted. Shyam is reviewing the skew config (FI otherwise performing well). On 2026-10-19 MK asked for skew to be turned off or toned down a lot over the weekend and Isaac said he would look into it that day. Separately on 2026-10-20 Stephen queried an A_BOOK cancel-ratio alert (12 XBTUSD limit orders from one counterparty cancelled LIQUIDITY_VIOLATION/FORCE_INTERNALISATION): Nathan showed the counterparty, long on the A-Retail Catch-All profile, was auto-classified Arbitrageur on 2026-10-13 and so filled against the continuity pool price, then rehabilitated; Nathan thinks the classification was wrong and suggested blacklisting them from Arbitrageur, which Stephen will do and revisit (some licences make classification awkward).
Next: Stephen to blacklist the counterparty from Arbitrageur classification; Nathan reviewing the misclassification; Isaac to review crypto skew sizing and the weekend setting; Shyam to whitelist the arbing accounts.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792355023754729?thread_ts=1792355023.754729&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1792467208123369?thread_ts=1792464616.833879&cid=C06AR8MT8NT

### crypto-hedging — Crypto spot hedger tuning and LP de-prioritisation
status: open · since: 2026-07-13 · last: 2026-10-20
State: Spot crypto hedgers were reworked in September to de-prioritise LPs that cancel/reject; on 2026-10-15 Isaac added HRP to hedger rules it was excluded from. On 2026-10-19 XAUT/SOL opposite positions came from a June merge of per-LP LPR rules judging spread across all four LPs; Isaac restored per-market LPR rules for non-XBT/XET pairs and cut LPR delays. On 2026-10-20 Stephen said XAUT and PAXG hedging has no cost benefit; Nathan offered to remove them via instrumentToProfileMappings (also hybridHedgerSITotalNYC1), Stephen will discuss internally. Kraken is now an AUDUSD weekend fallback.
Next: Stephen to decide whether to drop XAUT/PAXG from SI hedging.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1783981698651339 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792414394365519?thread_ts=1792414394.365519&cid=C06AR8MT8NT

### data-access — Pepperstone DB, S3/Athena access and IP whitelists
status: open · since: 2026-06-29 · last: 2026-10-20
State: Tom Smith's office IP was whitelisted on the DBs 2026-10-01, though Sam Dammers says only Cloudflare IPs should be used. On 2026-10-20 Stephen was locked out of both NY and LD crypto environments; Nathan reset them. Still open: Sebastian Andrews' PROD_LIVE_CLIENTDB access (2026-09-15) still fails on TCP 3306 from his Cloudflare WARP address after Mahi whitelisted two Cloudflare IPs and sent the failure to Beeks; he suspects his own Cloudflare, last chased 09-28. Also James White's trade_id join outliers vs OneZero (2026-09-23) and Reece's question on S3 backfill before 2026-08-10.
Next: Mahi to answer Sebastian, James and Reece.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1782731133990719 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792460410497769?thread_ts=1792460410.497769&cid=C06AR8MT8NT

### perps-pricing — Perp instruments: pricing, rollover and KRX
status: open · since: 2026-06-26 · last: 2026-10-20
State: WTI perp mispricing (2026-09-20) led to Binance being removed from non-XAUUSD perp references. Brent perp rollover: Isaac added a 16-minute force-indicative window failing over to marked-up HRP_GOLDI, basis-jump fix (MahiMain PR 1168) deployed 2026-09-30, off on the beta pricer only to compare at the next funding adjustment. KRXUSD-PERP replaced KRXKRW-PERP on 2026-10-07; 2dp-vs-1dp price rejects fixed 2026-10-20. XAGUSD-PERP still unlaunched (Pepperstone to finish config and test).
Next: Isaac to compare beta vs prod at the next funding basis adjustment; Pepperstone to launch XAGUSD-PERP.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1782431997282909 https://mahifx.slack.com/archives/C06AR8MT8NT/p1789944667574059 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792481789618939

### roll-arb — Roll-time arbitrage on FX majors and Mahi's defensive LR/widening
status: open · since: 2026-07-17 · last: 2026-10-19
State: NZDUSD roll arb spread to EURCHF, AUDNZD, EURUSD, USDCAD and EURNZD (USD 90M, 2026-10-14); roll LR plus defensive widening cut NZDUSD roll volume 87% by 2026-09-23. After a 2026-10-15 call Mahi switched to an across-the-board roll LR on all majors (channel cap 25/M to 200/M, NZD/USD 600/M) and reduced some widening; Pepperstone want a walkthrough. On 2026-10-19 Shyam tightened the global roll LR further (burst 250k to 0, refill 500k/s to 250k/s on EUR, GBP, USD, AUD, JPY, CHF, CAD), agreed with Stephen, who is considering A-booking some of this flow. Stephen also repointed the toxic NYC pool (PB instruments to Invast_Defensive), needing a SOR restart that Nathan scheduled.
Next: Shyam to show Stephen's team the roll LR set-up; Nathan to do the NYC SOR restart just before 5pm NYT on 2026-10-19.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1784250309662259 https://mahifx.slack.com/archives/C033K2P0RPT/p1792377289163719 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792384520826769?thread_ts=1792384520.826769&cid=C06AR8MT8NT

### hrp-ld-md — HRP market data missing in London after tag change
status: open · since: 2026-10-18 · last: 2026-10-19
State: From about 07:45 UTC on 2026-10-18, when HRP-Agg quotes on all symbols were cancelled, the PEP-LD4_Q feed resumed tagged HRP-2, while Mahi's HRP_LDN market mapping is still HRP-Agg, so no HRP data is reaching London. Shyam asked whether the change is expected or the mapping should move to HRP-2; Diego says it looks like an HRP-side change and at 03:44 BST on 2026-10-19 was still waiting on HRP. This overlaps the HRP hedging weight in crypto-hedging.
Next: Diego to get HRP's answer; Shyam to update the mapping to HRP-2 if confirmed.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792362092980019?thread_ts=1792362092.980019&cid=C06AR8MT8NT

### gateway-cpi-reject — NY gateway kill switch on CPI print, SYSTEM_CLOSED rejects
status: open · since: 2026-10-14 · last: 2026-10-15
State: On 2026-10-14 around 12:30 GMT a Mahi NY distribution gateway tripped its kill switch on the CPI print. Liam traced it to a Last Look latency spike on clientDistributionGateway4 that had recovered; books were switched back on. XAUUSD orders on Mahi_B_NY_4 were rejected SYSTEM_CLOSED and OZ retried ~25k orders on the London backup stream. Mariapaz asked why; Diego separately reported a ~20s LD price delay (Rory 2026-10-15: distributed price was updating through, logs being pulled). Nathan sent only a holding reply and wants a fuller incident response.
Next: Mahi (Rory/Nathan) owes Diego the log-backed explanation of the kill-switch trip (latency-spike cause not yet shared) and the LD delay.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1791997243862479 https://mahifx.slack.com/archives/C033K2P0RPT/p1791981251222909 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792060740686789?thread_ts=1792018491.050639&cid=C06AR8MT8NT

### crypto-yield-psm — Crypto yields down; PSM scoping for XBTUSD/XETUSD
status: open · since: 2026-10-06 · last: 2026-10-15
State: Crypto spread yield fell to ~USD 200/M versus 350-450 historically; Isaac puts about half down to BTC's rally against a flat USD 15/BTC spread, the rest to lower volatility and LP tightening. Isaac proposed PSM to MK (agreed 2026-10-08) and on 2026-10-15, after a call with MK and Andrew, screened configs: a "middle ground" widen/tighten gives about +9.2/M on XBTUSD and +48.5/M on XETUSD; full backtest and Compass sim verification is under way. Andrew also notes Claude RoS/PnL tracking does not match Compass Account Summary for crypto SI.
Next: Isaac to finish engine verification (5 variants on 8 and 11 Oct flow) and send MK PnL/spread numbers for PSM fully active / defensive only / 10% widening.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1791285982179839 https://mahifx.slack.com/archives/C033K2P0RPT/p1792068068772829

### fi-skew-tuning — FI/skew/LR sizing and signals across FX, CFD and metals
status: open · since: 2026-08-18 · last: 2026-10-14
State: Isaac moved XAUUSD to flow-price-thresh after an early-Aug FI dip and it recovered (4.2/M). Reece had the EURUSD skew cap put back to 0.1 pip (2026-09-22); on 2026-10-14 Isaac moved FX majors to IFM-based benchmark adjustments. On CFD, skew was raised after Nathan's beta shadow test and MK approved promoting HSIHKD, JPXJPY, XAUUSD-F and NDXUSD to the price signal (2026-10-08, monitoring). CFD LR was reworked in September after LR-caused cancels: channel LR off, global cap USD 1000/M to 300/M, signals limited to oils, NDX, DOW, SPX (CAC 40%).
Next: Nathan to report on promoted CFD skew performance.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787060801310749 https://mahifx.slack.com/archives/C06AR8MT8NT/p1791453538861039?thread_ts=1788929145.526369&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C033K2P0RPT/p1791992133214739

### classification-upload — Pepperstone's own counterparty classification upload (SOW)
status: open · since: 2026-05-19 · last: 2026-10-13
State: MK/Reece have asked since May for an automated S3 upload of their external classifications. On 2026-10-13 Liam said MK has resurfaced and that Mahi will wrap the existing S3-based implementation in the SOW Pepperstone are expecting, aiming to be paid for it.
Next: Liam to issue the SOW.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1779146841798919 https://mahifx.slack.com/archives/C033K2P0RPT/p1791904949863369

### cfd-hedging — CFD inventory hedger rejections, LP liquidity and risk controls
status: open · since: 2026-07-27 · last: 2026-10-13
State: The CFD inventory hedger keeps hitting LP limits: Velocity cancelled 241/250 HSTHKD hedges (2026-09-11); price-precision rejects fixed with hedger-only overrides (indices pending). NG1 clips reject on 26Degrees (09-25, 09-29, 10-13); Isaac raised VaR reduction per second on 2026-09-29. IG limits hit WHEAT (Reece wants 100k clips). Andrew's 2026-09-01 analysis found NG1 hedging stopped 2026-08-06 when the trigger rose USD 2M to 3M.
Next: Reece to ask Invast/OZ whether NG1 depth is capped and whether the book can show remaining depth; Mahi to decide NG1 trigger appetite (USD 3M vs 2M) and the hedge venue review.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1785164826669399 https://mahifx.slack.com/archives/C06AR8MT8NT/p1791898246094219

### fx-si-sims — FX B-book SI/inventory sims for Pepperstone
status: watching · since: 2026-08-27 · last: 2026-09-22
State: Stephen asked on 2026-08-27 for SI/inventory backtests for the FX B-book (pure warehousing, 17M January swings). Nathan's sims (2026-09-11; David Cooney wanted NOP and margin metrics) went to Stephen on 2026-09-22 and he was happy and convinced pure B-booking is wrong, but his constraint is the prime-broker credit limit (USD 200M), which every simulated method exceeds. Watching: no activity since 2026-09-22; the 2026-10-23 XAG NOP-limit issue shows the same credit/NOP constraint.
Next: Nathan to rework artefacts toward risk within the USD 200M limit; Stephen to send exact credit numbers.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787786333971199 https://mahifx.slack.com/archives/C033K2P0RPT/p1790046562048089

### margin-exploit-throttle — New-account margin exploits and order throttling
status: watching · since: 2026-07-30 · last: 2026-09-14
State: Pepperstone clients exploited margin validation (CPI-print bursts, small-deposit martingale). Diego asked for symbol-level throttling (2026-08-31); Stephen promised more exploiting accounts (2026-09-14). Daria: the existing 150 orders/1000ms per-counterparty throttle cannot be scoped to new accounts or symbols without a dev change; MK then asked for a per-timezone / NZDUSD override, which looks unanswered.
Next: Mahi to answer MK on a timezone/NZDUSD-scoped throttle override (and raise the dev change); Stephen to send accounts.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1788172536055649 https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619

### xau-spreads-toxic — XAUUSD spread algorithm and toxic gold flow
status: watching · since: 2026-08-13 · last: 2026-09-14
State: Shyam proposed a PSM-style XAUUSD spread algo (cap 18pt, avg near today's) that Stephen broadly liked (2026-08-24). On 2026-09-14 Stephen was talking about a 16c average next month and taking the proposal back internally; QQ EA signal detection is live and Pepperstone want its benefit quantified. Watching: waiting on Stephen.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619

### arb-classification — Dynamic arb classification false positives and realtime detection
status: watching · since: 2026-07-27 · last: 2026-09-02
State: Mahi tightened cycle badCheck yield (-1.5/M to -4/M) and enabled realtime arb detection on riskPathBBook (2026-08-21; gates USD 50M volume, 50 fills, worse than -5/M rolling hour); the B-book arber list fell from ~700 to ~39 problem CPs by 2026-09-02, Reece and Stephen happy. One missed Chinese client (-8.87/M) on 2026-09-03. Watching: no activity since.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1785166480858439 https://mahifx.slack.com/archives/C033K2P0RPT/p1788388750800949

### findings-athena-creds — Findings routine lacks Athena access
status: watching · since: 2026-09-01 · last: 2026-09-01
State: Andrew's findings routine has no credentials for the ring-fenced Pepperstone Athena account, so pepperstone-cfd findings ship unsized and skew/LR checks run config-only. Andrew calls this the highest-leverage fix on this client; no resolution seen. Watching.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1788284401790649

### positions-mismatch-alert — TradePositions vs Positions mismatch alert after weekend upgrade
status: closed · since: 2026-10-26 · last: 2026-10-27 · closed: 2026-10-27
State: Small HKD TradePositions/Positions mismatch alert since 2026-10-24 (weekend upgrade, no trading impact); Shyam booked an adjustment on 2026-10-27 so it should stop.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793004200709869?thread_ts=1793004200.709869&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1793059314284639?thread_ts=1793004200.709869&cid=C06AR8MT8NT

### compass-263-release — Compass 26.3 release to all Pepperstone systems
status: closed · since: 2026-10-20 · last: 2026-10-21 · closed: 2026-10-22
State: Done. All Pepperstone pricers (CFD, crypto, FX) on 26.3 as of 2026-10-21; outstanding items go on the 26.4 list.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792489817664909 https://mahifx.slack.com/archives/C033K2P0RPT/p1792608882275709

### xau-fill-vs-price — XAUUSD fill vs displayed price gap (two pricers)
status: closed · since: 2026-10-21 · last: 2026-10-21 · closed: 2026-10-22
State: Fill differed by cents from the screen because the second NYC pricer filled it (separate skew timers). Reece accepted.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792587213386379?thread_ts=1792587213.386379&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1792593460283749?thread_ts=1792587213.386379&cid=C06AR8MT8NT

### ld-estate-incident — London estate inter-region connectivity incident
status: closed · since: 2026-10-16 · last: 2026-10-16 · closed: 2026-10-19
State: LD/NY cross-region latency and disconnects from a Mahi London estate issue (2026-10-16); resolved 12:29 BST, no root cause given.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792142815121549 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792142873267079?thread_ts=1792142873.267079&cid=C06AR8MT8NT

### echo-price-queries — Echo/Compass price and slippage discrepancy questions
status: closed · since: 2026-10-07 · last: 2026-10-07 · closed: 2026-10-15
State: Answered: price shown is price at request (~50ms before fill); XAUUSD fills were a last-look move plus global LR.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1791377823659449

## Arc
- 2021 — first (failed) negotiation; Mahi did ~3 months free goodwill work
- 2023-07-31 — Pepperstone board approves including CFDs
- 2023-12-21 — 3-year MSA signed (MFXEcho + Compass + Pulse, FX and metals)
- 2024-04 — Compass live in production for FX MM
- 2025-07-16 — 3rd Addendum: term to 2028-07-16, USD 115,088/mo from 2025-08-01, no termination for convenience
- 2025-Q4 — Modulus crypto exchange live with 6 AUD pairs
- 2026-Q1 — CFD licence signed; crypto SI profitable every week of 2026
- 2026-07-22 — CFD desk live (NY and LDN)
- 2026-08 — Tom Williams promoted to COO; Stephen Hendrie becomes main counterpart
- 2026-08-21 — Rob Bowen leaves Pepperstone; Pepperstone drops Modulus for spot crypto
- 2026-08-26 — Steven Reed (Modulus-side) no longer at Pepperstone
