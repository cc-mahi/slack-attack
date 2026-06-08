---
slug: axiory
refs:
  vibepulse: ../VibePulse/.claude/clients/axiory.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: axiory
  hosts: ../MahiProduct/data/client-hosts.json          # entry: axiory
  wiki: null                                             # ../MahiProduct/wiki/clients/axiory.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Adam Foltyn", role: "client trading ops — LP/pricing escalations", confidence: low}
  - {name: "Roman", role: "Axiory main commercial/relationship contact (no surname confirmed)", confidence: low}
  - {name: "Magda", role: "Axiory — possibly attending Cyprus event alongside Roman", confidence: low}
last_catchup: 2026-06-08T07:10:58Z
---

## Recent issues

> [open] 2026-05-22 — GBPAUD arb + persistent skew / arbitrageur classification gaps; AXIORY_MT5_LDN party filter fix pending
> Counterparty 2040811 arbing GBPAUD triggered repeated FI PnL drop alerts (~$5k each) via PXM Give Up Clients. Will Denny whitelisted 2040811 as Arbitrageur on PXM_GU_CLIENTS, turned off GBPAUD skew, and bounced pricers; fix initially only took effect on CLIENT_PRICE_TKY not LDN. Bounced signalProcessFI1 → CLIENT_PRICE_LDN stabilised ~19:49 BST. 2026-05-25: Adam Foltyn confirmed on #mahi-axiory that the fix was received ("skew arb again?" → Will: "yes, prevented now" → Adam: "Perfect, thank you"). [client-thread](https://mahifx.slack.com/archives/C06KHNQQYMR/p1779695244195939) 2026-05-26 (overnight BST): Daria deployed real-time arb detection to admin riskPath (Zendesk ticket 22989 still open for a separate fix; no hedgers/pricers on that component). [deploy](https://mahifx.slack.com/archives/C06KQT6EU3W/p1779752194345309) LIVE1_2040811 also separately whitelisted for arbitrageur classification. [whitelist](https://mahifx.slack.com/archives/C06KQT6EU3W/p1779762621419089) Open: skew was still responding to 2040811's trades even after whitelist — Daria investigating why; AXIORY_MT5_LDN has `market = AXIORY` (TKY market) in its config, not showing in order history — may need tenant profile fix to be included in arbitrageur checks; Daria asked Kate to confirm switching the market. [party-filter-q](https://mahifx.slack.com/archives/C06KQT6EU3W/p1779762621419089) XAUUSD LDN switched to synapse as performance was dropping — monitoring. [xauusd-synapse](https://mahifx.slack.com/archives/C06KQT6EU3W/p1779745658082699) Daria also proposed a "skew kill switch" (auto-disable skew if PnL loss >10k on single instrument, reset on pricer restart) — design idea, not actioned. [kill-switch-idea](https://mahifx.slack.com/archives/C06KQT6EU3W/p1779752537203349) [alert](https://mahifx.slack.com/archives/C06KQT6EU3W/p1779469727749819) [client-notification](https://mahifx.slack.com/archives/C06KHNQQYMR/p1779471380642269) [arb-detection-q](https://mahifx.slack.com/archives/C06KQT6EU3W/p1779607931370729)

> [resolved] 2026-04-27 — LD4 pricing broken at market open — US Oil + multiple CFDs + all FX wider than TY3
> Adam Foltyn pulled MAHI pricing on US Oil → GER40/HKD50/US30/US100 → all FX to backup at LD4 open. Restored 04-27 after Sam Hewitt restarted the publishing process; Adam confirmed pricing recovered and switched back. Root cause (Daria, 04-28): a hazelcast WAN replication `Update overrides[distribution.distributionChannels]` at 2026-04-20 00:48:48 UTC set the LDN dist channel's internalisation market to `CLIENT_PRICE_TKY` (override last edited 2024) — surprise it didn't trigger sooner; Kate to watch LDN for similar oddities. Adam pinged 04-29 asking for RCA update — no reply yet, RCA write-up still owed. 2026-05-02: Adam confirmed `_z` suffix symbols switched back to MAHI pricing and included in give-ups as agreed — full pricing restoration complete. [permalink](https://mahifx.slack.com/archives/C06KHNQQYMR/p1777254243398619) [internal-rca](https://mahifx.slack.com/archives/C06KQT6EU3W/p1777276704165709) [resolution](https://mahifx.slack.com/archives/C06KHNQQYMR/p1777738779200109)

## Notable topics

> 2026-05-22 — Client call: low-spreads campaign had no volume impact; PSM interest; Compass routing still blocked by double-bubble cost
> Kate's call notes: the low-spreads/commissions campaign Axiory ran produced no increase in volumes or account numbers — no plans to repeat. Roman interested in PSM setup. Compass routing conversation re-visited: Roman views it as still in the pipeline but "double bubble" (paying both PXM and Compass fees via XCore) remains the blocker; Kate to check whether the PXM fee-reduction agreement for clients sending flow could resolve this, and follow up with Roman. Roman planning to attend Cyprus (possibly with Magda). [permalink](https://mahifx.slack.com/archives/C06KQT6EU3W/p1779449151258899)
