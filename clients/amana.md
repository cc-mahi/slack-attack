---
slug: amana
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/amana.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: amana
  hosts: ../MahiProduct/data/client-hosts.json          # entry: amana
  wiki: ../MahiProduct/wiki/clients/amana.md
channels:
  internal-amana: C08T42TMKU3
  mahi-amana: C08SYSMP0EB
contacts:
  - {name: "Karen Montero", role: "ops / test trading liaison"}
  - {name: "Nikos", role: "primary desk contact: skew, LR, roadmap, escalations"}
  - {name: "Princess Rosete", role: "test trading / ops liaison"}
  - {name: "Hadeel Salah", role: "dealer / ops: go-lives, positions, spread config, order queries", confidence: low}
  - {name: "Mohamad El Masri", role: "ops: manual hedging, position adjustments", confidence: low}
  - {name: "PH NOC (Jake Denley Alvaro, Maynard Notario, John Carlo Desierto et al)", role: "monitoring, rejections, pre/post checks", confidence: low}
  - {name: "Andreas Kleanthous / Mohamad Malkani / Rafik Mansour", role: "ops: futures expiry/start notices", confidence: low}
  - {name: "Omar Maatouk", role: "ops: pricing / hedging config, LP NOP", confidence: low}
  - {name: "Ali Wehbe / Ahmad Hashem", role: "ops: energy futures specs; Mahi_B rejection reports", confidence: low}
last_catchup: 2026-11-26T08:12:52Z
status: active
---
## Now
11-21 weekend outage: CFD and crypto sessions were down about 12:00-15:20 UTC Saturday after the weekly reboot (gateways dist3/HP4 did not relaunch, HZ-003); RCA given 11-23, startup fix and reboot-timing change pending; Amana NOC chased for hours with no weekend support answering.
Amana is migrating everything onto Mahi in stages. Nikos drives, escalates fast.
11-23: hot-hot failover (second Compass in AWS London) needs Centroid dedicated AWS link, Nikos to ask; energies-roll hedger hold-back pending.
Open: NFP LR-off review (no owner), TRADEVOLUME reset bug, NDXUSD price flip, DAXFUT-Z spread, IG NOP/commission, manual-intervention protocol.

## Streams

### hedger-offhours-rejects — Hedger sending orders outside session hours
status: open · since: 2026-11-13 · last: 2026-11-26
State: 11-26 PH NOC saw D30 "out of session" rejects: Mahi hedge orders on G30 hit CMC's 02:00-02:15 UTC break; no CMC session times are configured and CMC published a stale price until a filter dropped it after 10 minutes. A per-instrument session override is possible (offered for G30EUR, Nikos undecided); per-market override raised with Dev. 11-23 CL1USD orders rejected during the energies roll: a valid IG_CENTROID quote was not cancelled; Daria to make the hedger hold back during the roll. 11-13 USDCHF rejects; William filed CHG-2611-Y8P9 (11-16) to stop G8 weekend orders.
Next: Nikos to decide on the G30EUR override; Dev on per-market sessions; William to apply the weekend change; Daria to implement the roll hold-back.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794607758054459 https://mahifx.slack.com/archives/C08SYSMP0EB/p1795668853553909

### delay-rule-client — Removing a lone client from the 500 ms delay rule
status: open · since: 2026-11-24 · last: 2026-11-24
State: 11-24 Masri could not remove a client from the 500 ms delay because he is the only client on that rule; Nikos then put the client on another profile (08:06 UTC). No Mahi reply yet.
Next: Mahi to advise how to empty/remove the rule.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1795506928637669 https://mahifx.slack.com/archives/C08SYSMP0EB/p1795507614464439


### weekend-reboot-outage — Gateways not relaunching after the weekly reboot (CFD/crypto down 11-21)
status: open · since: 2026-11-21 · last: 2026-11-23
State: Sat 11-21 about 12:00 UTC the Amana bridge got no response on reconnect to the CFD and crypto sessions (MAHI_A_HP_CFDCRY_LIVE; CFDCRYPTO second sessions); PH NOC and Omar chased from 12:55 UTC with no answer for about 3 hours; Inald restarted the gateways, sessions back about 15:20 UTC. 11-23 Daria gave the RCA: after the weekend reboot (~11:45 UTC) clientDistributionGateway3 and HP4 failed building B_CRYPTO_CLIENTS (Hazelcast lock timeout, then "Consumer for 806 already registered", HZ-003) and exited unrelaunched; only CLIENT_PRICE_BETA_LDN is in-band, CLIENT_PRICE_CRYPTO_LDN is still on Hazelcast. David Cooney floated weekend support for Amana; Daria offered moving the reboot to just before Sunday checks.
11-23 Will reviewed it with Nikos, who asked about hot-hot failover; engineering's option is a second Compass instance in AWS London (eu-west-2), needing a dedicated Centroid link into AWS (Equinix Fabric/Megaport or a Direct Connect cross-connect); Liam drafted the ask for Nikos to put to Centroid.
Next: Nikos to ask Centroid for dedicated AWS connectivity; Engineering to make gateways self-recover; Liam to decide on in-band rollout for Amana; Amana to reply on reboot time; David to raise weekend support.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1795277723540489 https://mahifx.slack.com/archives/C08T42TMKU3/p1795430924104739


### ig-xau-hedging — IG_CENTROID as a metals hedge venue
status: open · since: 2026-11-03 · last: 2026-11-25
State: 11-25 06:30 UTC Masri asked for another internal XAUUSD position adjustment; Isaac picked it up 08:02 (outcome not yet seen). 11-20 Omar had IG client-net XAUUSD corrected again (110.13 vs 50.13 lots at the LP): -60 lots booked internally, nothing sent to IG. 11-17 Masri had IG_CENTROID -5,500 oz and CMC_CENTROID +5,500 oz adjusted likewise. 11-16 Nikos asked to enable IG for XAGUSD aggregation on the non-swapfree account; Kate asked whether for hedging or price formation (unanswered). IG_CENTROID is a metals hedge LP (regular account only); Isaac enabled it for A-book XAU hedging 11-05 with a temporary max position pending IG NOP/margin. Omar asked whether per-LP commission can feed aggregation (Daria checking).
Next: Nikos to answer Kate (XAGUSD hedging vs pricing); Mahi (Daria) to answer Omar on LP commission in aggregation.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793784345213029 https://mahifx.slack.com/archives/C08SYSMP0EB/p1795588225642219


### vip-feed — Third (VIP) pricing feed for XAU/XAG, now A_CLIENTS_VIP channel
status: open · since: 2026-10-08 · last: 2026-11-20
State: CLIENT_PRICE_VIP_LDN pricers added 10-08 (CMC only from 10-14). 11-19 Nikos moved a large returning client onto the A_CLIENTS_VIP channel; Nathan: it shares the VIP feed (depth/spread not per-channel; a channel markup or new feed is needed), set riskSplitting on A_CLIENTS_VIP. 11-20 the feed rounded up to 9c, Isaac traced it to a leftover fat-feed BMSL multiplier and fixed it; Nikos moved the client on at 08:35 UTC. CMC and LMAX TOB referenced at 100oz, published at 500oz. 11-19 (internal) VIP session was on Dist1 only, which since the 11-18 Dist3 move carries FX and metals, so VIP NDX futures rejected; fix is a VIP_CLIENTS_CFD session on A_CLIENTS_VIP plus a Dist3 restart at the 17:00 NY break.
Next: Rory to add the VIP_CLIENTS_CFD session and Dist3 restart; Mahi to adjust depth/spread after Nikos's tuning.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1791457134754879 https://mahifx.slack.com/archives/C08T42TMKU3/p1795084157976699


### futures-expiry-recs — Futures rolls, expiries and position adjustments
status: open · since: 2026-08-17 · last: 2026-11-25
State: 11-25 Rafik gave notice of GC6Z and SI6Z (Dec) settlement; Nathan flattened both in Compass by 21:08 UTC. 11-20 Andreas gave notice of CM6Z settlement; Masri confirmed it is the December corn contract, not live on Mahi, so no action. Amana posts expiry and start notices and Mahi zeroes positions at EOD, re-subscribing new contracts on Mahi_CMC_FIX. 11-17 Andreas announced CrudeOilZ6 settlement (Daria: no open position) and Mohamad Malkani said CrudeOilG7 and SI7H start 11-18; Daria switched the subscriptions and scheduled EOD restarts to pick them up.
11-19 Masri reported hedging on the wrong symbol after SI7H was enabled: XAGFUT-H was not remapped from the P to the W futures hedger profile at EOD. Rory remapped it, restarted the hedgers and netted the mismatch at CMC (10,250oz) by 16:09 UTC.
Next: Mahi to check futures contract rolls are fully remapped at EOD; Daria to confirm CrudeOilG7 is live.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786993422025149 https://mahifx.slack.com/archives/C08SYSMP0EB/p1795637173171259


### si-books — SI energies and SI indices books
status: open · since: 2026-08-17 · last: 2026-11-18
State: Energies SI live 09-11 (4h, 500K VaR); indices SI 09-25 (4h, 100K VaR). SI PnL went blank repeatedly; permanent fix MahiMain#1203 deployed 10-29 (CHG-2610-TXKS). 11-04 energies lost about $110k in minutes (see manual-intervention). MXN SI go-live 11-05 (CHG-2611-749Q, 50k VaR). 11-18 SI net book PnL stuck from the morning, believed due to a new oil futures contract; Rory bounced riskReportingCore1.
Next: confirm indices PnL shows at Monday's open and the riskReportingCore log shows the Graphite last-mids load line.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786981181951769 https://mahifx.slack.com/archives/C08T42TMKU3/p1795014015075649


### client-tag-passthru — Client login tag for CMC dynamic logins
status: open · since: 2026-09-28 · last: 2026-11-25
State: 11-25 Nikos could not find markouts per tag in Yield Profiles; Isaac: the tag 58 value is stored in Pulse as Comment on yieldprofiles, but only on B_CLIENTS_LDN (the pre-risk-split order), not carried to B_FX_CLIENTS_LDN, though present in SWAPFREE_CLIENTS_LDN. CMC needs dynamic FIX API client logins, so Amana wants to send them on tag 109 and have Mahi consume and echo them. Execution reports do not return 109 today (Rory 09-28); 11-02 Karen asked about a "tag 90017 plan", none visible. 11-03 Amana tested tag 58 (sub-login), live for one client; Rory: stored per order in Compass comments, not passed to CMC. 11-18 Karen enabled tag 58 sublogin for Mahi analytics and asked whether the new return tags are available; Rory to test 109=222.
Next: Mahi to say whether tag 109 (or 90017) can be consumed and returned; Amana to extend tag 58 to more clients/instruments.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790602136754039 https://mahifx.slack.com/archives/C08SYSMP0EB/p1795602679174819


### gold-hedger-params — Gold B-book hedge/unhedge parameters
status: open · since: 2026-11-18 · last: 2026-11-18
State: 11-18 Masri asked why gold B-book hedging and unhedging felt slow. Rory: hedging starts above 15M USD XAU notional and immediately above about 18M; unhedging starts once LP exposure exceeds client exposure, straight away if bigger by roughly 100-160 oz (moves with volatility), else after 5 minutes of staying bigger. Masri's screenshot net -136 oz meant nothing to unhedge; Masri accepted.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1795012985651829 https://mahifx.slack.com/archives/C08SYSMP0EB/p1795016416372829


### cp-39001415-lr — Counterparty LR for a bursty XAUUSD client (39001415)
status: open · since: 2026-11-17 · last: 2026-11-17
State: 11-17 Nikos asked for a custom LR profile for client 39001415: aggressive limit-order flow with bad 5s markouts, worst in sustained bursts; nothing to be added before he discusses it. Rory offered options: B (his ask) burst 2,000,000 then 2,000,000 per 10,000 ms, or A burst 1,000,000 then 125,000 per 500 ms; internally Rory recommends B, Will Carter notes it degrades the client's execution (could tell Nikos to speak to his LP). Nikos will discuss internally on 11-18.
Next: Nikos to choose A or B (or neither); Mahi implements only on his confirmation.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794923308374639 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794943129736329


### last-look-tuning — Last look and TP slippage
status: open · since: 2026-08-20 · last: 2026-11-20
State: 11-20 a client's EURUSD fill took 500ms; Rory: he is in the manual arber selection of the B-book execution rule, which has a 500ms last look. Clients complain about slipped TP limits and Nikos wants last look cut from 50ms to 25ms then 10-15ms via the execution profile (Nathan checking for a lower limit, no answer seen). 11-16 an XBTUSD buy limit cancelled at 150ms (ABOOK Cryptos rule value); client price missing in price-forensics (VWAP-for-quantity fault, raised internally).
Next: Nathan to confirm minimum last-look setting; William to raise the VWAP price-generation issue internally.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787200767810479 https://mahifx.slack.com/archives/C08SYSMP0EB/p1795190587378189


### fx-hedge-pool-nop — FX exotic hedging pool, NOP and hedger stalls
status: open · since: 2026-11-10 · last: 2026-11-13
State: 11-10 USDTRY A-book hedger blocked (CMC too wide); Nikos and Omar agreed LMAX for all FX with 5M NOP on MXN and TRY (Omar talking to LMAX), actioned. Nikos asked for a max-spread alert. 11-13 residual TRY/MXN exposure explained by Nathan: A-book hedger clips 50k USD with a 50k minimum position, so the VaR trigger fired but sent no order.
Next: Mahi to decide whether to lower the 50k clip/minimum on USDTRY/USDMXN and finish explaining normal quantity to Nikos; Isaac to add the max-spread alert; Mahi to confirm LMAX NOP limits for exotics once Omar hears back.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794312795036509 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794546126185519


### ndx-price-flip — NDXUSD / NDXFUT price flipping, wrong client price
status: open · since: 2026-11-12 · last: 2026-11-12
State: 11-12 Nikos asked Mahi to look at an NDXUSD distribution-HP fill (yield-profile view) and said Mahi's price was wrong. Nathan found the price switching back and forth was unintentional and is hunting the root cause; Hadeel asked whether the previous day's move of all indices to the new Maker sessions is related and later said NDXFUT has the same issue (price-forensics view). Nikos is out most of the day; Hadeel is the contact.
Next: Nathan to report the root cause (and whether it relates to the 11-11 index session move) to Hadeel/Nikos.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794458187874679 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794468307057449


### spread-widening-check — Is the illiquid-hours spread widening still enabled?
status: open · since: 2026-11-11 · last: 2026-11-11
State: 11-11 Nikos asked Mahi to investigate spread widening during illiquid hours back in August. He knows it is an algo feature protecting against arbers on sudden moves but does not remember whether it is still enabled or whether the maximum widening was reduced. Rory acknowledged and will look.
Next: Rory to check the current widening feature and its max-spread cap and reply to Nikos.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794384286346449 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794384343189959


### xpt-xpd-exposure — XPT/XPD A-book exposure stuck (hedger blocked)
status: open · since: 2026-11-11 · last: 2026-11-11
State: 11-11 Masri flagged XPD/XPT A House exposure. Rory: built up since pricing moved to Jump-only 10-07, as Jump's spread (about 2.4 XPT, 6.7 XPD) exceeded the hedger's max distance from mid. Cleared 10:42 UTC after fixes and restarts; Rory set a separate XPD/XPT hedging profile and raised minor-metals backstop spreads. Nikos's why-stuck question unanswered.
Next: Rory to answer Nikos's last question and add alerting for a persistently blocked hedger; further hedger-rule review.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794385645413669 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794400320702809


### gateway-split — Distribution gateway split (dist3 / HP dist4)
status: open · since: 2026-10-23 · last: 2026-11-25
State: 11-25 Isaac called the instrument split complete and began dropping the gateway throttle from 1/10ms to 1/8ms, aiming for 1/5ms or 2/10ms. Plan (CHG-2610-TRFK): FX and Metals stay on dist1/HP dist2; Crypto, Indices, Energies and futures move to dist3 and HP dist4. CFDs and cryptos switched 11-05, oils and gas 11-06, all indices and crypto 11-11 (only metals and FX still on the originals). Karen asked about removing a Mahi-side pricing throttle and disabling CFD/crypto on old sessions (no answer seen). Hadeel suspects ndx-price-flip relates to the index move.
Next: Rory to answer Karen; Isaac to remove migrated symbols from dist1/HP dist2 at an EOD restart and keep stepping the throttle down.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792765304547529 https://mahifx.slack.com/archives/C08T42TMKU3/p1795598397306789


### dax-spread-vs-cmc — DAXFUT-Z spread wider than CMC
status: open · since: 2026-11-10 · last: 2026-11-10
State: On 11-10 Nikos said CMC is the main LP for DAX futures but Mahi's client spread does not follow CMC; Rory saw a different comparison on his side, then Nikos posted a 06:45-07:00 UTC Light-vs-CMC spread CSV/HTML (Mahi significantly wider, now also seeing 60). Same morning he asked Mahi to act as clients are complaining about the spread.
Next: Rory to investigate the DAXFUT-Z spread config against CMC and reply.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794297408817199 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794297567238929


### fx-bbook-roll-pnl — FX B-book PnL differs Friday close vs Sunday roll
status: open · since: 2026-11-09 · last: 2026-11-09
State: Nikos noted FX B-book at -28.9K from Friday close vs -17.4K at the Sunday 11-08 roll. Rory: Friday close is correct; the Saturday server restart reloaded weekend prices from Friday's average instead of the close, shifting the book about -11.5k on paper and so the roll figure. Raised internally for review.
Next: Mahi to decide whether to fix weekend price reload after restart and update Nikos.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794238430106659 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794240841128049


### ibxeur-precision — IBXEUR rejections at Jump (1dp prices)
status: open · since: 2026-11-09 · last: 2026-11-09
State: 11-09 IBXEUR rejections (E35EUR first reported); Rory: fills at JUMP_CENTROID, which accepts only 1dp prices. Rory agreed to change the config (min/step size 1) by EOD.
Next: Rory to confirm the IBXEUR precision change was applied.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794228473570299 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794233939269029


### analytics-data-asks — Yield profiles, party IDs and data access
status: open · since: 2026-08-17 · last: 2026-11-09
State: 11-09 Nikos found TRADEVOLUME in riskreportingmetrics resetting after a restart; Nathan: no volume lost, gave workaround queries, creating a dev ticket; skew PnL (PRICINGBENCHMARKMIDLIFETIMEPNL) same-issue question unanswered. Nikos also asked to confirm fixed-price fee YTD (1.83 RPM, 1 Jan-30 Oct); Isaac: B_GOLD_CLIENTS_LDN double counts B_CLIENTS_LDN.
Next: Isaac to confirm the FP YTD figure excluding the B_GOLD double count; Nathan to file the TRADEVOLUME ticket and answer on skew PnL.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786982712342769 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794221465833699


### nfp-lr-review — NFP 11-06: LR off and negative skew on gold
status: open · since: 2026-11-06 · last: 2026-11-06
State: Internal (Will, 11-06): through NFP (13:30-13:33 UTC) Amana earned close to nothing while other clients made real LR: B_CLIENTS_LDN $28M with LR $0, CLIENTS_LDN $9M and SWAPFREE $8M, LR $42 in total, skew about -$721 net. No owner yet;
Next: owner needed: confirm whether LR is off by design on the B and swapfree books or a gap (lr-health-check), sim a stronger or adaptive skew (skew-health-check), scope PSM for gold, and check the open XAUUSD A-book override issue CARTER-1000.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1793977507421709


### ng-depth-feed — Natgas client depth (TOB only) on the light feed
status: open · since: 2026-11-06 · last: 2026-11-06
State: 11-06 Karen and Hadeel reported NGXUSD and NG futures reaching Centroid as top of book only, though Mahi pricing shows full depth. Fix CHG-2611-JMEA (full client depth) was set for Sat 11-07 11:25-11:59 UTC; no client confirmation seen.
Next: Amana (Karen/Hadeel) to confirm depth now arrives; Rory to confirm the change went through.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793972045779729 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793981700994789


### manual-intervention — Manual risk transfers and desk processes
status: open · since: 2026-11-04 · last: 2026-11-05
State: 11-04 the SI energies book (CL) went +20k to -90k around 16:30 UTC on headlines; total VaR breached and Mahi triggered a manual risk transfer 16:37 UTC (about $177k saved). 11-05 Nikos asked what triggered it and wants a defined manual-intervention process; Isaac and Will plan a protocol and failover runbooks; a news calendar is a gap.
Next: Isaac to send Nikos the energies VaR and saving; Mahi to draft the manual intervention protocol with Nikos.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1793811329971989 https://mahifx.slack.com/archives/C08T42TMKU3/p1793865062079869


### min-size-rejects — Below-minimum reject storms after quantity-rule changes
status: open · since: 2026-11-01 · last: 2026-11-04
State: 11-03 hedger CMC crypto rejects (BTCUSD rule 0.001 vs CMC 0.005); Nathan reverted definitions; true CMC minimums unresolved. 11-01 1,498 rejected AVAXUSD 0.01 orders to GCEX (10-30 quantityDefinition rule overrode the real 0.1); Daria switched the crypto hedge book OFF, stayed off (about 6k VaR unhedged).
Next: Amana to get CMC's real crypto minimums/increments; Isaac to confirm GCEX's AVAX minimum, fix the 10-30 rule, and confirm the crypto hedge book is back ON.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793513045608259 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793747127837329


### crypto-rollout — Crypto go-live and hedging
status: open · since: 2026-08-17 · last: 2026-11-04
State: First cryptos live 09-04, BTC 09-21, seven GCEX coins 10-01. Amana's risk committee decided 10-21 to stop trading with GCEX; Cameron Hughes moved crypto hedging and pricing to CMC_CENTROID by 11-04 (GCEX flat, GCEX-PRIMARY removed from pools and mappings). CMC is 24/7. B2C2 comes on later.
Next: Cameron Hughes to delete GCEX-PRIMARY from reference.lists.instrument.custom once the EOD restarts are clean; onboard B2C2 when Amana asks; Daria's ticket ZD-23543 root cause.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793513045608259 https://mahifx.slack.com/archives/C08T42TMKU3/p1793813241969279


### dowusd-continuity-gap — DOWUSD price gap and continuity-pool failover
status: open · since: 2026-10-30 · last: 2026-11-02
State: 10-30 2s DOWUSD gap from a Mahi restart; the quote came from LMAX via the continuity pool at failover. Kate fixed the pool exclusions. 11-02 Nikos asked whether the pricer failed over to the continuity pool and insisted its LPs must match the main LP for CFDs (dow, ndx, oils).
Next: Mahi to answer Nikos on continuity-pool LP matching per CFD; dev to root-cause the restart gap.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793346104217759 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793602301837479


### fx-metals-rollout — FX B-book and XPT/XPD go-lives
status: open · since: 2026-09-25 · last: 2026-11-02
State: 11-02 USDMXN flow moved onto Mahi (Rory imported positions at market with the A-book hedger off); MXN moved to SI 11-05 (CHG-2611-749Q). FX B-book live 10-14 (USD majors, no hedger by Amana's choice; other majors followed), FX quantity config HP 0.001 / Non-HP 1000 / LP 1000. 10-19 FX execution aggregation enabled (USD pairs to LMAX and CMC); 
Next: Rory to clarify the all-FX hedger execution config with Nikos; confirm FX qty config and spread aggregation.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790335963373189 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793632582556009


### hp-indices-energies — Indices and energies onto Mahi_A_HP
status: open · since: 2026-10-20 · last: 2026-10-29
State: Indices and energies live on Mahi_A_HP from 10-20, then minimum/increment problems: NDX futures INVALID_INCREMENT, SPXUSD hedger min 0.1, E35EUR below minimum (moved to Jump, min 0.01), D30 out-of-session orders from hybridHedgerIndicesSI1. Nikos asked to disable trading when markets are closed; Hadeel asked for min/step by venue.
Next: Mahi to apply Hadeel's 10-26 indices Min/Step sheet and answer Nikos on market-closed trading; Amana to answer Shyam on disabling hybridHedgerIndicesSI1 17:00-18:00 NY and say whether NDX futures need 0.01.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792497820771659 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793285687915249


### pricing-load-latency — Pricing model load and latency
status: open · since: 2026-08-20 · last: 2026-10-28
State: 219 instruments on CLIENT_PRICE_LDN caused an XAU/XAG pricing gap 08-20 (to be cut to XAU, XAG, futures). 10-23 Nikos found an unannounced 10ms throttle on A_CLIENTS, wants it removed or 1ms. 10-28 Karen asked for a Centroid tick capture.
Next: William to remove the 10ms A_CLIENTS throttle and explain the 40ms gap; Isaac to run the Centroid capture for Karen; Isaac to complete the instrument reduction on CLIENT_PRICE_LDN.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787240208405969 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793198412378569


### hp-gateway-precision — High-precision (HP2) gateway and quantity precision
status: watching · since: 2026-08-13 · last: 2026-10-23
State: Watching (quiet since 10-23). HP2 gateway (up to 8dp) live after 08-18; 08-23 XAU/XAG increment mismatch rejected ~120k orders; 1e-8 over-fill above ~1,000.
Next: Amana to fix HP vs non-HP account routing; Mahi dev to fix the 1e-8 over-fill, confirm the permanent quantityDefinition fix is live and send Nikos the (unsent) RCA response.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786632001568829 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792769478527769


### gcex-indices-lp — GCEX as second LP for indices
status: closed · since: 2026-10-16 · last: 2026-10-22 · closed: 2026-11-23
State: Superseded by the 10-21 decision to stop trading with GCEX; no activity since 10-22.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792148151058599 https://mahifx.slack.com/archives/C08T42TMKU3/p1792664415225229


### dashboard-releases — Dashboard deploys and fixes
status: watching · since: 2026-08-26 · last: 2026-11-08
State: Mahi ships dashboard-only releases to Amana PROD roughly weekly; NOC checks clean through 11-22.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787731205446379 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794175624367319


### friday-hedger-off — Weekly Friday gold B-book hedger switch-off
status: watching · since: 2026-11-06 · last: 2026-11-22
State: 11-22 Karen asked about an alert that both gold hybrid hedgers were off; Daria updated the expected status since Amana switches them off for the weekend and on before open. Amana turns the gold B-book hedgers off every Friday night. Since the 11-06 dashboard deploy the book icon reads On/Off; disabling the two gold B-book hedgers is the switch.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793996267458159 https://mahifx.slack.com/archives/C08SYSMP0EB/p1795360163943539


### outage-rcas — Outages with written RCAs
status: watching · since: 2026-09-05 · last: 2026-10-16
State: (no activity since 10-16; downgraded pending the engineering ticket) 09-05 weekend crypto outage (Centroid logon gate); 10-14 CMC froze SPX/NDX 16 min (NDXUSD hedger could not route off CMC, about -$567); 10-16 17 XAUUSD B-book fills force-cancelled (dashboard user creation in trading hours costs CPU in every JVM). 11-21: see weekend-reboot-outage. Isaac asked for no user creation in trading hours.
Next: Mahi to raise the user-create/CEP-core engineering ticket; Mahi to decide whether to add non-CMC hedge routing for NDXUSD.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1788769386806729 https://mahifx.slack.com/archives/C08T42TMKU3/p1792168920916789


### hedger-execution — Hedger partial-fill crashes and swapfree sizing
status: watching · since: 2026-08-18 · last: 2026-09-28
State: Tag 17 duplicate on partial fills crashed hybridHedger1 in August (fixed 08-23); LMAX NOP breaches recurred 09-08. One 500oz CMC rejection trips a 30s stand-down. After Nikos's 09-24 tiny-clip complaint Rory re-tuned backstop and DTA rules; improved by 09-28.
Next: Rory's targeted rule for the CMC roll window; answers to Nikos on which VaR targets changed and on raising the normal quantity.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787084603512219 https://mahifx.slack.com/archives/C08SYSMP0EB/p1790584111487529


### gold-24-7 — 24/7 XAU pricing
status: closed · since: 2026-08-24 · last: 2026-09-21 · closed: 2026-11-23
State: No activity since 09-21; Isaac was happy to pipe weekend gold pricing to clients.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787559144038639 https://mahifx.slack.com/archives/C08T42TMKU3/p1789983776166919


### xau-spread-agg-q — How XAUUSD spread aggregation behaves under LP skew
status: closed · since: 2026-11-17 · last: 2026-11-17 · closed: 2026-11-18
State: Answered 11-17 (William): XAUUSD base spread 8c for TOB 250oz, no skew shading on the CMC mid.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794902050001049 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794908679108229


## Arc
- 2026-04-30 — Amana management happy with Mahi; goal is all flow through Mahi
- 2026-06-29 — XAGUSD B-book go-live; XAUUSD B-book 2026-07-01; mobile clients on Mahi B-book 2026-07-03
- 2026-07-21 — Nikos submits cross-asset migration roadmap (gold futures, indices, crypto, oils; FX deprioritised)
- 2026-08-17 — A-book live for all spot energies and indices except VIX; XAUUSD A-book execution aggregation on 2026-08-18
- 2026-08-23 — XAU/XAG precision reject incident (~20 min); RCA 2026-08-24
- 2026-09-04 — First cryptos live (XRP, SOL, XET)
- 2026-09-11 — SI Energies book live
- 2026-09-21 — BTC live
- 2026-09-25 — SI Indices book live
- 2026-10-01 — Seven GCEX cryptos live (ADA, AAVE, AVAX, DOG, DOT, LTC, TRX)
- 2026-10-07 — XPT/XPD live
- 2026-10-14 — FX B-book flow live (EURUSD, GBPUSD, USDJPY)
