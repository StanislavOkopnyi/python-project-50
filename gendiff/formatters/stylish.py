from gendiff.compare_dicts import get_dict_value, \
    get_item_versions, get_name, get_type


COMMON = "  "
IN_FIRST_FILE = "- "
IN_SECOND_FILE = "+ "
FIRST_LEVEL_INDENTATION = 2
DEEP_LEVEL_INDENTATION = 4


def make_stylish(source: list, depth: int = 0) -> str:
    '''
    Returns json-like output from list of "item" and "common_dict"
    If key: value is equal in both files - returns:
        "{COMMON} {key: value}"
    If key: value is different in first and second files - returns:
        "{IN_FIRST_FILE} {key1: value1}"
        "{IN_SECOND_FILE} {key2: value2}"
    '''
    result = ["{", ]
    indentation = " " * FIRST_LEVEL_INDENTATION +\
                  " " * DEEP_LEVEL_INDENTATION * depth

    for object in source:
        name = get_name(object)
        if get_type(object) == "common_dict":
            value = get_dict_value(object)
            value = make_stylish(value, depth + 1)
            result.append(f"{indentation}{COMMON}{name}: {value}")
        if get_type(object) == "item":
            last_version, current_version = get_item_versions(object)
            if last_version == current_version:
                result.append(
                    f"{indentation}{COMMON}{name}: {last_version}"
                )
                continue
            if last_version != '"__empty_value__"':
                result.append(
                    f"{indentation}{IN_FIRST_FILE}{name}: "
                    f"{_check_type(last_version, depth)}"
                )
            if current_version != '"__empty_value__"':
                result.append(
                    f"{indentation}{IN_SECOND_FILE}{name}: "
                    f"{_check_type(current_version, depth)}"
                )

    result.append(" " * DEEP_LEVEL_INDENTATION * depth + "}")
    result = "\n".join(result)
    return result.replace('"', '')


# if value is a sub dict returns json-like output with bigger indentation
def _check_type(obj: str | list, depth: int) -> str:
    if isinstance(obj, list):
        return make_stylish(obj, depth + 1)
    return obj
