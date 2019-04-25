import os
import json


def parse_folders(filepath):
    folderpath = os.path.join(filepath, os.pardir, "boostnote.json")

    with open(folderpath, "r") as f:
        parsed_json = json.load(f)

    folders = parsed_json["folders"]

    f_dict = {}

    for i in folders:
        f_dict[i["key"]] = i["name"]

    return f_dict
