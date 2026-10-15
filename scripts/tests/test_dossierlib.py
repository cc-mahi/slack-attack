import unittest

from helpers import LEGACY, dossier, link, stream
import dossierlib as dl


class ParseTest(unittest.TestCase):
    def test_parses_streams_and_meta(self):
        d = dl.parse(dossier(stream(), stream("mt4-decom", status="closed", since="2026-10-11",
                                               last="2026-10-13", closed="2026-10-13")))
        self.assertFalse(d.legacy)
        self.assertEqual([s.id for s in d.streams], ["tegis-api", "mt4-decom"])
        s = d.streams[1]
        self.assertTrue(s.heading_ok)
        self.assertEqual(s.status, "closed")
        self.assertEqual(str(s.date("closed")), "2026-10-13")
        self.assertEqual(s.field("State"), "Paused for algo testing.")
        self.assertIn("frontmatter", dl.Dossier.__dataclass_fields__)
        self.assertIn("slug", dl.frontmatter_keys(d.frontmatter))

    def test_legacy_detected(self):
        self.assertTrue(dl.parse(LEGACY).legacy)

    def test_invalid_calendar_date_gives_no_meta(self):
        d = dl.parse(dossier(stream(since="2026-02-30", refs=link("2026-10-14"))))
        self.assertIsNone(d.streams[0].meta)

    def test_bad_heading_flagged(self):
        d = dl.parse(dossier(stream().replace(" — ", " - ", 1)))
        self.assertFalse(d.streams[0].heading_ok)

    def test_permalink_dates(self):
        self.assertEqual([str(x) for x in dl.permalink_dates(link("2026-10-14"))], ["2026-10-14"])

    def test_remove_streams_roundtrip(self):
        text = dossier(stream("a-one"), stream("b-two"))
        d = dl.parse(text)
        out = dl.remove_streams(d, {"a-one"})
        self.assertEqual([s.id for s in dl.parse(out).streams], ["b-two"])
        self.assertEqual(dl.remove_streams(d, set()), text)


if __name__ == "__main__":
    unittest.main()
