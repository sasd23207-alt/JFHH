import unittest

from main import greet


class TestGreeting(unittest.TestCase):
    def test_greet_uses_name(self):
        self.assertEqual(greet("Salem"), "Hello, Salem! Welcome to MASAR Development Studio.")

    def test_greet_trims_spaces(self):
        self.assertEqual(greet("  Salem  "), "Hello, Salem! Welcome to MASAR Development Studio.")

    def test_greet_uses_default_for_empty_name(self):
        self.assertEqual(greet("   "), "Hello, Developer! Welcome to MASAR Development Studio.")


if __name__ == "__main__":
    unittest.main()
