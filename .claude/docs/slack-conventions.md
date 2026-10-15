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

## My user ID

`U099FA0D7CP` — use for `from:`, `to:`, and mention detection.
