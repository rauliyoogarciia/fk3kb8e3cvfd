import os
import json
import shutil
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class FiveChangerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("FiveChanger - Gestor de Perfiles")
        self.geometry("800x700")
        self.resizable(False, False)

        self.font_title = ctk.CTkFont(family="Segoe UI", size=24, weight="bold")
        self.font_text = ctk.CTkFont(family="Segoe UI", size=14, weight="bold")

        self.fondo_color = self.cget("bg")

        self.title_label = ctk.CTkLabel(self, text="Gestor de Perfiles de FiveM", font=self.font_title)
        self.title_label.pack(pady=(30, 10))

        self.frame_lista = ctk.CTkFrame(self, fg_color=self.fondo_color)
        self.frame_lista.pack(padx=40, pady=10, fill="both", expand=True)

        self.perfiles_listbox = tk.Listbox(
            self.frame_lista,
            font=self.font_text,
            activestyle='none',
            selectmode=tk.SINGLE,
            bg="#1e1e1e",
            fg="white",
            highlightthickness=0,
            borderwidth=0,
            relief="flat",
            selectbackground="#333333",
            selectforeground="white",
            height=20
        )
        self.perfiles_listbox.pack(side="left", fill="both", expand=True, padx=(0, 0), pady=0)
        self.perfiles_listbox.bind("<MouseWheel>", self.scroll_listbox)

        # Campo visible siempre
        self.crear_frame = ctk.CTkFrame(self, fg_color=self.fondo_color)
        self.crear_frame.pack(padx=40, pady=(0, 10), fill="x")

        self.crear_entry = ctk.CTkEntry(self.crear_frame, font=self.font_text, placeholder_text="Nombre del nuevo perfil")
        self.crear_entry.pack(side="left", padx=10, pady=10, expand=True, fill="x")

        self.confirmar_btn = ctk.CTkButton(self.crear_frame, text="Crear", font=self.font_text, command=self.confirmar_creacion)
        self.confirmar_btn.pack(side="left", padx=10, pady=10)

        self.botones_frame = ctk.CTkFrame(self, fg_color=self.fondo_color, corner_radius=0)
        self.botones_frame.pack(pady=(0, 5))

        button_width = 170

        self.botones_contenedor = ctk.CTkFrame(self.botones_frame, fg_color="transparent")
        self.botones_contenedor.pack(pady=10)

        self.btn_eliminar = ctk.CTkButton(self.botones_contenedor, text="Eliminar Perfil", width=button_width,
                                          fg_color="#f44336", hover_color="#d32f2f", font=self.font_text,
                                          command=self.eliminar_perfil)
        self.btn_eliminar.grid(row=0, column=0, padx=10)

        self.btn_abrir = ctk.CTkButton(self.botones_contenedor, text="Abrir Carpeta Perfil", width=button_width,
                                       fg_color="#2196F3", hover_color="#1976d2", font=self.font_text,
                                       command=self.abrir_carpeta_perfil)
        self.btn_abrir.grid(row=0, column=1, padx=10)

        self.btn_aplicar = ctk.CTkButton(self.botones_contenedor, text="Aplicar Perfil", width=button_width,
                                         fg_color="#FFA500", hover_color="#cc8400", font=self.font_text,
                                         command=self.aplicar_perfil)
        self.btn_aplicar.grid(row=0, column=2, padx=10)

        self.ruta_base = self.obtener_ruta_base()
        self.perfiles_path = os.path.join(self.ruta_base, "FiveChangerProfiles")
        os.makedirs(self.perfiles_path, exist_ok=True)

        self.cargar_perfiles()

    def scroll_listbox(self, event):
        self.perfiles_listbox.yview_scroll(-1 * int(event.delta / 120), "units")

    def confirmar_creacion(self):
        nombre = self.crear_entry.get().strip()
        if not nombre:
            messagebox.showwarning("Error", "El nombre no puede estar vacío.")
            return

        ruta_perfil = os.path.join(self.perfiles_path, nombre)
        if os.path.exists(ruta_perfil):
            messagebox.showwarning("Error", "Ese perfil ya existe.")
            return

        os.makedirs(os.path.join(ruta_perfil, "citizen"), exist_ok=True)
        os.makedirs(os.path.join(ruta_perfil, "mods"), exist_ok=True)
        os.makedirs(os.path.join(ruta_perfil, "plugins"), exist_ok=True)

        self.crear_entry.delete(0, tk.END)
        self.cargar_perfiles()

    def obtener_ruta_base(self):
        config_path = os.path.join(os.getenv('LOCALAPPDATA'), 'FiveChanger', 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
                return config.get("fivem_app_path", os.path.join(os.getenv('LOCALAPPDATA'), 'FiveChanger'))
        return os.path.join(os.getenv('LOCALAPPDATA'), 'FiveChanger')

    def cargar_perfiles(self):
        self.perfiles_listbox.delete(0, tk.END)
        if os.path.exists(self.perfiles_path):
            perfiles = sorted(os.listdir(self.perfiles_path))
            for perfil in perfiles:
                if os.path.isdir(os.path.join(self.perfiles_path, perfil)):
                    self.perfiles_listbox.insert(tk.END, f"  {perfil}")

    def eliminar_perfil(self):
        seleccion = self.perfiles_listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un perfil para eliminar.")
            return
        perfil = self.perfiles_listbox.get(seleccion[0]).strip()
        confirmar = messagebox.askyesno("Eliminar", f"¿Eliminar el perfil '{perfil}'?")
        if confirmar:
            shutil.rmtree(os.path.join(self.perfiles_path, perfil))
            self.cargar_perfiles()

    def abrir_carpeta_perfil(self):
        seleccion = self.perfiles_listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un perfil para abrir su carpeta.")
            return
        perfil = self.perfiles_listbox.get(seleccion[0]).strip()
        ruta = os.path.join(self.perfiles_path, perfil)
        if os.path.exists(ruta):
            os.startfile(ruta)

    def aplicar_perfil(self):
        seleccion = self.perfiles_listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un perfil para aplicar.")
            return

        perfil = self.perfiles_listbox.get(seleccion[0]).strip()
        ruta_perfil = os.path.join(self.perfiles_path, perfil)
        ruta_fivem = self.obtener_ruta_base()

        for folder in ["citizen", "mods", "plugins"]:
            origen = os.path.join(ruta_perfil, folder)
            destino = os.path.join(ruta_fivem, folder)

            if os.path.exists(destino):
                shutil.rmtree(destino)
            if os.path.exists(origen):
                shutil.copytree(origen, destino)

        messagebox.showinfo("Perfil Aplicado", f"El perfil '{perfil}' se ha aplicado correctamente.")

if __name__ == "__main__":
    app = FiveChangerApp()
    app.mainloop()
