import json


def pretty_print(input_dict: dict):
    print(json.dumps(input_dict, sort_keys=False, indent=4))
