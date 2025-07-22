import os
import shutil
from utils.config_manager import get_fivem_app_path

FIVEM_APP_PATH = get_fivem_app_path()
PROFILES_PATH = os.path.join(os.getenv("LOCALAPPDATA"), "FiveChanger", "FiveChangerProfiles")

def get_profiles():
    if not os.path.exists(PROFILES_PATH):
        os.makedirs(PROFILES_PATH)
    return [name for name in os.listdir(PROFILES_PATH) if os.path.isdir(os.path.join(PROFILES_PATH, name))]

def save_profile(profile_name):
    profile_path = os.path.join(PROFILES_PATH, profile_name)
    if os.path.exists(profile_path):
        shutil.rmtree(profile_path)
    os.makedirs(profile_path)

    for folder_name in ["citizen", "mods", "plugins"]:
        src = os.path.join(FIVEM_APP_PATH, folder_name)
        dst = os.path.join(profile_path, folder_name)
        if os.path.exists(src):
            shutil.copytree(src, dst)

def load_profile(profile_name):
    profile_path = os.path.join(PROFILES_PATH, profile_name)
    if not os.path.exists(profile_path):
        raise FileNotFoundError(f"El perfil '{profile_name}' no existe.")

    for folder_name in ["citizen", "mods", "plugins"]:
        src = os.path.join(profile_path, folder_name)
        dst = os.path.join(FIVEM_APP_PATH, folder_name)

        if os.path.exists(dst):
            shutil.rmtree(dst)

        if os.path.exists(src):
            shutil.copytree(src, dst)

def delete_profile(profile_name):
    profile_path = os.path.join(PROFILES_PATH, profile_name)
    if os.path.exists(profile_path):
        shutil.rmtree(profile_path)
    else:
        raise FileNotFoundError(f"El perfil '{profile_name}' no existe.")
