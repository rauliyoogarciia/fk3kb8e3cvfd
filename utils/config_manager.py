import os
import json

CONFIG_PATH = os.path.join(os.getenv("LOCALAPPDATA"), "FiveChanger")
CONFIG_FILE = os.path.join(CONFIG_PATH, "config.json")

def get_fivem_app_path():
    if not os.path.exists(CONFIG_FILE):
        return None
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("fivem_app_path")
    except Exception:
        return None

def save_fivem_app_path(path):
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)
    data = {"fivem_app_path": path}
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
