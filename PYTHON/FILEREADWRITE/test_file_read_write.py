import unittest
import os
from file_read_write import write_to_file, read_from_file

class TestFileReadWrite(unittest.TestCase):
    def test_write_and_read(self):
        filename = "temp_test_file.txt"
        content = "Hello, file!"
        write_to_file(filename, content)
        result = read_from_file(filename)
        self.assertEqual(result, content)
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
