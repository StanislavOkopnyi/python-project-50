from gendiff import generate_diff
from gendiff.formatters.json import make_json


def test_generate_dif():
    input_data = ("test/fixtures/json_yaml/file1.json",
                  "test/fixtures/json_yaml/file2.json")
    assert generate_diff(*input_data, make_json)
