import unittest
from lambdas import add

class TestLambdas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_squares(self):
        numbers = [1, 2, 3, 4]
        expected = [1, 4, 9, 16]
        result = list(map(lambda x: x ** 2, numbers))
        self.assertEqual(result, expected)

    def test_even(self):
        numbers = [1, 2, 3, 4, 5, 6]
        expected = [2, 4, 6]
        result = list(filter(lambda x: x % 2 == 0, numbers))
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
