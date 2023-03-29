from gendiff.compare_dicts import compare_dicts, get_dict_value, \
    get_item_versions, get_name, get_type, make_common_dict, make_item
from test.fixtures.compare_results.compare_dicts_results import \
    test_compare_dicts1, test_make_common_dict1


def test_compare_dicts():
    dict1 = {"foo": "bar", "joo": {"zoo": "xar", "noo": "mar"}, "roo": "aar"}
    dict2 = {"foo": "bar", "joo": {"qoo": "xar", "noo": "mar"},
             "loo": {"moo": "dar"}}
    expected = test_compare_dicts1

    assert compare_dicts(dict1, dict2) == expected
    assert compare_dicts({}, {}) == []


def test_make_item():
    name = "foo"
    last = "bar"
    now = "foobar"
    expected = {
        "name": name,
        "last": f'"{last}"',
        "now": f'"{now}"',
        "type": "item"
    }

    assert make_item(name, last, now) == expected

    expected_empty = {
        "name": name,
        "last": '"__empty_value__"',
        "now": '"__empty_value__"',
        "type": "item"
    }

    assert make_item(name) == expected_empty


def test_make_common_dict():
    name = "foo"
    dict1 = {"x": "y", "w": "z"}
    dict2 = {"x": "y", "w": "w"}
    expected = test_make_common_dict1

    assert make_common_dict(name, (dict1, dict2)) == expected

    expected_empty = {
        "name": name,
        "value": [],
        "type": "common_dict"
    }

    assert make_common_dict(name, ({}, {})) == expected_empty


name = "foo"
item = make_item(name, "y", "z")
common_dict = make_common_dict(name, ({"foo": "y"}, {"foo": "z"}))


def test_get_name():
    assert get_name(item) == name
    assert get_name(common_dict) == name


def test_get_type():
    assert get_type(item) == "item"
    assert get_type(common_dict) == "common_dict"


def test_get_dict_value():
    assert get_dict_value(common_dict) == [item]


def test_get_versions():
    assert get_item_versions(item) == ('"y"', '"z"')
