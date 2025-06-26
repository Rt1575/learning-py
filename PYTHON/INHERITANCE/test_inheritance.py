import unittest
from inheritance import Animal, Dog

class TestInheritance(unittest.TestCase):
    def test_animal_speak(self):
        a = Animal("Generic")
        self.assertEqual(a.speak(), "Generic makes a sound.")

    def test_dog_speak(self):
        d = Dog("Tommy")
        self.assertEqual(d.speak(), "Tommy barks!")

if __name__ == "__main__":
    unittest.main()
