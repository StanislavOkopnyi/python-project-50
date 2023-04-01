from yaml import load
from gendiff.formatters.json import make_json
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_stylish
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
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

    if formatter == "stylish":
        formatter = make_stylish
    elif formatter == "plain":
        formatter = make_plain
    elif formatter == "json":
        formatter = make_json

    loaded_first_file = check_file(first_file)
    loaded_second_file = check_file(second_file)

    if isinstance(loaded_first_file, str):
        return loaded_first_file
    if isinstance(loaded_second_file, str):
        return loaded_second_file

    compared_files = compare_dicts(loaded_first_file, loaded_second_file)
    compared_files = formatter(compared_files)

    return compared_files


# If file doesn't exist reutns - Can't find "file"
# Else returns parsed file
def check_file(file_path: str) -> dict | str:
    try:
        with open(file_path) as file:
            return load(file, Loader=Loader)
    except FileNotFoundError:
        return (f"Can't find {file_path}")
