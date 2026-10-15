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

## Not clients

Channels `/slack-attack`'s new-client check has ruled out (internal projects, advisers, dead leads). Add to this list rather than re-judging daily; remove a line if one becomes a client.

- `#internal-greyspark` — advisers on Mahi's business plan
- `#internal-funded-next` — prospect declined 2026-10-08
- `#mahi-xrigroup` — Sammy's consultancy, not a client
- `#mahi-client-test`, `#internal-client-updates`, `#internal-product`, `#internal-billing`, `#internal-competitors`, `#internal-cyprus-expo-2026`, `#internal-mahi-central` — internal
- `#mahi-funded-next` — client side of `#internal-funded-next`, declined 2026-10-08
- `#internal-ai-reports`, `#internal-ai-ml`, `#internal-claude-code`, `#internal-trading-operations`, `#internal-trading-daily-checks`, `#internal-trading-analytics`, `#internal-trading-analytics-jira`, `#internal-analytics-sales`, `#internal-analytics-onboarding`, `#internal-prop-reporting`, `#internal-prop-firm`, `#internal-technical-prop`, `#internal-prospects`, `#internal-aws-lambda-alerts`, `#internal-hotforex` (now the internal gold-open review channel) — internal
- `#internal-fastmt`, `#mahi-fastmt` — FastMT, a bridge vendor/partner, not a client
- `#internal-river-prime` (terminated 2023-12), `#internal-tattvam-ekaa` (terminated, services ceased 2026-03-25), `#internal-8cap` (quiet since 2025-10), `#internal-xs` (2025 pilot talk, quiet since), `#internal-tradehaven` (quiet since 2024), `#mahi-blackbull` (empty), `#mahi-admirals-trading` (quiet since 2022), `#mahi-libertex-config-updates`, `#mahi-think-config-updates` (dead bot channels) — former or dead leads
- Sub-channels of tracked or retired clients, not new clients: `#internal-valutrades-classifier-automation`, `#internal-valutrades-options`, `#mahi-valu-alerts`, `#mahi-exinity-businessintel`, `#mahi-exinity-technical`, `#mahi-exinity-classifier`, `#mahi-alphacapital-technical`, `#mahi-alphacapital-support`, `#mahi-alphacapbroker-fastmt`, `#mahi-brightfunded-support`, `#mahi-tapaas-ic` (IC Markets), `#mahi-fintokei-bridge`, `#mahi-pepperstone-config-updates`, `#mahi-argamon-config-updates`, `#mahi-axiory-config-updates`, `#mahi-rostro-notifications-config`, `#internal-ig-group`, `#mahi-ig-group`, `#mahi-to-ig-integration`, `#internal-fundingpips`, `#mahi-fundingpips`

## Private channels

Many relevant channels are private. Always pass `channel_types: "public_channel,private_channel"` to search tools.

## My user ID

`U099FA0D7CP` — use for `from:`, `to:`, and mention detection.
