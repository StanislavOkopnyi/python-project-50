from gendiff.formatters.json import make_json
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_stylish
from gendiff.compare_dicts import compare_dicts
from gendiff.file_parser import parse_json_yaml, open_file

FORMATTERS = {
    "stylish": make_stylish,
    "plain": make_plain,
    "json": make_json
}


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

    formatter_function = FORMATTERS[formatter]

    opened_first_file = open_file(first_file)
    opened_second_file = open_file(second_file)

    parsed_first_file = parse_json_yaml(opened_first_file)
    parsed_second_file = parse_json_yaml(opened_second_file)

    compared_files = compare_dicts(parsed_first_file, parsed_second_file)
    compared_files = formatter_function(compared_files)

    return compared_files
