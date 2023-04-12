from yaml import load
from yaml import CLoader as Loader


# If file doesn't exist returns - Can't find "file"
# Else returns parsed file
def open_file(file_path: str) -> str | None:
    try:
        with open(file_path) as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't find \"{file_path}\"")


# Parse readed json/yaml file
def parse_json_yaml(file: str) -> dict:
    return load(file, Loader=Loader)
