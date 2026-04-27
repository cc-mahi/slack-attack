# Slack conventions

Adapted from `../pagerbuddy/.claude/docs/slack-channels.md` — trimmed to what `/catchup` needs.

## Channel naming

- `internal-<client>` — Mahi-internal discussion about one client.
- `mahi-<client>` (or `mahi-<client>-<suffix>`) — shared with the client. Not all clients follow the plain `mahi-<slug>` pattern — some have suffixes (e.g. `mahi-pepperstone-vnd`, `mahi-gomarkets-2025`). Use `slack_search_channels` as a fallback if the obvious name doesn't exist.
- `#dev`, `#dev-eu`, `#dev-support`, `#dev-infra` — cross-cutting engineering.

## Always skip (bot noise, no human discussion)

- `*-notifications` (e.g. `mahi-<client>-notifications`)
- `*-bridge-alerts` (e.g. `internal-<client>-bridge-alerts`)
- `#frontoffice-alerts`
- `#dev-alerts`, `#dev-commits`, `#dev-status`

## Private channels

Many relevant channels are private. Always pass `channel_types: "public_channel,private_channel"` to search tools.

## Known channel IDs

Populate here as we discover them (from search results) — avoids re-resolving.

| Channel | ID |
|---------|----|
| `internal-ic-markets` | C07TZ00FK1Q |
| `internal-pepperstone` | C033K2P0RPT |
| `mahi-ic-markets` | C07UBJNUWG1 |
| `mahi-pepperstone-vnd` | C06AR8MT8NT |
| `mahi-gomarkets-2025` | C09J1DP2QQH |
| `mahi-ig-group` | C097U77HR42 |
| `internal-rostro` | C08ALS66EDC |
| `mahi-rostro` | C08AQKRU953 |
| `internal-amana` | C08T42TMKU3 |
| `mahi-amana` | C08SYSMP0EB |
| `dev-eu` | C08KZ4L2HPF |
| `dev` | C8568C6HG |
| `mahi-argamon-operations` | C06TW3D8NMV |
| `mahi-atc` | C04AZM0LPMH |
| `mahi-axiory` | C06KHNQQYMR |
| `internal-axiory` | C06KQT6EU3W |
| `mahi-base-markets` | C09D8V41JAG |
| `mahi-brightfunded` | C08473TFD7Z |
| `mahi-exinity` | C0456LSHQQK |
| `mahi-fintokei` | C08QWKFARDL |
| `mahi-fundingpips` | C073FHA6TAR |
| `mahi-gcc-brokers` | C09PNC1MFAA |
| `mahi-infinox` | C022S6NL82D |
| `mahi-instant-funding` | C076RHNUP36 |
| `mahi-starprime` | C096422RPKK |
| `internal-errante` | C09LE05K3FC |
| `internal-go` | CNF3WPNSK |
| `internal-the-5-percenters` | C079M09MGGP |
| `mahi-the-five-percenters` | C07AQJS4E80 |
| `internal-toponetrader` | C08TG143F4L |
| `mahi-toponetraders` | C08U853T684 |
| `internal-valutrades` | CP7A1F8BT |
| `mahi-valutrades` | CSLM3Q8AD |
| `mahi-valutrades-operations` | C09HN93T0G2 |
| `internal-velocity` | CPDS0M2KF |
| `mahi-velocity` | C05NB72AGR2 |

## My user ID

`U099FA0D7CP` — use for `from:`, `to:`, and mention detection.
