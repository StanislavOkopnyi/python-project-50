from gendiff.compare_dicts import empty_value, get_dict_value, \
    get_item_versions, get_name, get_type
from gendiff.indentations import COMMON, IN_FIRST_FILE, IN_SECOND_FILE


def stylish(source: list, depth: int = 0) -> str:
    result = []
    indentation = " " * 2 + " " * 4 * depth

    for object in source:
        name = get_name(object)
        if get_type(object) == "common_dict":
            value = get_dict_value(object)
            value = stylish(value, depth + 1)
            result.append(indentation + COMMON + name + ": " + value)
        if get_type(object) == "item":
            last_version, current_version = get_item_versions(object)
            if last_version == current_version:
                result.append(indentation + COMMON + name +
                              ": " + last_version)
                continue
            if last_version != empty_value:
                result.append(indentation + IN_FIRST_FILE + name +
                              ": " + _check_type(last_version, depth))
            if current_version != empty_value:
                result.append(indentation + IN_SECOND_FILE + name +
                              ": " + _check_type(current_version, depth))

    result.append(" " * 4 * depth + "}")
    result.insert(0, "{")
    result = "\n".join(result)
    return result.replace(' ""', '').replace('"', '')


def _check_type(obj: str | list, depth: int) -> str:
    if isinstance(obj, list):
        return stylish(obj, depth + 1)
    return obj
