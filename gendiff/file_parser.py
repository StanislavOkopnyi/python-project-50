from yaml import load
from gendiff.stylish import stylish
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from gendiff.compare_dicts import compare_dicts


def generate_diff(first_file: str, second_file: str, formatter=stylish) -> str:
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

    compared_files = compare_dicts(loaded_first_file, loaded_second_file)
    compared_files = formatter(compared_files)

    return compared_files
