---
slug: gcc-brokers
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/gcc-brokers.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: gcc-brokers
  hosts: ../MahiProduct/data/client-hosts.json          # entry: gcc-brokers
  wiki: ../MahiProduct/wiki/clients/gcc-brokers.md
channels:
  internal-gcc-brokers: C09QS1NUA80
  mahi-gcc-brokers: C09PNC1MFAA
contacts:
  - {name: Youssef Bouz, role: "GCC head of trading/ops; main client voice, routes perps, MFXPulse and SI asks", confidence: low}
  - {name: Nael Abu Yousef, role: "GCC trading ops; approves test trades, NOP limits, LP routing", confidence: low}
  - {name: Layan, role: "GCC ops; posts daily Finalto gold fills asking Compass adjustment", confidence: low}
  - {name: Carl Tannous, role: "GCC ops; closes positions, escalates Finalto unresponsiveness", confidence: low}
  - {name: Khalil, role: "senior GCC contact above Youssef; pushed $70k compensation demand after 2026-05-15 XAGUSD incident", confidence: low}
last_catchup: 2026-10-16T07:05:38Z
status: active
---
## Now
GCC is a happy, growing internalising client ("client for life", Will Carter 09-28); the Finalto/LMAX hedger tuning has lifted PnL materially since August.
Live work: LMAX perps (test-traded, not yet live), Amana as a third hedging venue (waiting on client funding) and an institutional pricing stream.
Finalto became spiky again on 2026-10-14/15; Rory is offering GCC an Infinox LP intro (call 10-16).

## Streams

### layan-adjustments — Daily Finalto gold fill reports, Compass adjustment
status: open · since: 2026-04-30 · last: 2026-10-15
State: Almost every weekday ~15:00 BST Layan posts a gold long (occasionally short) filled on Finalto and asks Mahi to adjust Compass; Rory, Cameron Hughes or William answers "will do" and confirms. Volumes ran 160oz to 9.8k oz in the window. Confirmation is not always prompt: GCC had to chase on 09-22 (done next day), 10-07 ("is this done?", confirmed 10-08) and 10-09 (2,572 oz; Layan asked again 10-13 18:00 BST and no confirmation is visible). 10-15 report (1,694 oz) was acknowledged by Rory within a minute.
Next: Rory/ops to confirm the 10-09 2,572 oz Finalto gold adjustment to Layan; confirm each adjustment in thread same day.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1786976522444999 https://mahifx.slack.com/archives/C09PNC1MFAA/p1791555113608319 https://mahifx.slack.com/archives/C09PNC1MFAA/p1791910856126109 https://mahifx.slack.com/archives/C09PNC1MFAA/p1792075794201709

### finalto-execution — Finalto rejections, spikiness and hedger tuning
status: open · since: 2026-07-29 · last: 2026-10-15
State: Finalto fill ratio and rejects have swung. Rejections and throttling in Aug (hedger stands down 5s after 500oz of Finalto rejects; LMAX stand-down between waves raised 200 to 500 after LMAX's book was under 10oz during a hedge cycle, which lifted LMAX fills from 1-3oz to 10-200oz; LMAX also grumbled to Youssef about the hedge flow; VaR reduction 3.5k to 8k; adding Finalto back into the hedger helped even at poor fill rates), then Finalto removed GCC from its defensive (SOR) tag list and fill rate went from 9-22% to 85-87% with rejects 1,824/day to 12/day (Rory's 09-01 summary). XAUUSD book earns about 2.8x more per day and CLIENTS_NET went from +$14.8k/wk to +$23.7k then +$44.8k; Will Carter reported an $80k week on 09-04. On 10-12 the manual Finalto hedger stopped firing because NOP was $87.65m vs an $80m cap; raised to $120m at Nael's request (LMAX limit $80m, $26.58m used). On 10-15 Rory saw Finalto XAUUSD TOB getting spiky since ~13:05 UTC on 10-13 (previously steady ~12c) and planned a quick call with Youssef on 10-16 AM to offer an intro to Infinox (unnamed, "a client") as an additional gold LP alongside Finalto and LMAX; Infinox's own institutional gold price looked tighter and deeper than Finalto/LMAX at GCC in engine data (not a quote, fill rates unchecked). Talking points withhold the crypto deal, figures and that our engine prices the stream.
Next: Rory to hold the Infinox intro call with Youssef (10-16) and report back; keep watching Finalto behaviour.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1785352468874599 https://mahifx.slack.com/archives/C09QS1NUA80/p1788257182280109 https://mahifx.slack.com/archives/C09QS1NUA80/p1792074743531799

### lmax-perps — LMAX perpetual futures integration (XAUUSD-PERP, BTC)
status: open · since: 2026-09-05 · last: 2026-10-11
State: Youssef asked on 09-05 to bring LMAX Perps (separate platform/FIX account, treated as a new LP) into Compass; Mahi needed material FIX/MD changes (deployed in the weekend maintenance window), LMAX conformance was approved by 09-16 (Justin emailed LMAX), a full release went out the weekend of 09-19/20, perps FIX/MD/hedger processes were added 09-25 to 10-01, and Youssef approved 0.1oz test trades which succeeded on 10-01. Depth was fixed from 1 layer of 70oz to LMAX's full 6 layers on 10-01; Rory recommends opening spreads a bit wider than LMAX's ~$0.35-0.40 (about $3 at the 21:00 UTC close). On 10-09 Nael's "same price on spot and perps" was a mapping slip (XAUUSDPERP vs XAUUSD-PERP, fixed in thread); his 0.1oz test trade (tag 4036) then hedged to LMAX_PERPS both legs, confirmed by both sides, and he asked to test BTC perps next. A weekend dry run on 10-11 succeeded after fixing a reset-sequence flag; hybridHedgerPerps1 and arbHedgerPerps are held off via expectedBookStatus overrides (Rory to revisit the arb hedger this week), so it is not live. GCC wants a dedicated channel with wider markups and weekend LR; the Saturday 12:00-13:00 GMT+3 maintenance window is agreed because perps run 24/7.
Next: GCC to fund the perps account; Rory to finish hedger config, set up BTC-PERP pricing/test and set a go-live date.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1788610242999719 https://mahifx.slack.com/archives/C09PNC1MFAA/p1791544494071149 https://mahifx.slack.com/archives/C09PNC1MFAA/p1790845208134599 https://mahifx.slack.com/archives/C09QS1NUA80/p1791723831791499

### insto-pricing — Institutional pricing stream
status: open · since: 2026-10-06 · last: 2026-10-06
State: On a 10-06 call Youssef and Nael said GCC is now targeting institutional client flow (none of the current counterparties are STP brokers), so Mahi must match or beat the insto clients' current offering. Plan is a new channel and pricer for insto pricing aimed at capturing flow even if initial PnL per account is lower. GCC will send the parameters they see today.
Next: GCC to send pricing parameters; Rory to build the channel and pricer.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1791287464442599

### amana-lp — Amana as hedging venue and taker
status: open · since: 2026-09-14 · last: 2026-10-05
State: Amana was set up (fixOrders3/fixMD3, XAUUSD and EURUSD mapped, in the beta pricer since late Sep) after Will Carter flagged an "interesting request to setup Amana as a taker" on 09-14. Connection worked 09-15 and Youssef confirmed quantity definitions that day (gold contract 100oz, step 0.01 = 1oz; FX 100k contract, min 1,000). Nael approved test trades 09-23 and XAUUSD and EURUSD buy/sell looked good, on a small test-only funding; Rory still to map the remaining instruments and asked whether to set an NOP limit like Finalto's. As of 10-05 GCC was to fully fund the Amana account that week, after which NOPs are configured and Amana added as a third hedging venue; full funding not yet confirmed in the channels.
Next: GCC to fully fund Amana and answer on NOP limit; Rory to map remaining instruments, set NOPs and add it to the hedger.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1789388024317479 https://mahifx.slack.com/archives/C09PNC1MFAA/p1790170512445709 https://mahifx.slack.com/archives/C09QS1NUA80/p1791204525364089

### platform-ops — Stability, maintenance windows, access
status: watching · since: 2026-08-23 · last: 2026-10-11
State: Sunday checks on 08-23 found clientDistributionGateway1 and systemStateMonitor down from a notionalCap config that would not deserialize (fixed). systemStateMonitor memory was doubled on 09-01. Maintenance moved to Saturday 09:05 UTC (admin) and 09:25 UTC (trading) to fit the LMAX window at 12:00 GMT+3; Youssef agreed the window 09-07 (anything longer must be pre-scheduled with notice to GCC's clients). Liam Cordelle raised the no-weekend-support gap on 09-08 but dropped it as not significant once Rory showed the reboot only moved ~2h; GCC may want weekend support as perps go 24/7. Dashboard logins failed on 09-06 (FXCubic provider offline) and on 09-20 (connection-limit too low for GCC's number of books, fixed by Sam). Whitelist for Youssef's additional IP was requested and actioned 10-11.
Next: revisit weekend support if perps go live.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1787462534322929 https://mahifx.slack.com/archives/C09PNC1MFAA/p1789932675132249 https://mahifx.slack.com/archives/C09PNC1MFAA/p1791751897689189

### defensive-feeds — LMAX and Finalto defensive feeds and news hedging
status: watching · since: 2026-08-19 · last: 2026-09-23
State: Daria moved LMAX_DEFENSIVE positions back to LMAX on 08-19 so LPR rules see the right position. Will added a news hedging rule on 09-04 after a 26s window with no hedge at NFP; the hedger's News config went from 40s to 60s and added both defensive feeds on 09-11 (about +$17k on CPI). Nael approved Finalto defensive test trades 09-15; the first was rejected ("Account not enabled on the gateway", defensive session GCC_Brokers5) until Youssef supplied the right Finalto account id, and buy/sell succeeded 09-17, confirmed by both sides. On 09-21 Nael said two tags had been moved again to Finalto SOR, so William set up Finalto defensive in the pool, blacklisted tags 334380 and 700154 from core Finalto and added 334380 to the defensive-feed execution rules (Finalto defensive in executionMarkets 09-22). Finalto's core feed dropped for ~1 min on 09-04 NFP according to Finalto.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1788519496962869 https://mahifx.slack.com/archives/C09PNC1MFAA/p1789470718891469 https://mahifx.slack.com/archives/C09QS1NUA80/p1789991663722519 https://mahifx.slack.com/archives/C09QS1NUA80/p1790091163474149

### si-book — Systematic internaliser book
status: watching · since: 2026-07-03 · last: 2026-09-15
State: SI was live from 07-24 with a 200oz XAUUSD cap, but flow into it stayed thin (an $800 drop from tag 334514 on 08-24). On 09-15 Rory moved SI from exclusion-tagged to inclusion-tagged: 50% of specified counterparties and 100% of "Should B Book" flow go to the SI book, everything else skips it. A review doc lives in MahiProduct (2026-09-15-si-review-default-in-vs-out.md); larger counterparties are still under review.
Next: Rory to review larger-notional counterparties and add tags as Youssef confirms them.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1784780445088809 https://mahifx.slack.com/archives/C09QS1NUA80/p1789491725123129

### instrument-mappings — Instrument and spread requests
status: watching · since: 2026-09-06 · last: 2026-09-21
State: DOWUSD was indicative 09-06 to 09-07 because LMAX was not pricing it (pricing again 09-08). Nael then said the DOWJ spread (~150) was tighter than LMAX (~200); Rory widened the beta and then main DOWUSD spreads with Nael's OK and confirmed 09-08, so that is closed. Youssef asked to delete TONUSD on 09-15 (no liquidity) and Cameron Hughes removed it from the overrides; Nathan noted 09-21 the client has not been told it is done. Rory's 08-25 comms summary also listed DXY/VIX proxied prices (DXY done) and an LMAX trade data request as action items, with no closure seen.
Next: tell Youssef TONUSD removal is done; confirm VIX proxy and LMAX trade data request status.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1788764770364529 https://mahifx.slack.com/archives/C09QS1NUA80/p1789480193711279 https://mahifx.slack.com/archives/C09QS1NUA80/p1789973503309009

### flow-toxicity — Large-order tags 700106 / 700154
status: watching · since: 2026-08-06 · last: 2026-09-14
State: Tag 700106 (informed, large clips of 2k+ oz) cost $6k on $37m on 08-18 and was answered with DYNAMIC-LARGEORDER hedger rule (max time-to-flat 138s vs up to 6,067s), a 700106-specific LR profile ($100/M) and channel LR 50 to 100. Youssef declined routing 700106 to LMAX only (08-25) and chose to keep internalising. 700106's client leg moved from -$15k to +$76k at 30s. On 09-14 Daria reported a $4k A-book loss from a 3k oz 700154 trade and asked whether flow has got more toxic; Rory said markouts two weeks earlier were still onside out to 30s, volumes were light (~20m the prior week), and relabelled it brokered, fine to leave for now.
Next: monitor 700154; Rory is content to leave it as is for now.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1786023089729289 https://mahifx.slack.com/archives/C09QS1NUA80/p1787674237025029 https://mahifx.slack.com/archives/C09QS1NUA80/p1789347578163429

### mfxpulse-access — MFXPulse data lake for GCC
status: watching · since: 2026-08-20 · last: 2026-09-03
State: Youssef asked on 08-20 how to get P&L via the MFXPulse API, then on 09-02 asked for both S3/Parquet and Athena access with a list of credentials, workgroup, yieldprofiles_latest view and book IDs. Daria said she would set it up with the dev team and Rory said he would check status when Youssef asked on 09-03; no provisioning or confirmation is visible after that.
Next: Rory/Daria to provision MFXPulse (details in the 09-02 request) and confirm to Youssef.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1788376707168249 https://mahifx.slack.com/archives/C09PNC1MFAA/p1788427041816899

### manual-hedger-nop — Finalto XAGUSD close blocked by NOP cap
status: closed · since: 2026-10-12 · last: 2026-10-12 · closed: 2026-10-15
State: Carl could not close XAGUSD on Finalto on 10-12; the manual hedger was blocked by Finalto NOP above the $80m cap. NOP limit raised to $120m, position closed on open and manual hedgers switched off by Carl.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1791836695198179 https://mahifx.slack.com/archives/C09QS1NUA80/p1791843024196049

### pnl-report-gap — Youssef's STP report vs Compass P&L
status: closed · since: 2026-08-14 · last: 2026-08-17 · closed: 2026-10-15
State: Youssef's comparison showed about 2x Compass's August P&L; on 08-17 he retracted it ("some confusion and wrong thinking on our side, all is good").
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1786712998616739 https://mahifx.slack.com/archives/C09QS1NUA80/p1786976617585179

### xag-incident-comp — Compensation demand after 2026-05-15 XAGUSD incident
status: closed · since: 2026-05-15 · last: 2026-05-27 · closed: 2026-10-16
State: A stale max market position cap left ~45k oz XAGUSD unhedged for ~90 minutes on 2026-05-15 (about $70k client loss); GCC (Khalil) demanded $70k cash and Mahi held at forgoing its value-add share for the pilot. No later signal on the dispute; presumably overtaken by the 12-month terms agreed 07-22 and contract signed 08-07, but never explicitly closed in Slack; no activity since 2026-05-27, assumed resolved.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1778851998984029 https://mahifx.slack.com/archives/C09QS1NUA80/p1779888805588859

## Arc
- 2026-04-23 — CFD internalisation go-live list proposed; live 2026-05-07
- 2026-05-15 — XAGUSD ~45k oz unhedged ~90 min (~$70k loss); post-mortem 05-18
- 2026-06-22 — post-pilot volume-band commercial options drafted
- 2026-07-22 — commercial terms locked for 12 months
- 2026-08-07 — fully signed contract received
- 2026-09-01 — hedger and 700106 improvements: Finalto fill rate 85-87%, best PnL week to date
- 2026-09-07 — Youssef: "much better shape compared to a year ago"
- 2026-10-01 — LMAX perps test trades succeeded; perps go-live pending funding
