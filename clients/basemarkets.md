---
slug: basemarkets
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/basemarkets.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: basemarkets
  hosts: ../MahiProduct/data/client-hosts.json          # entry: basemarkets
  wiki: ../MahiProduct/wiki/clients/base-markets.md
channels:
  internal-base-markets: C09D05EPCTV
  mahi-base-markets: C09D8V41JAG
contacts:
  - {name: "Alex Kolpokchi", role: "Base Markets CEO; primary client contact (algo / flow, Tegis relay)", confidence: low}
  - {name: "Kate B", role: "Base Markets - client contact (A book hedger, LMAX/Scope accounts, group codes)", confidence: low}
  - {name: "Aytugan Khafizov", role: "FastMT/Tegis - integration contact (Centroid setup, TEM config)", confidence: low}
  - {name: "Anatoly", role: "Base Markets / Tegis - sign-off contact for TEM switch", confidence: low}
last_catchup: 2026-10-26T08:04:59Z
status: active
---

## Now
Tegis (Base's main flow) is paused for algo testing: hybridHedgerC1 is off and being removed from hiera, and Tegis now wants only a FIX 4.4 price feed from Mahi while trading through MT5's own API (agreed 2026-10-20; Mahi sent pricing connection details 2026-10-21, awaiting Base's IP for whitelisting). Base has decommissioned MT4; Mahi has asked to remove the MT4 bridge connections. Two LMAX_2 fills Base placed outside Compass (AUDUSD, XAGUSD) need Compass positions corrected. XAU hedging on the A book was retuned 2026-10-08 after repeated overnight PnL drops from account 111125, and brokered-XAU slippage is being monitored after the $20/M markup was removed.

## Streams

### lmax2-offsystem-fills — LMAX_2 fills placed outside Compass, positions out of sync
status: open · since: 2026-10-21 · last: 2026-10-22
State: Nathan Burch told Base on 2026-10-21 that two LMAX_2 fills (AUDUSD sell 7,000 on 10-21, XAGUSD buy 500oz on 10-15) did not come from Compass orders, while Compass shows both instruments flat at A_HOUSE with offsetting SCOPE_B positions. Kate (Base) replied 2026-10-22 that the trades were placed outside Compass and that LMAX_2 and SCOPE_B both hold zero in both instruments. Compass has not yet been adjusted to match.
Next: Mahi (Nathan Burch / Kate Stagg) to correct Compass positions for AUDUSD and XAGUSD at LMAX_2 and SCOPE_B.
Refs: https://mahifx.slack.com/archives/C09D8V41JAG/p1792620629451529 https://mahifx.slack.com/archives/C09D8V41JAG/p1792653037394839

### tegis-mt5-api — Tegis moving to MT5 API trading with Mahi price feed only
status: open · since: 2026-04-29 · last: 2026-10-21
State: Direct-API ask began 2026-04-29 (Alex asked about piping trades off MT4/MT5; Mahi has FIX but no margin or credit checks). Call held 2026-09-04: Tegis wanted off the MT5 EA/copy-trading setup, Mahi gave no timelines. On 2026-10-14 Alex said Tegis will trade via MT5's API (MT5 handles balances, rejections, no coverage account) and need only pricing from Mahi. Kate Stagg replied Mahi can give a FIX 4.4 price connection plus a conformance environment to build against; internally she asked whether Tegis could take prices from MT5's API since Mahi has no API clients today. Tegis's proposed workflow (FIX 4.4 pricing to its algo, orders via MT5 API into a Base MT5 account, hedging via Mahi into LMAX as today) was posted in the client channel and Kate Stagg accepted it 2026-10-20: the only change on Mahi's side is the new pricing connection. Kate Stagg posted the FIX pricing connection details in the client channel on 2026-10-21 (credentials are in that message; not copied here). FastMT (Aytugan) also asked whether the Mahi gateway executes orders initiated from MT5 Manager (Dealer); Kate Stagg confirmed it is supported.
Next: Base/Tegis to give the IP for whitelisting and connect to the price feed.
Refs: https://mahifx.slack.com/archives/C09D05EPCTV/p1777470115067619 https://mahifx.slack.com/archives/C09D8V41JAG/p1788345375042849 https://mahifx.slack.com/archives/C09D8V41JAG/p1792572631430259

### group-additions-1019 — Base requests for new A/B book MT groups in Compass config
status: open · since: 2026-10-19 · last: 2026-10-21
State: Recurring request type. On 2026-10-19 Kate (Base) asked for three A book and four B book USD MT groups, done the same day. On 2026-10-21 she asked for two more A book groups and one B book group; no Mahi reply seen yet.
Next: Kate Stagg to add the three groups to config and confirm.
Refs: https://mahifx.slack.com/archives/C09D8V41JAG/p1792404682249699 https://mahifx.slack.com/archives/C09D8V41JAG/p1792597504276599

### xauusd-1000oz-tob — Suffixed XAUUSD symbol with 1000oz top of book for a larger client
status: open · since: 2026-10-13 · last: 2026-10-21
State: Kate (Base) wants a suffixed XAUUSD symbol for a larger client wanting 1000oz TOB. On 2026-10-16 Kate Stagg said Rory will set up a new XAUUSD-only pricing model replicating LMAX_2 tiers (1000oz TOB; LMAX being asked to switch feeds) with markup, streamed under a suffix via MCC to one Base client. Change CHG-2610-DYQM (two pricers for a new full pricing model) was approved 2026-10-21 and Rory bounced restAdminServer1 and dashboardGateway to pick it up; likely this model, not confirmed in-channel.
Next: Rory to finish the pricing model; LMAX feed switch.
Refs: https://mahifx.slack.com/archives/C09D05EPCTV/p1791886072967149 https://mahifx.slack.com/archives/C09D05EPCTV/p1792573543784969

### tegis-book-pause — Tegis C book warehoused while Tegis tests algo/API
status: open · since: 2026-05-18 · last: 2026-10-13
State: Tegis flow runs through the Compass-managed C book hedged to LMAX (positions migrated 2026-06-29; VIP zero-spread prices via CLIENT_PRICE_VIP_LDN routed to C_CLIENTS). Tegis closed out positions around 2026-10-02 to change algos, and on 2026-10-13 asked for the book to be warehoused while they test. Kate Stagg turned off hybridHedgerC1 with startInOffState=TRUE, then said she is stopping it and removing it from hiera; it must not be turned on until testing is done and positions are flat.
Next: Tegis to say when they go live again; re-add hybridHedgerC1 to hiera then.
Refs: https://mahifx.slack.com/archives/C09D05EPCTV/p1782780254069969 https://mahifx.slack.com/archives/C09D05EPCTV/p1791885596379839 https://mahifx.slack.com/archives/C09D05EPCTV/p1791886158813629

### mt4-decom — Base decommissioned MT4; Mahi removing MT4 bridge connections
status: open · since: 2026-10-11 · last: 2026-10-13
State: Shyam Hari saw SYNAPSE_MT4 disconnected on 2026-10-11; Kate (Base) confirmed 2026-10-13 that MT4 is decommissioned. Shyam asked whether Mahi may remove the primary and backup MT4 bridge connections; no reply yet.
Next: Base to confirm nothing still needs the MT4 bridge; then Mahi removes both connections.
Refs: https://mahifx.slack.com/archives/C09D8V41JAG/p1791755009916399 https://mahifx.slack.com/archives/C09D8V41JAG/p1791925041012299

### brokered-xau-slippage — Slippage on brokered XAU fills; markup removed
status: open · since: 2026-10-02 · last: 2026-10-07
State: XBTUSD orders were cancelled 2026-10-02 because brokered flow priced outside the limit; fixed with local crypto in LIQUIDITY_POOL_LDN and a temporary A BOOK rule. On 2026-10-06 Kate (Base) complained of slippage on small XAU trades (200479). Kate Stagg's analysis of 2,096 brokered fills found median $29/M worse than published, mostly the $20/M brokering fee; LMAX_2 was added to LIQUIDITY_POOL_LDN, liquidityPoolSOR1 bounced, and Base removed the $20/M markup (replay: median $0/M, ~$7.8k/week back to clients). Price improvement still off on A BOOK profiles.
Next: Kate Stagg to check real fills after Athena catches up and again after a week (about 2026-10-14); no result posted yet.
Refs: https://mahifx.slack.com/archives/C09D8V41JAG/p1790957952350349 https://mahifx.slack.com/archives/C09D8V41JAG/p1791281610611709 https://mahifx.slack.com/archives/C09D05EPCTV/p1791385257726699

### xau-hedging-tuning — A book XAU hedging losses and hedger retuning
status: open · since: 2026-08-10 · last: 2026-10-08
State: Recurring A book PnL drops from large internalised XAU tickets (111319 $6k 2026-09-18; 111125 ~$8.7k 2026-09-29 with 1,960oz in one second; ~$3k and ~$4k 2026-10-08), driven by slow hedging. Fixes so far: LMAX_2 brought in as primary venue beside SCOPE_B (Scope kept as backstop after Scope blacklisting/cancel problems in August), dynamic execution rules enabled for Broker-classified tag, VAR-CLEARANCE-OVERNIGHT-LARGE rule (50oz floor), and on 2026-10-08 the SCOPE_B static adjustment removed, a 30s dynamic fill-ratio adjustment added and 10 pip tolerance on the overnight rule. 111125 whitelisted to A BOOK Broker list as a stopgap. Monitoring.
Next: Watch overnight XAU unwinds after the 2026-10-08 retune; decide whether to un-whitelist 111125.
Refs: https://mahifx.slack.com/archives/C09D05EPCTV/p1786349367512409 https://mahifx.slack.com/archives/C09D05EPCTV/p1790644032875939 https://mahifx.slack.com/archives/C09D05EPCTV/p1791454047171069

### a-book-hedger-netting — Base switches A book hedger off while netting LP positions
status: watching · since: 2026-09-04 · last: 2026-10-15
State: Kate (Base) repeatedly turns the A book hedger off to net LP positions manually (2026-09-14, 09-22, 10-09, 10-15; back on within ~20 minutes on 10-15). Manual hedge trades through LP GUIs bypass Compass, so positions then need correcting in Compass (SCOPE_B buy 510 / LMAX_2 sell 407 XAU on 09-22). On 2026-09-22 Base asked to route all A book hedging to LMAX_2.
Refs: https://mahifx.slack.com/archives/C09D8V41JAG/p1790055333398639 https://mahifx.slack.com/archives/C09D8V41JAG/p1792073335429129

### admin-server-reboots — Admin server failing to return after weekend restarts
status: watching · since: 2026-06-07 · last: 2026-09-07
State: Admin server did not come back after weekend restarts on 2026-06-07, 2026-08-16 and 2026-09-06 (Beeks tickets; the 09-06 case needed a previous-kernel boot and the new kernel may fail again). PricerVIP1/2 were also restored after the 09-06 restarts. No fresh outage since 2026-09-07.
Next: Dev-infra to address the kernel boot failure; Beeks reboot autonomy procedure (Liam Cordelle) not confirmed.
Refs: https://mahifx.slack.com/archives/C09D05EPCTV/p1780822809497359 https://mahifx.slack.com/archives/C09D05EPCTV/p1788787318138619

### ld-network-incident — Beeks LD campus network incident, Base disconnections
status: closed · since: 2026-10-16 · last: 2026-10-16 · closed: 2026-10-19
State: On 2026-10-16 Base reported disconnections and no Compass login. Liam Cordelle announced a networking incident across Beeks' whole LD campus, saw recovery by 11:46 BST and confirmed resolved at 12:29 BST.
Refs: https://mahifx.slack.com/archives/C09D8V41JAG/p1792143013486049 https://mahifx.slack.com/archives/C09D8V41JAG/p1792150197114369

### mt5-bridge-licence — MT5 Bridge licence renewal on Base backup server
status: closed · since: 2026-10-08 · last: 2026-10-08 · closed: 2026-10-15
State: Arun Patel sent a new licence; Yuliya Dziurayeva (FastMT) confirmed it installed successfully the same day.
Refs: https://mahifx.slack.com/archives/C09D8V41JAG/p1791450091502369 https://mahifx.slack.com/archives/C09D8V41JAG/p1791465228493509

## Arc
- 2026-04 — Base Markets onboarding Tegis flow; Tegis/Centroid FIX integration begins
- 2026-05-11 — Distribution FIX credentials sent; Centroid workaround adopted for MT4/MT5 zero-spread split
- 2026-05-21 — First LMAX end-to-end test trades confirmed
- 2026-06-16 — Tegis goes live on copy-trade setup
- 2026-06-29 — Tegis positions migrated; C book with LMAX hedging live
- 2026-08-07 — Fast hedging live on FX/CFD A book for Base's -S accounts; R group phasing into S
- 2026-08-26 — Tegis grid paid $93.6k C book gain on data print; Tegis plug-in in use
- 2026-09-29 — ~$8.7k A book loss from 111125; overnight clearance rule added
- 2026-10-13 — Base decommissions MT4; Tegis book paused for algo/API testing
- 2026-10-16 — Beeks LD campus network incident disconnects Base for about 2 hours
