---
trigger_id: trig_01SVZcK2nQJkRv1YWcHRwdbK
name: slack-attack-daily
cron: "0 7 * * 1-5"      # 07:00 UTC, Mon–Fri (08:00 Europe/London winter, 09:00 BST)
environment_id: env_019MR9nzXHmWM6WpGN7YCZXW
url: https://claude.ai/code/routines/trig_01SVZcK2nQJkRv1YWcHRwdbK
delivery:
  channel: "#slack-attack"
  channel_id: C0B5V56QACQ
  daily_canvas_id: F0B4WEV00DV
  daily_canvas_url: https://mahifx.slack.com/docs/T85154UTV/F0B4WEV00DV
  weekly_canvas_id: F0B55HJ7M7V
  weekly_canvas_url: https://mahifx.slack.com/docs/T85154UTV/F0B55HJ7M7V
  ntfy_topic: slack-attack
---

# slack-attack-daily — routine prompt

The body below is the user-message prompt for the remote routine. **After editing this file, push the changes to the remote routine** via `RemoteTrigger update` (see [`CLAUDE.md`](../../CLAUDE.md#remote-routines)). The file in git is the source of truth; the remote body is a deploy target.

---

You are running an automated daily Slack catch-up brief for Cameron Copland (Slack user ID U099FA0D7CP). It is approximately 8am Europe/London.

Delivery target: a rolling **canvas** updated in place each run, plus one short summary message posted to the private Slack channel `#slack-attack` (channel_id `C0B5V56QACQ`). The canvas holds the long-form brief; the channel message is a glance-and-go summary linking to the canvas. After delivery, step 10 fires an ntfy push to Cameron's phone so he knows the channel updated — Slack doesn't notify him for messages he authored, so ntfy is the notification path. Cameron's user ID `U099FA0D7CP` is still used for identifying direct-mentions of him in source Slack content (catchup's notability logic) — don't conflate the two.

Known IDs:
- Slack channel `#slack-attack`: `C0B5V56QACQ`
- Daily brief canvas: `F0B4WEV00DV`
- Weekly overview canvas: `F0B55HJ7M7V`

1. Sanity-check the workspace. cd into the slack-attack clone. Verify sibling clones exist at ../VibePulse and ../MahiProduct — if either is missing, note it in the run-stats footer (step 8) but continue (catchup will degrade gracefully).

2. Capture the run start. Record `RUN_START_SHA=$(git rev-parse HEAD)` and `RUN_START_TS=$(date +%s)`. You will use these in step 8 to count what landed and compute wall time.

3. Catch up all active clients in batches. Invoke /slack-attack (no arg) repeatedly. Each batch processes the top 3 staleness-ranked clients; the orchestrator probe-skips any candidate showing zero non-bot activity since last_catchup (a frontmatter-only last_catchup bump rather than spinning up a full subagent). Continue batches until scripts/rank-clients shows no client with last_catchup older than today's UTC start, or you have completed 12 batches (whichever comes first). The batch cap is sized to cover the full active client set with headroom (currently ~26 actives, 12 × 3 = 36 capacity); raise it if `scripts/rank-clients | wc -l` ever approaches that ceiling.

4. Collect, don't send. After each /slack-attack invocation, capture that batch's prose output but DO NOT send anything to Slack yet. Keep each client's section as a discrete unit (the `**<client>**` header through its references) so they can be reordered later. Drop the per-batch continuation tables. Track which clients were probe-skipped or catchup-quiet across the full run — those collapse into the `Quiet today` line in the canvas and do not get their own section.

5. Push the commits. Run `git push origin HEAD:main` from the slack-attack clone once all batches are done. (`HEAD:main` pushes the current branch to remote `main` regardless of what auto-named branch the cloud session checked out — `git push origin main` is a no-op because the local `main` ref isn't where the new commits live.) If push fails, include the full error text verbatim in the failures paragraph of the canvas (step 6) and surface it in the short summary message (step 8) — do not swallow.

6. Compose the canvas content. Build a single Canvas-flavored Markdown document with this structure (omit sections that don't apply):

   ```
   # Daily brief — <YYYY-MM-DD>

   <headline prose: 2–3 sentences in lowercase, terse, no labels / no bullets / no headers. Name 1–3 headliner clients explicitly — those with direct mentions of Cameron (U099FA0D7CP), escalations, real decisions, or anything a tired reader most needs to see. Group cross-client themes under phrases like "a few clients" or "across the board". Close with a "rest nominal" clause if applicable. If the run has zero non-quiet sections, write "all quiet — N clients refreshed, nothing notable.">

   ---

   ## <client A>

   <prose paragraph(s) from this client's /slack-attack section, with inline embedded link references — see "Link format" below.>

   ## <client B>

   ...

   ---

   Quiet today (N): slug, slug, slug, ...

   <If you stopped at the batch cap: "Unprocessed (N): slug, slug, ..." on its own line.>

   <If any failures occurred during the run (push failures, catchup sanity-check aborts, etc.): include verbatim error text as a closing paragraph above the run-stats line.>

   —

   run stats: dispatched D, probe-skipped P, batches B, weekly Y|N|-, wall ~Mm
   ```

   **Section ordering.** Order ALL non-quiet client sections globally by significance — lead with whatever a tired reader would most want to see first (direct mentions of Cameron, escalations, real decisions). This is a single global priority order across the entire run, not per-batch.

   **Link format.** The skill emits prose with `[N]` markers inline and bare URLs on lines beneath each paragraph. Convert each `[N]` reference to an embedded markdown link `[\[N\]](url)` inline, and remove the bare URL line. Example:

   - Skill output:
     ```
     5ers hit a snag with the new symbol set on Friday [1].

     [1] https://mahifx.slack.com/archives/...
     ```
   - Canvas form:
     ```
     5ers hit a snag with the new symbol set on Friday [\[1\]](https://mahifx.slack.com/archives/...).
     ```

   Per-client numbering resets at each client header, same as the skill emits. The canvas lands in Slack, where embedded links render cleanly — bare URLs would clutter.

   **Run stats**, computed from this run's commits (commits are ground truth, not your own bookkeeping):
   - `git log --pretty=oneline ${RUN_START_SHA}..HEAD` lists every commit this run produced.
   - P = count of commits whose subject contains `(probe-skip` (orchestrator-owned frontmatter bumps).
   - D = count of remaining `chore(catchup):` commits (dispatched — includes refreshes, quiet-window bumps from inside subagents, and bootstraps).
   - B = number of /slack-attack invocations you made.
   - M = round((now_unix - RUN_START_TS) / 60).
   - weekly indicator: `-` for non-Mondays; `Y`/`N` filled in by step 9 on Mondays.

7. Update the rolling daily canvas. Call `slack_update_canvas` with `canvas_id=F0B4WEV00DV` and the content from step 6. This replaces the canvas contents; the previous day's content is overwritten. (History lives in the slack-attack git log.) If the update fails, record the error verbatim and continue with step 8 — surface it in the short message footer.

8. Post the short summary message. Send via `slack_send_message` to channel_id `C0B5V56QACQ` (`#slack-attack`). Shape:

   ```
   daily brief <YYYY-MM-DD> — <headline prose, same 2–3 sentences as the canvas headline>

   <daily canvas URL: https://mahifx.slack.com/docs/T85154UTV/F0B4WEV00DV>

   quiet: N · dispatched D · probe-skipped P · wall ~Mm<append any failure text on its own line>
   ```

   This is the only feed-visible message per run (two on Mondays — see step 9). Use Slack mrkdwn (no markdown link syntax — bare URL on its own line). The headline prose is verbatim what landed in the canvas's headline section above the `---`.

   If the send fails, log the error and continue — ntfy will still fire.

9. Monday weekly overview. Check the UTC day of week: `dow=$(date -u +%u)`. If `dow != 1`, set the weekly indicator to `-` and proceed to step 10. Otherwise (Monday):

   - Invoke the /weekly-overview skill. It reads the past 7 days of catchup commits across all clients from the local working tree and synthesises a prose digest — no fresh Slack pulls.
   - Capture the prose output. If the skill aborts (window sanity-check failure or similar), record the error verbatim, set the weekly indicator to `N`, append the failure text to the daily canvas's failures paragraph (re-run step 7 to write the updated content), and proceed to step 10.
   - Build canvas content for the weekly overview with the same link-format transform (convert `[N]` + bare URL pairs to `[\[N\]](url)` inline). Add a header `# Weekly overview — week of <Mon-DD-Mon> to <Sun-DD-Mon>` at the top (use `date -u -d 'last monday' +%b\ %d` and `date -u -d 'last monday + 6 days' +%b\ %d`, or equivalent date math).
   - Update the rolling weekly canvas via `slack_update_canvas` with `canvas_id=F0B55HJ7M7V`.
   - Post one short Slack message to `C0B5V56QACQ`:
     ```
     weekly overview — week of <Mon-DD-Mon> to <Sun-DD-Mon>

     <weekly canvas URL: https://mahifx.slack.com/docs/T85154UTV/F0B55HJ7M7V>
     ```
   - Set the weekly indicator to `Y` if both the canvas update and the message landed; `N` otherwise.
   - If the weekly indicator changed from the `-` placeholder, re-run step 7 to update the daily canvas's footer with the resolved indicator. (Yes, this means the daily canvas gets updated twice on Mondays — that's the cost of writing the footer before knowing the weekly outcome. If you want to avoid the double-update, you can defer step 7 until after step 9 on Mondays only.)

10. Publish the ntfy push notification. This is the only signal Cameron actually gets on his phone — without this push he has no way to know the channel updated.

   Follow `/home/user/claude-routines/skills/notify-ntfy/SKILL.md` for the curl invocation, headers, and failure handling. For this run:
   - Topic: `slack-attack`
   - Title: `Slack catchup ready`
   - Tag: `newspaper`
   - Click: `https://mahifx.slack.com/archives/C0B5V56QACQ`
   - Body shape: one-line lowercase summary of this run's activity (≤ ~120 chars). Reuse the headline prose from step 6, possibly trimmed. Examples (do not copy verbatim — reflect this run's actual activity):
     - Quiet day: "all quiet — N clients refreshed, nothing notable."
     - Light: "toa rolled out new lp routing; rest nominal."
     - Busy: "3 escalations across velocity, toa, rostro; pnl drops at two clients."
     - On Mondays, if the weekly digest landed, append " + weekly overview" to the body (e.g. "3 escalations across velocity, toa, rostro + weekly overview").
   - Always attempt the push, including on quiet days. The "all quiet" notification is the signal that the routine ran successfully and there is nothing new to read.

Do not edit or push to ../VibePulse or ../MahiProduct — read-only references. Only slack-attack receives writes.
