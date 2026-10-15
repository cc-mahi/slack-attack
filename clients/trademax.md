---
slug: trademax
aliases: [tmgm]                                            # MahiProduct onboarding tracker uses `tmgm`; infra/hosts use `trademax`
refs:
  vibepulse: null                                          # no ../VibePulse/.claude/clients/trademax.yaml yet
  billing: null                                            # not in ../MahiProduct/data/billing/clients.json
  hosts: ../MahiProduct/data/client-hosts.json             # entry: trademax (s3Slug TRADEMAX; LDN + NYC)
  wiki: ../MahiProduct/wiki/clients/trademax.md
  onboarding: ../MahiProduct/data/onboarding/tmgm.json     # stage tracker (slug `tmgm`)
channels:
  internal-tmgm: C03AP1L0Z7B
  mahi-tmgm: C03AP4AVCCR
contacts:
  - {name: "Bailey White", role: "TMGM — owned the integration decision; paused 2026-07-10, declined go-live 2026-08-26"}
  - {name: "Nik Teh", role: "TMGM — hub/FIX side; made the drop-copy Tag1 account-identifier change"}
  - {name: "Rainer", role: "TMGM — queried why account identifiers were needed on drop-copy", confidence: low}
last_catchup: 2026-10-15T13:08:56Z
status: retired
retired_at: 2026-10-15
retired_reason: TMGM declined go-live 2026-08-26 and is building its own pricing/skew; PTR pilot ended, setup decommissioned, Beeks hosting cancellation effective 2026-10-25.
---

## Now
TMGM declined go-live on 2026-08-26 and is building its own pricing/skew; the PTR pilot is over and the setup is being decommissioned.
Beeks hosting cancellation takes effect 2026-10-25.

## Streams

### decommission — Tear down TMGM pilot infrastructure
status: watching · since: 2026-08-26 · last: 2026-08-28
State: Liam took a config backup, stopped the app and put in the Beeks cancellation on 2026-08-26 (30 days notice, end date 2026-10-25). The servers may be reused for OS upgrades (Pepperstone and Argamon "need doing in that region"). On 2026-08-28 Liam brought the app back up as a PROD-like pentest target, with PROD connectivity config removed and external logins disabled. No Slack signal since 2026-08-28.
Next: Liam to confirm Beeks end 2026-10-25 and the pentest-system teardown; no owner named for server reuse.
Refs: https://mahifx.slack.com/archives/C03AP1L0Z7B/p1787732439446689 https://mahifx.slack.com/archives/C03AP1L0Z7B/p1787904798950809

### capital-blind-feed — Reuse pilot data for Capital.com blind-feed pitch
status: watching · since: 2026-08-26 · last: 2026-08-26
State: Nicola asked whether data captured during the TMGM pilot could support another conversation with Capital.com, who were interested in a blind feed. Unanswered in-channel.
Next: Mahi analytics (Will Carter / Shyam) to say what was captured; Nicola to decide on a Capital.com follow-up.
Refs: https://mahifx.slack.com/archives/C03AP1L0Z7B/p1787748832874629

### pilot-ptr-xau — PTR skew pilot for TMGM (XAU)
status: closed · since: 2026-07-07 · last: 2026-08-26 · closed: 2026-10-15
State: Bailey told Nicola on 2026-08-26 that TMGM will not go live and will build its own pricing/skew; the door was left open if that does not work out. Before that Bailey was slow to respond (paused 2026-07-10 over RMF/MT5 stability concerns, restarted 2026-07-23, XAU-only scope, pricing off TMGM's own pool feeds only). Open technical items at the time were never confirmed done: signalProcess1 27x gold-burst crash fix (2026-08-11), FX majors skew review, Tag1 account identifiers delivered 2026-07-26.
Refs: https://mahifx.slack.com/archives/C03AP4AVCCR/p1783677581133339 https://mahifx.slack.com/archives/C03AP1L0Z7B/p1787730439079069

### skew-value-add — Value-add metrics and 1c cap credibility
status: closed · since: 2026-08-05 · last: 2026-08-17 · closed: 2026-10-15
State: After Bailey flagged twice-wrong backtest figures, Will's final report (week of 9-14 Aug, hard 1c cap) put value-add at $26.6k / $0.75/M on $35.7bn XAU, 68.5% accuracy; sent to Bailey 2026-08-17 asking for a source IP to whitelist. Bailey never supplied it; superseded by the 2026-08-26 decline.
Refs: https://mahifx.slack.com/archives/C03AP4AVCCR/p1786099157627389 https://mahifx.slack.com/archives/C03AP4AVCCR/p1787002200375379

## Arc
- 2026-07-10 — Bailey pauses the project over RMF/MT5 platform-stability concerns
- 2026-07-23 — Project restarted as an urgent XAU-first setup
- 2026-08-05 — Hard 1c skew cap in force after Daria traces the over-widening to PSM config
- 2026-08-26 — TMGM declines go-live, will build its own pricing; decommission begins, Beeks cancelled (ends 2026-10-25)
