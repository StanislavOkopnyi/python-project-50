from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from itertools import product
from typing import Any


def _compare(dict1: dict, dict2: dict) -> list[tuple]:
    result = []

    for key_value1, key_value2 in product(dict1.items(), dict2.items()):
        key1, key2 = key_value1[0], key_value2[0]
        value1, value2 = key_value1[1], key_value2[1]
        if key1 == key2:

            if value1 == value2:
                result.append(("    " + key1, value1))
            elif value1 != value2:
                result.append(("  - " + key1, value1))
                result.append(("  + " + key2, value2))

    keys1, keys2 = dict1.keys(), dict2.keys()

    for key1 in keys1:
        if key1 not in keys2:
            result.append(("  - " + key1, dict1[key1]))

    for key2 in keys2:
        if key2 not in keys1:
            result.append(("  + " + key2, dict2[key2]))

    # В результате этой сортировки имена располагаются в алфавитном порядке
    # В случае если встречается два имени, то имя с "-", оказывается выше
    # имени с "+"
    result.sort(key=lambda x: x[0][2], reverse=True)
    result.sort(key=lambda x: x[0][4:])
    return result


def _process_value(value: Any) -> str:
    value = str(value)
    value = value[0].lower() + value[1:]
    value = value.replace("\'", "\"")
    return value


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

    files_compared = _compare(loaded_first_file, loaded_second_file)

    result = "{\n"
    for elem in files_compared:
        result += (f"{elem[0]}: {_process_value(elem[1])}\n")
    result += "}"

    return result
