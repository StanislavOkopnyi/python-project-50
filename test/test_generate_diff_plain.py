from gendiff import generate_diff
from gendiff.formatters.plain import make_plain
from test.fixtures.compare_results.plain_results import *


def test_gendiff_path():
    input_data1 = ("test/fixtures/json_yaml/filepath1.json",
                   "test/fixtures/json_yaml/filepath2.json")
    expected = filepath1_filepath2_json

    assert generate_diff(*input_data1, make_plain) == expected


def test_gendiff_yaml():
    input_data1 = ("test/fixtures/json_yaml/file1.yaml",
                   "test/fixtures/json_yaml/file2.yaml")

    expected1 = file1_file2_yaml

    assert generate_diff(*input_data1, make_plain) == expected1

    input_data2 = "test/fixtures/json_yaml/file3.yaml", "test/fixtures/json_yaml/file4.yaml"
    expected2 = file3_file4_yaml

    assert generate_diff(*input_data2, make_plain) == expected2


def test_gendiff_json():
    input_data1 = ("test/fixtures/json_yaml/file1.json",
                   "test/fixtures/json_yaml/file2.json")
    expected1 = file1_file2_json

    assert generate_diff(*input_data1, make_plain) == expected1

    input_data2 = ("test/fixtures/json_yaml/file3.json",
                   "test/fixtures/json_yaml/file4.json")
    expected2 = file3_file4_json

    assert generate_diff(*input_data2, make_plain) == expected2

    input_data3 = ("test/fixtures/json_yaml/file5.json",
                   "test/fixtures/json_yaml/file6.json")
    expected3 = file5_file6_json

    assert generate_diff(*input_data3, make_plain) == expected3


def test_gendiff_json_empty():
    input_data1 = ("test/fixtures/json_yaml/file3.json",
                   "test/fixtures/json_yaml/file3_1.json")
    expected1 = file3_file3_1_json

    assert generate_diff(*input_data1, make_plain) == expected1

    input_data2 = ("test/fixtures/json_yaml/file3_1.json",
                   "test/fixtures/json_yaml/file3.json")
    expected2 = file3_1_file3_json

    assert generate_diff(*input_data2, make_plain) == expected2
