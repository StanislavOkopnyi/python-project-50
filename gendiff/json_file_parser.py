import json
from itertools import product


def _parse(dict1: dict, dict2: dict) -> list[tuple]:
    set1 = dict1.items()
    set2 = dict2.items()

    result = []
    # Хотел сделать через set1 & set2 и т.д., но не работает, если
    # в JSON находится array

    for key_value1, key_value2 in product(set1, set2):
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


def generate_diff(first_file: str, second_file: str):
    """Принимает пути до двух JSON файлов - возвращает
    результат сравнения в виде строки"""

    try:
        with open(first_file) as f:
            json_first_file = json.load(f)
    except FileNotFoundError:
        return (f"Can't find {first_file}")

    try:
        with open(second_file) as f:
            json_second_file = json.load(f)
    except FileNotFoundError:
        return (f"Can't find {second_file}")

    json_parsed = _parse(json_first_file, json_second_file)

    result = "{\n"
    for elem in json_parsed:
        result += (f"{elem[0]}: {str(elem[1]).lower()}\n")
    result += "}"

    return result
