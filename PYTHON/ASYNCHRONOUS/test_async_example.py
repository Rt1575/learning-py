import asyncio
import unittest
from async_example import download_data

class TestAsyncExample(unittest.IsolatedAsyncioTestCase):

    async def test_download_data(self):
        result = await download_data("TestSource", 0.1)
        self.assertEqual(result, "Data from TestSource")

if __name__ == "__main__":
    unittest.main()
