from gendiff.file_parser import parse_json_yaml, open_file


def test_open_file_non_empty_file():
    path = 'test/fixtures/json_yaml/file1.json'
    expected = """{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}
"""
    assert open_file(path) == expected


def test_open_file_empty_file():
    path = 'test/fixtures/json_yaml/empty.json'
    expected = ''
    assert open_file(path) == expected


def test_open_file_non_existing_file():
    path = "non_exist.json"
    try:
        open_file(path)
        assert False
    except FileNotFoundError:
        assert True


def test_parse_json_yaml():
    path_json = 'test/fixtures/json_yaml/file1.json'
    expected_json = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    assert parse_json_yaml(open_file(path_json)) == expected_json

    path_yaml = 'test/fixtures/json_yaml/file1.yaml'
    expected_yaml = {
        "Bakery": [
            "Sourdough loaf",
            "Bagels"
        ],
        "Cheesemonger": [
            "Blue cheese",
            "Feta"
        ]
    }
    assert parse_json_yaml(open_file(path_yaml)) == expected_yaml
