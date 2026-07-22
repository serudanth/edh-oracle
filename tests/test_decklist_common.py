import sys
import pathlib
import unittest

# Ensure tools/ is on sys.path so tests can import decklist_common
REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import decklist_common as dc


class TestDecklistCommon(unittest.TestCase):
    def test_slugify_basic(self):
        self.assertEqual(dc.slugify("My Deck Name"), "my-deck-name")
        self.assertEqual(dc.slugify("  Leading and Trailing  "), "leading-and-trailing")
        self.assertEqual(dc.slugify("Punctuation!@#$%^&*()"), "punctuation")

    def test_classify_type_priority(self):
        # If types include a priority type, it should return that
        self.assertEqual(dc.classify_type(["Artifact", "Creature"]), "Creature")
        self.assertEqual(dc.classify_type(["Enchantment", "Instant"]), "Instant")

    def test_classify_type_fallback(self):
        # If no priority matched, return first provided
        self.assertEqual(dc.classify_type(["WeirdType", "Another"]), "WeirdType")
        self.assertEqual(dc.classify_type([]), "Other")


if __name__ == '__main__':
    unittest.main()
