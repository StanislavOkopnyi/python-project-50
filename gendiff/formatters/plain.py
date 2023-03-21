from gendiff.compare_dicts import get_dict_value, \
    get_item_versions, get_name, get_type


def make_plain(source: list[dict], path="") -> str | list[str]:
    '''
    Returns plain output from list of "item" and "common_dict"
    If key: value doesnt change - returns nothing
    If key: value changed in second file - returns:
        "Property {path} was updated. From {old_value} to {new_value}"
    If key: value is only in second value - returns:
        "Property {path} was added with value: {new_value}
    If key: value is only in first file - returns:
        "Property {path} was removed"
    '''
    result = []

    for obj in source:
        name = get_name(obj)
        new_path = path + "." + name if path != "" else name
        if get_type(obj) == "common_dict":
            result.extend(make_plain(get_dict_value(obj), new_path))
            continue
        old_value, new_value = get_item_versions(obj)

        if old_value == new_value:
            continue
        if old_value == '"__empty_value__"':
            result.append(
                f"Property '{new_path}' was added "
                f"with value: {_type_check(new_value)}")
        elif new_value == '"__empty_value__"':
            result.append(f"Property '{new_path}' was removed")
        elif new_value != old_value:
            result.append(
                f"Property '{new_path}' was updated. "
                f"From {_type_check(old_value)} to "
                f"{_type_check(new_value)}"
            )

    if path == "":
        return "\n".join(result).replace('"', "'")
    return result


# if value is subdict returns [complex value]
def _type_check(source: str | list) -> str:
    if isinstance(source, list):
        return "[complex value]"
    return source
