---
slug: easton
refs:
  vibepulse: ../VibePulse/.claude/clients/easton.yaml
  billing: ../MahiProduct/data/billing/clients.json
  hosts: ../MahiProduct/data/client-hosts.json
  wiki: null
channels_override: null
key_people_overrides:
  - {name: "Shervin Arian", role: "ex-Easton — primary contact during integration; departed 2025-08-15, indicated would resurface at next firm", confidence: low}
  - {name: "Carlos Rico-Ospina", role: "ex-Easton — quant / handover after Shervin's exit; left ~2025-08-19", confidence: low}
last_catchup: 2026-04-30T00:00:00Z
status: retired
retired_at: 2025-08-19
retired_reason: |
  UK prop firm (controlled by Skilled Funded Trader / part of TheFundedTrader group) suspended prop trading operations
  mid-August 2025 and entered liquidation. Both client-side principals (Shervin Arian, then Carlos Rico-Ospina)
  exited within days of each other; no support, no dashboard access, customer fallout reported on Trustpilot.
  Servers stopped 2025-08-28, PD service disabled 2025-08-27, AWS firehose / hiera entries removed 2026-01-22,
  internal-easton channel archived 2026-03-26.
  https://mahifx.slack.com/archives/C090T6MM867/p1755605834221869
  https://mahifx.slack.com/archives/C090T6MM867/p1755618424594379
  https://mahifx.slack.com/archives/C090T6MM867/p1755698991736899
  https://mahifx.slack.com/archives/CC59PPM8X/p1769076622561289
---

## Recent issues

> [resolved] 2026-03-26 — `internal-easton` channel archived
> Bonnie archived the channel; concludes the wind-down. No further activity expected. [permalink](https://mahifx.slack.com/archives/C090T6MM867/p1774522071835749)

> [resolved] 2026-01-22 — AWS firehose + hiera entries removed
> Liam flagged `awsFirehoseRxEaston` (along with Tattvam, Finotive, Zenfinex) for removal from firehose-2; Arun stopped the firehose and removed from hiera. Easton no longer flowing trades to Graphite. [permalink](https://mahifx.slack.com/archives/CC59PPM8X/p1769076094485069)

> [resolved] 2025-08-28 — servers stopped
> Liam stopped the AWS servers after Bonnie raised the question (initially unsure of the legal position during their notice period, decided risk was low since client wasn't using them and they're easy to start again if needed). PD service for Easton Analytics had been disabled the day before by Daria. [permalink](https://mahifx.slack.com/archives/C090T6MM867/p1756368693931789)

> [resolved] 2025-08-19 — Easton suspends prop trading, enters liquidation
> Trades stopped flowing; Trustpilot reviews piling up about no support, no dashboard, accounts being force-migrated from MT5/cTrader to Match-Trader without notice. Will linked the Finance Magnates piece — "Easton Controlled Skilled Funded Trader Suspends Prop Trading Operations". Carlos out the same day after taking the handover from Shervin earlier in the week; sent a goodwill note via personal email. Bonnie booked a call with the liquidator for the following week to confirm what AWS infra needed terminating. Sentiment internally was pragmatic — "nothing we could have done here", part of the prop wash-out post-ODI; Shervin had already signalled he'd bring Mahi into his next firm. [permalink](https://mahifx.slack.com/archives/C090T6MM867/p1755605834221869)

> [resolved] 2025-08-15 — Shervin Arian's sudden exit
> Out-of-the-blue farewell from Shervin ("today is my last day in my current role"). Will called immediately — sudden exit, Carlos taking over, Carlos out the same day. Shervin's cited reason for hopping was that "every prop firm I have spoken to that uses your technology only has positive things to say… huge impacts in payout reductions and improvements to price quality" — and he was planning to bring Mahi into his next gig. In hindsight this was the leading edge of the firm collapsing. [permalink](https://mahifx.slack.com/archives/C090T6MM867/p1755250287151899)

> [resolved] 2025-08-10 — failover gap during Exinity reboot
> Crypto switched on the previous week with a tested failover to Mahi Central LDN, but a connectivity issue to Exinity from all servers post-reboot exposed that the failover feed hadn't been correctly set up alongside the other feeds. Daria committed to sorting that day. Will flagged separately that he wasn't sure they'd explicitly green-lit trading on the crypto feeds — investigation note rather than incident. [permalink](https://mahifx.slack.com/archives/C090T6MM867/p1754859441680399)

> [resolved] 2025-08-07 — crypto live + Mahi Central failover wired
> All crypto pairs live through Compass; Mahi Central failover set up and tested (Isaac). Shervin keen to get the bridge set up the following week. [permalink](https://mahifx.slack.com/archives/C090T6MM867/p1754529946162349)

> [resolved] 2025-08-04 — force internalisation tuning
> Mio investigated cancels: ~77% of volume was hitting Force Internalize and getting force-internalised to the continuity pool, then breaching the limit order price after LR + markup. Recommended lowering channel LR and markup. Cancel volumes inflated by spammed retries — Mio flagged to Shervin to fix on Easton's side (was supposed to be already fixed). [permalink](https://mahifx.slack.com/archives/C090T6MM867/p1754307266931499)

## Notable topics

- Lessons-from-the-collapse: prop firm wash-out post-ODI affected Easton, Tattvam, Finotive, Zenfinex (all decommissioned together in the Jan 2026 firehose cleanup). Easton's collapse was sudden — no warning beyond Shervin's exit-day message — but client-side traders had clearly been signalling distress publicly.
- Shervin Arian relationship is the durable thread here: he was the inbound advocate, exited just before the firm imploded, and indicated he'd reintroduce Mahi at his next firm. Worth recognising the name if it surfaces in another prop's onboarding.
