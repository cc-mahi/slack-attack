---
slug: toa
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/toa.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json          # entry: toa
  wiki: null
channels:
  internal-toa-ops: C035H1VNCAD
  toa-nado-shared: C09RGU1T1GE
contacts: []
last_catchup: 2026-11-13T08:17:23Z
status: active
---

## Now
Toa is a sister company (same CTO, James Furness; also posts as James@toalabs.xyz). Nado is wound down; the live workload is Argamon FX/metals market making on LDN, CHI and APN1, with ops watching PagerDuty in `internal-toa-ops`. `toa-nado-shared` has been silent since the wind-down.
Main threads: the CBOE hedger on CHI keeps tripping its PnL firewall (six trips on 10-30, more on 11-04, 11-05 and 11-12; daily limit -3M, likely to rise), the CBOE state-mismatch code fix is due, and LDN insti pricing goes indicative around rolls since the EBS feed was killed.
Several Argamon-raised issues arrive as forwards from `mahi-argamon-operations`, which is not in this dossier's channels.

## Streams

### cboe-hedger-chi — hedgerCBOE1 on CHI: firewall/PnL trips and state mismatches
status: open · since: 2026-08-03 · last: 2026-11-12
State: hedgerCBOE1 (moved to Chicago 2026-07-22/23 after the London book was left off) trips repeatedly: firewall on 08-03, 08-05, 08-06 (Lee raised limits per a Zendesk ticket), PnL breach 09-17, firewall 09-28, down at the US CPI release 10-14, restarted again 10-22 by James ("looks fine"), and on 10-30 tripped `UnrealisedPnlFirewall` (`pnlProfitLimitPerDay`, 2M) six times in about three hours from 13:04 UTC, re-tripping after each restart until Lee bumped the unrealised limits and restarted it. On 11-04 it tripped again: realised P&L firewall at about 05:58 UTC (Daria restarted it, suggested reviewing the sweep config), then the unrealised 1-hour firewall as XAUUSD gained about $60 in an hour; Daria raised PnL Limit Per Hour from 1.6m to 2m, then to 2.2m after another trip at 06:57, and Inald restarted it after another hedgerCBOE down alert at 07:50. At 00:30 UTC on 11-05 it crashed again, this time on the daily realised-PnL firewall (the hourly limit had been raised, not the daily); Shyam restarted it and, with James's go-ahead ("we want a bigger limit"), raised realisedPnlLimitPerDay from -2M to -3M. At 14:58 UTC on 11-12 it came down again on a 24-hour PnL breach (4,002,402, past the -3M daily limit); Arun is checking, and James said net PnL looks fine (bigger offsetting positions) and limits will be raised further if it stays a pain. Cameron restarted it on 09-17 and 10-14 after checking net PnL. James's guidance (09-17): hedger PnL firewalls see only the hedger side, so restart is fine if net PnL is healthy. Separately, ordersCboe1 state-mismatch alerts (price 1.32503 vs 1.325, and a 100 EURUSD mismatch) are on the Argamon-to-CBOE side. On 2026-09-30 Lee said a code fix is ready and "should be sorted this week"; no confirmation of release seen.
Next: Lee/James to ship the state-mismatch fix and confirm; ops ignore mismatches meanwhile; Arun to restart/check after the 11-12 breach and James to raise the limit further if needed; limit tuning or root cause of the repeated PnL trips (sweep config review suggested 11-04) is open.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1785757251842839 https://mahifx.slack.com/archives/C035H1VNCAD/p1792683541640309 https://mahifx.slack.com/archives/C035H1VNCAD/p1793376250627589 https://mahifx.slack.com/archives/C035H1VNCAD/p1794495489920819

### infra-releases — releases, new gateways and box changes on Argamon/Toa
status: open · since: 2026-08-17 · last: 2026-11-12
State: On 11-12 traderBinance on Argamon APN1 came down on a BINANCE_FUTURES_UM cancel timeout (order breaches limit 0); Arun was starting it back up. On 11-04 marketDataNado1 on Toa APN1 OOMed again (Inald); James (Toa Labs) disabled PagerDuty for Toa APN1 and Isaac Dann agreed it is fine to stop the box, so the leftover Nado process is being retired. Kraken Futures market data on Argamon APN1 has been down since about 02:20 UTC on 10-30 (Kraken-side incident, PagerDuty open, no resolution seen). Licence renewed 2026-08-17. 26.4 deployed to Argamon LDN/CHI on 09-26, then APN with `connectivity.aeron.metadata.inband` enabled for KRAKEN as a low-risk test. FX contracts were rolled by restart on 09-11. Lee set up new gateways on CHI (09-22), removed the natwest channel from LDN clientDist (restart planned EOD 09-24), and began setting up a new LP in TKY on 10-14. The secondary APN1 box was decommissioned but its multi-region infra was not unwound, so config updates queue up (09-07). hazelcastNode OOMs recurred (08-18, 09-07) and marketDataNado1 OOMed on 10-28 (Shyam restarted it, PagerDuty incident; a Nado process still running despite the wind-down) and CENTROID_NY4_A-MD sessions dropped for about 2 minutes on 09-16, flowing through to Argamon's TOA_CRYPTO-ORDER.
Next: stop the Toa APN1 box (approved 11-04); Lee to finish the TKY LP; unwind the multi-region infra left from the sec-1 decommission.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1787001242923619 https://mahifx.slack.com/archives/C035H1VNCAD/p1793148848983029 https://mahifx.slack.com/archives/C035H1VNCAD/p1793329652756379 https://mahifx.slack.com/archives/C035H1VNCAD/p1794474981996009

### pnl-var-alerting — PnL-drop, VaR and not-ticking alert noise
status: open · since: 2026-06-25 · last: 2026-11-02
State: HRP_CLIENTS_NET PnL-drop alerts recur on LDN. James raised `monitoring.pnlDrop` limits on 2026-08-11 because Toa is running more risk. Leonardo flagged a -16,953 in 8 minutes drop on 09-11 with no follow-up. The 08-27 high-VaR alert was CHI and had cleared. On 08-31 Justin asked for auto-resolve on cleared-risk alerts, and James pointed at MXC-66. No tuning change after the 08-11 limit rise. On 2026-11-02 Daria said not-ticking alerts fire regularly around roll for ISAM_NW_LDN (down about 16:20-18:00 NY) and KGI_RCTV_NYC (about 16:50-18:15 NY) and asked whether to extend the alert threshold or disable monitoring for them; one thumbs-up, no decision seen.
Next: Toa/Mahi to answer Daria on extending or disabling the ISAM/KGI not-ticking alerts; MXC-66 for auto-resolve.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1782371422081669 https://mahifx.slack.com/archives/C035H1VNCAD/p1788162803181199 https://mahifx.slack.com/archives/C035H1VNCAD/p1789134750585619 https://mahifx.slack.com/archives/C035H1VNCAD/p1793662534164719

### insti-indicative-pricing — LDN insti pricing indicative after EBS decommission and around rolls
status: open · since: 2026-08-17 · last: 2026-11-01
State: EBS decommission removed `EBS_IMP_CHI`, which LDN insti pricing relied on, so insti FX went indicative; the EBS feed is now killed. During rolls CBOE_HR_LDN is the main reference and CBOE liquidity can be too thin for a stable price (Elan was to ask CBOE). Ops muted alerts via `monitoring.pricing.suppressAlertsDuring` and Lee removed SINGAPORE_MONDAY. James: CLIENT_PRICE_INSTI_LDN may be indicative because it is the only model without index reference-price fallback ("rather no price than a degraded price"). 2026-10-15 Nathan Burch asked whether 6A/6B/6E/6J/6M/6N/6S/6Z, GC, MGC, SI and SIL Dec-26 futures should be priced: LDN pricerInsti reference markets changed, and no base spreads exist on CHI or LDN insti. Lee replied that they are not published to clients but are available via CME/COMEX. On 2026-11-01 Daria restarted the Argamon LDN prices and pricerInsti1 raised `marketData.pricing.modelError` (unable to create 12 of 35 pricing models, all no-reference-price markets, same as the 10-15 case); she asked whether those instruments should be removed.
Next: Toa/Argamon to answer whether those futures (and the 12 failing models) should be priced or removed; Elan to follow up with CBOE on liquidity.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1787002323906439 https://mahifx.slack.com/archives/C035H1VNCAD/p1787003951012219 https://mahifx.slack.com/archives/C035H1VNCAD/p1792028629227619 https://mahifx.slack.com/archives/C035H1VNCAD/p1793571986506049

### argamon-relays — Argamon-raised issues relayed from mahi-argamon-operations
status: watching · since: 2026-08-19 · last: 2026-10-09
State: Argamon issues reach this channel as forwards from Daria, William Denny and James. XBTJPY min-size and distribution config was updated (08-19) but Lee found no explicit 0.01 source. On 2026-09-21 Argamon raised an issue that William and James forwarded; its content is not visible in-channel. 2026-10-09 Shyam flagged XAUUSD invalid-increment rejects from B2PRIME, and Lee said he would raise it with Levi in `mahi-argamon-operations`.
Next: Lee to raise the B2PRIME increment rejects with Argamon. Downgraded to watching: no activity for 35 days.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1787118229196849 https://mahifx.slack.com/archives/C035H1VNCAD/p1789997987559629 https://mahifx.slack.com/archives/C035H1VNCAD/p1791507126707139

### arg-chi-disk — Argamon CHI /app/fx/apps/mahifx at 90%
status: watching · since: 2026-10-05 · last: 2026-10-11
State: Disk alert on 2026-10-05. Most space is model weights under `common/var`, plus EBS data that James said can be deleted. On 10-11 Nathan extended the volume by 50GB (422GB of 470GB, about 90%, down to about 80%) rather than the 200GB first proposed. Watching because EBS data deletion and model-weight growth are not confirmed.
Next: someone to delete the EBS data.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1791220309661789 https://mahifx.slack.com/archives/C035H1VNCAD/p1791711442423979

### cme-hedger-chi — hedgerHrpCME1 and COMEX/CME gateway outages on CHI
status: watching · since: 2026-07-21 · last: 2026-09-27
State: hedgerHrpCME1 keeps going down on CHI. On 09-07 a `hedging.rules.profiles.profileDefinitions` edit caused "No rule for converting: XAU to: ZAR", and Leonardo reverted it via the LDN audit log (audit does not replicate between regions). On 08-30 propTrader1HrpChi1 was down after the weekend restart because a profile mapping pointed at expired MGCQ6; Nathan repointed it to MGCZ6. On 09-27 the hedger tripped on order breaches and ordersCME1/ordersCOMEX1 were stuck in starting; Lee left the hedger off, turned it back on, and said he would fix ordersCOMEXMarex1 later.
Next: Lee to fix ordersCOMEXMarex1. Downgraded to watching: no activity for 31 days, outcome unseen.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1784613134154519 https://mahifx.slack.com/archives/C035H1VNCAD/p1788800584804799 https://mahifx.slack.com/archives/C035H1VNCAD/p1790548332936469

### config-breakage — bad config writes stopping processes
status: closed · since: 2026-08-23 · last: 2026-09-13 · closed: 2026-11-13
State: A recurring failure mode is a config write that live processes tolerate but that breaks them at the next restart. On 2026-08-20 a "B2Prime FX" profile with GBPUSD as a Currency asset sat in the store, then took down four distribution/state-monitor processes on LDN and CHI until Sam Hewitt removed it on 08-23. 2026-09-01 pricerInstiLight2 on LDN went down while Elan was changing config. 2026-09-13 Argamon APN1 pricers would not start ("DefaultIndex OMX is not in the name factory"); Daria could not find OMX in config, Lee said he was looking, and Argamon flagged it too. No resolution is visible in-channel.
No activity since 2026-09-13; assumed resolved.
Refs: https://mahifx.slack.com/archives/C035H1VNCAD/p1787462723096659 https://mahifx.slack.com/archives/C035H1VNCAD/p1788223120406549 https://mahifx.slack.com/archives/C035H1VNCAD/p1789286572338989

## Arc
- 2025-09 — CVEX wound down (rebranded Pascal/Jetstream).
- 2025-11-21 — Nado live; markets expanded rapidly through April 2026 (replace workflow 2026-02-23, FX perps 2026-03-26, ETF pricing 2026-03-31).
- 2026-06-15 — Nado wind-down announced; NLP set to Close Only.
- 2026-06-17 — Nado flat, traders/order processes stopped; USDC position closed after an exploit of the passive close-out.
- 2026-06-26 — Argamon Tokyo relaunched on minor coins.
- 2026-07-04 — toa-apnortheast1-prod-sec-1 stopped (no longer needed for Nado).
- 2026-07-16 — Vertex formally closed; crypto-1 AWS box shut down.
- 2026-07-22 — hedgerCBOE1 moved from LDN to Chicago.
- 2026-08-17 — EBS decommission on Argamon CHI removes `EBS_IMP_CHI`; LDN insti pricing indicative.
- 2026-09-26 — 26.4 deployed to Argamon LDN/CHI/APN.
