import unittest
import os
from with_usage import write_and_count_lines

class TestWithUsage(unittest.TestCase):
    def test_write_and_count(self):
        filename = "test_with.txt"
        lines = ["line1", "line2", "line3"]
        count = write_and_count_lines(filename, lines)
        self.assertEqual(count, 3)
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
