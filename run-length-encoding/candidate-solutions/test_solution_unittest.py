#!/usr/bin/env python3

import os
import unittest
import importlib

class TestCompressDecompress(unittest.TestCase):
    @classmethod
    def setUpClass(test_class):
        module_name = os.getenv("CANDIDATE_NUMBER")
        test_class.module = importlib.import_module(module_name)

    def setUp(self):
        self.inputs = {
            "aaabbbbccccc":                         "a3b4c5",
            "abc":                                  "abc",
            "aaaaaaaaaaabbbbbccccaaaaaaa":          "a11b5c4a7",
            "aaabbccccccccccccddddaaaaaaaaaaaaaaa": "a3b2c12d4a15",
            "aaaaaabcccc":                          "a6bc4",
            "abbbbbcccccccccccccccdda":             "ab5c15d2a",
            "dddccccbbbbbbbaaa":                    "d3c4b7a3",
            "aaaaacccca":                           "a5c4a",
            "aaaaaaaaaabbbbbbbbbbcccccccccc":       "a10b10c10",
            "abbcccddddeeeeeffffffggggggghhhhhhhh": "ab2c3d4e5f6g7h8",
        }

    def test_compress(self):
        compress = self.module.compress
        for input_str, expected_output in self.inputs.items():
            with self.subTest(input=input_str):
                result = compress(input_str)
                self.assertEqual(result, expected_output)

    def test_decompress(self):
        decompress = self.module.decompress
        for expected_output, input_str in self.inputs.items():
            with self.subTest(input=input_str):
                result = decompress(input_str)
                self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
