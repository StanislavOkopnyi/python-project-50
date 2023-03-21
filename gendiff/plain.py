from gendiff.compare_dicts import get_dict_value, \
    get_item_versions, get_name, get_type


def make_plain(source: list[dict], path="") -> str | list[str]:
    result = []

    for obj in source:
        name = get_name(obj)
        new_path = path + "." + name if path != "" else name
        if get_type(obj) == "common_dict":
            result.extend(make_plain(get_dict_value(obj), new_path))
            continue
        last_version, current_version = get_item_versions(obj)

        if last_version == current_version:
            continue
        if last_version == '"__empty_value__"':
            result.append(
                f"Property '{new_path}' was added "
                f"with value: {_type_check(current_version)}")
        elif current_version == '"__empty_value__"':
            result.append(f"Property '{new_path}' was removed")
        elif current_version != last_version:
            result.append(
                f"Property '{new_path}' was updated. "
                f"From {_type_check(last_version)} to "
                f"{_type_check(current_version)}"
            )

    if path == "":
        return "\n".join(result).replace('"', "'")
    return result


def _type_check(source: str | list) -> str:
    if isinstance(source, list):
        return "[complex value]"
    return source
