"""Tests for the package itself: skill frontmatter, plugin manifests, install commands. Standard library only.

    python3 -m unittest discover -s tests -v
"""
import json
import os
import re
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
URL = "https://github.com/aldushmedia/find-skills-es"
EM_DASH = "\u2014"
# split so this file does not match itself
ORIGINAL_LINKS = ("github.com/" + "vercel-labs", "vercel" + ".com")


def read(*parts):
    with open(os.path.join(REPO, *parts), encoding="utf-8") as fh:
        return fh.read()


def frontmatter():
    text = read("skills", "find-skills", "SKILL.md")
    return re.match(r"^---\n(.*?)\n---\n", text, re.S).group(1)


class Skill(unittest.TestCase):
    def test_name_is_still_find_skills(self):
        self.assertIn("name: find-skills\n", frontmatter() + "\n")

    def test_description_keeps_original_triggers_and_adds_spanish(self):
        desc = re.search(r"^description: (.+)$", frontmatter(), re.M).group(1)
        for trigger in ('"how do I do X"', '"find a skill for X"', '"is there a skill that can..."',
                        '"cómo hago X"', '"busca una skill para X"', '"¿hay una skill que...?"'):
            self.assertIn(trigger, desc)

    def test_cli_commands_are_unchanged(self):
        text = read("skills", "find-skills", "SKILL.md")
        for cmd in ("npx skills find [query] [--owner <owner>]",
                    "npx skills add <package>",
                    "npx skills update",
                    "npx skills add <owner/repo@skill> -g -y",
                    "npx skills add vercel-labs/agent-skills@react-best-practices",
                    "npx skills init my-xyz-skill"):
            self.assertIn(cmd, text)


class Package(unittest.TestCase):
    def test_plugin_and_marketplace(self):
        plugin = json.loads(read(".claude-plugin", "plugin.json"))
        self.assertEqual(plugin["name"], "find-skills")
        self.assertEqual(plugin["author"]["name"], "Aldush Media")
        self.assertEqual(plugin["homepage"], URL)
        self.assertEqual(plugin["repository"], URL)
        market = json.loads(read(".claude-plugin", "marketplace.json"))
        self.assertEqual(market["name"], "find-skills-es")
        self.assertEqual(market["owner"]["name"], "Aldush Media")
        self.assertEqual(market["plugins"][0]["name"], "find-skills")
        self.assertEqual(market["plugins"][0]["homepage"], URL)

    def test_readme_installs_from_aldushmedia(self):
        readme = read("README.md")
        for line in ("npx skills add aldushmedia/find-skills-es --skill find-skills -a claude-code",
                     "git clone %s.git" % URL,
                     "cp -r find-skills-es/skills/find-skills ~/.claude/skills/find-skills",
                     "/plugin marketplace add aldushmedia/find-skills-es",
                     "/plugin install find-skills@find-skills-es",
                     "22.20"):
            self.assertIn(line, readme)

    def test_license_keeps_original_and_adds_aldush_line(self):
        lic = read("LICENSE")
        self.assertTrue(lic.startswith("MIT License\n\nCopyright (c) 2026 Vercel, Inc.\n"))
        self.assertTrue(lic.rstrip("\n").endswith(
            "Copyright (c) 2026 Aldush Media (traducción y adaptación al español)"))

    def test_no_em_dash_or_original_author_links(self):
        bad = []
        for root, dirs, files in os.walk(REPO):
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
            for name in files:
                path = os.path.join(root, name)
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    text = fh.read()
                if EM_DASH in text or any(link in text for link in ORIGINAL_LINKS):
                    bad.append(os.path.relpath(path, REPO))
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
