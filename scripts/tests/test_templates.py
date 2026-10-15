import datetime as dt
import os
import unittest

from helpers import SCRIPTS
import dossierlib as dl

REPO = os.path.dirname(SCRIPTS)


class TemplateTest(unittest.TestCase):
    def check(self, rel, as_path):
        with open(os.path.join(REPO, rel)) as fh:
            d = dl.parse(fh.read(), as_path)
        self.assertFalse(d.legacy)
        self.assertEqual(dl.check(d, dt.date(2026, 10, 14))[0], [])

    def test_client_template_valid(self):
        self.check("clients/_template.md", "clients/example.md")

    def test_channel_template_valid(self):
        self.check("channels/_template.md", "channels/example.md")


if __name__ == "__main__":
    unittest.main()
