import unittest

from helpers import TODAY, dossier, link, stream
import dossierlib as dl


def closed(sid, day):
    return stream(sid, status="closed", since=day, last=day, closed=day, refs=link(day))


class PruneTest(unittest.TestCase):
    def test_prunes_only_old_closed(self):
        text = dossier(stream("live-one"), closed("old-done", "2026-09-20"), closed("new-done", "2026-10-05"))
        out, removed = dl.prune_text(text, TODAY)
        self.assertEqual(removed, ["old-done"])
        self.assertEqual([s.id for s in dl.parse(out).streams], ["live-one", "new-done"])

    def test_prune_last_stream_keeps_arc(self):
        text = dossier(stream("live-one"), closed("old-done", "2026-09-01"))
        out, _ = dl.prune_text(text, TODAY)
        d = dl.parse(out)
        self.assertIn("arc", d.sections)
        self.assertIn("- 2026-06-29 — C Book live", out)
        self.assertEqual(dl.check(d, TODAY)[0], [])

    def test_noop_and_legacy_untouched(self):
        text = dossier(stream())
        self.assertEqual(dl.prune_text(text, TODAY), (text, []))
        from helpers import LEGACY
        self.assertEqual(dl.prune_text(LEGACY, TODAY), (LEGACY, []))


if __name__ == "__main__":
    unittest.main()
