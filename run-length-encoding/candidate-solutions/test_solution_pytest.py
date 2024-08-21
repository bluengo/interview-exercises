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