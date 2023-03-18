from typing import Any
from yaml import load
from gendiff.indentations import COMMON, IN_FIRST_FILE, IN_SECOND_FILE
from gendiff.stylish import stylish
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from json import dumps


def generate_diff(first_file: str, second_file: str, foramter=stylish):
    '''
    Returns string with two compared json/yaml files.
    If function can't find file returns "Can't find {file path}"

        Parameters:
            first_file (str): A path to first json/yaml file
            second_file (str): A path to second json/yaml file

        Returns:
            compared_files (str): String with differences between files
    '''

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

    compared_files = _compare_files(loaded_first_file, loaded_second_file)
    compared_files = foramter(compared_files)

    return compared_files


def _compare_files(dict1: dict, dict2: dict) -> str:

    compared_list = []

    compared_list.extend(_compare_common_keys(dict1, dict2))
    compared_list.extend(_compare_uncommon_keys(dict1, dict2))

    # Сортируем, получая "-" выше "+"
    compared_list.sort(key=lambda x: x[1], reverse=True)
    # Сортируем по названию(до ":")
    compared_list.sort(key=lambda x: x[2:x.index(":")])

    compared_list.insert(0, "{")
    compared_list.append("}")

    result = "\n".join(compared_list)
    result = result.replace(' ""', '')
    result = result.replace('"', '')
    return result


def _is_dicts(obj1: Any, obj2: Any) -> bool:
    return isinstance(obj1, dict) and isinstance(obj2, dict)


def _check_type(obj: Any) -> str:
    if isinstance(obj, dict):
        return _compare_files(obj, obj)
    return dumps(obj)


def _compare_common_keys(dict1: dict, dict2: dict) -> list[str]:
    common_keys = dict1.keys() & dict2.keys()
    result = []
    for key in common_keys:

        if dict1[key] == dict2[key] and not _is_dicts(dict1[key], dict2[key]):
            result.append(COMMON + f"{key}: {dumps(dict1[key])}")

        if dict1[key] != dict2[key] and not _is_dicts(dict1[key], dict2[key]):
            result.append(IN_FIRST_FILE +
                          f"{key}: {_check_type(dict1[key])}")
            result.append(IN_SECOND_FILE +
                          f"{key}: {_check_type(dict2[key])}")

        if _is_dicts(dict1[key], dict2[key]):
            result.append(
                COMMON + f"{key}: "
                f"{_compare_files(dict1[key], dict2[key])}"
            )
    return result


def _compare_uncommon_keys(dict1: dict, dict2: dict) -> list[str]:
    only_dict1_keys = dict1.keys() - dict2.keys()
    only_dict2_keys = dict2.keys() - dict1.keys()

    result = []

    for key in only_dict1_keys:
        if isinstance(dict1[key], dict):
            result.append(
                IN_FIRST_FILE + f"{key}: "
                f"{_compare_files(dict1[key], dict1[key])}"
            )
            continue
        result.append(IN_FIRST_FILE +
                      f"{key}: {_check_type(dict1[key])}")

    for key in only_dict2_keys:
        if isinstance(dict2[key], dict):
            result.append(
                IN_SECOND_FILE + f"{key}: "
                f"{_compare_files(dict2[key], dict2[key])}"
            )
            continue
        result.append(IN_SECOND_FILE +
                      f"{key}: {_check_type(dict2[key])}")

    return result
