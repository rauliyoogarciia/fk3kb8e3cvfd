import os
import json
import sys
import subprocess

def get_config_path():
    local_appdata = os.getenv('LOCALAPPDATA')
    app_folder = os.path.join(local_appdata, 'FiveChanger')
    if not os.path.exists(app_folder):
        os.makedirs(app_folder)
    return os.path.join(app_folder, 'config.json')

def load_config():
    config_path = get_config_path()
    if os.path.isfile(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def main():
    config = load_config()
    if config.get("fivem_app_path"):
        # Ya tiene ruta guardada: abrir gestor de perfiles
        ruta_fivechanger_gui = os.path.join(os.path.dirname(__file__), "fivechanger_gui.py")
        subprocess.Popen([sys.executable, ruta_fivechanger_gui])
    else:
        # No tiene ruta: abrir ventana para seleccionar ruta (gui.py)
        from gui import GuiApp
        app = GuiApp()
        app.mainloop()

if __name__ == "__main__":
    main()
