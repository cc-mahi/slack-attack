---
slug: instantfunding
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/instantfunding.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: instantfunding
  hosts: ../MahiProduct/data/client-hosts.json          # entry: instantfunding
  wiki: ../MahiProduct/wiki/clients/instantfunding.md
channels:
  internal-instant-funding: C07K2E5P0G2
  mahi-instant-funding: C076RHNUP36
contacts: []
last_catchup: 2026-10-15T13:04:16Z
status: active
---

## Now
Exited client. Served notice 2026-07-01 (out of money), stopped sending flow EOD 2026-07-10, replica disconnected and monitoring removed by 2026-08-06. No Slack activity in either channel since. Only loose end is whether the outstanding June invoice was ever paid.

## Streams

### june-invoice — Outstanding June invoice chase
status: watching · since: 2026-07-01 · last: 2026-07-01
State: May invoice was paid; June invoice was outstanding at notice and Susan wanted it chased in the formal acknowledgment letter. No Slack follow-up seen through 2026-10-15; payment status unknown from Slack.
Next: confirm payment in billing data / finance; if unpaid, owner for recovery is unclear.
Refs: https://mahifx.slack.com/archives/C07K2E5P0G2/p1782902838604579

### offboarding — IF served notice and exited
status: closed · since: 2026-06-19 · last: 2026-08-06 · closed: 2026-10-15
State: IF served notice 2026-07-01 (cash exhausted after culling staff); contract notice nominally 19 July, Mahi may have held to 1 August. Beeks hosting terminated effective 31 July. Flow stopped EOD 2026-07-10. DB replica fell over ~1-2 Aug and was rebuilt, then noted as no longer connected; removed from Nagios/Sunday Checks 2026-08-06. No activity since; assumed fully exited.
Refs: https://mahifx.slack.com/archives/C07K2E5P0G2/p1782899168223089 https://mahifx.slack.com/archives/C07K2E5P0G2/p1785982831416769

### discount-retention — 50% billing discount
status: closed · since: 2026-06-03 · last: 2026-06-04 · closed: 2026-10-15
State: 50% discount extended through end of August after Lewis said they would look at leaving otherwise; Bonnie owned the relationship call. Moot after notice.
Refs: https://mahifx.slack.com/archives/C07K2E5P0G2/p1780479841433249 https://mahifx.slack.com/archives/C07K2E5P0G2/p1780570419557709

### ftp-and-payout-sims — FTP acquisition and payout rule sims
status: closed · since: 2026-06-03 · last: 2026-06-08 · closed: 2026-10-15
State: IF acquired FTP (shrinking, staff cut 21 to 3); FTP flow would fall under the same Customer Group contract. IF also supplied payout/trailing-drawdown rules for sims. Both cancelled by the notice; nothing proceeded.
Refs: https://mahifx.slack.com/archives/C07K2E5P0G2/p1780479841433249 https://mahifx.slack.com/archives/C07K2E5P0G2/p1780932899300319

### clarity-mt5-groups — MT5 Clarity group whitelisting
status: closed · since: 2026-06-08 · last: 2026-06-08 · closed: 2026-10-15
State: Kate Stagg whitelisted the new Clarity demo/funded groups for Patrick; done.
Refs: https://mahifx.slack.com/archives/C076RHNUP36/p1780913933693819

## Arc
- 2026-06-04 — Bonnie agrees to keep 50% discount to end of August
- 2026-07-01 — IF serves termination notice
- 2026-07-10 — IF stops sending flow
- 2026-07-31 — Beeks hosting termination effective
- 2026-08-06 — Removed from Nagios/Sunday Checks; effectively decommissioned
