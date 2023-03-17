from typing import Any
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from json import dumps
COMMON = "    "
IN_FIRST_FILE = "  - "
IN_SECOND_FILE = "  + "


def is_dicts(obj1: Any, obj2: Any) -> bool:
    return isinstance(obj1, dict) and isinstance(obj2, dict)


def check_type(obj: Any, depth: int) -> str:
    if isinstance(obj, dict):
        return compare_files(obj, obj, depth=depth+1)
    return dumps(obj)


def compare_files(dict1: dict, dict2: dict, depth: int = 0) -> str:
    keys1, keys2 = dict1.keys(), dict2.keys()

    common_keys = keys1 & keys2
    only_dict1_keys = keys1 - keys2
    only_dict2_keys = keys2 - keys1

    result = []

    for key in common_keys:

        if dict1[key] == dict2[key] and not is_dicts(dict1[key], dict2[key]):
            result.append(COMMON + f"{key}: {dumps(dict1[key])}")

        elif dict1[key] != dict2[key] and not is_dicts(dict1[key], dict2[key]):
            result.append(IN_FIRST_FILE +
                          f"{key}: {check_type(dict1[key], depth)}")
            result.append(IN_SECOND_FILE +
                          f"{key}: {check_type(dict2[key], depth)}")

        elif is_dicts(dict1[key], dict2[key]):
            result.append(
                COMMON + f"{key}: "
                f"{compare_files(dict1[key], dict2[key], depth=depth+1)}"
            )

    for key in only_dict1_keys:
        if isinstance(dict1[key], dict):
            result.append(IN_FIRST_FILE + f"{key}: "
                          f"{compare_files(dict1[key], dict1[key], depth=depth+1)}")
        else:
            result.append(IN_FIRST_FILE +
                          f"{key}: {check_type(dict1[key], depth)}")

    for key in only_dict2_keys:
        if isinstance(dict2[key], dict):
            result.append(IN_SECOND_FILE + f"{key}: "
                          f"{compare_files(dict2[key], dict2[key], depth=depth+1)}")
        else:
            result.append(IN_SECOND_FILE +
                          f"{key}: {check_type(dict2[key], depth)}")

    # Сортируем, получая "-" выше "+"
    result.sort(key=lambda x: x[2], reverse=True)
    # Сортируем по названию(до ":")
    result.sort(key=lambda x: x[4:x.index(":")])

    result.insert(0, "{")
    result.append("}")

    return f"\n{COMMON * depth}".join(result).replace(' ""', '').replace('"', "")


def generate_diff(first_file: str, second_file: str):
    """Принимает пути до двух JSON файлов - возвращает
    результат сравнения в виде строки"""

    try:
        with open(first_file) as file:
            loaded_first_file = load(file, Loader=Loader)
    except FileNotFoundError:
        return (f"Can't find {first_file}")

    try:
        with open(second_file) as file:
            loaded_second_file = load(file, Loader=Loader)
    except FileNotFoundError:
        return (f"Can't find {second_file}")

    return compare_files(loaded_first_file, loaded_second_file)
