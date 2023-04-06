from yaml import load
from gendiff.formatters.json import make_json
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_stylish
from yaml import CLoader as Loader
from gendiff.compare_dicts import compare_dicts


def generate_diff(first_file: str, second_file: str,
                  formatter="stylish") -> str:
    '''
    Returns string with two compared json/yaml files.
    If function can't find file returns "Can't find {file path}"

        Parameters:
            first_file (str): Path to first json/yaml file
            second_file (str): Path to second json/yaml file
            formatter (str): Type of formatter

        Returns:
            compared_files (str): String with differences between files
    '''

    formatters = {
        "stylish": make_stylish,
        "plain": make_plain,
        "json": make_json
    }

    formatter_function = formatters[formatter]

    opened_first_file = _open_file(first_file)
    opened_second_file = _open_file(second_file)

    parsed_first_file = _parse_json_yaml(opened_first_file)
    parsed_second_file = _parse_json_yaml(opened_second_file)

    compared_files = compare_dicts(parsed_first_file, parsed_second_file)
    compared_files = formatter_function(compared_files)

    return compared_files


# If file doesn't exist returns - Can't find "file"
# Else returns parsed file
def _open_file(file_path: str) -> str | None:
    try:
        with open(file_path) as file:
            return file.read()
    except FileNotFoundError:
        raise SystemExit(f"Can't find \"{file_path}\"")


# Parse readed json/yaml file
def _parse_json_yaml(file: str) -> dict:
    return load(file, Loader=Loader)
