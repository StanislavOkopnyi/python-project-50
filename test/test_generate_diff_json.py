from gendiff import generate_diff


def test_generate_dif():
    input_data = "test/fixtures/file1.json", "test/fixtures/file2.json"
    assert generate_diff(*input_data)
