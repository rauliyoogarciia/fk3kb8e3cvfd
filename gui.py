import os
import json
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from fivechanger_gui import FiveChangerApp  # Asegúrate que la ruta y nombre sea correcto

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class GuiApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("FiveChanger - Configurar Ruta")
        self.geometry("500x300")
        self.resizable(False, False)

        self.font_title = ctk.CTkFont(family="Segoe UI", size=20, weight="bold")
        self.font_text = ctk.CTkFont(family="Segoe UI", size=13, weight="normal")

        self.title_label = ctk.CTkLabel(self, text="Configurar Ruta de FiveM", font=self.font_title)
        self.title_label.pack(pady=(30, 15))

        self.frame_entry = ctk.CTkFrame(self)
        self.frame_entry.pack(padx=15, pady=15, fill="x")

        self.path_entry = ctk.CTkEntry(self.frame_entry, placeholder_text="Ruta de la carpeta FiveM", font=self.font_text)
        self.path_entry.pack(side="left", expand=True, fill="x", padx=(10, 5), pady=10)

        self.browse_btn = ctk.CTkButton(self.frame_entry, text="Seleccionar...", command=self.browse_folder)
        self.browse_btn.pack(side="left", padx=(5, 10), pady=10)

        self.save_btn = ctk.CTkButton(self, text="Guardar Ruta", command=self.guardar_ruta, font=self.font_text)
        self.save_btn.pack(pady=(10, 20))

        ruta = self.obtener_ruta_base()
        self.path_entry.insert(0, ruta)

    def browse_folder(self):
        from tkinter import filedialog
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder_selected)

    def guardar_ruta(self):
        ruta = self.path_entry.get().strip()
        if not ruta or not os.path.exists(ruta):
            messagebox.showerror("Error", "Por favor, selecciona una ruta válida.")
            return

        carpeta_config = os.path.join(os.getenv('LOCALAPPDATA'), 'FiveChanger')
        os.makedirs(carpeta_config, exist_ok=True)
        config_path = os.path.join(carpeta_config, 'config.json')

        config = {"fivem_app_path": ruta}
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)

        messagebox.showinfo("Guardado", "Ruta guardada correctamente.")

        self.destroy()  # Cierra esta ventana

        app_gestor = FiveChangerApp()  # Abre el gestor
        app_gestor.mainloop()

    def obtener_ruta_base(self):
        config_path = os.path.join(os.getenv('LOCALAPPDATA'), 'FiveChanger', 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
                return config.get("fivem_app_path", os.path.join(os.getenv('LOCALAPPDATA'), 'FiveChanger'))
        else:
            return os.path.join(os.getenv('LOCALAPPDATA'), 'FiveChanger')


if __name__ == "__main__":
    app = GuiApp()
    app.mainloop()
