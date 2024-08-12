#!/usr/bin/env python3

"""Test Length Encoder"""

import unittest
from lenght_encoder import LengthEncoder

TEST_DATA = {
    "aaabbbbbbccddddabbbbbbcccdddddd":  "a3b6c2d4a1b6c3d6",
    "aaaaabbccccccccccccddddddd":       "a5b2c12d7",
    "aaaaaaaaaaaaaaabbbbbbbbbbbbbbb":   "a15b15",
}

class TestLengthEncoder(unittest.TestCase):
    def setUp(self):
        self.le = LengthEncoder()
        self.data = TEST_DATA

    def test_compress(self):
        for uncompressed, compressed in self.data.items():
            self.assertEqual(
                self.le.compress(uncompressed),
                compressed
            )

    def test_decompress(self):
        for uncompressed, compressed in self.data.items():
            self.assertEqual(
                self.le.decompress(compressed),
                uncompressed
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)