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
  - {name: "Stephen Hendrie", role: "exchange/product lead; main counterpart"}
  - {name: "Marianna Konstantinidi (MK)", role: "trading ops, CFD/crypto config, CFD sponsor"}
  - {name: "Reece Singh", role: "ops; classification, YPs"}
  - {name: "Ruby Wang", role: "OZ/exchange trading ops"}
  - {name: "Diego Arranz", role: "CFD ops, OZ config, IP whitelisting"}
  - {name: "Gabriel Bignon", role: "YP/arb, failover breaks", confidence: low}
  - {name: "Tom Smith", role: "tech/ops: DB/IP (not Tom Williams)", confidence: low}
  - {name: "Tom Williams", role: "COO since 2026-08"}
last_catchup: 2026-11-27T08:14:57Z
status: active
---

## Now
Gateway kill switches keep tripping (slow consumer on NYC failover sessions plus a 26.4 regression); fix goes out on FX and CFD in the 11-21 reboots, crypto next week. Crypto SI hedger outage (11-14) fix still open. HRP_PROXY crypto NOP is over its watermark: perps hedger blocked and arb hedger off (11-27). CFD: ASX timezone table reverted at MK's request, HSIHKD depth tier added after cancels (11-20), LDN on Java 25.
Owed: FX SI report to MK, 1003 tag on crypto hedgers, GBPUSD FI loss look, 78 missing arbers, CPI kill-switch note, 26D-Toxic whitelist answer, spot backup trader. CFD licence steps to USD 45k/month; procurement contests the USD 1,500 day rate.

## Streams
### perps-pricing — Perp instruments: pricing, hedging cost, new perps
status: open · since: 2026-06-26 · last: 2026-11-26
State: Isaac finds perp hedging costly (+$37.3k client spread vs -$32.0k hedging, about $8k a month) and proposes taking all perps except XAUUSD-PERP out of the hedger. JPXUSD-PERP, I50USD-PERP and XCUUSD-PERP copper requested 11-12; copper (CHG-2611-CPW7, Goldi feed) staged for the 11-17 22:00Z restart. XAGUSD-PERP unlaunched. 11-20 MK asked to add NDXUSD-PERP and XAUUSD-PERP from the HRP_PROXY feed to the price (benchmark only, no normalising) and to the perps hedger; Isaac actioned it. 11-26 MK asked to add CL1USDPERP pricing from HRP now that it is visible.
Next: Mahi to add CL1USDPERP from HRP; Isaac to raise hedger removal with Stephen/MK; Shyam to confirm copper live after the 11-17 restart; Pepperstone to launch XAGUSD-PERP.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1793788289609159 https://mahifx.slack.com/archives/C06AR8MT8NT/p1795182632653789?thread_ts=1795182632.653789&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1795679108014849

### compass-26-4-upgrade — FX and CFD environments upgraded to Compass 26.4
status: open · since: 2026-11-13 · last: 2026-11-26
State: FX and CFD upgraded 11-14 (CHG-2611-542H), 8 checks pending. Follow-on 11-20 to fix a 26.4 kill-switch regression: FX update (CHG-2611-P53V, notice 11-20 from Liam) and CFD update (CHG-2611-CRJQ) staged Fri, live at Sat 21 Nov reboots; CRJQ implemented 11-21 with 6 of 8 checks pending. LDN moved to Java 25 (CHG-2611-ZVKQ), implemented, 3 of 6 checks pending. 11-26 Liam self-approved Java 25 on the London servers, wave 1 (CHG-2611-1JQG, to 11-29 05:30Z) and the wider set (CHG-2611-4TSX, to 11-29 23:00Z), staged for the weekend restart.
Next: Arun to verify 542H (was due 2026-11-17); Liam to verify CRJQ by 11-24 and ZVKQ by 11-25; crypto 26.4 fix to be arranged next week.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794567662931909 https://mahifx.slack.com/archives/C033K2P0RPT/p1795699319720219

### data-access — Pepperstone DB, S3/Athena access and IP whitelists
status: open · since: 2026-06-29 · last: 2026-11-25
State: Still open: Sebastian Andrews' DB access (2026-09-15) fails on TCP 3306 from Cloudflare WARP despite whitelisted IPs; last chased 09-28. Also open: James White's trade_id outliers, Reece's S3 backfill. Tom Smith's missing FX tables (11-16) were a permission issue, fixed by Rory. 11-25 Tom Smith asked to whitelist an FX range (already accepted on 3306) then a single static IP; Isaac set it up on crypto, FX and CFD DB instances, pending Beeks whitelist.
Next: Beeks to whitelist Tom's static IP; Mahi to answer Sebastian, James and Reece.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1782731133990719 https://mahifx.slack.com/archives/C06AR8MT8NT/p1795612698068449

### crypto-yield-psm — Crypto yields down; PSM scoping for XBTUSD/XETUSD
status: open · since: 2026-10-06 · last: 2026-11-24
State: Crypto spread yield fell to ~USD 200/M (350-450 before). Isaac proposed PSM (MK agreed 10-08). 2026-11-23 16:04Z the beta stream was retuned to MK's chosen $9 shape ($5 floor after 5s without flow, base $8, PSM-W-T90 widening, four states up to $15.29). First 16h averaged $8.64 vs $15.01 live; first 17h repriced fills score -15 $/M vs live 244 $/M (about 7% more flow needed to hold revenue; one night too short to conclude, month emulation gives +3 $/M).
Next: Isaac to keep monitoring the beta against live and report to MK; Isaac to finish engine verification and send MK PnL/spread numbers for PSM variants.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1791285982179839 https://mahifx.slack.com/archives/C033K2P0RPT/p1795513662439569

### cfd-session-spreads — CFD custom sessions, BMSL timezone overrides and thin layers
status: open · since: 2026-11-09 · last: 2026-11-23
State: MK (2026-11-09) saw ASXAUD spreads wider than 2 at the 22:50Z open: the custom session started late; Isaac moved its start to 09:30 Sydney after the 22:00Z restart. MK also reports a deeper G30EUR layer missing from the model and broken Compass audit history. 11-17: G30EUR 0.01 orders cancel in CFD NYC (G30 min quantity 0.1 on the LIQUIDITY_POOL_NYC/LDN pools). 11-20: at MK's request Kate reverted the ASX timezone table (Custom 2 back to 05:30-06:10 and 21:00-22:00 UK), undoing the 09:30 Sydney start. 11-23 MK asked again to remove the leftover 22:30-23:00 Sydney entry from Custom 2 so ROLL and SNGMON apply, leaving only 05:30-06:10 and 21:00-22:00; no reply yet.
Next: Mahi to remove the Custom 2 22:30-23:00 Sydney entry for MK; Isaac/MK to confirm the ASXAUD open under the reverted table; Rory to look at the G30EUR layer and audit history; MK to decide on G30 min quantity.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794221476797189 https://mahifx.slack.com/archives/C06AR8MT8NT/p1795432877937119

### crypto-hedging — Crypto spot hedger tuning and LP de-prioritisation
status: open · since: 2026-07-13 · last: 2026-11-20
State: Stephen (10-20): XAUT/PAXG hedging has no cost benefit. 2026-11-20: B2C2 gets no XBTUSD hedges: no config ranks it lower, hedgers favour LMAX/Wintermute on skew, and over 80% of about 25M attempted to B2C2 this week were cancelled on price (1 pip tolerance); Stephen will monitor.
Next: Daria can raise B2C2 flow if asked; Stephen to decide whether to drop XAUT/PAXG from SI hedging; Diego to get HRP's answer on the PEP-LD4_Q feed now tagged HRP-2 (Mahi's HRP_LDN mapping is HRP-Agg, so London gets no HRP data since 2026-10-18), then Shyam to update the mapping.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1783981698651339 https://mahifx.slack.com/archives/C06AR8MT8NT/p1795142823404709

### gateway-cpi-reject — NY gateway kill switch trips on data events (CPI, FOMC)
status: open · since: 2026-10-14 · last: 2026-11-20
State: Tripped again 2026-11-20 (LDN clientDistributionGateway1 after re-enable; books off again): Kate: slow consumer on the A then B NYC failover sessions. Liam: a kill-switch regression in 26.4 raises the trip rate; the fix ships this weekend on FX (CHG-2611-P53V) and CFD (CHG-2611-CRJQ), crypto next week; a network-path problem causing extra disconnects is also under review with OZ. MK asked whether Pepperstone can do anything. Earlier trips 10-14 to 11-16.
Next: Liam to verify the fix after the weekend and schedule crypto; Mahi (Rory/Nathan) owes Diego the CPI kill-switch explanation; Mahi to decide failover-exempt levels.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1791997243862479 https://mahifx.slack.com/archives/C06AR8MT8NT/p1795185336168619 https://mahifx.slack.com/archives/C033K2P0RPT/p1795187036575319

### cfd-depth-cap — CATTLEUSD 96k trade break: spread layers and distributed quantity cap
status: open · since: 2026-10-29 · last: 2026-11-20
State: A 96k CATTLEUSD trade broke (published 40k, channel cap 70k); Ruby added layers, Nathan raised depth to 100k. 2026-11-03: a 97k trade failed over; MK asked Cameron Hughes to double cattle quantities (agreed). 2026-11-09: a client could not close Cocoa against a single 10 layer; MK bumped it to 30. 11-20: HK50 cancels: buys of 212.4 HSIHKD exceeded the 200 published; William added a 300 tier (31 HKD base spread).
Next: Cameron Hughes to double the cattle quantities as MK asked; Gabriel to confirm his question is answered; check other thin commodity books for single-layer depth.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793234694691149 https://mahifx.slack.com/archives/C06AR8MT8NT/p1795207562317369?thread_ts=1795207562.317369&cid=C06AR8MT8NT

### fx-si-sims — FX B-book SI/inventory sims for Pepperstone
status: open · since: 2026-08-27 · last: 2026-11-19
State: Nathan's SI/inventory sims reached Stephen 2026-09-22; he is convinced pure B-booking is wrong, but every simulated method exceeds the USD 200M prime-broker credit limit. 2026-11-16 MK asked for the FX SI model test results, instruments and lookback; Nathan (11-17): the report (28 FX pairs, Sep 2025 to mid-Nov 2026) goes to MK by Friday 2026-11-20; on 11-19 Nathan posted the report artifact amended with Daria's edits and invited feedback.
Next: Nathan to send MK the SI report by 2026-11-20; Nathan to rework artefacts toward risk within the USD 200M limit; Stephen to send exact credit numbers.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787786333971199 https://mahifx.slack.com/archives/C033K2P0RPT/p1795082677496309

### java4shell-stopgap — Java4Shell JVM-flag stopgap restarts on NY and admin servers
status: open · since: 2026-11-18 · last: 2026-11-18
State: CHG-2611-8S2H and CHG-2611-GD62 (Base64 JVM flag; NY stack and admin restarts) self-approved by Liam, implemented 11-18 23:07Z; 4 of 6 checks pending.
Next: Liam to verify (was due 2026-11-20; no update seen).
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1795005886462009 https://mahifx.slack.com/archives/C033K2P0RPT/p1795043227111189?thread_ts=1795005886.462009&cid=C033K2P0RPT

### toxic-pool-failover — Toxic client internalised after failover to LD, request for hard 26D whitelist
status: open · since: 2026-10-26 · last: 2026-11-17
State: 2026-10-26: a 26D Toxic Pool client traded EURCAD and, after a brief failover to LD, was internalised. Stephen asked for a 100% 26D-Toxic whitelist; no answer seen. 2026-11-16 Stephen asked to export the 26D Toxic Pool counterparties: not possible in Compass, so Shyam pulled a CSV; no bulk edit either, so Stephen prunes accounts by hand.
Next: Mahi (Shyam) to answer Stephen on a no-exceptions 26D-Toxic whitelist and why the failover internalised.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792988548313129?thread_ts=1792988548.313129&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1794874640691249?thread_ts=1794870549.915759&cid=C06AR8MT8NT

### compass-tob-qty — Quantity display in the new Compass top-of-book view
status: open · since: 2026-11-17 · last: 2026-11-17
State: MK asked where the new TOB view shows quantity in instrument units (XAU in oz) as Echo did; William: shorten the window and use per-tick plot, hover shows quantity.
Next: MK to confirm that works.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794922777524659 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794932549738729?thread_ts=1794922777.524659&cid=C06AR8MT8NT

### crypto-hedger-tag — Counterparty tag 1003 on crypto hedgers in the FX environment
status: open · since: 2026-11-16 · last: 2026-11-17
State: MK asked 2026-11-16 for a fixed counterparty tag 1003 on the crypto Arb NYC and Hybrid NYC hedgers running in the FX environment (like the inventory hedgers' 1001/1002); Kate agreed, switching them from last-non-blacklisted client tag, and bounced the NYC crypto hedgers to pick it up. The hybrid hedger being off in FX is intentional: the arb clears the risk and pays less spread (Daria).
Next: Kate to confirm 1003 is live on both hedgers.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794846344426819 https://mahifx.slack.com/archives/C033K2P0RPT/p1794849319031779

### crypto-si-hedger-stop — Crypto SI hedger terminated on first order breach over the weekend
status: open · since: 2026-11-14 · last: 2026-11-16
State: Shyam restarted the crypto SI hedger Sun 03:21Z at MK's request. RCA: Pepperstone's oneZero LD4 hub went silent ~6 min from 03:17Z Sat after two ETH sells to HRP_PROXY, no ack, and with order breach limit 0 the NY hedger terminated 03:18:36; SI book unhedged ~24h. Daria suggests configurable.
Next: Engineering to decide breach behaviour (degrade vs terminate, configurable); infra with oneZero on the hub outage and a backup endpoint; review the 30s heartbeat.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1794798340059999 https://mahifx.slack.com/archives/C033K2P0RPT/p1794798470888159?thread_ts=1794798340.059999&cid=C033K2P0RPT

### crypto-restart-window — Agreed restart slots for crypto; HRP NOP limit cut
status: open · since: 2026-11-14 · last: 2026-11-16
State: Daria (2026-11-15) proposed ad-hoc config/code restarts outside the weekend reboot at NYC 17:00-17:05 and LDN 17:05-17:10 New York time, other region confirmed up first; Stephen agreed; wants a bigger gap between regions. Separately Tom Smith cut the HRP_PROXY NOP limit in crypto (28m/27m to 16.9m/15.4m) on 11-14 and traded out manually; HRP takes only NOP-reducing trades until it falls.
Next: Daria to leave a bigger gap between regions.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794776442047159 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794677329133139

### fi-skew-tuning — FI/skew/LR sizing and signals across FX, CFD and metals
status: open · since: 2026-08-18 · last: 2026-11-16
State: On 2026-10-14 Isaac moved FX majors to IFM-based benchmark adjustments; MK approved promoting HSIHKD, JPXJPY, XAUUSD-F and NDXUSD to the price signal (2026-10-08, monitoring). 11-16 MK reported FI GBPUSD PnL negative, the evening of 12 Nov the culprit; Rory will look.
Next: Rory/Nathan to look at the GBPUSD FI loss on the evening of 2026-11-12; Nathan to report on CFD skew.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787060801310749 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794847832483919

### gbpjpy-position-break — GBPJPY A-book position mismatch from a 28 Oct cross-book trade
status: open · since: 2026-11-13 · last: 2026-11-13
State: Ruby (2026-11-13): GBPJPY A-book client +5k vs Mahi books -3m (hedge -100k both). Nathan: account 51305808 bought 3m on 2026-10-28 ~14:29Z in the A House and sold back to the B House within a minute. He proposed three 1M book-to-book transfers on DISTRIBUTION_NYC at the original sell prices (210.229, 210.220, 210.210); Ruby will book them.
Next: Ruby to book the transfers.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794531022323509 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794535924722929?thread_ts=1794531022.323509&cid=C06AR8MT8NT

### ton-pricing-gap — No TONUSD quotes since 2026-11-10 (LMAX feed stopped)
status: open · since: 2026-11-12 · last: 2026-11-12
State: Mariapaz: no TONUSD quotes since 09 Nov. Nathan: the mid forms from LMAX, HRP and Wintermute; HRP sent no TONUSD since 18 Oct and Wintermute never quoted, so LMAX alone fed it, and LMAX stopped TONUSD 10 Nov 09:00Z. With no LP price it is indicative. Diego will check with the LPs.
Next: Diego to check with the LPs; decide on adding TONUSD LPs.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794517157344189 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794524618181479?thread_ts=1794517157.344189&cid=C06AR8MT8NT

### xau-cpi-price-gap — XAUUSD pricing gap and delayed fills at the 2026-11-10 CPI release
status: open · since: 2026-11-11 · last: 2026-11-12
State: No XAUUSD pricing 13:30:01-13:30:06Z at the 2026-11-10 CPI release. IG and Velocity cancelled XAUUSD-F quotes; all three gold MWMS benchmark LPs stopped quoting, so the pricer went indicative. A 5-6s fill delay was London-to-NY OZ hub execution-report queueing, not the engine.
Next: Pepperstone to respond; continuity pool shares the MWMS benchmark LPs (not yet raised).
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794416974543159 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794446900688329?thread_ts=1794416974.543159&cid=C06AR8MT8NT

### barclays-adapters — Barclays maker adapters offboarded; UBS via Wedbush coming
status: open · since: 2026-11-11 · last: 2026-11-12
State: Georgios (2026-11-11): Barclays_NY and Barclays_LD maker adapters are disabled and will be offboarded; taker adapters stay, renamed Mahi_NY_A_UBS_Wed and Mahi_LD_A_UBS_Wed for a new UBS-via-Wedbush maker; timing to follow.
Next: Pepperstone to give timing; Mahi (Daria/Shyam) to update session and config names when renamed.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1794404269481209 https://mahifx.slack.com/archives/C06AR8MT8NT/p1794470635568689?thread_ts=1794404269.481209&cid=C06AR8MT8NT

### nfp-value-add — NFP value-add draft for Pepperstone, figures corrected
status: open · since: 2026-11-06 · last: 2026-11-11
State: Isaac (2026-11-11): XAUUSD 12:00-17:00Z B Book FI $229.2k on ~$9.1B (25.1 $/M), LR $21.0k (2.3 $/M). Daria sent the QBR to seniors. Will's 11-06 NFP message overstated figures ~3x (corrected); FX skew slightly negative, left out.
Next: Will/Daria to review the corrected figures (was due 2026-11-09) and send to Tom and Tammas; skew-health check on the negative FX skew.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1793976769629449 https://mahifx.slack.com/archives/C033K2P0RPT/p1794397891032079

### arb-list-gap — 78 of 116 latency arbers missing from the B-book dynamic arb list
status: open · since: 2026-11-05 · last: 2026-11-06
State: Reece listed 116 latency arbers (YTD) but only 38 are in the NY B Book arbitrageurs list, leaving 78 uncaught. Daria said London capacity permitting today, otherwise Monday (2026-11-09); no reply seen in channel yet.
Next: Mahi (Daria/London team) to explain why 78 are not picked up and reply to Reece by Monday at the latest.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793857304268939 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793942588498509?thread_ts=1793857304.268939&cid=C06AR8MT8NT

### classification-upload — Pepperstone's own counterparty classification upload (SOW #5)
status: open · since: 2026-05-19 · last: 2026-11-06
State: Live on crypto as of 2026-11-06: Pepperstone can upload up to three counterparty lists (Compass UPLOAD1-3); Reece's 116-account test list loads hourly into the A Book's UPLOAD1 (NYC only). FX and CFD are on 26.4 but have no download config yet.
Next: Ask Pepperstone whether each platform gets its own list; add the FX and CFD download config on request; Liam to confirm the SOW is issued.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1779146841798919 https://mahifx.slack.com/archives/C033K2P0RPT/p1793972837891119

### a-book-client-risk — Client losing A-book money, accounts trading both books
status: open · since: 2026-11-06 · last: 2026-11-06
State: Stephen (2026-11-06): client 51506969 cost the A book -$8k while flat on the day; he will broker them meanwhile. Daria: A gained ~$5k from them earlier, aggregate yield looks good; review next week. Two other accounts trade the same way.
Next: Daria to review the counterparty mid next week; Pepperstone cleaning up the related accounts.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793929253708569 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793936446011299?thread_ts=1793929253.708569&cid=C06AR8MT8NT

### crypto-a-book-arb — Crypto A-book dynamic arb classifying too harshly; realtime detection
status: open · since: 2026-10-29 · last: 2026-11-05
State: Crypto A-book dynamic arb classified too harshly (633 accounts in sims, 2026-10-29); Stephen chose Light: Shyam set the 7-day and 30-minute bad checks to -$5/M, list reset to 193. Realtime arb detection was tightened live 2026-11-05 (CHG-2611-092T).
Next: Isaac to review crypto skew sizing and weekend setting.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792355023754729?thread_ts=1792355023.754729&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C033K2P0RPT/p1793851009921779

### polaris-migration — Spot crypto moving from Modulus to Polaris (SOW)
status: open · since: 2026-08-21 · last: 2026-11-05
State: Modulus dropped 2026-08-21; Liam wants an SOW (none seen). Crypto env upgrade: London done 2026-11-05, NY started, completion unseen; Stephen calls the missing spot backup a blocker. NY backup trader ready; Daria asked Pepperstone to approve (11-05).
Next: Shyam to confirm NY upgrade completion; Isaac to answer on internalising at the continuity price; Daria to switch on the backup trader if Pepperstone confirm; Liam to scope the SOW.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1787289556446609 https://mahifx.slack.com/archives/C033K2P0RPT/p1793856168156919

### cfd-equities — Pepperstone CFD equities to be priced by Mahi
status: open · since: 2026-11-03 · last: 2026-11-04
State: After the 2026-11-03 quarterly call MK asked which equities Mahi covers; Isaac: anything Pepperstone supplies market data for, most traded first. MK sent ~45 US names; Isaac shared a symbol-map CSV. Nathan needs quantity definitions, spreads and LPs.
Next: MK to confirm coverage/symbol map, supply market data and the quantity/spread/LP parameters; Nathan/Isaac to set up the instruments in the CFD environment.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793699237499969 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793825895651279

### cfd-licence-fee — CFD licence fee step-up at month 4 and quarterly review prep
status: open · since: 2026-10-19 · last: 2026-11-03
State: The Global Quarterly Steering ran 2026-11-03. The CFD licence enters month 4, when the fee uplift moves from USD 30k to USD 45k a month; Andrew wanted Pepperstone reminded (Bonnie); not visible whether it was.
Next: Check the meeting notes for whether the fee step-up and open QBR checks (hero-moment links, cross-region failover) were covered; if not, raise the step-up before the next invoice.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1792425618470259 https://mahifx.slack.com/archives/C033K2P0RPT/p1793697818244769

### echo-cfd-ld-parties — LD parties not visible in the CFD Echo
status: open · since: 2026-11-03 · last: 2026-11-03
State: MK sees LD parties in FX and crypto NYC Echo but not CFD; Isaac is checking a setting (CHG-2611-0Z3D undid the 2026-11-02 multicast change).
Next: Isaac to apply the CFD Echo setting.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793723922411939 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793724158099669?thread_ts=1793723922.411939&cid=C06AR8MT8NT

### fx-a-book-hedging — FX A-book metals hedging, LP limits and prime-broker positions
status: open · since: 2026-09-14 · last: 2026-10-29
State: Since 2026-09-18 metals hedge via Finalto and Invast with per-LP backstops. 10-26: MK asked how an ISPRIME XAUUSD position arose despite LPR rules; Kate loosened metals LPR conditions, 10-28 Daria added immediate LPR rules. 10-29: MK asked for further hedger changes to keep XAU risk near 0.
Next: Daria/Kate to answer MK on holding XAU near zero and review the loosened LPR conditions.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793272154618899

### cfd-pricing-feeds — CFD feed gaps, reference-market changes and indicative alerts
status: open · since: 2026-09-22 · last: 2026-10-29
State: USDCLP gap (2026-09-22) is QRT-side. IG fallback for the IG-feed latency exploit live 2026-10-27 (CHG-2610-4GVE); clean fallback at next cash close unchecked. Ten indices moved to Velocity primary; VELOCITY_LDN does not price JPXJPY.
Next: Reece to check whether VELOCITY_LDN should stream JPXJPY; Isaac/Shyam to do the OOH timetable update (due 1 Nov); Isaac to confirm IG fallback at next cash close; Pepperstone to chase OneZero on USDCLP.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1790096194336949 https://mahifx.slack.com/archives/C033K2P0RPT/p1793274530228519

### normalisation-mid — Model mid diverging from the normalisation market
status: watching · since: 2026-11-05 · last: 2026-11-06
State: Tom Williams (2026-11-05) asked about bringing the model mid closer to the normalisation market (CL1USD-PERP). Daria: divergence is basis changing over the look-back; a shorter window tracks better. Tom sees no issue.
Next: Daria to answer Tom's compute and slow-market question if he wants to pursue it.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793922940079729 https://mahifx.slack.com/archives/C06AR8MT8NT/p1793943588875729?thread_ts=1793922940.079729&cid=C06AR8MT8NT

### dev-day-rate — Pepperstone procurement challenges the USD 1,500 SOW day rate
status: watching · since: 2026-10-22 · last: 2026-10-22
State: Procurement (Lisa) objected to the SOW day rate rising from USD 1,000 to 1,500; SOW #4 agreed at 1,250 with Stephen. Bonnie's draft (1,250 for 12 months, then 1,500) not seen sent.
Next: Bonnie to send/revise the reply to Lisa; Liam to review the draft. Downgraded: no activity since 2026-10-22.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1792657103153339 https://mahifx.slack.com/archives/C033K2P0RPT/p1792688981792389

### cfd-hedging — CFD inventory hedger rejections, LP liquidity and risk controls
status: watching · since: 2026-07-27 · last: 2026-10-13
State: No activity since 2026-10-13. The CFD inventory hedger keeps hitting LP limits: NG1 clips reject on 26Degrees; NG1 hedging stopped 08-06 when the trigger rose USD 2M to 3M.
Next: Reece to ask Invast/OZ whether NG1 depth is capped and whether the book can show remaining depth; Mahi to decide NG1 trigger appetite (USD 3M vs 2M) and the hedge venue review.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1785164826669399 https://mahifx.slack.com/archives/C06AR8MT8NT/p1791898246094219

### cfd-limit-breach — CFD limit orders to IG via OZ filled through their limits
status: closed · since: 2026-11-18 · last: 2026-11-20 · closed: 2026-11-20
State: Daria reported (11-18) two CFD limit orders to IG via OZ filled through their limits (3728.12 vs 3872.00); client orders kept theirs. Diego (11-20): IG was mapping the limit orders as market orders; OZ will add the right mapping.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1795150336898869?thread_ts=1795038777.609329&cid=C06AR8MT8NT

### crypto-env-upgrade — Crypto environment upgrade, blocked on spot backup trader
status: closed · since: 2026-10-22 · last: 2026-11-05 · closed: 2026-11-13
State: merged into polaris-migration.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793920459251039

### fx-xag-nop-limit — Inventory hedger blocked on XAGUSD per-market NOP limits
status: closed · since: 2026-10-23 · last: 2026-11-02 · closed: 2026-11-19
State: hedger was inside limits (risk -1.41M vs 1.6M level); Stephen to reconcile; no activity since 2026-11-02; assumed resolved.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793579076774179

### dst-sunday-check — US DST change: confirm no pricing/execution breaks
status: closed · since: 2026-10-29 · last: 2026-11-01 · closed: 2026-11-19
State: no breakage reported since 2026-11-01; no activity since; assumed resolved.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793564093291219?thread_ts=1793525397.111909&cid=C06AR8MT8NT

### open-failover-breaks — Trades failing over to the internal maker at the open
status: closed · since: 2026-10-27 · last: 2026-10-27 · closed: 2026-11-13
State: IG first tick beat Mahi by 1ms at the open; assumed resolved.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1793118304272449?thread_ts=1793118304.272449&cid=C06AR8MT8NT

### margin-exploit-throttle — New-account margin exploits and order throttling
status: closed · since: 2026-07-30 · last: 2026-09-14 · closed: 2026-11-16
State: symbol-scoped throttle needs a dev change (150 orders/1000ms is global); no activity since 2026-09-14; assumed resolved.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619

### xau-spreads-toxic — XAUUSD spread algorithm and toxic gold flow
status: closed · since: 2026-08-13 · last: 2026-09-14 · closed: 2026-11-16
State: PSM-style XAUUSD spread algo (cap 18pt) liked by Stephen; QQ EA detection live; no activity since 2026-09-14; assumed resolved.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619

## Arc
- 2021 — first negotiation failed; ~3 months free work
- 2023-07-31 — Pepperstone board approves including CFDs
- 2023-12-21 — 3-year MSA signed (MFXEcho + Compass + Pulse, FX and metals)
- 2024-04 — Compass live in production for FX MM
- 2025-07-16 — 3rd Addendum: term to 2028-07-16, no termination for convenience
- 2025-Q4 — Modulus crypto exchange live with 6 AUD pairs
- 2026-Q1 — CFD licence signed; crypto SI profitable every week of 2026
- 2026-07-22 — CFD desk live (NY and LDN)
- 2026-08 — Tom Williams promoted to COO; Stephen Hendrie becomes main counterpart
- 2026-08-21 — Rob Bowen leaves Pepperstone; Pepperstone drops Modulus for spot crypto
