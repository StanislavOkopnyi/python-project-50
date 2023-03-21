from typing import Any

import json


def compare_dicts(dict1: dict, dict2: dict) -> list[dict]:
    '''
    Returns list with "common_dict" and "item"

        Parameters:
            dict1 (dict): Loaded json/yaml file or subdict in this file
            dict2 (dict): Loaded json/yaml file or subdict in this file

        Returns:
            compared_list (list): List with "common_dict" and "item"
    '''
    compared_list = []

    compared_list.extend(_compare_common_keys(dict1, dict2))
    compared_list.extend(_compare_uncommon_keys(dict1, dict2))

    compared_list.sort(key=lambda x: x["name"])

    return compared_list


def _compare_common_keys(dict1: dict, dict2: dict) -> list[dict]:
    common_keys = dict1.keys() & dict2.keys()
    result = []

    for key in common_keys:

        if not _is_dicts(dict1[key], dict2[key]):
            result.append(make_item(key, dict1[key], dict2[key]))
        if _is_dicts(dict1[key], dict2[key]):
            result.append(make_common_dict(key, (dict1[key], dict2[key]))
                          )

    return result


def _compare_uncommon_keys(dict1: dict, dict2: dict) -> list[dict]:
    only_dict1_keys = dict1.keys() - dict2.keys()
    only_dict2_keys = dict2.keys() - dict1.keys()

    result = []
    for key in only_dict1_keys:
        result.append(make_item(key, last=dict1[key]))

    for key in only_dict2_keys:
        result.append(make_item(key, now=dict2[key]))
    return result


def _process_value(value: Any):
    if isinstance(value, dict):
        return compare_dicts(value, value)
    return json.dumps(value)


def _is_dicts(obj1: Any, obj2: Any) -> bool:
    return isinstance(obj1, dict) and isinstance(obj2, dict)


def make_item(name: str, last: Any = "__empty_value__",
              now: Any = "__empty_value__") -> dict:
    '''
    Return "item"
    Everything that doesn't match "common_dict"
    If in the first/second file no such key value will be "__empty_value__"

        Parameters:
            name (str): Key of the value
            last (Any): Value in the first file
            now (Any): Value in the second file

        Returns:
            item (dict): dict with name, lat, now and type = "item"

    '''
    item = {"name": name,
            "last": _process_value(last),
            "now": _process_value(now),
            "type": "item"}
    return item


def make_common_dict(name: str, value: tuple[dict, dict]) -> dict:
    '''
    Returns "common_dict"
    If two files have the same key and value is dict in both files, then
    dict converts to "common_dict", which contains "item" and/or "common_dict"

        Parameters:
            name (str): Key of the value
            value (tuple): Contains dicts from first and second
                                                file respectively

        Returns:
            common_dict (dict): dict with name, value and type = "common_dict"
    '''
    common_dict = {"name": name,
                   "value": compare_dicts(*value),
                   "type": "common_dict"}
    return common_dict


def get_name(source: dict) -> str:
    '''Returns name of common_dict/item'''
    return source["name"]


def get_type(source: dict) -> str:
    '''Returns type of common_dict/item'''
    return source["type"]


def get_dict_value(source: dict) -> list:
    '''Returns value of common_dict'''
    return source["value"]


def get_item_versions(source: dict) -> tuple[Any, Any]:
    '''Returns (value from first file, value from second file) from item'''
    return source["last"], source["now"]
