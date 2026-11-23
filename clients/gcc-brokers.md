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
last_catchup: 2026-11-23T08:14:00Z
status: active
---
## Now
GCC is a happy, growing internalising client (record 2bn+ volume week to 11-06, heading for the >6bn/mo billing tier) ("client for life", Will Carter 09-28); the Finalto/LMAX hedger tuning has lifted PnL materially since August.
Live work: LMAX perps (test-traded, not yet live), Amana as a third hedging venue (funded and first hedge trade sent 11-10) and an institutional pricing stream.
On 11-19 Youssef said GCC's flow looks sharp to its LPs since 11-13 and wants to discuss the hedger's order slicing. Finalto became spiky again on 2026-10-14/15 and is being pushed on wider spreads; GCC agreed on the 10-20 call to an Infinox LP intro, but Youssef reacted badly on 10-22 once he learned who it was, so Mahi is walking it back to no pressure. Perps are close to ready. On 10-27 a Mahi tag-blacklist change blocked a client at Finalto on all instruments (reverted in ~15 min); Youssef is jumpy ("no room to trial and error") and Will Carter has told the team to be very careful with anything touching client experience.
On 11-02 a perps demo test by Will Carter hit live LMAX (about $5.5k equity, flattened, no open risk) and exposed incomplete perps execution rules and yield profile setup. A Mahi LD networking incident on 10-16 left GCC's connection down ~2h; Youssef is unhappy and now wants GCC to provision its own main plus standby servers (reply from Rory pending), and GCC awaits the provider's incident report.

## Streams

### lp-position-split — GCC LP positions split across Finalto/LMAX
status: open · since: 2026-11-20 · last: 2026-11-23
State: On 11-20 Will Carter saw GCC's LP positions split Finalto +85k oz XAUUSD, LMAX -80.24k, clients (Dist) -9.96k, called it inefficient and worth getting ahead of; Rory said the only positions GCC trades outside Compass are Finalto fix requests (the daily adjustments) plus a manual trading book used to move positions between LPs; Will then confirmed the HOUSE book is in good shape (he had been looking at the parent book). On 11-23 Daria set expected book status to match actual for the Futs hybrids and asked Rory to check.
Next: Rory to check the Futs hybrid expected book status change.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1795173233350249 https://mahifx.slack.com/archives/C09QS1NUA80/p1795401445168369

### layan-adjustments — Daily Finalto gold fill reports, Compass adjustment
status: open · since: 2026-04-30 · last: 2026-11-20
State: Almost every weekday ~15:00 UTC GCC ops (Layan, lately Nael) posts a gold long (occasionally short, sometimes silver) filled on Finalto (from 11-20 also Amana) and asks Mahi to adjust Compass; Rory, Cameron Hughes, William or Isaac Dann acknowledges and confirms. Since 11-04 Rory answers "will do" within minutes and confirms done same day, though confirmation sometimes lags 1-3 hours (11-20: 2,000 oz at 10:50 and 2,209 oz Finalto plus 2,500 oz Amana at 15:40, both confirmed done within 2h). Earlier confirmation gaps: GCC chased on 09-22, 10-07 and 10-09 (2,572 oz, asked again 10-13); 10-21 (5,508 oz gold plus 69,767 oz silver), 10-27 and 10-29 have no done-confirmation visible. Late on 10-27 Carl posted GCC's LP exposure and Daria found Compass showed 4,081 XAU vs the client's 6,404; positions aligned and Carl confirmed.
Next: Rory/ops to confirm the 10-21 gold and silver adjustment and the 10-09 2,572 oz Finalto gold adjustment to Layan; confirm each adjustment in thread same day.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1786976522444999 https://mahifx.slack.com/archives/C09PNC1MFAA/p1793117803222009 https://mahifx.slack.com/archives/C09PNC1MFAA/p1795195290083309

### sharp-flow-hedging — Youssef: GCC flow "sharp" at LPs, order slicing
status: open · since: 2026-11-19 · last: 2026-11-19
State: Rory forwarded Youssef's overnight message (11-19): after talking to Amana's contact, Youssef says GCC's flow has looked sharp to its LPs since Friday 11-13 (LMAX occasionally, Finalto and its feeds, especially defensive), and wants a discussion with Mahi about how the hedger breaks volume into small pieces to use top of book and "machine guns" orders to the LP; he says fast hedge and short-term intervals are fine. Will Carter's reaction: this is fine because execution can now be tuned from GCC's side, but comms about Amana's view should run between Amana and Youssef.
Next: Mahi to respond to Youssef on the order-slicing question; Rory/Will to decide whether to tune hedger slicing.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1795076441863229

### futures-contract-roll — UKOFUT-F price gap and futures month mappings
status: open · since: 2026-10-23 · last: 2026-11-18
State: On 11-17 at 23:09 UTC Carl Tannous reported USOIL rejected: Finalto mapping USOILG7 is CLG7 (Compass USOFUT-G), which Finalto answered 'unknown symbol' because the subscription went out before Finalto enabled CLG7 (opened 11-17 23:00 UTC); Nathan Burch scheduled a resubscribe for the EOD restart at Carl's choice, and agreed GCC will give advance notice of any intra-week contract opening so a daily-break restart can be scheduled (subscriptions are only sent when the Finalto session logs on, normally the weekend restart). On 11-18 Carl flagged a new silver contract on 11-19 (Finalto SIH7); Nathan confirmed SIH7 is mapped to XAGFUT-H and tomorrow's restart will resubscribe it with CLG7. Earlier: on 10-23 Nael reported no UKOFUT-F price from Mahi while Finalto LCOF7 priced. Isaac Dann found Mahi subscribed to expired LCOF6 and is switching UKOFUT-F to LCOF7; he proposed rolling all futures mappings (Brent, WTI, gas, metals, indices; still on 2026 contracts) to the next live contract so every month is available and two nearest contracts always price together (LCOZ6 and LCOF7 now; LCOF7 and LCOG7 from November). Nael agreed. It needs a short Finalto gateway restart, targeted for next week, and LCOZ6 rolls to LCOZ7 after 30 Oct.
Next: Nathan to restart at the 11-19 EOD and confirm CLG7 and SIH7 are pricing; Isaac to confirm the broader futures mapping roll is applied.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1792744200127579 https://mahifx.slack.com/archives/C09PNC1MFAA/p1794957744613579 https://mahifx.slack.com/archives/C09PNC1MFAA/p1794974329616059

### finalto-execution — Finalto rejections, spikiness and hedger tuning
status: open · since: 2026-07-29 · last: 2026-11-18
State: Finalto fill ratio and rejects have swung. After Aug rejections and throttling (hedger stands down 5s after 500oz of Finalto rejects; LMAX stand-down between waves raised 200 to 500, lifting LMAX fills from 1-3oz to 10-200oz), Finalto removed GCC from its defensive (SOR) tag list and fill rate went from 9-22% to 85-87% with rejects 1,824/day to 12/day (Rory's 09-01 summary); CLIENTS_NET went from +$14.8k/wk to +$44.8k, and Will Carter reported an $80k week on 09-04. On 10-12 the manual Finalto hedger stopped firing because NOP was $87.65m vs an $80m cap; raised to $120m at Nael's request (LMAX limit $80m, $26.58m used). On 10-15 Rory saw Finalto XAUUSD TOB getting spiky since ~13:05 UTC on 10-13 and planned a quick call with Youssef on 10-16 AM to offer an intro to Infinox (unnamed, "a client") as an additional gold LP alongside Finalto and LMAX; On the 10-20 call Youssef and Nael agreed to an exploratory Infinox LP intro (Infinox not named to them; Isaac Dann tagged to pick it up) and said Finalto, after a call just before, is being asked to move spreads wider again and may add a third intermediate feed alongside regular and defensive. GCC stays with Finalto for its London fix access; there was some hesitation on their side about Amana. On 10-22 Rory sent the Infinox intro email to Youssef and Cameron Hughes; Youssef replied he wishes he had been told who it was first, citing bad stories about Infinox (withdrawals, write-offs, client treatment). Internally Andrew Morgan said to walk it back ("GCC's interests are our number 1", preserve integrity over a quick revenue win) and Rory will reply that there is no pressure to move forward, perhaps a catch-up later just to see the offering.
On 11-18 Rory bounced starfishFilePersisterExternalMarketData1, tracking Finalto's systematic feed in the DB.
Next: Rory to send the no-pressure reply to Youssef on the Infinox intro (do not push it); keep watching Finalto behaviour and the third feed.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1785352468874599 https://mahifx.slack.com/archives/C09QS1NUA80/p1792498517091019 https://mahifx.slack.com/archives/C09QS1NUA80/p1792663706559759 https://mahifx.slack.com/archives/C09QS1NUA80/p1795010103395349

### instrument-mappings — Instrument and spread requests
status: open · since: 2026-09-06 · last: 2026-11-18
State: On 11-18 09:11 UTC Nael asked Mahi to subscribe and map three Finalto instruments not yet mapped in Compass (XAUUCNH, XCUUSD, XALUSD); no reply visible yet. DOWUSD was indicative 09-06 to 09-07 because LMAX was not pricing it (pricing again 09-08). Nael then said the DOWJ spread (~150) was tighter than LMAX (~200); Rory widened the beta and then main DOWUSD spreads with Nael's OK and confirmed 09-08, so that is closed. Youssef asked to delete TONUSD on 09-15 (no liquidity) and Cameron Hughes removed it from the overrides; Nathan noted 09-21 the client has not been told it is done. Rory's 08-25 summary also left a VIX proxy and an LMAX trade data request open, no closure seen.
Next: Mahi to map and subscribe XAUUCNH, XCUUSD, XALUSD; tell Youssef TONUSD removal is done; confirm VIX proxy and LMAX trade data request status.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1788764770364529 https://mahifx.slack.com/archives/C09QS1NUA80/p1789480193711279 https://mahifx.slack.com/archives/C09QS1NUA80/p1789973503309009 https://mahifx.slack.com/archives/C09PNC1MFAA/p1794993071759659

### high-var-sustain — High VaR alert sustain setting
status: open · since: 2026-11-17 · last: 2026-11-17
State: Cameron Copland posted internally on 11-17 that the High VaR sustain setting came to GCC with Saturday's 26.4 release; GCC generated 56% of all high VaR pages last week (122 of 218), mostly spikes of a few seconds. Suggested setting monitoring.criticalVarThreshold.sustainMs and clearHoldMs to 60000 (1 min), which on the last 4 weeks would cut GCC's alerts by about 98%. One acknowledgement reaction; not yet confirmed applied.
Next: apply sustainMs/clearHoldMs = 60000 at GCC if agreed.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1794916859626179

### amana-lp — Amana as hedging venue and taker
status: open · since: 2026-09-14 · last: 2026-11-17
State: Amana was set up from 09-14 (XAUUSD and EURUSD mapped, in the beta pricer since late Sep); Nael approved test trades 09-23 and they looked good. GCC hesitated on 10-20, but on 11-06 Rory said he had confirmed with Youssef that Amana comes into the mix the week of 11-09 to help hedging costs overall. On 11-10 Youssef confirmed Amana is funded and flow can start; Rory added Amana to the RPMS, BMSL and MWMS pricers (in line with the beta pricer) and the arb and hybrid hedgers pre-CPI, and the first hedge trade (XAUUSD) went to Amana at 13:03 UTC. On 11-11 Nael asked for a 40M USD NOP limit on Amana (about 10k oz for now) and Rory added it to risk.nop.perMarket and bounced the hedgers. At 00:50 UTC on 11-12 Daria set up hybridHedgerManualAmana1 for position moving and asked Rory to test it once GCC agrees, then give GCC the details. On 11-12 Rory tested the manual Amana setup with 1k EURUSD against LMAX successfully. Youssef checked that Amana symbol mapping covers only XAUUSD, XAGUSD and EURUSD; Rory said yes, other instruments will be scoped shortly, and Youssef will provide Amana's symbol list for subscription. Youssef is thinking of pressuring LMAX and Finalto on TOB and execution; Rory to bring Amana-vs-LP numbers (due 11-13). On 11-13 Youssef asked whether the Amana tag solution is part of the weekend Compass upgrade and Arun confirmed it is (see compass-26-4-upgrade). On 11-17 Will Carter noted the Amana side shows GCC's flow in its own Compass yield profiles and that Amana's contact is struggling to read it; Will said Mahi optimises each Compass treating LPs as an anonymous random panel, so Amana's pricing will be optimised on the same basis.
Next: Rory to send Amana vs LMAX/Finalto performance numbers (11-13) and hand manual-hedger details to GCC; Youssef to supply Amana symbol list; Rory to map remaining instruments.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1789388024317479 https://mahifx.slack.com/archives/C09PNC1MFAA/p1794504876996289 https://mahifx.slack.com/archives/C09QS1NUA80/p1794912752684699

### inst-hedger-deploy — Inst hedger Puppet deploy left broken
status: open · since: 2026-10-30 · last: 2026-11-16
State: The Inst hedger deploy (CHG-2610-2Q0F, Infra-Deploy #640) failed at Puppet on admin-1 on 10-30 from a corrupt Puppet backup entry, so the arbHedgerInst1 Nagios check and nagios/nsca/collectd refreshes did not apply and the Puppet cron is off on both boxes. William Denny brought up hybridHedgerInst1 and arbHedgerInst1 anyway; after a PagerDuty alert Daria left them off on 11-01 as no trades showed under Inst house for the last week (the institutional stream, see insto-pricing, is not trading yet). Nathan logged it on the GCC wiki 11-02. After the 11-14 Compass upgrade Shyam Hari set the expected book state to off for hybridHedgerInst1 and arbHedgerInst1 (11-16 00:07 UTC) and for hybridHedgerPerps1 (11-15 22:43 UTC), so those hedgers stay down until Inst and perps flow start.
Next: Fix the Puppet backup entry and re-run the deploy; Daria to turn the Inst hedgers on when Inst flow starts.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1793380821002989 https://mahifx.slack.com/archives/C09QS1NUA80/p1793602997317929 https://mahifx.slack.com/archives/C09QS1NUA80/p1794787664562689

### pnl-drop-1116 — 2026-11-16 XAUUSD PnL drop, CP 700124
status: open · since: 2026-11-16 · last: 2026-11-16
State: At 05:46:20 UTC on 11-16 CP 700124 sold 3,000 oz XAUUSD into an already falling market; it was internalised and the hedger began selling out within 17 ms across Amana, Finalto and LMAX. Gold fell a further ~$8/oz while the long cleared, flat by 05:46:32, CLIENTS_NET -7.6k in 2 min. The High VaR alert and the Amana cancel-ratio alert (hedger IoCs cancelled in the fast market; Amana still filled 1,900 oz, cancel rate within its normal range) were the same event. Shyam Hari's analysis; no client discussion yet.
Next: none stated; watch 700124.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1794810189330639

### lmax-perps — LMAX perpetual futures integration (XAUUSD-PERP, BTC)
status: open · since: 2026-09-05 · last: 2026-11-15
State: Youssef asked on 09-05 to bring LMAX Perps (separate platform/FIX account, treated as a new LP) into Compass; Mahi needed material FIX/MD changes (deployed in the weekend maintenance window), LMAX conformance was approved by 09-16 (Justin emailed LMAX), a full release went out the weekend of 09-19/20, perps FIX/MD/hedger processes were added 09-25 to 10-01, and Youssef approved 0.1oz test trades which succeeded on 10-01. Depth was widened to LMAX's full 6 layers on 10-01; Rory recommends opening spreads a bit wider than LMAX's ~$0.35-0.40 (about $3 at the 21:00 UTC close). On 10-09 a mapping slip (XAUUSDPERP vs XAUUSD-PERP) was fixed and Nael's 0.1oz test trade hedged to LMAX_PERPS both legs; he asked to test BTC perps next. A weekend dry run on 10-11 succeeded after a reset-sequence fix; hybridHedgerPerps1 and arbHedgerPerps are held off via expectedBookStatus overrides (Rory to revisit the arb hedger this week), so it is not live. On the 10-20 call Rory said perps are more or less ready pending his weekend config and pricing review. On 11-02 ~16:30 UTC an XAU-PERP test on the demo server used a live account and moved PnL; see perps-test-misroute. On 11-15 Shyam Hari set hybridHedgerPerps1 expected book state to off. GCC wants a dedicated channel with wider markups and weekend LR; the Saturday 12:00-13:00 GMT+3 maintenance window is agreed because perps run 24/7.
Next: Rory to finish config/pricing review, hedger config, BTC-PERP pricing/test and set a go-live date; GCC to fund the perps account.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1788610242999719 https://mahifx.slack.com/archives/C09PNC1MFAA/p1790845208134599 https://mahifx.slack.com/archives/C09PNC1MFAA/p1793637180588499 https://mahifx.slack.com/archives/C09QS1NUA80/p1794782597326859

### volume-tier — Record volume week, NFP positioning and billing tier
status: open · since: 2026-11-06 · last: 2026-11-06
State: On 11-06 Will Carter called it a storming week; Rory said GCC trades over 2bn so far this week, which if repeated across the month reaches the next billing tier (above 6bn a month). Into NFP he saw nothing needing change ("pure dependence on the whales"); Will floated brokering to go low risk and Rory said he would raise it with GCC. Post-NFP the book took a ~5k PnL drop, with tag 4004532 flow a bit sharper than usual.
Next: Rory to raise the low-risk/brokering option with GCC; watch 4004532 flow.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1793969013807299 https://mahifx.slack.com/archives/C09QS1NUA80/p1793976030377669

### defensive-feeds — LMAX and Finalto defensive feeds and news hedging
status: open · since: 2026-08-19 · last: 2026-11-05
State: Will added a news hedging rule on 09-04 after a 26s window with no hedge at NFP; the hedger's News config went from 40s to 60s and added both defensive feeds on 09-11 (about +$17k on CPI). Nael approved Finalto defensive test trades 09-15; the first was rejected ("Account not enabled on the gateway", defensive session GCC_Brokers5) until Youssef supplied the right Finalto account id, and buy/sell succeeded 09-17, confirmed by both sides. On 09-21 Nael said two tags had been moved again to Finalto SOR, so William set up Finalto defensive in the pool, blacklisted tags 334380 and 700154 from core Finalto and added 334380 to the defensive-feed execution rules (Finalto defensive in executionMarkets 09-22). On 10-26 Nael said Finalto had moved tag 700154 from its defensive feed back to its main feed again and asked Mahi to mirror it; William made the change on the Finalto side and, per Nael, left the LMAX leg of 700154 on the LMAX main feed.
On 11-02 Nael asked to add tags 8000031, 4004152, 4002083, 4004357 and 4004482 to the defensive feed and move 4004072 and 700106 back to the main feed; Youssef said only Finalto (not LMAX) had changed them, Rory first asked if it applied to both venues, then corrected himself and adjusted. On 11-05 Nael asked to move tag 4004530 from the main feed to defensive; Rory actioned it. On 10-27 Finalto moved tag 4004532 to defensive and the mirror went wrong (see finalto-tag-blacklist).
Next: Rory to confirm the 11-02 tag moves are applied; watch for Finalto moving tags between feeds again.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1788519496962869 https://mahifx.slack.com/archives/C09PNC1MFAA/p1789470718891469 https://mahifx.slack.com/archives/C09PNC1MFAA/p1793024358924139 https://mahifx.slack.com/archives/C09PNC1MFAA/p1793872842787499

### perps-test-misroute — 2026-11-02 XAU-PERP demo test hit live LMAX
status: open · since: 2026-11-02 · last: 2026-11-02
State: From ~16:33 UTC on 11-02 Isaac Dann saw NOT_ENOUGH_FUNDS rejects on LMAX XAU perps and Rory asked Youssef about unexpected trades from tag 4012 with a sizeable PnL gain. It turned out Will Carter had tested the perps setup on the demo server with the wrong demo account, so orders went to live LMAX (about $5.5k equity lost on LMAX Perps; Will asked that the PnL be waived/written off). GCC confirmed no open LMAX perps position and Mahi flattened the books to undo the PnL spike. Will's review: the perps execution rules lacked their own section and trading account and defaulted to broker-first (agreed behaviour is internalise and hedge), and test trades had no yield profiles to show classifier routing; Isaac added the tag to partyToTradeTypeMapping. Will resolved it at 17:18 UTC: no open risk, system brought in line.
Next: finish yield profile setup for XAUUSD-PERP; Will to review sign-off and change-management procedures.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1793637180588499 https://mahifx.slack.com/archives/C09QS1NUA80/p1793639896746729

### finalto-tag-blacklist — 2026-10-27 tag 4004532 blacklist rejects
status: open · since: 2026-10-27 · last: 2026-10-28
State: On 10-27 Finalto moved tag 4004532 to its defensive feed; Youssef asked Mahi to mirror it while disputing the decision with Finalto (markouts healthy, just a sharp day or two). Isaac Dann agreed markouts are generally fine (~$50/M decay over 10s, dampened by high spread paid) but found the hedger trading client risk under the client's tag gives Finalto a more toxic view (house +72.39 $/M, broker -42.78, hybrid -23, arb -13), so he added 4004532 to the Finalto tag blacklist for the hedgers. That change blacklisted the client from Finalto for all instruments: from ~12:34 UTC tag 4004402 and USOIL were rejected ("reason expired"), GCC routed the client to Finalto directly, and Isaac scoped the blacklist to hedgers only and reverted both tags by 12:50 (dynamic config, broker process confirmed). Youssef: 4004532 would have been critical had it traded; 4004402 saw many rejects before a fill; he wants no inconsistencies on non-gold instruments. Will Carter internally asked for no more silly mistakes. On 10-28 evening Nael asked whether 4004532 was filling on the LMAX main feed rather than defensive; Shyam Hari explained the tag is in the defensive execution rules but those also require Signal Follow or Broker classification, which it lacks, so it is internalised on the G8/XAU/XAG/indices/oil rule and fast-hedged out; removing the classification condition would always broker it to the defensive pools. Youssef (Finalto matters, LMAX did not complain) said "keep as is".
Next: Isaac to watch closely; Mahi to confirm to GCC it is safe to route back via Compass (GCC will match open exposure) and whether Finalto reverts 4004532.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1793100261800059 https://mahifx.slack.com/archives/C09PNC1MFAA/p1793105234041459 https://mahifx.slack.com/archives/C09QS1NUA80/p1793105896213549 https://mahifx.slack.com/archives/C09PNC1MFAA/p1793223520570629

### insto-pricing — Institutional pricing stream
status: watching · since: 2026-10-06 · last: 2026-10-21
State: No Slack activity since 10-21; downgraded to watching, feed completion not confirmed. On a 10-06 call Youssef and Nael said GCC is now targeting institutional client flow (none of the current counterparties are STP brokers), so Mahi must match or beat the insto clients' current offering. Plan is a new channel and pricer for insto pricing aimed at capturing flow even if initial PnL per account is lower. GCC will send the parameters they see today. On 10-20 Rory confirmed the institutional feed is still to be set up, with a deeper TOB aimed at volume rather than PnL, and aims to finish it before end of week. On 10-21 Rory posted change record CHG-2610-VR2K (two pricers for an institutional stream plus infra backlog, 15:15-16:00Z), approved by Liam Cordelle.
Next: Rory to finish the insto feed by EOW; GCC to send pricing parameters if not yet sent.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1791287464442599 https://mahifx.slack.com/archives/C09QS1NUA80/p1792594740438909

### ld-network-incident — 2026-10-16 LD networking outage
status: watching · since: 2026-10-16 · last: 2026-10-20
State: No Slack activity since 10-20; downgraded to watching with the standby/server-provisioning reply and provider incident report still not visible. On 10-16 at 10:31 BST Liam Cordelle told GCC of a networking incident in Mahi's LD environment and advised failing over if possible. Liam said resolved at 12:30 (GCC confirmed stable 11:55); GCC had switched flow directly to its LPs and disabled Mahi as a provider meanwhile. Nael (12:39) said the connection was down about 2 hours, called it very disappointing after a long stable run, and asked for confirmation before re-enabling Mahi. Liam confirmed at 12:40 that the hosting provider had fixed it and that incident details would follow once the provider supplies them. Youssef's follow-ups (Fri 10-16, forwarded by Rory 10-19) say he is unhappy: GCC had fallbacks so was fine, but as the broker it would bear any consequences. He recalls being steered to Mahi/Beeks rather than provisioning his own servers at ThinkHuge, and his backup-server idea going unprioritised. He now prefers to provision a main and a standby server on GCC's side, with Mahi access unchanged, and asks whether a standby would have let Mahi fail over. Rory confirmed on Friday it was Beeks-related. On the 10-20 call Rory assured Youssef and Nael a full operational review is under way and a fuller picture will follow; Youssef said he chose ThinkHuge over Beeks for his own servers and that service has been excellent.
Next: Rory/Liam to answer Youssef on the standby/failover and server-provisioning proposal; send the provider's incident report; confirm GCC has re-enabled Mahi.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1792143095130599 https://mahifx.slack.com/archives/C09QS1NUA80/p1792147398651509 https://mahifx.slack.com/archives/C09QS1NUA80/p1792417622069019 https://mahifx.slack.com/archives/C09QS1NUA80/p1792498517091019

### platform-ops — Stability, maintenance windows, access
status: watching · since: 2026-08-23 · last: 2026-10-11
State: Sunday checks on 08-23 found clientDistributionGateway1 and systemStateMonitor down from a notionalCap config error (fixed). Maintenance moved to Saturday 09:05 UTC (admin) and 09:25 UTC (trading) to fit the LMAX window at 12:00 GMT+3; Youssef agreed the window 09-07 (anything longer must be pre-scheduled with notice to GCC's clients). Liam Cordelle raised the no-weekend-support gap on 09-08 but dropped it as not significant once Rory showed the reboot only moved ~2h; GCC may want weekend support as perps go 24/7. Dashboard logins failed on 09-06 (FXCubic provider offline) and on 09-20 (connection-limit too low for GCC's number of books, fixed by Sam). Whitelist for Youssef's additional IP was requested and actioned 10-11.
Next: revisit weekend support if perps go live.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1787462534322929 https://mahifx.slack.com/archives/C09PNC1MFAA/p1789932675132249 https://mahifx.slack.com/archives/C09PNC1MFAA/p1791751897689189

### compass-26-4-upgrade — Compass 26.4 upgrade (CHG-2611-542H)
status: closed · since: 2026-11-13 · last: 2026-11-14 · closed: 2026-11-20
State: Upgrade completed successfully 11-14 (Amana tag solution included); verification checks were due 11-17, no issue raised.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1794567605273569 https://mahifx.slack.com/archives/C09PNC1MFAA/p1794679489112679

### lmax-price-outage — 2026-10-29 LMAX pricing gap
status: closed · since: 2026-10-29 · last: 2026-10-29 · closed: 2026-11-20
State: LMAX pricing gap of ~16 min on 10-29 recovered; cause not stated; no recurrence seen.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1793285629414699 https://mahifx.slack.com/archives/C09PNC1MFAA/p1793285935629259

### lmax-xau-limit — LMAX XAUUSD max-position rejects
status: closed · since: 2026-10-26 · last: 2026-10-26 · closed: 2026-11-20
State: GCC raised its LMAX XAUUSD limit and shifted volume to Finalto on 10-26; no further rejects reported; assumed resolved.
Refs: https://mahifx.slack.com/archives/C09PNC1MFAA/p1792985886827929 https://mahifx.slack.com/archives/C09PNC1MFAA/p1792990642060759

### si-book — Systematic internaliser book
status: closed · since: 2026-07-03 · last: 2026-09-15 · closed: 2026-11-16
State: No activity since 09-15; assumed resolved. SI live from 07-24 (200oz XAUUSD cap, thin flow); 09-15 moved to inclusion-tagged. Review doc in MahiProduct (2026-09-15-si-review-default-in-vs-out.md).
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1784780445088809 https://mahifx.slack.com/archives/C09QS1NUA80/p1789491725123129

### flow-toxicity — Large-order tags 700106 / 700154
status: closed · since: 2026-08-06 · last: 2026-09-14 · closed: 2026-11-16
State: No activity since 09-14; assumed resolved. Tag 700106 cost $6k on 08-18 and was answered with a DYNAMIC-LARGEORDER hedger rule and a 700106 LR profile; Youssef chose to keep internalising. 09-14 a 3k oz 700154 trade lost $4k; Rory relabelled it brokered, fine for now.
Refs: https://mahifx.slack.com/archives/C09QS1NUA80/p1786023089729289 https://mahifx.slack.com/archives/C09QS1NUA80/p1787674237025029 https://mahifx.slack.com/archives/C09QS1NUA80/p1789347578163429

## Arc
- 2026-04-23 — CFD internalisation go-live list proposed; live 2026-05-07
- 2026-05-15 — XAGUSD ~45k oz unhedged ~90 min (~$70k loss); post-mortem 05-18
- 2026-06-22 — post-pilot volume-band commercial options drafted
- 2026-07-22 — commercial terms locked for 12 months
- 2026-08-07 — fully signed contract received
- 2026-09-01 — hedger and 700106 improvements: Finalto fill rate 85-87%, best PnL week to date
- 2026-09-07 — Youssef: "much better shape compared to a year ago"
- 2026-10-01 — LMAX perps test trades succeeded; perps go-live pending funding
- 2026-10-16 — LD networking incident, GCC down ~2h, flow moved to its LPs
