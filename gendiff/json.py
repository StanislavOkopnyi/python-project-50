import json


def make_json(source: list[dict]) -> str:
    return json.dumps(source)
