import datetime as dt
import os
import sys

SCRIPTS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, SCRIPTS)

TODAY = dt.date(2026, 10, 14)


def link(day, cid="C09D8V41JAG"):
    """A real-shaped Slack permalink whose ts falls at 12:00 UTC on `day`."""
    secs = int(dt.datetime.fromisoformat(day + "T12:00:00+00:00").timestamp())
    return f"https://mahifx.slack.com/archives/{cid}/p{secs}000123"


def stream(sid="tegis-api", status="open", since="2026-09-02", last="2026-10-14",
           closed=None, refs=None, title="Tegis direct integration",
           state="Paused for algo testing.", meta=None):
    if meta is None:
        meta = f"status: {status} · since: {since} · last: {last}"
        if closed:
            meta += f" · closed: {closed}"
    if refs is None:
        refs = f"{link(since)} {link(last)}"
    return f"### {sid} — {title}\n{meta}\nState: {state}\nRefs: {refs}\n"


CLIENT_FM = (
    "slug: basemarkets\n"
    "refs:\n"
    "  wiki: null\n"
    "channels:\n"
    "  mahi-base-markets: C09D8V41JAG\n"
    "last_catchup: 2026-10-14T09:00:57Z\n"
)


def dossier(*streams, now="Tegis paused.", arc="- 2026-06-29 — C Book live\n", fm=CLIENT_FM):
    body = "\n".join(streams)
    return f"---\n{fm}---\n\n## Now\n{now}\n\n## Streams\n\n{body}\n## Arc\n{arc}"


LEGACY = (
    "---\nslug: x\nlast_catchup: 2026-08-17T08:00:00Z\n---\n\n"
    "## Recent issues\n\n"
    "> [open] 2026-08-10 — Something\n"
    f"> Detail. [permalink]({link('2026-08-10')})\n"
)
