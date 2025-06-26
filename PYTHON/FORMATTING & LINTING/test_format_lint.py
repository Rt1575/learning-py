import unittest
from format_lint import greet  

class TestFormatGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Rakshit"), "Hello, Rakshit! Welcome.")

if __name__ == "__main__":
    unittest.main()
