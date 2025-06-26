import unittest
import os
from filesystem_example import list_files_in_directory

class TestFileSystem(unittest.TestCase):
    def test_list_files(self):
        temp_dir = "temp_test_dir"
        os.makedirs(temp_dir, exist_ok=True)
        with open(os.path.join(temp_dir, "file.txt"), "w") as f:
            f.write("test")
        self.assertIn("file.txt", list_files_in_directory(temp_dir))
        os.remove(os.path.join(temp_dir, "file.txt"))
        os.rmdir(temp_dir)

if __name__ == "__main__":
    unittest.main()
