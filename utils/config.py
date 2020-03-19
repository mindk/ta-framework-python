import json
import os
import logging


def get_config(attr):
    test_data_path = os.path.abspath("../config.json")
    with open(test_data_path) as f:
        json_file = json.load(f)
        prop = json_file.get(attr)
    return prop
