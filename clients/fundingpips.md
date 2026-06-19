---
slug: fundingpips
refs:
  vibepulse: ../VibePulse/.claude/clients/fundingpips.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: fundingpips
  hosts: ../MahiProduct/data/client-hosts.json          # entry: fundingpips
  wiki: null                                             # ../MahiProduct/wiki/clients/fundingpips.md (not yet)
channels_override: null
key_people_overrides: []
last_catchup: 2026-06-19T07:06:24Z
---

## Status

- **Stage**: Live (infra maintained — servers stopped, config kept)
- **Integration**: Paused — no Compass orders since 2026-02-26
- **Relationship**: At risk — client MIA since mid-April 2026; no reply to re-engagement attempts

## Recent issues

> [open] 2026-04-15 — FundingPips MIA; no flow since Feb 2026; futures business collapse
> Flow from FundingPips stopped entirely from 2026-02-26; Compass received no orders. Daria flagged the silence 2026-03-03. David Cooney called Mahmoud 2026-03-05: confirmed lost ~$10M USD on futures business, future in doubt; Mahi offered 2 months free service. Bonnie: "this will be potentially the second time we saved them from going under." Kate was actioning position flattening 2026-03-09 ("nearly ready to turn flow back on but have requested book positions to be flattened"). Kate attempted re-engagement 2026-04-14 in mahi channel ("are you ready to route flow back to Compass?") with no reply. By 2026-04-15 internal team flagging client gone MIA; Bonnie: "They seem to have gone MIA." David confirmed the $10M futures loss context same day.
>
> https://mahifx.slack.com/archives/C073X2B83CH/p1772499625057829
> https://mahifx.slack.com/archives/C073X2B83CH/p1772716849249759
> https://mahifx.slack.com/archives/C073X2B83CH/p1776249963328299

> [resolved] 2026-04-27 — AWS infra wind-down vs preserve decision
> Following the mid-April flow stop, Bonnie asked whether to decommission. Liam costed it on 2026-04-27: ~$100/mo to keep servers stopped, or delete-and-keep-config-backup at negligible cost. Isaac resolved 2026-05-05: chose option A (keep servers stopped, can delete later). https://mahifx.slack.com/archives/C073X2B83CH/p1777329277763629
>
> Resolution: https://mahifx.slack.com/archives/C073X2B83CH/p1777944196442699
>
> Cross-channel context: 2026-04-29 Hussain imported fundingpips into pulse automation terraform state alongside rostro — consistent with "keep infra, don't delete". https://mahifx.slack.com/archives/C8X18LPH9/p1777502447886849

> [resolved] 2025-12-09 — Finalto rogue LP pricing incident at XAUUSD Sunday open
> Mahmoud complained in mahi channel about bad XAUUSD pricing around 28 Nov CME outage. David Cooney investigated and traced to Finalto LP supplying bad price through the fallback pool at Sunday open. David: "stupidity on our part." Finalto removed from any price source as resolution. https://mahifx.slack.com/archives/C073FHA6TAR/p1765268107777949

> [resolved] 2025-11-14 — XAUUSD 10x spreads / MAHI_LP_2 dropout
> Mahmoud complained about very wide XAUUSD spreads. Daria investigated: MAHI_LP_2 had dropped out causing BMSL widening; pricing signals also widening on top. Fixed by removing signals and restarting marketDataProxyHubRx. https://mahifx.slack.com/archives/C073X2B83CH/p1763106167247749
>
> Mahi channel complaint: https://mahifx.slack.com/archives/C073FHA6TAR/p1763103206297689

> [resolved] 2025-11-16 — Duplicate ClOrdID from FXCubic bridge (recurring Oct–Nov)
> Leonardo flagged recurring duplicate ClOrdID rejections from FXCubic bridge Oct 2025. FXC acknowledged and promised a fix by 2025-11-03. Mahmoud confirmed the FXC fix was applied by 2025-11-16 — no further recurrence noted after that date. https://mahifx.slack.com/archives/C073FHA6TAR/p1761322561730119
>
> Confirmation: https://mahifx.slack.com/archives/C073FHA6TAR/p1763328796147479

## Notable topics

- **Lifecycle — futures collapse & MIA**: Flow stopped Feb 2026 after FundingPips lost ~$10M on futures business. David Cooney confirmed on a call 2026-03-05; Mahi offered 2 months free. Client went MIA from mid-April despite re-engagement attempts. Infra kept stopped (not deleted) per Isaac's call 2026-05-05. Not retired — keep watching for restart signal or explicit shutdown decision.
- **Tradin broker brand launched Nov 2025**: Mahmoud mentioned FundingPips launched "Tradin" as a separate broker brand (Mauritius license) on 2025-11-13. https://mahifx.slack.com/archives/C073X2B83CH/p1763041038436839
- **Books active pre-pause**: Three qualifying books (Q1/Q2/Q3_CLIENTS) plus Grads (CLIENTS); FX + Metals only (no CFD/Crypto rollout despite prior upsell discussions).
