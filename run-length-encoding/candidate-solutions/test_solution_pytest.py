import os
import pytest
import importlib

module_name = os.getenv("CANDIDATE_NUMBER")
candidate_module = importlib.import_module(module_name)

inputs = {
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

@pytest.mark.parametrize("input_str,expected_output", inputs.items())
def test_compress(input_str, expected_output):
    compress = candidate_module.compress
    result = compress(input_str)
    assert result == expected_output

@pytest.mark.parametrize("expected_output,input_str", inputs.items())
def test_decompress(expected_output, input_str):
    decompress = candidate_module.decompress
    result = decompress(input_str)
    assert result == expected_output
