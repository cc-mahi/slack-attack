---
name: dev
channel_id: C8568C6HG
purpose: "Core engineering channel — daily huddle, cross-cutting dev discussion, release coordination, PR triage"
scope: cross-cutting
last_catchup: 2026-10-15T13:08:55Z
---

## Now
Private team-wide engineering channel. Live: the 26.4 release wave (11 envs still on 26.3), release-process automation skills, the Graphite to Pulse/Athena migration for dashboard aggregates, and the CPS/margin delivery plan. GitHub review-reminder bots dominate message volume; ignore them.

## Streams

### dashboard-expedite — /deploy-component --expedite for dashboard
status: open · since: 2026-10-15 · last: 2026-10-15
State: Justin added `--expedite` to `/deploy-component` (dashboard only; commit fb81f40 on release/26.3, not pushed as of 10-15). Skips waiting on ~30 min UI acceptance, cancel window 3 min instead of 10, RC and precheck fire without prompts. Operator override is named in the announcement and can still be vetoed with :no_entry:. Other gates (CI, tarball, version/schema, per-client precheck) unchanged.
Next: Justin to push the commit.
Refs: https://mahifx.slack.com/archives/C8568C6HG/p1792049870471409

### graphite-to-pulse — Dashboard aggregates off Graphite, Athena backfill
status: open · since: 2026-10-12 · last: 2026-10-14
State: Justin is moving Analyze tabs and remaining dashboard aggregates from Graphite polling to pub/sub persisted to Athena. 10-12 fixed a missing-parentheses bug that published POSITION/POSITIONINBASE from both Core and Extended1, and made AdvancedFilePersister persist them (2198985e65e, de97857d3cb). 10-14 he specced an `/aggregate-backfill` skill (scripts not written; 90 days of history, ledger in the client Pulse bucket, runs on the admin box; two runs per release). Liam's feedback: make it a plain script rather than a skill, S3-only, ledger on the box, avoid extra weekend work (intra-week preferred, mind weekly reboot), document as an entry in the release gotchas file that release-prep reads, 180d is available in Graphite, probably needs a change record. Justin was to review; pilot client for the coming weekend not chosen.
Next: Justin to rework the approach per Liam's feedback; pick pilot client; settle change-record question.
Refs: https://mahifx.slack.com/archives/C8568C6HG/p1791789479856879 https://mahifx.slack.com/archives/C8568C6HG/p1791959431009529 https://mahifx.slack.com/archives/C8568C6HG/p1791969368035789

### release-26-4-wave — Compass 26.4 rollout across clients
status: open · since: 2026-09-17 · last: 2026-10-15
State: Weekly Release Radar posts (Liam, Thursdays) track tickets pending release. 26.4 waves ran from 09-13 (Alpha Capital) with GCC Brokers, GTCFX, Amana, Valutrades deployed by 09-24; GCC and Amana had an unresolved post-reboot SSM auth issue (books not turning on); Top One Trader unresponsive on a maintenance window. Zendesk #23528 (contractSize deserialize fix 938aabc928 merged to 26.4 but prod build predates it) and #23419 (GCC on pre-7-Jul build) were open on 09-24/09-17. A wave ran Fri 2026-10-09. On 10-13 Liam listed envs still on 2026.4 upgrade: 5%ers, AlphaCap Broker, Base Markets, Bright-Funded, Exinity, Go Markets, Kama, Pepperstone (all envs; may prefer intra-week), StarPrime, Top One, Velocity; hoping to cover some or all that weekend. 10-08 Justin asked for 26.3 clients and Mahi central to be covered by Radar too. 10-08 and 10-15 Radar: no release plan, no tickets pending.
Next: Liam to run the next wave; confirm SSM issue and #23528 status (not discussed after 09-24).
Refs: https://mahifx.slack.com/archives/C8568C6HG/p1789625635329999 https://mahifx.slack.com/archives/C8568C6HG/p1790230339533799 https://mahifx.slack.com/archives/C8568C6HG/p1791882357372659 https://mahifx.slack.com/archives/C8568C6HG/p1792044824628439

### release-skills — AI-driven release tooling and process
status: open · since: 2026-09-18 · last: 2026-10-12
State: Liam has built deploy skills (WIP 09-18) and on 10-12 announced `/release-prep` plus `/deploy-gates`, `/deploy-all`, `/infra-deploy`, `/change-record`: live release tracker, auto changelog and risk review, per-client gotchas, parallel prechecks, reboot schedule, dbSync tabs, parallel post-release checks, one change record per wave. In thread James and Liam discussed dropping the per-release Zendesk ticket in favour of the change record as audit trail (Liam open to it, not decided). James has MahiProduct PRs #115 and #105 aligning change-model docs with the skills; a governance ruleset now restricts who can touch the change process. James also turned commit-message writing into a skill (09-18, monitoring trigger reliability).
Next: decide whether to retire the Zendesk ticket; Liam to action PR #115.
Refs: https://mahifx.slack.com/archives/C8568C6HG/p1789731431031639 https://mahifx.slack.com/archives/C8568C6HG/p1791808885632489 https://mahifx.slack.com/archives/C8568C6HG/p1791809628716659

### cps-margin-delivery — CPS, Margin Server and API trading plan
status: watching · since: 2026-09-30 · last: 2026-10-05
State: Andrew (via ChatGPT-drafted post) asked Inald and Maten for a delivery plan covering reconciliation vs MQ, individual positions, API position behaviour, settlement, ordering/credit, rolls and margin, citing commercial demand from Argamon (Centroid to PXM) and AlphaCap (T4B replacement); drawdown modelling explicitly deferred. Review held 10-05 16:00 UK (Liam and Inald attended; Maten out sick). Outcome not posted in channel. 10-01 standup: Anton on CPS reconciliation, Kaloyan on FIX message storage/CPS plugin coverage/delayed execution reports.
Next: unknown whether the smallest supported API-client release and dates were agreed; check with Andrew/Liam.
Refs: https://mahifx.slack.com/archives/C8568C6HG/p1790765876862429 https://mahifx.slack.com/archives/C8568C6HG/p1791212487741549

### dev-call-cadence — Dev call, standup updates, Tech Talk rota
status: watching · since: 2026-09-17 · last: 2026-10-13
State: Thursday dev call with Slack huddle notes. Liam posts a weekly Tech Talk rota nudge (Inald 09-21, Justin 10-05, Leonardo 10-13). When Liam is out, standup updates go in a channel thread and Justin updates the sheet. 10-01 updates included Cameron: sustained VaR alerting and monitoring dashboard (PR MahiMain #1190 awaiting Liam's review as of 10-13). Daylight savings shifted call time (10-01).
Refs: https://mahifx.slack.com/archives/C8568C6HG/p1790834019770979 https://mahifx.slack.com/archives/C8568C6HG/p1791882357372659

### jvm-hugepages — Zendesk #23490 heap/hugepage RAM exhaustion
status: watching · since: 2026-10-01 · last: 2026-10-01
State: Radar on 10-01 listed a pending infra-deploy for pepperstone-crypto-ln-trading-1 to shrink the hugepage pool (62000 to 54500) after the heap resize already went out. Slated for 09-28; unconfirmed. Later Radars (10-08, 10-15) list no pending tickets, so likely done.
Next: confirm completed at standup.
Refs: https://mahifx.slack.com/archives/C8568C6HG/p1790835400933909

## Arc
- 2026-09-13 — Alpha Capital first deployed on 26.4
- 2026-09-17 — Release Radar posts begin appearing in channel
- 2026-10-09 — 26.4 weekend wave
- 2026-10-12 — /release-prep suite announced
