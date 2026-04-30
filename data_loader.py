import json
import os

BASE_PATH = "dataset/expanded"


def load_json_folder(folder, key_name):
    data = {}
    path = os.path.join(BASE_PATH, folder)

    for file in os.listdir(path):
        with open(os.path.join(path, file), "r", encoding="utf-8") as f:
            obj = json.load(f)

            key = obj.get(key_name)
            if key:
                data[key] = obj

    return data

MERCHANTS = load_json_folder("merchants", "merchant_id")
TRIGGERS = load_json_folder("triggers", "trigger_id")
CUSTOMERS = load_json_folder("customers", "customer_id")
CATEGORIES = load_json_folder("categories", "category_id")
