---
slug: infinox
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/infinox.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: infinox
  hosts: ../MahiProduct/data/client-hosts.json          # entry: infinox
  wiki: ../MahiProduct/wiki/clients/infinox.md
channels:
  internal-infinox: C01QGUXPKEY
  mahi-infinox: C022S6NL82D
contacts:
  - {name: "Clio Constantinou", role: "Infinox sales / risk liaison (FSC EU/CY)", confidence: low}
  - {name: "Georgia Tzyrkalli", role: "Infinox trading ops — arb classification, LR/classification queries; Echo access confirmed 2025-05"}
  - {name: "CH", role: "Infinox sales escalation contact — drives commercial asks (discounts, new LR profiles, crypto intro deal)"}
  - {name: "Kerim Horoz", role: "Infinox London dealing desk — toxic flow triage, LR config, order throttle queries; day-to-day ops contact"}
  - {name: "Sadiq", role: "Infinox trading ops — latency, tick-data and spread queries, MT4/MT5 config", confidence: low}
  - {name: "Andreas Lykotrafitis", role: "Infinox trading desk (night shift) — Echo training attendee", confidence: low}
  - {name: "Andreas Kazelas", role: "Infinox trading ops — Heavy/No LR and Toxic XAUUSD requests", confidence: low}
  - {name: "Aditya", role: "Infinox product/strategy head — Mahi bridge-deal advocate; reported leaving for RCX 2026-10", confidence: low}
last_catchup: 2026-10-29T07:19:59Z
status: active
---

## Now
Gold3X had no price from Sunday's open to ~04:40 UTC 10-26 (engine bug in geared session start tied to next week's US clock change; pricers restarted, ZD 23699), and Infinox then reported XAUUSD spikes Shyam could not see in Mahi's pricing; Infinox wants ticks to escalate to its bridge team.
Custom layered XAUUSD symbol (`XAUUSD.l`) go-live awaits Rory next steps; Isaac's gold LR redesign (+$406k/month modelled, sent 10-21) awaits Infinox, and Isaac chased for an answer on 10-27; routine LR / classification support continues in #mahi-infinox.
Commercially live: CH's crypto-intro deal, plus unpaid invoices since August. Sadiq asked for Echo access for two more users; Kate says Echo is now in Compass and they need Compass logins.

## Streams

### lr-redesign — B_CLIENTS XAUUSD LR redesign proposal
status: open · since: 2026-10-20 · last: 2026-10-27
State: After Trading Ops asked why Toxic XAUUSD Harsher earned little LR, Isaac proposed (10-21) a gold-only channel Burst cut from $8.5M to $2M, a $5/M cap on Default, and Volume Multiplier 5 on Signal Follow, Dynamic Broker, Dynamic Fast Hedge and Centroid, leaving manual profiles untouched. Backtest on 21 Sep-20 Oct says directional flow rises from 2.9 to 10.7 $/M, benign flow falls from 2.5 to 0.15 $/M and total LR goes from $705k to $1,056k a month (+$406k, CI $215k-$566k), matching production on 97-99% of fills; caveats are no client behaviour change and FX/XAG not modelled. Root cause of weak Harsher: the MT5_87952662 flow fans out over ~48 suffixed IDs with per-ID buckets, and small tickets rarely pass the first 100 oz tier. Infinox asked for the full settings, got them in-thread, and said on 10-21 they will review and revert; no reply seen, and Isaac chased in-channel on 10-27 (14:19 UTC) asking for updates on implementing the LR changes.
Next: Infinox Trading Ops to answer Isaac's 10-27 chase and revert; Mahi applies the rebased, schema-validated config only after their go-ahead.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1792578729447559 https://mahifx.slack.com/archives/C022S6NL82D/p1793110786085069

### echo-compass-access — Echo / Compass logins for new Infinox users
status: open · since: 2026-10-26 · last: 2026-10-28
State: On 10-28 Trading Ops asked for Compass access for a further user (Andreas Sofocleous); Isaac found a user already exists and Trading Ops asked for a password-reset link by email. Earlier, Sadiq asked for Echo access for Dmitrii Ponomarev and Alain Saad; Kate replied Echo pages are now integrated into Compass, linked the yield profiles and price forensics screens, and noted neither user has a Compass login yet.
Next: Mahi to send the password-reset link and create Compass logins for the two 10-26 users; Sadiq to say what they want to look into.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1792999339513029 https://mahifx.slack.com/archives/C022S6NL82D/p1793197137096099

### fill-tick-queries — Execution, slippage and raw-tick requests
status: open · since: 2026-07-08 · last: 2026-10-28
State: On 10-28 Trading Ops asked which execution profile suits XAUUSDmini at 0.1-0.2 lots and what the Small Size Fast 10,000 Base Notional means; Isaac explained the rule applies only to orders of USD 10k or less, so 0.1-0.2 lots (~40-80k) hit mid size fast if under 50k, else the catch-all rule, and Trading Ops accepted. William also confirmed Mahi does not execute tag VIDA_MT5__21246122 (no delay). Infinox periodically queries fills and asks for raw ticks (XAUUSD 09-04, 07-15; EURUSD 10-09 on 10-13). On 10-23 Andreas reported an MT5 pricing issue 13:10:12-13:10:28 GMT+3 and Isaac supplied the XAUUSD Price Forensics tick CSV. On 10-26 Andreas reported many XAUUSD spikes (06:23-06:24 GMT+3 and 04:10-04:11 GMT) and asked for ticks; Shyam said Mahi's XAUUSD pricing looked clean at both times and no spikes were visible, ticks were being pulled, and Andreas replied he needs them to escalate to Infinox's bridge team. Rory delivered the EURUSD ticks (full day, then re-cut to 21:00 UTC 10-08..20:59 UTC 10-09) and confirmed bid_price_0/offer_price_0 is TOB. Will Carter noted internally on 10-15 that the reason behind the request is unknown and the team should not be blindsided on pricing; he has discussed it with Rory. Recent explainers: last-look start-vs-end fill rule (09-08), default LR profile burst mechanics for MT5_plain_b_87997401 (10-08).
Next: Mahi to deliver the 10-26 XAUUSD ticks to Andreas; still unknown why Infinox wanted 10-09 EURUSD ticks (26.4 upgrade impact?).
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1791886436475979 https://mahifx.slack.com/archives/C022S6NL82D/p1793195881447619

### xau-x3-gearing — XAUUSDx3 / Gold3x pricing and abuse
status: open · since: 2026-07-21 · last: 2026-10-26
State: Gold3x is built on the post-skew XAUUSD client price, amplifying skew 3x; David and Nathan concluded the fix is an unskewed source (buildGearedPricingNode), and riskPath forms its own mid so analytics.riskpath.formOwnMid would need to be per-instrument. A dedicated Gold3X toxic profile exists. On 09-18 Infinox reverted to a clean 3x and will re-add jitter jointly with Mahi. On 10-26 Andreas reported no Gold3X pricing; Shyam (internal) found none from Sunday's open until ~04:40 UTC, caused by an engine bug in the geared session start triggered by next week's US clock change (Sunday open check thought the session had not started, so no start price loaded); restarting pricers fixed it and Andreas asked for the reason (answered internally, ZD 23699). At 08:12 UTC CH escalated that clients still saw Gold3x frozen; Kate checked the FIX logs, found a live moving XAUUSDx3 price streaming to the PXM MT5 session with no gaps (08:15-08:21 UTC) and asked CH to check or re-subscribe the symbol in PXM; no reply seen. The permanent engine fix is not confirmed. The 07-20 Monday first-tick discrepancy was never closed out.
Next: CH to confirm whether Gold3x is unfrozen in PXM; Mahi to ship the engine fix before the US clock change and tell Infinox the cause; unskewed source fix and jitter re-introduction still unconfirmed.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1784673730662679 https://mahifx.slack.com/archives/C022S6NL82D/p1793003403134579

### lr-profile-ops — Routine LR / execution-profile moves
status: open · since: 2026-05-12 · last: 2026-10-28
State: On 10-28 Andreas Kazelas asked for three MT5_87018814_Centroid accounts to go on Heavy LR and Kate said she would do it. Near-daily requests from Trading Ops to move counterparties between Heavy, Extra Heavy, Medium, Short LL, No LL and Toxic XAUUSD profiles, normally actioned within an hour or so by Isaac, Kate, Rory, William, Shyam, Nathan or Daria. On 10-21 two Centroid accounts went to Heavy LR and the 16 MT5_87952662_* accounts moved from Heavy to Extra Heavy LR (Isaac confirmed 19:38 BST) after Isaac modelled Harsher at 26 $/M, Heavy at 59 and Extra Heavy at 141 on their 30-day flow; one more Centroid account was added to Toxic XAUUSD on 10-22 (Isaac: will action), and MT5_3001867_VidaMarkets_80001857 went to No LL on 10-22 (William confirmed within 9 minutes). On 10-23 Trading Ops asked whether tags INF_MT5__87964749 / MT5_+_b_87964749 sit under a profile and to keep that client on No LR until further notice, and Andreas asked for MT5_87018814_Centroid_3623025 to go to Heavy LR (Kate: will do). On 10-26 Georgia asked whether MT5_87036249_ServiceCom is under any LR profile; Kate found it in none and unclassified, no action needed. Shyam notified that NZ support is on bank holiday Mon 10-26 (emergency cover; email support@ or phone). Medium-vs-Heavy rule order (10-15): rules apply top-down, Kate recommends exclusions first, then harshest to least harsh. Extra Heavy LR (05-21, CH request) and Gold3X profile exist.
Next: Georgia to review rule order and come back to Kate.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1779345609246989 https://mahifx.slack.com/archives/C022S6NL82D/p1792578729447559 https://mahifx.slack.com/archives/C022S6NL82D/p1792649005718889 https://mahifx.slack.com/archives/C022S6NL82D/p1793173780315089

### custom-xau-layers — Custom layered XAUUSD symbol (XAUUSD.l)
status: open · since: 2026-10-19 · last: 2026-10-20
State: Clio asked for a new XAUUSD symbol with client-specific volume and spread layers; CH stressed it is important and Rory promised it for 10-20, with Clio chasing again 08:10 BST. Shyam deployed pricers and a CLIENT_PRICE_L_LDN model (100-4000 oz ladder, no skew or signals) plus a B_CLIENTS_L channel and a `.l` suffix rule (change CHG-2610-EGQJ). Not live: the client distribution gateway needs a restart in a window agreed with Infinox, and Infinox must not enable XAUUSD.l before then.
Next: Rory to reply to Clio, agree the restart window, and get answers on per-layer vs average spreads and lot size; Rory to decide arb protection, skew and LR/WSS settings; change record and approval needed before gateway restart.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1792416827862309 https://mahifx.slack.com/archives/C022S6NL82D/p1792480216320949 https://mahifx.slack.com/archives/C01QGUXPKEY/p1792468132574129

### auto-classification — Automated classification exclusions and LR-by-classification
status: open · since: 2026-07-15 · last: 2026-10-15
State: Infinox repeatedly asks to pull accounts out of automated classifications. Today Georgia asked to remove four accounts (MT5_plain_b_87031851, MT5_CN_.a_b_87946548, MT5_CN_Standard_b_88000123, MT5_CN_.a_b_87953449) from Arbitrageur and "Unclassified Big XAUUSD"; William blacklisted them from Arbitrageur per Tenant profile, then said the Big XAUUSD rule should not hit them since they already carry a classification, and offered to whitelist a fixed classification. Georgia says some trades still executed under Unclassified Big XAUUSD and wants them excluded. Earlier: Centroid_* accounts excluded from Automated Classification (07-15); classifier auto-rehabilitates CPs that are profitable for the book over 24h (10-06); LR rules can use classification criteria (07-23).
Next: William/Mahi to reconcile why Big XAUUSD fired for classified accounts and reply to Georgia.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1784122243791649 https://mahifx.slack.com/archives/C022S6NL82D/p1791239276076609 https://mahifx.slack.com/archives/C022S6NL82D/p1792065605339689

### crypto-intro-deal — CH crypto business for broker intros
status: open · since: 2026-10-06 · last: 2026-10-14
State: CH offered Mahi Infinox's crypto business, with help towards an Infinox crypto licence, if Mahi introduces 2-3 brokers to take the liquidity. Isaac's view: start with XBT and XET, crypto skew PnL maybe 20k-100k p/m, 24/7 XAU raised but not pursued. On 10-14 Isaac said the plan is to introduce CH to Youssef at GCC; Will thinks the candidates are Amana GCC plus one more, preferring brokers without horrendous flow who are flexible and not too big. Velocity was floated earlier.
Next: Isaac and Will to settle 1-2 more broker candidates and make the intros.
Refs: https://mahifx.slack.com/archives/C01QGUXPKEY/p1791283923202179 https://mahifx.slack.com/archives/C01QGUXPKEY/p1791994970744929

### pxm-latency — XAUUSD fill latency dispute with PrimeXM
status: open · since: 2026-10-01 · last: 2026-10-06
State: Infinox says the 2026-09-28 12:04 UTC XAUUSD fill reflects a price about 400ms stale. Mahi (Isaac, Rory): order arrived 12:04:08.138, filled .220 (82ms, within 75-100ms last-look), publishing was normal, Tag 52 is 1-4ms after TransactTime and PXM-to-Mahi sessions average 0.25ms. PrimeXM replied its "received" time is bridge processing time, with delays of up to 381ms across 12:04:07.9-14.5, so the gap sits after Mahi hands off.
Next: Infinox Trading Ops to ask PrimeXM what accounts for the arrival-to-processing delay; they said on 10-06 they would revert. Nothing since.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1790862218777389 https://mahifx.slack.com/archives/C022S6NL82D/p1791251845973249

### compass-26-4-upgrade — 26.3 to 26.4 upgrade and LDN infra move
status: watching · since: 2026-10-08 · last: 2026-10-09
State: Infinox was upgraded from Compass 26.3 to 26.4 over the weekend of 10-09 (approved at RC #7223/#7224, restart at the weekend, monitored over the open); Infinox opted out of the PSM overlays, so no pricing change was intended. A separate infra change moved "infra main" to LDN on 10-09. No post-upgrade fallout reported in channel; the Sadiq EURUSD tick request on 10-13 may be related (see fill-tick-queries).
Refs: https://mahifx.slack.com/archives/C01QGUXPKEY/p1791483335954819 https://mahifx.slack.com/archives/C01QGUXPKEY/p1791558221851879

### index-cfd-spikes — LP-driven spikes on indices and CFDs
status: watching · since: 2026-05-20 · last: 2026-09-18
State: Recurring client complaints about spikes and wide spreads on US30, NAS100, SPX500, JPN225 and BTCUSD, traced to Vantage and B2Broker feed quality; Mahi mitigates via benchmarking and pricing tweaks, most recently lower-quantity rungs (500/1k/2k/4k) for JPN225, implemented 09-18. Vantage's off-market opening ticks (07-13) led Shyam to offer a ~1s indicative suppression, which Infinox never decided on; the BTCUSD B2B/Vantage identical-feed question (07-02) was left unresolved.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1779259961824069 https://mahifx.slack.com/archives/C022S6NL82D/p1789687354550679

### billing-invoices — Unpaid invoices, discounts and volume fee
status: watching · since: 2026-07-02 · last: 2026-09-11
State: After the 07-01 SPX500 feedback-loop incident CH asked for a ~$350k three-bill discount, which Mahi declined (offering a walkthrough and divergence alerting). In August David gave a one-off $40k discount and waived the $25k volume-threshold fee (volume 179/194/191bn May-Jul). Infinox was two invoices behind; on 09-11 their finance asked for patience pending a payment plan, with David expecting settlement the next payment run. Whether the 10% bridge discount still applies is unanswered.
Next: confirm payment received and the bridge-discount answer; nothing seen since 09-11.
Refs: https://mahifx.slack.com/archives/C01QGUXPKEY/p1782992001195759 https://mahifx.slack.com/archives/C01QGUXPKEY/p1789118720343269

### ld-network-incident — LD hosting network incident
status: closed · since: 2026-10-16 · last: 2026-10-16 · closed: 2026-10-19
State: On 10-16 Liam told Infinox of a networking incident in Mahi's LD environment and advised switching to failover if available. Infinox (Sadiq) saw no pricing disruption and Liam said their environment was mostly unaffected; the hosting provider fixed it that day and Georgia confirmed no abnormality.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1792143327385389 https://mahifx.slack.com/archives/C022S6NL82D/p1792150361206559

### fi-party-review — FI signal party correctness by instrument
status: closed · since: 2026-07-06 · last: 2026-07-06 · closed: 2026-10-15
State: No activity since 2026-07-06; assumed resolved. Andrew asked whether pricing.adjustmentSignalProcessFlowImbalanceOptimisationParty is still correct per instrument; Kate said the team would review and change where needed. No confirmation of changes was seen.
Refs: https://mahifx.slack.com/archives/C01QGUXPKEY/p1783353826108009 https://mahifx.slack.com/archives/C01QGUXPKEY/p1783354691007529

## Arc
- 2026-05-15 — Lazaros Zografopoulos (trading desk, arb classification oversight) left Infinox
- 2026-05-21 — Extra Heavy LR profile created at CH's request; volume multiplier doubled 05-22
- 2026-06-19 — Infinox Global left #mahi-infinox; staff now use the Infinox Capital Slack account, channel unaffected
- 2026-06-23 — Infinox reported in advanced talks to acquire Admirals
- 2026-07-01 — SPX500/US30 feedback loop via PXM XCore (Mahi price echoed on 7 LP streams); CH claimed 50+ Insti clients hit; formal incident report sent
- 2026-07-02 — CH asked for a ~$350k discount after the incident; declined
- 2026-07 — recurring skew arbs on EURUSD, USDJPY, EURGBP, AUDUSD mitigated by reducing skew and tightening badCheck; no realtime arb detection
- 2026-07-30 — FI PnL flat two weeks after signal dropped from registry in 07-16 release; Shyam re-added it
- 2026-08-24 — $40k one-off discount and $25k volume fee waived
- 2026-09-21 — Infinox rebrand coverage in trade press
- 2026-10-07 — Aditya, Mahi's bridge-deal advocate at Infinox, reported leaving for RCX
- 2026-10-09 — Compass 26.4 upgrade and LDN infra move
- 2026-10-16 — LD hosting network incident; Infinox unaffected, resolved same day
- 2026-10-19 — Infinox requested a custom layered XAUUSD symbol; pricer and channel built 10-20, go-live pending
- 2026-10-21 — Mahi proposed a gold LR redesign (+$406k/month modelled); Infinox reviewing
