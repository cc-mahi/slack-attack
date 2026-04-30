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
  - {name: "Georgia Tzyrkalli", role: "Infinox trading ops — arb classification / blacklist queries", confidence: low}
  - {name: "CH", role: "Infinox sales escalation contact", confidence: low}
  - {name: "Lazaros", role: "Infinox — wants call on automatic classification PnL impact", confidence: low}
last_catchup: 2026-04-30T09:10:00Z
---

## Recent issues

> [open] 2026-04-30 — Lazaros wants call on classification/arb-profile PnL contribution
> Infinox-side request to schedule a call "today" to understand how much extra PnL the automatic classification / arb classification / profiles is generating for them, and how Infinox can produce those numbers themselves. Isaac said he'll get the London team to schedule. [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1777535019524179)

> [open] 2026-04-29 — Georgia asked for FX vs CFD B-Book blacklist clarification
> Follow-up to the unflag action: Georgia checked the CFD B-Book blacklist and couldn't see the 13 unflagged accounts; Kate's link pointed at the FX B-Book blacklist. Nathan explained classifications are per tenant profile — 12 of the 13 trade on FX B-Book and were added there; one (87939648) trades on CFD B-Book and went on the CFD B-Book arb blacklist. Georgia hasn't acked the explanation yet. [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1777506691683789)

> [resolved] 2026-04-28 — Slippage complaint storm on 18 EURUSD/B_CLIENTS logins; arb-classifier false positives
> Clio escalated (CH bumped to "max priority" — multiple sales teams complaining simultaneously) about clients seeing observable slippage on EURUSD market orders and SL/limit fills, in group `FSC\INF\ZEROF02M02_MMM_USD` (markdown group). David Cooney took the call with Clio; Kate produced a per-account breakdown — 13 of 18 were arb-classified (force-internalised at continuity-pool mid + flat markup) on small-negative spread-yield false positives, 5 non-arb saw last-look-driven slippage (notably 200ms LL on Unclassified Big XAUUSD; e.g. 87939648 LL=66%, 87946983 LL=50%). Will's analysis (`y60m`) confirmed classifier thresholds too sensitive — e.g. 87928871/87947068/87957409/87957449/87957488 are arb-flagged but long-horizon profitable to the book. EURUSD-specific cut (last 7d) showed only 87932042 ($139M, "don't b book", LL 29% / LR 11%) and 87957488 ($9M, arb) had material EURUSD volume; the rest are tiny tickets, so the EURUSD framing is misleading — wider 28d table is the right lens. Will also confirmed Compass has no `markdown` config — the `FSC\INF\ZEROF02M02_MMM_USD` markdown sits on Infinox's MT plugin side and doesn't feed our classifier. Georgia requested the 13 arb accounts be unflagged as a temporary fix; Kate actioned it (added to FX B-Book / CFD B-Book Arbitrageurs blacklists). [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1777355727656879)

> [open] 2026-04-28 — B_CLIENTS LR config layer review — actions outstanding
> While investigating the slippage complaint, Will pulled 7d of B_CLIENTS yieldprofile ($39.5B notional) against the LR config and surfaced layering issues: channel ≈ global on burst (global effectively dormant), CP-Default rate equals channel rate (CP rule never binds first), Toxic XAUUSD `maxRed=250` silently clipped to channel ceiling 200, no timezone differentiation despite XAUUSD spreads blowing 10–20× at ROLL. Heavy LR (volMult 25) is working ($45.85/M, 50% hit, ~$45K/wk on $989M); Toxic XAUUSD barely fires (5 of 9 CPs stale, 2 of 4 active are long-horizon profitable signal-followers); No LR exemption is dead (all 15 CPs absent from B_CLIENTS — one active member trades only on PXM_GU_CLIENTS / BBOOK_CFD_VANTAGE); Reduced LR too soft (y60m −$153/M with hit rate 0.5%). Proposed: ROLL-specific channel profile (burst 1M, rate 200k/500ms, volMult 1.5) + lift channel maxRed to 250, drop CP-Default rate to 300k/s, drop 5 stale Toxic XAUUSD CPs, sunset/migrate No LR profile, promote 2 underperformers from Reduced LR → Medium/Heavy. Will offered (a) identify specific Reduced LR CPs to promote, (b) re-run Toxic XAUUSD over 30d, (c) draft Compass JSON patch — no decision in window. [permalink](https://mahifx.slack.com/archives/C01QGUXPKEY/p1777368117734019)

> [open] 2026-04-28 — Per-instrument continuity-pool markup + LL educational comms owed to Infinox
> Out of the slippage thread Kate proposed two follow-ups beyond the temporary unflag: (1) tighten arb-classifier thresholds to reduce false positives and free LR headroom for genuinely toxic accounts, (2) scope per-instrument markup on the continuity pool (currently flat) so it scales with instrument liquidity, plus an educational explainer for Infinox on why the LL delay is appearing as slippage on non-arb accounts. Not yet drafted/sent to client. [permalink](https://mahifx.slack.com/archives/C01QGUXPKEY/p1777369511441669)

> [open] 2026-04-28 — Infinox asked for self-serve Compass/Echo execution-quality report
> Trading Ops opened a parallel ticket asking whether any Compass/Echo report shows per-order delay/slippage/LL/LR/classification across all orders so they can self-monitor. Nathan confirmed there's no canned report; pointed at echo `yieldProfiles` filtering (interest_to_fill / publish_to_fill / execution_profile groupings) plus the per-CP diagnostics screen. Trading Ops hasn't replied — this is the same need that drove Lazaros' call request. [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1777352682372649)

> [resolved] 2026-04-24 — Routine LR-profile adds (86050343 → Heavy, 86047343 → Medium)
> Trading Ops requested LR-profile assignments; Isaac applied 86050343→Heavy, client side confirmed taking 86047343→Medium. [permalink](https://mahifx.slack.com/archives/C022S6NL82D/p1777008813990629)

## Notable topics

- 2026-04-28 — Arb classifier currently flags on small-negative spread yield alone; many flagged accounts are long-horizon profitable to the book (false positives). Threshold tightening is the standing fix; temporary blacklist unflag is in place pending that work.
- 2026-04-28 — `FSC\INF\ZEROF02M02_MMM_USD` markdown is Infinox-side (MT plugin), not Mahi-side — confirmed not feeding our classifier or execution behaviour.
- 2026-04-28 — Last-look mechanic (200ms on Unclassified Big XAUUSD profile) is a major source of perceived slippage on non-arb-classified accounts; LL fires regardless of classification. Educational comms owed to Infinox.
