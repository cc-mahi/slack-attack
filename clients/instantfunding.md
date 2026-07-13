---
slug: instantfunding
refs:
  vibepulse: ../VibePulse/.claude/clients/instantfunding.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: instantfunding
  hosts: ../MahiProduct/data/client-hosts.json          # entry: instantfunding
  wiki: null                                             # ../MahiProduct/wiki/clients/instantfunding.md (not yet)
channels_override: null
key_people_overrides: []
last_catchup: 2026-07-13T07:04:17Z
---

## Recent issues

> [open] 2026-07-01 — IF served notice: running out of money, offboarding by 31 July
> Bonnie announced to internal channel: IF have served notice, citing they're running out of money after culling key staff who could have helped. Lewis informed Bonnie on 19 June; formal termination letter received 2026-07-01. One month's notice per contract — effective date nominally 19 July (from Lewis's original email), though Mahi may hold to 1 August if being magnanimous ("depends if we want to be dicks about it"). Liam actioned Beeks hosting termination immediately (30-day notice, effective 31 July). May invoice was paid; June invoice outstanding — Susan wants it chased in the formal acknowledgment letter. Susan's stance: "Do the month but they are last on the list for any support." Andrew verified the financial narrative was accurate. Susan noted David had given discounts and helped many times — this is on IF's decisions, not Mahi's services. [permalink](https://mahifx.slack.com/archives/C07K2E5P0G2/p1782899168223089) [Beeks termination](https://mahifx.slack.com/archives/C07K2E5P0G2/p1782908559971509) [June invoice thread](https://mahifx.slack.com/archives/C07K2E5P0G2/p1782902838604579)

> [resolved] 2026-06-03 — FTP acquisition: migrating flow to Compass, LP contract check underway
> IF has acquired FTP, which is roughly half IF's size and shrinking; plan is to grow FTP back up. George (client-side) is checking how long remains on FTP's current Taurex LP contract. Migration of FTP flow to Compass was discussed. Nicole confirmed FTP falls under the "Customer Group" contract definition, so FTP flow can be included in the same IF contract — billing will increase via counterparty count. David Cooney noted the irony of requesting a discount while simultaneously acquiring FTP and wanting to route that additional flow through Compass. [permalink](https://mahifx.slack.com/archives/C07K2E5P0G2/p1780479841433249)
> 2026-06-04 update: Bonnie called Lewis directly. FTP cut staff 21→3, moved everything to MetaTrader, revenue declining all of last year. Had a $200k loss the month before last. Lewis sells ~2k accounts/month (larger accounts). Lewis said if discount removed they'd "have to look at letting Mahi go" — discount confirmed as retention lever. Lewis noted August is typically their worst month, September their best. [permalink](https://mahifx.slack.com/archives/C07K2E5P0G2/p1780566216212199)
> 2026-07-01 update: Moot — IF have served notice and are offboarding. FTP migration never proceeded.

> [resolved] 2026-06-03 — Payout rule sim requested (trailing drawdown addition)
> IF wants to change their payout criteria, including adding a trailing drawdown rule. Kate Stagg to send over the parameters so sims can be kicked off. [permalink](https://mahifx.slack.com/archives/C07K2E5P0G2/p1780479841433249)
> 2026-06-08 update: IF provided full rule parameters for two account types. (1) Standard: daily DD 3%, max trailing drawdown 6% equity-based (trailing up to starting balance), profit target 9%, min days N/A, consistency N/A, min withdrawal 1.5% of starting balance at funded, paid every 14 calendar days — penalty mechanic: if account ever goes -1.5% equity, payout split at first payout cut in half. (2) Instant Funding: daily DD 3%, max trailing 6% balance-based, consistency 20%, min withdrawal 3% at funded, same -1.5% equity penalty on first payout split. Kate Stagg tagged Cameron Hughes to build a sim skill and run these. [permalink](https://mahifx.slack.com/archives/C07K2E5P0G2/p1780932899300319)
> 2026-07-01 update: Moot — IF served notice and are offboarding; sim work no longer required.

> [resolved] 2026-06-08 — New Clarity MT5 account groups whitelisted
> IF (Patrick) requested whitelisting of new MT5 Clarity account groups (demo + funded, multiple server/CT/MTCH variants). Kate Stagg clarified funded vs eval accounts (funded = groups ending IF_MT5, Micro_IF, or containing "Funded"). Config placed, pending EOD restarts to pick up the additional groups. [permalink](https://mahifx.slack.com/archives/C076RHNUP36/p1780913933693819)

> [resolved] 2026-06-03 — 50% billing discount extended through end of August
> Nicole Vivian asked if the 50% discount had been extended after Lewis requested a bill revision. David Cooney initially confirmed June + July. 2026-06-04: Bonnie Cassidy called Lewis, agreed to continue discount until end of August; diarised a call with Lewis after August to discuss. Lewis's position: they'd have to look at leaving Mahi if discount removed. Bonnie diarised the August review. [permalink](https://mahifx.slack.com/archives/C07K2E5P0G2/p1780570419557709)

## Notable topics

- 2026-06-03 — May value-add reviewed on call: XAUUSD skew $8.5/M, all-instrument skew $6.7/M, LR $4/M. Low slippage complaints lately; plan to increase LR settings slightly. [permalink](https://mahifx.slack.com/archives/C07K2E5P0G2/p1780479841433249)
- 2026-06-04 — Internal note: Susan Cooney flagged that someone other than David should manage IF commercials; Bonnie took the Lewis call and is diarising ongoing review. Lewis is the commercial contact (not George as previously thought). [permalink](https://mahifx.slack.com/archives/C07K2E5P0G2/p1780561016159079)

## Status

- Stage: offboarding — served notice 2026-07-01; effective date ~19 July–1 August (contract ambiguity); Beeks hosting terminated by Liam, effective 31 July
- Integration: Compass live (LDN) running to end of notice period; no further development (FTP migration cancelled)
- Relationship: exiting — financial distress (ran out of money, culled key staff); June invoice outstanding and being chased; Mahi supporting through notice period at lowest priority; Bonnie managing handoff
