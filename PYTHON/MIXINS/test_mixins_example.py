import unittest
from mixins_example import Person

class TestMixins(unittest.TestCase):
    def test_walk_talk(self):
        p = Person("Rakshit")
        self.assertEqual(p.walk(), "Rakshit is walking.")
        self.assertEqual(p.talk(), "Rakshit says hello.")

if __name__ == "__main__":
    unittest.main()
