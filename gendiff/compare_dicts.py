from types import FunctionType
from typing import Any

import json


def compare_dicts(dict1: dict, dict2: dict) -> list[dict]:

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
    return {"name": name,
            "last": _process_value(last),
            "now": _process_value(now),
            "type": "item"}


def make_common_dict(name: str, value: tuple[dict, dict]):
    return {"name": name,
            "value": compare_dicts(*value),
            "type": "common_dict"}


def get_name(source: dict) -> str:
    return source["name"]


def get_type(source: dict) -> str:
    return source["type"]


def get_dict_value(source: dict) -> list:
    return source["value"]


def get_item_versions(source: dict) -> tuple[Any, Any]:
    return source["last"], source["now"]
