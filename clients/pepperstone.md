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
  - {name: "Gabriel Bignon", role: "Pepperstone; YP/arb queries, failover breaks", confidence: low}
  - {name: "Tom Smith", role: "Pepperstone tech/ops: DB/IP requests (not Tom Williams, COO)", confidence: low}
  - {name: "Sebastian Andrews", role: "Pepperstone; DB access", confidence: low}
  - {name: "James White", role: "Pepperstone data", confidence: low}
  - {name: "Georgios Voulgaropoulos", role: "Pepperstone OZ network", confidence: low}
  - {name: "Saemi Kim", role: "Pepperstone; pricing config", confidence: low}
  - {name: "Sam Dammers", role: "Pepperstone security", confidence: low}
  - {name: "Tom Williams", role: "Pepperstone COO since 2026-08"}
last_catchup: 2026-10-30T07:21:42Z
status: active
---

## Now
Crypto A-book dynamic arb was too harsh (633 accounts, client complaints): Light settings and a list reset to 193 went in 2026-10-30, realtime arb detection to follow. Polaris cut over 2026-10-23 but the London crypto server rebooted twice on 2026-10-25 (backup prop trader and alerting owed); 26D-Toxic whitelist answer owed. MK wants the A-book hedger held near zero XAU risk (2026-10-29). CPI/FOMC kill-switch explanation owed to Diego; US DST check due before Sunday. Quarterly review moved to Tuesday 2026-11-03; CFD licence steps to USD 45k/month; procurement contests the USD 1,500 day rate.

## Streams

### crypto-a-book-arb — Crypto A-book dynamic arb classifying too harshly; realtime detection
status: open · since: 2026-10-29 · last: 2026-10-30
State: Reece (2026-10-29) said the crypto A-book dynamic arb classifies far too harshly; Stephen (10-30) reported more client complaints and asked for a quick fix or whitelists. Shyam's 60-day sims showed the cycle flagged anything worse than $0/M on small gates, so 633 accounts sat on the list. Stephen chose the Light profile: Shyam set the 7-day and 30-minute bad checks to -$5/M and reset the list to 193 problem accounts (the 29 realtime-flagged accounts all kept; a before/after CSV was shared). Stephen also agreed to realtime arb detection ($1M, 50 fills, worse than -$50/M over a rolling hour) and Shyam said it will be implemented. Absorbs the 2026-10-18..20 XBTUSD skew-arber thread (ten accounts of one client at about -$55/M, accounts whitelisted against rehab, a wrongly rehabilitated Arbitrageur to be blacklisted by Stephen, MK's request to tone down skew over weekends, Isaac to review crypto skew sizing).
Next: Shyam to enable realtime arb detection; Stephen to blacklist the misclassified counterparty; Isaac to review crypto skew sizing and weekend setting.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792355023754729?thread_ts=1792355023.754729&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1793329376387089?thread_ts=1793262497.615879&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1793330613302529?thread_ts=1793262497.615879&cid=C06AR8MT8NT

### gateway-cpi-reject — NY gateway kill switch trips on data events (CPI, FOMC)
status: open · since: 2026-10-14 · last: 2026-10-29
State: On 2026-10-14 ~12:30 GMT a NY gateway tripped its kill switch on the CPI print (Last Look latency spike on clientDistributionGateway4; XAUUSD SYSTEM_CLOSED rejects, OZ retried ~25k orders on the London backup); Mahi still owes Diego a log-backed explanation and an account of the ~20s LD price delay. It recurred 2026-10-28 18:47Z at the FOMC presser: clientDistributionGateway1 dropped the NY-to-LDN backup quote sessions for "Slow consumer" (primaries also 0.3-2.6s latent), went to ERROR ~85s, and NY books were re-enabled at 19:00Z; the NY hub failed over to LDN cleanly. Daria (2026-10-29) argues failover-session drops should not trip the kill switch and asks whether configurable per-connection alert levels are still planned.
Next: Mahi (Rory/Nathan) owes Diego the CPI kill-switch explanation and LD delay; Mahi to decide on configurable/failover-exempt kill-switch alert levels.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1791997243862479 https://mahifx.slack.com/archives/C033K2P0RPT/p1791981251222909 https://mahifx.slack.com/archives/C033K2P0RPT/p1793213720273189 https://mahifx.slack.com/archives/C033K2P0RPT/p1793238933942589?thread_ts=1793213720.273189&cid=C033K2P0RPT

### cfd-depth-cap — CATTLEUSD 96k trade break: spread layers and distributed quantity cap
status: open · since: 2026-10-29 · last: 2026-10-29
State: A 96k CATTLEUSD trade broke overnight ("Internalisation Quantity greater than Published"): the spread table gave only 40k and the channel cap (visible quantity 350 x normal quantity 200) limited the book to 70k. Pepperstone (Ruby) added six layers on NY and LD (25k top of book, 15k each behind); Nathan raised CATTLEUSD's normal quantity for a 100k book, with an EOD restart scheduled to apply it, and checked the layers. Pepperstone will own the channel-level cap (channel explorer, max 1000).
Next: Nathan to confirm the CATTLEUSD change is live after the EOD restart.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793234694691149 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793245677481509?thread_ts=1793234694.691149&cid=C06AR8MT8NT

### dst-sunday-check — US DST change: confirm no pricing/execution breaks
status: open · since: 2026-10-29 · last: 2026-10-29
State: Diego asked on 2026-10-29 for confirmation that US DST on Sunday (2026-11-01) causes no pricing or execution breaks. Shyam expects none and will sweep config and report back.
Next: Shyam to sweep config and confirm to Diego.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793250276577629 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793251365699289?thread_ts=1793250276.577629&cid=C06AR8MT8NT

### cfd-licence-fee — CFD licence fee step-up at month 4 and quarterly review prep
status: open · since: 2026-10-19 · last: 2026-10-30
State: The CFD licence enters month 4, when the addendum fee uplift moves from USD 30k to USD 45k a month. Nicole will annotate the invoice. On 2026-10-21 Andrew suggested using the quarterly review with Pepperstone (in about two weeks) to remind them of the fee increase and show current value-add, plans and anything further Mahi can do; Bonnie is happy to raise it there and Will asked the team to get a system health review ready for it.
On 2026-10-29 Daria shared a first-pass QBR artifact and Andrew updated it (Athena skew, DR scenarios, weekend gold, swaps, AI agents); he still needs the hero-moment links opened and FX/CFD cross-region failover confirmed. The quarterly moved from Monday 8am to Tuesday 2026-11-03 (Stephen fine, awaiting MK; Andrew joins).
Next: Isaac/Nathan to finish the QBR draft and checks; Daria to confirm Tuesday with MK; Mahi to raise the CFD fee step-up there or before the next invoice.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1792425618470259 https://mahifx.slack.com/archives/C033K2P0RPT/p1792573119829529 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793308448617129?thread_ts=1793305398.074479&cid=C06AR8MT8NT

### fx-a-book-hedging — FX A-book metals hedging, LP limits and prime-broker positions
status: open · since: 2026-09-14 · last: 2026-10-29
State: PB LPs are off the table for metals; since 2026-09-17/18 Mahi hedges metals via Finalto and Invast with per-LP backstops and round-robin over look-alike tags. On 2026-10-26 MK asked how an ISPRIME XAUUSD position arose despite LPR rules (LPR sold there on the cheapest offer, Mahi bought, sold to Finalto/Invast) and wants metals LPR rules at top priority (Pepperstone are margin-squeezed at LPs); Kate loosened metals LPR spread/quantile conditions and Reece traded down positions on 2026-10-27. On 2026-10-28 Daria delayed the $5k-VaR clearance rule by 5s (it was adding to XAUUSD), added equivalent immediate LPR rules (backstop immediate above $15k VaR) and raised VaR trigger and backstop delays so combined and LPR rules hedge first, restarting hybridHedgerNY1 twice. On 2026-10-29 MK asked for further A-book hedger changes to keep XAU risk always close to 0 (excess risk currently).
Next: Daria/Kate to answer MK on holding XAU near zero and review the loosened LPR conditions.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793272154618899

### open-failover-breaks — Trades failing over to the internal maker at the open
status: open · since: 2026-10-27 · last: 2026-10-27
State: Gabriel is investigating breaks tied to failover trades: a coffee close at Monday's open reached the hub 1ms after IG's first tick, before Mahi's price arrived, so it failed over. Isaac says Mahi cannot stream earlier and a longer last look would not help. Gabriel will look at other fixes.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793118304272449?thread_ts=1793118304.272449&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1793125987953359?thread_ts=1793118304.272449&cid=C06AR8MT8NT

### roll-arb — Roll-time arbitrage on FX majors and Mahi's defensive LR/widening
status: open · since: 2026-07-17 · last: 2026-10-27
State: NZDUSD roll arb spread to EURCHF, AUDNZD, EURUSD, USDCAD, EURNZD (USD 90M, 2026-10-14); roll LR plus widening cut NZDUSD roll volume 87% by 2026-09-23. After a 2026-10-15 call Mahi moved to an across-the-board roll LR on all majors, and on 2026-10-19 Shyam tightened it further (burst 250k to 0, refill 500k/s to 250k/s), agreed with Stephen, who is considering A-booking some flow; the toxic NYC pool was repointed (PB instruments to Invast_Defensive, SOR restart scheduled). On 2026-10-27 Stephen said wide USDCAD Finalto prices at the 2026-10-19 open are deliberate to restrict roll traders; Gabriel closed it.
Next: Shyam to show Stephen's team the roll LR set-up.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1784250309662259 https://mahifx.slack.com/archives/C033K2P0RPT/p1792377289163719 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792384520826769?thread_ts=1792384520.826769&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1793134266443239?thread_ts=1793125676.700959&cid=C06AR8MT8NT

### toxic-pool-failover — Toxic client internalised after failover to LD, request for hard 26D whitelist
status: open · since: 2026-10-26 · last: 2026-10-26
State: On 2026-10-26 Stephen reported a client on the A-China>Broker 26D Toxic Pool rules traded EURCAD and, apparently after a brief failover to LD, was internalised, leaving 26D positions to trade out. He asked whether such clients can be whitelisted as 26D-Toxic 100% of the time so open and close are both captured. Shyam replied that Mahi will check and revert.
Next: Mahi (Shyam) to answer Stephen on a no-exceptions 26D-Toxic whitelist and why the failover internalised.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792988548313129?thread_ts=1792988548.313129&cid=C06AR8MT8NT

### dev-day-rate — Pepperstone procurement challenges the USD 1,500 SOW day rate
status: open · since: 2026-10-22 · last: 2026-10-22
State: Pepperstone procurement (Lisa) objected to the SOW day rate moving from USD 1,000 to 1,500 and proposed a rate card, volume tiers and a lower base. Liam: 1,000 since Nov 2021, SOW #4 agreed at 1,250 with Stephen; suggests 6-12 months at 1,250. Bonnie drafted a reply (1,250 for 12 months then 1,500, rate card, no tiers); not seen sent.
Next: Bonnie to send/revise the reply to Lisa; Liam to review the draft.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1792657103153339 https://mahifx.slack.com/archives/C033K2P0RPT/p1792688981792389

### fx-xag-nop-limit — Inventory hedger blocked on XAGUSD per-market NOP limits
status: open · since: 2026-10-23 · last: 2026-10-23
State: On 2026-10-23 the FX inventory hedger sat short about 89k oz XAGUSD (~USD 4.8M, risk level USD 1.6M) because Finalto, Invast and ISPrime NY were over the USD 20M per-market NOP watermark, so only NOP-reducing trades were allowed. Stephen says opposing XAU/XAG positions across markets are the problem; he will loosen Finalto limits for now.
Next: Stephen to loosen Finalto NOP limits and revisit; Mahi to help if asked.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792722843067479 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792723876829419

### crypto-env-upgrade — Crypto environment upgrade in APAC window, held on pre-check conflicts
status: open · since: 2026-10-22 · last: 2026-10-23
State: Liam asked on 2026-10-22 to upgrade the crypto environment in the next APAC session; Diego approved. Shyam held the deploy on 2026-10-23 after pre-checks showed riskPath not coming back up and odd indicative-pricing execution (ZD 23682), and asked Isaac whether internalising at the continuity price while indicative is acceptable.
Next: Isaac to answer on internalising at the continuity price when indicative; Shyam to review the pre-check conflicts and reschedule.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792665503647569 https://mahifx.slack.com/archives/C033K2P0RPT/p1792721043650659

### polaris-migration — Spot crypto moving from Modulus to Polaris (SOW)
status: open · since: 2026-08-21 · last: 2026-10-25
State: Modulus dropped 2026-08-21; Liam wants an SOW (none seen yet). Liam self-approved the 2026-10-23 cutover (CHG-2610-T16F): propTraderPolaris1 on London trades Polaris and the three old prop traders are decommissioned. The London crypto server rebooted twice on 2026-10-25 night after the RAM upgrade, taking propTraderPolaris1 down; Stephen asked for a NY/LD backup so maintenance has no downtime, plus alerting urgently.
Next: Mahi to set up a backup/failover for propTraderPolaris1 and alerting; Liam to scope the SOW.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1787289556446609 https://mahifx.slack.com/archives/C033K2P0RPT/p1792638948097249 https://mahifx.slack.com/archives/C033K2P0RPT/p1792964887567969 https://mahifx.slack.com/archives/C033K2P0RPT/p1792968665134069

### cfd-pricing-feeds — CFD feed gaps, reference-market changes and indicative alerts
status: open · since: 2026-09-22 · last: 2026-10-29
State: USDCLP gap (2026-09-22) is QRT-side; Pepperstone to raise with OneZero. IG-feed latency exploitation (2026-10-16): CHG-2610-4GVE republished cash/front-month feeds as proxy markets under the 13 forward symbols, primary with IG fallback, live on all four prod pricers 2026-10-27 (proxy mid ran ~200-300ms ahead on beta; timing only, no backtest); remaining check is a clean fallback to IG at the next cash close. Ten indices went to Velocity as primary for pricing and hedging in LDN and NYC (CHG-2610-GF87, 2026-10-24); VELOCITY_LDN does not price JPXJPY; Isaac fixed an LDN-only Nikkei backup rule and is auditing. Out-of-hours timezone update follows 1 Nov with US DST end; on 2026-10-25 Pepperstone said they cannot see the Custom2 timezone times (tradingTimeTable.timezoneOverrides). MK asked for @here on channel alerts; William agreed.
Next: Shyam to raise visibility of timezone overrides with dev; Reece to check whether VELOCITY_LDN should stream JPXJPY; Isaac/Shyam to do the OOH timetable update on 1 Nov; Isaac to confirm IG fallback at next cash close; Pepperstone to chase OneZero/QRT on USDCLP.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1790096194336949 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792155095799099?thread_ts=1792155095.799099&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C033K2P0RPT/p1792581335519849?thread_ts=1792581335.519849&cid=C033K2P0RPT https://mahifx.slack.com/archives/C033K2P0RPT/p1793274530228519

### infra-resilience — Crypto server reboots, failover sessions and patching
status: open · since: 2026-08-09 · last: 2026-10-23
State: Infra patches moved to Monday windows with notice after Aug 29 reboots. On 2026-10-05 Arun found the NYC OZ failover MD/order sessions flapping every 7-8 minutes from TCP retransmits (primary healthy). Beeks powered down the London crypto server for a RAM upgrade (NOCINT-854295, orders failing over to NY); the server then rebooted twice on the night of 2026-10-25 (see polaris-migration).
Next: Arun to raise the packet loss with Beeks if it persists; Mahi to find why the London server rebooted twice on 2026-10-25.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1786319051125299 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792489392693439 https://mahifx.slack.com/archives/C033K2P0RPT/p1792767468812089

### crypto-hedging — Crypto spot hedger tuning and LP de-prioritisation
status: open · since: 2026-07-13 · last: 2026-10-20
State: Spot crypto hedgers de-prioritise LPs that cancel/reject; HRP added to hedger rules 2026-10-15. On 2026-10-19 XAUT/SOL opposite positions traced to merged per-LP LPR rules; Isaac restored per-market LPR rules for non-XBT/XET pairs and cut LPR delays. On 2026-10-20 Stephen said XAUT/PAXG hedging has no cost benefit; Nathan offered to remove them via instrumentToProfileMappings.
Next: Stephen to decide whether to drop XAUT/PAXG from SI hedging.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1783981698651339 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792414394365519?thread_ts=1792414394.365519&cid=C06AR8MT8NT

### data-access — Pepperstone DB, S3/Athena access and IP whitelists
status: open · since: 2026-06-29 · last: 2026-10-20
State: Tom Smith's office IP was whitelisted 2026-10-01 (Sam Dammers wants only Cloudflare IPs). Still open: Sebastian Andrews' DB access (2026-09-15) fails on TCP 3306 from Cloudflare WARP despite whitelisted IPs; last chased 09-28. Also James White's trade_id join outliers vs OneZero and Reece's S3 backfill question.
Next: Mahi to answer Sebastian, James and Reece.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1782731133990719 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792460410497769?thread_ts=1792460410.497769&cid=C06AR8MT8NT

### perps-pricing — Perp instruments: pricing, rollover and KRX
status: open · since: 2026-06-26 · last: 2026-10-20
State: WTI perp mispricing (2026-09-20): Binance removed from non-XAUUSD perp references. Brent perp rollover: Isaac added a 16-minute force-indicative window, basis-jump fix (MahiMain PR 1168) deployed 2026-09-30, off on beta only to compare at the next funding adjustment. KRXUSD-PERP replaced KRXKRW-PERP on 2026-10-07; 2dp-vs-1dp price rejects fixed 2026-10-20. XAGUSD-PERP still unlaunched (Pepperstone to finish config and test).
Next: Isaac to compare beta vs prod at the next funding basis adjustment; Pepperstone to launch XAGUSD-PERP.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1782431997282909 https://mahifx.slack.com/archives/C06AR8MT8NT/p1789944667574059 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792481789618939

### hrp-ld-md — HRP market data missing in London after tag change
status: open · since: 2026-10-18 · last: 2026-10-19
State: Since 2026-10-18 the PEP-LD4_Q feed resumed tagged HRP-2 while Mahi's HRP_LDN mapping is still HRP-Agg, so no HRP data reaches London. Diego thinks it is an HRP-side change and was waiting on HRP (2026-10-19). Overlaps crypto-hedging.
Next: Diego to get HRP's answer; Shyam to update the mapping to HRP-2 if confirmed.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792362092980019?thread_ts=1792362092.980019&cid=C06AR8MT8NT

### crypto-yield-psm — Crypto yields down; PSM scoping for XBTUSD/XETUSD
status: open · since: 2026-10-06 · last: 2026-10-15
State: Crypto spread yield fell to ~USD 200/M versus 350-450 historically (about half BTC's rally against a flat spread). Isaac proposed PSM to MK (agreed 2026-10-08) and on 2026-10-15, after a call with MK and Andrew, screened configs: a "middle ground" widen/tighten gives about +9.2/M on XBTUSD and +48.5/M on XETUSD; full backtest and Compass sim verification is under way.
Next: Isaac to finish engine verification (5 variants on 8 and 11 Oct flow) and send MK PnL/spread numbers for PSM fully active / defensive only / 10% widening.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1791285982179839 https://mahifx.slack.com/archives/C033K2P0RPT/p1792068068772829

### fi-skew-tuning — FI/skew/LR sizing and signals across FX, CFD and metals
status: open · since: 2026-08-18 · last: 2026-10-14
State: Reece had the EURUSD skew cap put back to 0.1 pip (2026-09-22); on 2026-10-14 Isaac moved FX majors to IFM-based benchmark adjustments. On CFD, skew was raised after Nathan's beta shadow test and MK approved promoting HSIHKD, JPXJPY, XAUUSD-F and NDXUSD to the price signal (2026-10-08, monitoring). CFD LR was cut back in September after LR-caused cancels (channel LR off, global cap 1000/M to 300/M).
Next: Nathan to report on promoted CFD skew performance.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787060801310749 https://mahifx.slack.com/archives/C06AR8MT8NT/p1791453538861039?thread_ts=1788929145.526369&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C033K2P0RPT/p1791992133214739

### classification-upload — Pepperstone's own counterparty classification upload (SOW)
status: open · since: 2026-05-19 · last: 2026-10-13
State: MK/Reece have asked since May for an automated S3 upload of their external classifications. On 2026-10-13 Liam said MK has resurfaced and that Mahi will wrap the existing S3-based implementation in the SOW Pepperstone are expecting, aiming to be paid for it.
Next: Liam to issue the SOW.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1779146841798919 https://mahifx.slack.com/archives/C033K2P0RPT/p1791904949863369

### cfd-hedging — CFD inventory hedger rejections, LP liquidity and risk controls
status: open · since: 2026-07-27 · last: 2026-10-13
State: The CFD inventory hedger keeps hitting LP limits: Velocity cancelled 241/250 HSTHKD hedges (2026-09-11); precision rejects fixed with hedger-only overrides. NG1 clips reject on 26Degrees (09-25, 09-29, 10-13); Isaac raised VaR reduction per second on 2026-09-29. NG1 hedging stopped 2026-08-06 when the trigger rose USD 2M to 3M (Andrew).
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

### crypto-btc-arb — XBTUSD skew arbers hitting crypto pricing
status: closed · since: 2026-10-18 · last: 2026-10-20 · closed: 2026-10-30
State: merged into crypto-a-book-arb.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792355023754729?thread_ts=1792355023.754729&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1792467208123369?thread_ts=1792464616.833879&cid=C06AR8MT8NT

### crypto-limit-nofill — XBTUSD client limit not filled despite pool price through it
status: closed · since: 2026-10-29 · last: 2026-10-29 · closed: 2026-10-30
State: Reece's SELL limit sat inside the continuity price once the $100/M (about $8/XBT) markup applied to dynamic-arb executions; William explained, Reece accepted.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793263578250659 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793288055752659?thread_ts=1793263578.250659&cid=C06AR8MT8NT

### compass-264-release — Compass 26.4 upgrade of FX and CFD over the weekend
status: closed · since: 2026-10-23 · last: 2026-10-23 · closed: 2026-10-29
State: 26.4 applied to FX and CFD over 24-25 Oct (the TradePositions mismatch alert followed, see positions-mismatch-alert); no further issues seen.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792772169235949

### positions-mismatch-alert — TradePositions vs Positions mismatch alert after weekend upgrade
status: closed · since: 2026-10-26 · last: 2026-10-27 · closed: 2026-10-27
State: Small HKD TradePositions/Positions mismatch alert since 2026-10-24 (weekend upgrade, no trading impact); Shyam booked an adjustment on 2026-10-27 so it should stop.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793004200709869?thread_ts=1793004200.709869&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1793059314284639?thread_ts=1793004200.709869&cid=C06AR8MT8NT

### compass-263-release — Compass 26.3 release to all Pepperstone systems
status: closed · since: 2026-10-20 · last: 2026-10-21 · closed: 2026-10-22
State: Done: all pricers on 26.3 by 2026-10-21.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792489817664909 https://mahifx.slack.com/archives/C033K2P0RPT/p1792608882275709

### xau-fill-vs-price — XAUUSD fill vs displayed price gap (two pricers)
status: closed · since: 2026-10-21 · last: 2026-10-21 · closed: 2026-10-22
State: Second NYC pricer filled it (separate skew timers); Reece accepted.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792587213386379?thread_ts=1792587213.386379&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1792593460283749?thread_ts=1792587213.386379&cid=C06AR8MT8NT

### ld-estate-incident — London estate inter-region connectivity incident
status: closed · since: 2026-10-16 · last: 2026-10-16 · closed: 2026-10-19
State: Cross-region latency/disconnects 2026-10-16; resolved 12:29 BST, no root cause given.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792142815121549 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792142873267079?thread_ts=1792142873.267079&cid=C06AR8MT8NT

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
