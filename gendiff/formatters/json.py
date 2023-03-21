import json


def make_json(source: list[dict]) -> str:
    '''Returns json from list of "item" and "common_dict"'''
    return json.dumps(source)
