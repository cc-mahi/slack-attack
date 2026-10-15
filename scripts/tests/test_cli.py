import os
import shutil
import subprocess
import tempfile
import unittest

from helpers import SCRIPTS, dossier, link, stream

CHECK = os.path.join(SCRIPTS, "check-dossiers")
PRUNE = os.path.join(SCRIPTS, "prune-dossiers")


def git(cwd, *args):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


class CliTest(unittest.TestCase):
    def setUp(self):
        self.repo = tempfile.mkdtemp()
        git(self.repo, "init", "-q")
        git(self.repo, "config", "user.email", "t@example.com")
        git(self.repo, "config", "user.name", "t")
        os.makedirs(os.path.join(self.repo, "clients"))
        self.path = os.path.join(self.repo, "clients", "x.md")

    def tearDown(self):
        shutil.rmtree(self.repo)

    def write(self, text):
        with open(self.path, "w") as fh:
            fh.write(text)

    def run_check(self, *args):
        return subprocess.run([CHECK, *args], cwd=self.repo, capture_output=True, text=True)

    def test_staged_new_file_passes(self):
        self.write(dossier(stream()))
        git(self.repo, "add", "clients/x.md")
        r = self.run_check("--staged")
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_staged_removed_open_stream_blocks(self):
        self.write(dossier(stream(), stream("mt4-decom")))
        git(self.repo, "add", "clients/x.md")
        git(self.repo, "commit", "-qm", "seed")
        self.write(dossier(stream()))
        git(self.repo, "add", "clients/x.md")
        r = self.run_check("--staged")
        self.assertEqual(r.returncode, 1)
        self.assertIn("mt4-decom", r.stderr)

    def test_file_mode_and_stale_and_usage(self):
        self.write(dossier(stream("old-open", last="2026-01-05", since="2026-01-05", refs=link("2026-01-05"))))
        self.assertEqual(self.run_check("clients/x.md").returncode, 0)
        r = self.run_check("--stale", "clients/x.md")
        self.assertEqual(r.returncode, 0)
        self.assertIn("old-open", r.stdout)
        self.assertEqual(self.run_check().returncode, 2)

    def test_prune_cli(self):
        day = "2026-01-05"
        self.write(dossier(stream(), stream("old-done", status="closed", since=day, last=day,
                                            closed=day, refs=link(day))))
        r = subprocess.run([PRUNE, "clients/x.md"], cwd=self.repo, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("clients/x.md: pruned old-done", r.stdout)
        with open(self.path) as fh:
            self.assertNotIn("old-done", fh.read())


if __name__ == "__main__":
    unittest.main()
