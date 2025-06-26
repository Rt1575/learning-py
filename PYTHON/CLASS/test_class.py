import unittest
from person_class import Person  

class TestPerson(unittest.TestCase):
    def test_greet(self):
        p = Person("Rakshit", 20)
        expected = "My name is Rakshit and I am 20 years old."
        self.assertEqual(p.greet(), expected)

if __name__ == "__main__":
    unittest.main()
