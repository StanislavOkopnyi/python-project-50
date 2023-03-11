import json


def _parse(dict1: dict, dict2: dict) -> list[tuple]:
    set1 = dict1.items()
    set2 = dict2.items()

    common = set1 & set2
    only_set1 = set1 - set2
    only_set2 = set2 - set1

    common = set(map(lambda x: ("    " + x[0], x[1]), common))
    only_set1 = set(map(lambda x: ("  - " + x[0], x[1]), only_set1))
    only_set2 = set(map(lambda x: ("  + " + x[0], x[1]), only_set2))

    result = list(common | only_set1 | only_set2)

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
        print(f"Can't find {first_file}")
        return

    try:
        with open(second_file) as f:
            json_second_file = json.load(f)
    except FileNotFoundError:
        print(f"Can't find {second_file}")
        return

    json_parsed = _parse(json_first_file, json_second_file)

    result = "{\n"
    for elem in json_parsed:
        result += (f"{elem[0]}:{elem[1]}\n")
    result += "}"

    return result
