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
last_catchup: 2026-10-20T07:17:56Z
status: active
---

## Now
Clio and CH want a custom layered XAUUSD symbol (`XAUUSD.l`) urgently; Shyam built the pricer and channel overnight and handed go-live (gateway restart, Infinox mapping, decisions) to Rory, while Clio chased again this morning.
Day-to-day is routine LR / classification support via #mahi-infinox; open items are the four-account classification exclusion and overlapping Medium/Heavy LR rule order.
Commercially live: CH's crypto-intro deal, plus unpaid invoices since August. Sadiq's EURUSD tick request after the 26.4 upgrade is still unexplained.

## Streams

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

### lr-profile-ops — Routine LR / execution-profile moves
status: open · since: 2026-05-12 · last: 2026-10-15
State: Near-daily requests from Trading Ops to add or move counterparties between Heavy, Extra Heavy, Medium, Short LL, No LL and Toxic XAUUSD Harsher profiles, normally actioned within an hour or so by Kate, Rory, William, Shyam, Nathan or Daria. Today Georgia moved MT5_87986241_Cov from Medium to Heavy LR (Kate done 10:38 BST) and asked how an account in both Medium and Heavy resolves. Kate: rules apply top-down in the config editor, so Medium above Heavy wins; she recommends exclusion/reduced rules first, then harshest to least harsh, and offered to reorder. Extra Heavy LR (created 05-21 at CH's request, volume multiplier doubled 05-22) and Gold3X profile exist.
Next: Georgia to review rule order and come back to Kate.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1779345609246989 https://mahifx.slack.com/archives/C022S6NL82D/p1792056769953769 https://mahifx.slack.com/archives/C022S6NL82D/p1792057099943739

### fill-tick-queries — Execution, slippage and raw-tick requests
status: open · since: 2026-07-08 · last: 2026-10-15
State: Infinox periodically queries fills and asks for raw ticks (XAUUSD 09-04, 07-15; EURUSD 10-09 on 10-13). Rory delivered the EURUSD ticks (full day, then re-cut to 21:00 UTC 10-08..20:59 UTC 10-09) and confirmed bid_price_0/offer_price_0 is TOB. Will Carter noted internally on 10-15 that the reason behind the request is unknown and the team should not be blindsided on pricing; he has discussed it with Rory. Recent explainers: last-look start-vs-end fill rule (09-08), default LR profile burst mechanics for MT5_plain_b_87997401 (10-08).
Next: Mahi to work out why Infinox wanted 10-09 EURUSD ticks, i.e. whether the 26.4 weekend upgrade had pricing impact.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1791886436475979 https://mahifx.slack.com/archives/C01QGUXPKEY/p1792057675397809

### crypto-intro-deal — CH crypto business for broker intros
status: open · since: 2026-10-06 · last: 2026-10-14
State: CH offered Mahi Infinox's crypto business, with help towards an Infinox crypto licence, if Mahi introduces 2-3 brokers to take the liquidity. Isaac's view: start with XBT and XET, crypto skew PnL maybe 20k-100k p/m, 24/7 XAU raised but not pursued. On 10-14 Isaac said the plan is to introduce CH to Youssef at GCC; Will thinks the candidates are Amana GCC plus one more, preferring brokers without horrendous flow who are flexible and not too big. Velocity was floated earlier.
Next: Isaac and Will to settle 1-2 more broker candidates and make the intros.
Refs: https://mahifx.slack.com/archives/C01QGUXPKEY/p1791283923202179 https://mahifx.slack.com/archives/C01QGUXPKEY/p1791994970744929

### compass-26-4-upgrade — 26.3 to 26.4 upgrade and LDN infra move
status: watching · since: 2026-10-08 · last: 2026-10-09
State: Infinox was upgraded from Compass 26.3 to 26.4 over the weekend of 10-09 (approved at RC #7223/#7224, restart at the weekend, monitored over the open); Infinox opted out of the PSM overlays, so no pricing change was intended. A separate infra change moved "infra main" to LDN on 10-09. No post-upgrade fallout reported in channel; the Sadiq EURUSD tick request on 10-13 may be related (see fill-tick-queries).
Refs: https://mahifx.slack.com/archives/C01QGUXPKEY/p1791483335954819 https://mahifx.slack.com/archives/C01QGUXPKEY/p1791558221851879

### pxm-latency — XAUUSD fill latency dispute with PrimeXM
status: open · since: 2026-10-01 · last: 2026-10-06
State: Infinox says the 2026-09-28 12:04 UTC XAUUSD fill reflects a price about 400ms stale. Mahi (Isaac, Rory): order arrived 12:04:08.138, filled .220 (82ms, within 75-100ms last-look), publishing was normal, Tag 52 is 1-4ms after TransactTime and PXM-to-Mahi sessions average 0.25ms. PrimeXM replied its "received" time is bridge processing time, with delays of up to 381ms across 12:04:07.9-14.5, so the gap sits after Mahi hands off.
Next: Infinox Trading Ops to ask PrimeXM what accounts for the arrival-to-processing delay; they said on 10-06 they would revert. Nothing since.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1790862218777389 https://mahifx.slack.com/archives/C022S6NL82D/p1791251845973249

### xau-x3-gearing — XAUUSDx3 / Gold3x pricing and abuse
status: watching · since: 2026-07-21 · last: 2026-09-18
State: Gold3x is built on the post-skew XAUUSD client price, amplifying skew 3x; David and Nathan concluded the fix is an unskewed source (buildGearedPricingNode), and riskPath forms its own mid so analytics.riskpath.formOwnMid would need to be per-instrument. A dedicated Gold3X toxic profile was created and CPs added (09-11..15). On 09-18 Infinox said jitter spikes were landing in clients' favour, so they reverted to a clean 3x and will re-add jitter in a controlled way with Mahi; CH asked for a call before a sales push. Gold3x multiplies LR quantity 3.5x with 100k USD per 5s replenishment. The 07-20 Monday first-tick discrepancy (01:10 vs 01:00) was never closed out.
Next: code fix for the unskewed source and the joint jitter re-introduction are not confirmed; quiet since 09-18, downgraded to watching (no concrete pending action seen).
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1784673730662679 https://mahifx.slack.com/archives/C01QGUXPKEY/p1789727821608629

### index-cfd-spikes — LP-driven spikes on indices and CFDs
status: watching · since: 2026-05-20 · last: 2026-09-18
State: Recurring client complaints about spikes and wide spreads on US30, NAS100, SPX500, JPN225 and BTCUSD, traced to Vantage and B2Broker feed quality; Mahi mitigates via benchmarking and pricing tweaks, most recently lower-quantity rungs (500/1k/2k/4k) for JPN225, implemented 09-18. Vantage's off-market opening ticks (07-13) led Shyam to offer a ~1s indicative suppression, which Infinox never decided on; the BTCUSD B2B/Vantage identical-feed question (07-02) was left unresolved.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1779259961824069 https://mahifx.slack.com/archives/C022S6NL82D/p1789687354550679

### billing-invoices — Unpaid invoices, discounts and volume fee
status: watching · since: 2026-07-02 · last: 2026-09-11
State: After the 07-01 SPX500 feedback-loop incident CH asked for a ~$350k three-bill discount, which Mahi declined (offering a walkthrough and divergence alerting). In August David gave a one-off $40k discount and waived the $25k volume-threshold fee (volume 179/194/191bn May-Jul). Infinox was two invoices behind; on 09-11 their finance asked for patience pending a payment plan, with David expecting settlement the next payment run. Whether the 10% bridge discount still applies is unanswered.
Next: confirm payment received and the bridge-discount answer; nothing seen since 09-11.
Refs: https://mahifx.slack.com/archives/C01QGUXPKEY/p1782992001195759 https://mahifx.slack.com/archives/C01QGUXPKEY/p1789118720343269

### fi-party-review — FI signal party correctness by instrument
status: closed · since: 2026-07-06 · last: 2026-07-06 · closed: 2026-10-15
State: No activity since 2026-07-06; assumed resolved. Andrew asked whether pricing.adjustmentSignalProcessFlowImbalanceOptimisationParty is still correct per instrument; Kate said the team would review and change where needed. No confirmation of changes was seen.
Refs: https://mahifx.slack.com/archives/C01QGUXPKEY/p1783353826108009 https://mahifx.slack.com/archives/C01QGUXPKEY/p1783354691007529

### ld-network-incident — LD hosting network incident
status: closed · since: 2026-10-16 · last: 2026-10-16 · closed: 2026-10-19
State: On 10-16 Liam told Infinox of a networking incident in Mahi's LD environment and advised switching to failover if available. Infinox (Sadiq) saw no pricing disruption and Liam said their environment was mostly unaffected; the hosting provider fixed it that day and Georgia confirmed no abnormality.
Refs: https://mahifx.slack.com/archives/C022S6NL82D/p1792143327385389 https://mahifx.slack.com/archives/C022S6NL82D/p1792150361206559

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
