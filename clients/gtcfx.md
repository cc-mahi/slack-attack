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
last_catchup: 2026-10-16T07:06:21Z
status: active
---
## Now
GTC is live and ramping: all FX majors/crosses plus XAGUSD and XAUUSD B Book flow route to Mahi over 7 OneZero hubs (A and B sessions each), with an A Book account live since 2026-10-06 (hedging to HRP LPs only).
Main risk is load: cent accounts drive ticket rates (dist6 hit ~4k orders/s on 2026-10-15) and riskPath stalls; the riskPath fix is approved and was rescheduled to the 2026-10-15 12:15-14:45Z window.
In flight: Centroid connection (creds sent 10-13), crypto (BTC/ETH, Binance blocked by Beeks IP), 24/7 session switch with a restart planned 2026-10-16 17:00 NY.

## Streams

### dist-gateway-capacity — Distribution gateway load from cent/small-ticket flow
status: open · since: 2026-09-09 · last: 2026-10-15
State: B_CLIENTS is ~6% of XAU notional but 16-20% of tickets, and the small-ticket servers (Live 3/4/5) are ~5x the ticket count; 5% of trades are 78% of volume. Latency cancels on gateway5 (21-22 Sep) led to gateways 6-8 on trading-2, unexpected-fill-latency ceiling raised to 5000ms, dist9 added 2026-10-14. On 2026-10-15 dist6 saw 3,976 orders/s vs 235/s on the next busiest; Liam made config tweaks and CHG for an OZ-5 gateway latency fix (24G heap, 5 CEP threads) is booked Sat 17 Oct. Root cause of the 2026-09-21 XAU cancels (Nathan to GTC): a burst pushed internal processing past the last-look limit (overrun ceiling then 300ms, since raised), and OZ's hub rule re-routes to another maker after rejects, so no XAU orders reached Mahi for 60s (15:50:49-15:51:49Z) while GTC asked OZ about it; OZ-4/OZ-5 had shared a gateway, OZ-5 moved to its own ports 9016/9017 on 2026-09-28. On 2026-10-15 Isaac said GTC is already splitting flow more evenly inside OZ and should pass that on.
Next: GTC to confirm the rebalance across gateways (Isaac to chase); likely need 2 more servers for cent accounts and a cost conversation; dev review of latency cancels requested 2026-09-28.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1790591684124349 https://mahifx.slack.com/archives/C0AKRP8C049/p1790567720885579 https://mahifx.slack.com/archives/C0AKAPLU78W/p1792068184097149

### riskpath-stability — riskPath stalls, OOM crash-loops and yield-profile gaps
status: open · since: 2026-09-02 · last: 2026-10-15
State: riskPath OOM crash-looped on an unbounded analytics map (heap dumps filled disk and wiped logs, dumps now disabled); fix cherry-picked to release/26.3, process moved to trading-2/64GB then low-latency nodes (riskPathABook/BBook/MT split). Yield profiles were missing ~31% of XAU fills (9 Sep analysis) and classifier queries overloaded it (classification off for A and drop-copy profiles since 2026-09-11); 2026-09-24 YPs found not persisted to Pulse (Zendesk 23547). A "riskPath stall and overflow-crash fix" behind two flags (CHG-2610-MBV3) was self-approved by Liam and rescheduled on 2026-10-15 from 14:00-15:00Z to 12:15-14:45Z; no completion message seen yet.
Next: Isaac/Liam to confirm the 10-15 deploy landed; re-enable classification on A/drop copy once safe.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1788309377675289 https://mahifx.slack.com/archives/C0AKAPLU78W/p1792065637260039

### hedging-a-book — A Book go-live, STP rules and hedging structure
status: open · since: 2026-10-05 · last: 2026-10-15
State: A Book went live 2026-10-06 on one account, hedging via HRP markets only (hybridHedger markets switched from Finalto/Swift; Finalto/Swift still the two LPs in the hedger market, reason to be confirmed). 2026-10-12: flow from tag 52146947 was internalised though GTC expected STP to HRP; hedger cleared only 267oz, GTC closed 2100oz manually at HRP_MEX (avg 4177.43) and positions were adjusted in Compass. Thread outcome (resolved 2026-10-12): the hedger had bought 267oz (212 Swift, 55 Finalto), Mahi closed those and booked a 2100oz position adjustment at HRP_MEX 4177.43 to match GTC's manual close; tags 82025643 and 82025639 (moved to A Book 10-07/10-09, still STP to Mahi) were also switched to STP to HRP LPs. Kate told GTC to wait for Mahi to confirm STP whitelisting before routing a tag; the reason the hedger cleared only 267oz was still being looked at. 2026-10-14 GTC asked for percentage hedging split (A LP 30% / B LP 70%); Isaac replied a portion of a book's flow can go to a hedged book, split by counterparty, instrument or other factors, a new client with 1000-lot limit is being onboarded via risk-split from A, and hybridHedgerSI1/arbHedgerSI1 exist. HRP_SOLID and HRP_JANESTREET_FA streams added; SWIFT XCUUSD prices arrive per 100-unit lots (asked for per-unit).
Next: GTC to give the test-account counterparty so Mahi can test the new hedging book structure (asked 2026-10-15); agree the hedge-percentage setup with GTC; Swift to fix XCUUSD unit (Swift removed from reference markets 10-06, request logged on the wiki 10-12).
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1791202994256859 https://mahifx.slack.com/archives/C0AKRP8C049/p1792064520530769

### crypto-24x7 — Crypto onboarding and 24/7 sessions
status: open · since: 2026-09-15 · last: 2026-10-15
State: Crypto is next after gold. GTC's core BTC/ETH LP is Binance (pricing only; GTC confirmed it does not hedge or trade via it), so Mahi is connecting directly; the HRP Route28 connection was whitelisted both sides and confirmed established 2026-10-15 12:39Z. cryptoMarketData1 fails because Binance returns HTTP 451 for trading-1/2's Beeks public IP range (US-registered); Liam and Isaac agreed the preferred fix is to subscribe to Binance from mc-apnortheast-1 (same AWS region) and proxy it to mahi-central-ln via Fabric for London clients, rather than the Beeks egress ticket first proposed. Isaac proposed switching all A and B connections to 24/7 (Sat 10:59 to Sat 10:01 NY, 58 min server-reboot gap); B OZ-5 already runs it, GTC agreed an EOD restart 2026-10-16 17:00 NY. 24/7 XAUUSD is the upsell; a second London server cluster to stagger restarts was floated.
Next: get mc-apnortheast-1 consuming Binance and proxied to mahi-central-ln (Beeks egress ticket is the fallback); GTC to confirm session changes on PXM, Centroid and OZ 1-7; Mahi restart 2026-10-16 17:00 NY.
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1791975353055319 https://mahifx.slack.com/archives/C0AKRP8C049/p1792053281436189 https://mahifx.slack.com/archives/C0AKAPLU78W/p1791980737875259 https://mahifx.slack.com/archives/C0AKRP8C049/p1792064367521549

### oz-hub-connectivity — OneZero hub sessions, disconnects and tags
status: open · since: 2026-08-17 · last: 2026-10-15
State: GTC keeps adding OZ hubs because OZ fears it cannot handle their trade rate (7th hub requested 2026-10-09, in progress). Recurring session problems: OZ-2/OZ-3/OZ-4 hub drop-outs and "Session time ended" logouts (fixed by aligning all OZ sessions to Sun 17:00-Fri 17:30 NYT; OZ-4 outage 22-24 Sep fixed by a hub bridge restart), missing counterparty tags on OZ-4 (2026-09-08) and OZ PTR sessions disconnecting (2026-10-06, Mahi switched PTR analytics off). New-hub sessions needed whitelisting plus a cross-connect with several delays: OZ-6 (requested 2026-09-23) needed a Beeks NAT/routing change and was last pointed at the new ports on 10-06 with no confirmation in thread; OZ-7 (requested 10-09) details were sent 2026-10-14 and GTC acknowledged 10-15, needing an EOD restart; not yet confirmed connected.
Next: GTC to connect and confirm OZ-7 (and OZ-6 working) after the EOD restart; GTC weekly call is the forum.
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1786969418265589 https://mahifx.slack.com/archives/C0AKRP8C049/p1792050071553529

### pricing-skew-tuning — Skew, spread and last-look tuning
status: open · since: 2026-08-19 · last: 2026-10-15
State: Skew signal config tuned repeatedly: XAG ceilings lowered after quote "shake" complaints (09-09/10), IFMS leg removed from signal config 2026-10-07 for poor FX FI performance, arb protection and pre-triangulation spreads adjusted for wide FX crosses (09-29). Controls added: opening-window last look (800ms XAU, 400-500ms others) via CUSTOM1 timezone, indicative XAU pricing around open, 8 cent min TOB with news widening removed, XAU layers raised to 6. XAU spreads blew out into the Friday close (09-19) because BMSL/MWMS had only 3 benchmarks; MAHI_BENCHMARK_LDN added. 2026-10-12 GTC reported abnormal FX price spikes. 2026-10-15 GTC reported NZDJPY spread 3 JPY wide at the open because of SWIFT; Isaac removed SWIFT from arb protection, then found wide-spread suppression did not cover the custom execution timezone around the roll (B-OZ session saw wide spreads ~00:05-00:10 GTC time, now fixed). A dormant global force-indicative timetable (from April, possibly left over from a repurposed tmgm setup) that made all instruments indicative during roll was also removed. GTC also saw different spreads on GTC-B-Prices-OZ vs OZ-3 (cent hub); logs rolled off so not replayed.
Next: GTC to send tick data from both hubs for 23:55-00:15 their time so Isaac can confirm the OZ vs OZ-3 spread difference; Rory checking the 10-12 FX spike report.
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1788911767407019 https://mahifx.slack.com/archives/C0AKRP8C049/p1792082071865509

### centroid-connection — New Centroid LP connection
status: open · since: 2026-09-24 · last: 2026-10-13
State: GTC asked for a Centroid hub session (2026-09-24). GTC wants two Maker FIX connections for its Centroid bridge (backup over internet, primary over a Beeks X Connect/BGP); needs a separate distribution process (gateway8, ports 9020/9021). Centroid as taker resets sequence numbers on market data but not trade sessions. Beeks missed the first weekend window; Rory sent Centroid A/B credentials on 2026-10-13 and Marios acknowledged. Not yet confirmed working.
Next: GTC to connect and test A before B.
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1790236332277899 https://mahifx.slack.com/archives/C0AKRP8C049/p1791885592937159

### flow-rollout — Symbol and server migration to Mahi
status: open · since: 2026-08-17 · last: 2026-10-08
State: EURGBP moved 2026-08-17, then rolling in batches through 2026-10-05 (all FX majors/crosses, B Book). XAGUSD routed 2026-09-03 and XAUUSD 2026-09-10 with more servers added 09-16, 10-05 and 10-08 (mt4 live2). Remaining: cent accounts on small-ticket servers, indices (GTC worried about primary benchmark feed dropouts), crypto. Priorities per the 2026-09-24 Expo meeting: fix OZ hub drops, A Book with hedging, B Book via OZ, crypto, then 24/7 XAU.
Next: GTC picks the next server/day; weekly call 2026-10-13 notes remaining checks (24/7 connection 5, FX pair spikiness, HRP Jane Street).
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1786977281687209 https://mahifx.slack.com/archives/C0AKRP8C049/p1791442269445639

### commercial-value — Pilot value case and billing
status: watching · since: 2026-08-19 · last: 2026-09-29
State: Isaac's 2026-09-09 estimate: at 2.5 $/M LR and 4 $/M FI on XAU alone, billing reaches ~200k/month by January after the pilot (4M value-add on ~650B/month XAU). Kate cited ~$10/M skew PnL on drop-copy XAU flow (09-03). 2026-09-29 call KPIs: skew PnL on XAU, handling toxic HFT on A Book, 24/7 crypto uptime; upsell is 24/7 XAUUSD. OZ's fee waiver (quiet, not to be publicised) still stands.
Next: pilot end and billing terms to be confirmed outside Slack; downgraded to watching, no discussion since 2026-09-29.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1788950931799769 https://mahifx.slack.com/archives/C0AKAPLU78W/p1790674407124919

### infra-disk-alerting — Trading-server disk, replica and alert hygiene
status: open · since: 2026-08-10 · last: 2026-10-14
State: vg03-mysql extended repeatedly (trading-1/2 +200G on 09-10; trading-2 +50G on 09-30 with no more room in the vg, ZD 23574); a manual replica restore started 2026-10-01 was slow (two backups clashing, only reached 17 Sep after 3h) and was killed 10-02, the slave was reported back by 10-05, and nightly backup was switched off with bigger buffer pools (CHG 10-14) to help catch-up. The OneZero analytics drop copy (analyticsFixServerOZ1) was removed and stopped on trading-1 on 2026-10-05 for load reduction (revert commit to restore). The `mysql_optimize_enable=false` question from 2026-08-10 never got a reply. PD tuning: fiPnlDrop raised to alert severity, hedging-book alerts off until a hedger is live, fixOrders1 spam stopped.
Next: someone to answer the mysql_optimize_enable question and decide longer-term DB sizing.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1790734299323199 https://mahifx.slack.com/archives/C0AKAPLU78W/p1790870773608959 https://mahifx.slack.com/archives/C0AKAPLU78W/p1791980456302469

### compass-client-support — GTC's use of Compass, Echo and Pulse
status: watching · since: 2026-08-17 · last: 2026-10-13
State: Weekly Tuesday 10:00 UK call set up 2026-08-17. GTC asks about order CSV export in USD (fixed in the 25 Aug dashboard deploy), MT4/MT5 servers missing from yield profiles, price-forensics limits and classifier tag export. Pulse creds and spec passed to Manglai 2026-10-13 (Zendesk 23640).
Next: none outstanding.
Refs: https://mahifx.slack.com/archives/C0AKRP8C049/p1787663421577319 https://mahifx.slack.com/archives/C0AKRP8C049/p1791901914330729

### finalto-fix-noise — Finalto execution reports for non-Compass orders
status: closed · since: 2026-09-03 · last: 2026-09-21 · closed: 2026-10-15
State: Finalto sent fills for orders not placed via Compass on the GTC_Global5 session, spamming PD and forcing fixOrders1 off. Finalto removed the unwanted reports 2026-09-21 and Daria restarted fixOrders1.
Refs: https://mahifx.slack.com/archives/C0AKAPLU78W/p1788407276578049 https://mahifx.slack.com/archives/C0AKRP8C049/p1789969699635569

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
