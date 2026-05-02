---
slug: infinox
refs:
  vibepulse: ../VibePulse/.claude/clients/infinox.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: infinox
  hosts: ../MahiProduct/data/client-hosts.json          # entry: infinox
  wiki: null                                             # ../MahiProduct/wiki/clients/infinox.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Clio Constantinou", role: "Infinox sales / risk liaison (FSC EU/CY)", confidence: low}
  - {name: "Georgia Tzyrkalli", role: "Infinox trading ops — arb classification / blacklist queries; Echo access confirmed 2025-05"}
  - {name: "CH", role: "Infinox sales escalation contact — keen on white-label bridge; internal Mahi advocate for bridge deal"}
  - {name: "Lazaros Zografopoulos", role: "Infinox trading desk — arb classification PnL oversight, pricing oversight"}
  - {name: "Kerim Horoz", role: "Infinox London dealing desk — toxic flow triage, LR config, order throttle queries; primary day-to-day ops contact"}
  - {name: "Sadiq", role: "Infinox trading ops — XAUUSD spread complaints, MT4/MT5 config queries", confidence: low}
  - {name: "Andreas Lykotrafitis", role: "Infinox trading desk (night shift) — Echo training attendee", confidence: low}
  - {name: "Aditya", role: "Infinox new hire ~2mo as of 2025-07 — B2B focus, internal advocate for Mahi bridge; surname unknown", confidence: low}
last_catchup: 2026-05-02T07:28:42Z
---

## Recent issues

> [resolved] 2025-07-02 — Arb signal manipulation via ms-duration trades: CP 86043118 added to whitelist
> Daily checks flagged Infinox FX at −$725K (−$78/M) on $9.3B with arb CPs −$625 and EURUSD FI −$406. Sam Hewitt traced to CP 86043118 manipulating the FI signal by taking ms-holding-period XAUUSD trades to skew pricing, then trading at favourable continuity-pool prices while Mahi was offside. Added 86043118 to the Arbitrageur FX B-Book whitelist. [permalink](https://mahifx.slack.com/archives/C01QGUXPKEY/p1751497632525109)

> [resolved] 2025-07-11 — Party structure + drop-copy topology to be clarified on upcoming call
> David Cooney flagged need to clarify Infinox's party structure (which flow arrives via which drop-copy FIX session). Mio Knights agreed to raise on the next call. Separately, Echo credentials issued to Infinox users 2025-07-09 (Amir confirmed sent). [permalink](https://mahifx.slack.com/archives/C01QGUXPKEY/p1752229175947479)

> [open] 2025-07-02 — Bridge upsell: CH confirmed interest; Aditya call productive; deal not yet scoped
> Mahi bridge pitch has been building since April (Amir drafted April-15 narrative: replace PXM at ~$40K/M and YourBourse crypto whitelabel; bridge is 25c vs PXM's 50c). Will met CH in Cyprus 2025-06-19: CH very interested in white-label bridge for institutional business — asked to "validate bridge in our environment first." YourBourse described as worthless ("f8ck all flow"). Aditya (new Infinox hire, ~2mo in, B2B focus) met Andrew Morgan 2025-07-02: productive call, bridge raised, crypto licence + FI cap noted as expansion levers; Aditya recommends also engaging CH more. Aditya is too early for a commercial deal but is a strong internal advocate. CH eyes lit up on whitelabel optionality per Will (2025-07-02). No formal proposal or timeline agreed. [permalink](https://mahifx.slack.com/archives/C01QGUXPKEY/p1750321004954889)

> [resolved] 2025-06-13 — May billing understated by CFD skew PnL
> Andrew flagged May's bill likely understates by the CFD skew PnL (billing thread in #commissions). Confirmed understated with Bonnie. April CFD skew ~$55.7K, March $7.3K — same methodology may have missed those. Andrew noted some leniency may apply for Mar/Apr if CFDs weren't fully live then. [permalink](https://mahifx.slack.com/archives/C01QGUXPKEY/p1749824752223979)

> [resolved] 2025-06-03 — ADS/IS Prime reference-market lag distorting yield profiles + offside XAUUSD fills
> Amir identified ADS and IS Prime running >500ms behind Mahi's pricing model, making yield profiles look worse than they were (fills appearing "offside" vs lagged reference markets, not vs actual model price at execution). Fix: FX riskPaths reconfigured to use same markets as FX pricers; bounced 2025-06-03. Offside XAUUSD trades confirmed as no clear arb pattern (tags trading across price moves, not systematic). Will flagged Infinox want spreads as tight as Vantage — rationale questioned internally. [permalink](https://mahifx.slack.com/archives/C01QGUXPKEY/p1748942380107489)

> [resolved] 2025-05-27–29 — XAUUSD spread complaint: Mahi wider than Vantage on MT4; resolved by TOB revert + spread drop
> Sadiq complained 2025-05-27 that Mahi XAUUSD spread was higher than Vantage (Vantage 4pip, Mahi floor 8pip). Clients already complaining. Internal debate: Amir warned halving TOB spread would substantially cut spread revenue; Will questioned rationale (Vantage tightening doesn't make it right). MT4-specific issue identified: clients seeing 2nd tier instead of TOB — PXM bridge suspected (MT5 fine). Amir tightened second tier as temporary fix; TOB reverted to 100 (from 50) and Amir dropped XAUUSD base spread by further pip to $0.04 TOB. Sadiq confirmed resolved 2025-05-29. [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1748417607237339)

> [resolved] 2025-05-21 — API client 87899203 XAUUSD toxic flow — STP only viable option
> Kerim flagged API client 87899203 sending toxic XAUUSD flow (>$5K profit in <30s trigger). David confirmed: yield profiles initially sharp but revert, only 3 sets of risk, overall PnL marginally positive. Amir concluded: flow −ve 1-2min out, even 10x LR spread can't save it, B-booking too risky; STP only realistic but LP would likely reject. Tag issue also blocking (PXM FIX tag 448 missing for some API clients — code 526 workaround still pending from Kerim). No action taken; Kerim to provide more tagging info. [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1747816500994819)

> [resolved] 2025-05-19 — Echo demo + training session held (Georgia Tzyrkalli)
> CH requested Echo demo 2025-05-16 for Georgia + Andreas; CH/Andreas no-showed 2025-05-19 call. Georgia attended. Will shared training materials and counterparty PnL time-series analysis card. Will flagged internally: Georgia's LinkedIn does not show Infinox employment (regulator concern noted — caution around "skew" language). Georgia invited to #mahi-infinox 2025-05-20 per CH's request; confirmed her @infinox.com address. Echo credentials issued to Georgia 2025-05-22. [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1747664819977889)

> [resolved] 2025-05-08 — EURUSD order burst from 87906376 + 87049913: PD queue overflow alerts
> Daria flagged ~1K EURUSD orders in 1h from CPs 87906376 and 87049913 triggered two PagerDuty alerts (clientDistributionGateway1 queue depth 769/1024, request publisher overflow). Latency spikes visible but not severe. Both CPs were already throttle-listed; Daria extended throttle config to include them. Liam noted Infinox infra generally un-tuned; no further action required at the time. [permalink](https://mahifx.slack.com/archives/C01QGUXPKEY/p1746671103701289)

> [resolved] 2026-04-30 — Lazaros call on classification/arb-profile PnL contribution
> Call held 2026-05-01 at 2pm UK (Kate, Will with Lazaros). Lazaros' core question: is the PnL saved by arb classification worth the volume of client complaints? Will's call notes: ~800 arb-classified accounts, ~463 dormant (Kate's post-call count). Agreed to reduce classification intensity via config (done — see arb classifier threshold tightening issue below). LR Overview call agreed for next week. Outstanding analytical question: does arbing on one instrument justify worsened execution on all instruments? [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1777619106120579)

> [resolved] 2026-04-29 — Georgia asked for FX vs CFD B-Book blacklist clarification
> Follow-up to the unflag action: Georgia checked the CFD B-Book blacklist and couldn't see the 13 unflagged accounts; Kate's link pointed at the FX B-Book blacklist. Nathan explained classifications are per tenant profile — 12 of the 13 trade on FX B-Book and were added there; one (87939648) trades on CFD B-Book and went on the CFD B-Book arb blacklist. Kate closed the remaining gap on 2026-04-30: MT5_+_b_87956983 had also been picked up on the PXM-Book tenant (via drop copy) and was re-blacklisted there; remaining accounts from the provided list also blacklisted for completeness. [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1777561876.618799)

> [resolved] 2026-04-28 — Slippage complaint storm on 18 EURUSD/B_CLIENTS logins; arb-classifier false positives
> Clio escalated (CH bumped to "max priority" — multiple sales teams complaining simultaneously) about clients seeing observable slippage on EURUSD market orders and SL/limit fills, in group `FSC\INF\ZEROF02M02_MMM_USD` (markdown group). David Cooney took the call with Clio; Kate produced a per-account breakdown — 13 of 18 were arb-classified (force-internalised at continuity-pool mid + flat markup) on small-negative spread-yield false positives, 5 non-arb saw last-look-driven slippage (notably 200ms LL on Unclassified Big XAUUSD; e.g. 87939648 LL=66%, 87946983 LL=50%). Will's analysis (`y60m`) confirmed classifier thresholds too sensitive — e.g. 87928871/87947068/87957409/87957449/87957488 are arb-flagged but long-horizon profitable to the book. EURUSD-specific cut (last 7d) showed only 87932042 ($139M, "don't b book", LL 29% / LR 11%) and 87957488 ($9M, arb) had material EURUSD volume; the rest are tiny tickets, so the EURUSD framing is misleading — wider 28d table is the right lens. Will also confirmed Compass has no `markdown` config — the `FSC\INF\ZEROF02M02_MMM_USD` markdown sits on Infinox's MT plugin side and doesn't feed our classifier. Georgia requested the 13 arb accounts be unflagged as a temporary fix; Kate actioned it (added to FX B-Book / CFD B-Book Arbitrageurs blacklists). [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1777355727656879)

> [open] 2026-04-28 — B_CLIENTS LR config layer review — actions outstanding
> While investigating the slippage complaint, Will pulled 7d of B_CLIENTS yieldprofile ($39.5B notional) against the LR config and surfaced layering issues: channel ≈ global on burst (global effectively dormant), CP-Default rate equals channel rate (CP rule never binds first), Toxic XAUUSD `maxRed=250` silently clipped to channel ceiling 200, no timezone differentiation despite XAUUSD spreads blowing 10–20× at ROLL. Heavy LR (volMult 25) is working ($45.85/M, 50% hit, ~$45K/wk on $989M); Toxic XAUUSD barely fires (5 of 9 CPs stale, 2 of 4 active are long-horizon profitable signal-followers); No LR exemption is dead (all 15 CPs absent from B_CLIENTS — one active member trades only on PXM_GU_CLIENTS / BBOOK_CFD_VANTAGE); Reduced LR too soft (y60m −$153/M with hit rate 0.5%). Proposed: ROLL-specific channel profile (burst 1M, rate 200k/500ms, volMult 1.5) + lift channel maxRed to 250, drop CP-Default rate to 300k/s, drop 5 stale Toxic XAUUSD CPs, sunset/migrate No LR profile, promote 2 underperformers from Reduced LR → Medium/Heavy. Will offered (a) identify specific Reduced LR CPs to promote, (b) re-run Toxic XAUUSD over 30d, (c) draft Compass JSON patch — no decision in window. [permalink](https://mahifx.slack.com/archives/C01QGUXPKEY/p1777368117734019)

> [open] 2026-04-28 — Per-instrument continuity-pool markup + LL educational comms owed to Infinox
> Out of the slippage thread Kate proposed two follow-ups beyond the temporary unflag: (1) tighten arb-classifier thresholds to reduce false positives and free LR headroom for genuinely toxic accounts, (2) scope per-instrument markup on the continuity pool (currently flat) so it scales with instrument liquidity, plus an educational explainer for Infinox on why the LL delay is appearing as slippage on non-arb accounts. Not yet drafted/sent to client. [permalink](https://mahifx.slack.com/archives/C01QGUXPKEY/p1777369511441669)

> [resolved] 2026-04-28 — Infinox asked for self-serve Compass/Echo execution-quality report
> Trading Ops opened a parallel ticket asking whether any Compass/Echo report shows per-order delay/slippage/LL/LR/classification across all orders so they can self-monitor. Nathan confirmed there's no canned report; pointed at echo `yieldProfiles` filtering (interest_to_fill / publish_to_fill / execution_profile groupings) plus the per-CP diagnostics screen. Addressed in practice: CH requested Echo demo 2025-05-16; full training session held 2025-05-19 (Georgia attended, CH/Andreas no-shows); Georgia given Echo credentials 2025-05-22; Will shared Guru training materials and counterparty PnL time-series analysis card. Kerim subsequently using Echo for toxic-flow triage (87899203, 87031263). [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1777352682372649)

> [resolved] 2026-04-24 — Routine LR-profile adds (86050343 → Heavy, 86047343 → Medium)
> Trading Ops requested LR-profile assignments; Isaac applied 86050343→Heavy, client side confirmed taking 86047343→Medium. [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1777008813990629)

## Notable topics

- 2026-04-28 — Arb classifier currently flags on small-negative spread yield alone; many flagged accounts are long-horizon profitable to the book (false positives). Threshold tightening is the standing fix; temporary blacklist unflag is in place pending that work.
- 2026-04-28 — `FSC\INF\ZEROF02M02_MMM_USD` markdown is Infinox-side (MT plugin), not Mahi-side — confirmed not feeding our classifier or execution behaviour.
- 2026-04-28 — Last-look mechanic (200ms on Unclassified Big XAUUSD profile) is a major source of perceived slippage on non-arb-classified accounts; LL fires regardless of classification. Educational comms owed to Infinox.
- 2025-07-02 — Andrew's pre-call analysis: CFD LR PnL only $2K vs $165K on FX; skew PnL down ~50% this month; XBT is #4 most traded (effectively #2 by crypto-adjusted volume) but Mahi not capturing crypto skew PnL. NAS100ft, EURJPY, GBPJPY have no skew applied. Bridge pitch centres on replacing PXM (~$40K/M) + YourBourse crypto whitelabel simultaneously.
- 2025-06-19 — Infinox reported 233% revenue growth in 2025 and opened a new global HQ (FX News Group). Jay (previous signatory) has left; Lee is new CEO tasked with fighting an Alchemy legal battle (Alchemy owed significant cash). Andrew noted high credit risk.
- 2025-05-27 — Arb classifier 2-week analysis window may be too long for crypto; Cameron Hughes reviewed: min 3 trades + $500K volume, check every 15min via backgroundJobs. Will raised whether to shorten to 1 week — not yet decided.
- 2025-05-20 — Georgia Tzyrkalli's LinkedIn shows no Infinox employment history; Will raised regulator-spy concern. Bonnie confirmed she has an @infinox.com address so likely genuine, but caution flag noted around terminology in client-facing calls.
- 2025-04-28 — Lee's return to Infinox as CEO noted in Finance Magnates. Bonnie's prior relationship with Lee ("easier than Jay"). Mahi's billing adjustment from Xmas-eve PXM discount call made CH look good internally — useful relationship lever.
