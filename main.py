import customtkinter as ctk
from tkinter import filedialog, messagebox
from gui import ProfileManagerGUI
from utils.config_manager import get_fivem_app_path, save_fivem_app_path
from utils.keyauth_manager import init_keyauth, login_user, register_user, is_authenticated

import os
import sys

def seleccionar_ruta_fivem():
    fivem_path = get_fivem_app_path()
    if not fivem_path or not os.path.exists(fivem_path):
        root = ctk.CTk()
        root.withdraw()
        messagebox.showinfo("Seleccionar ruta FiveM", "Por favor selecciona la carpeta de instalación de FiveM.")
        carpeta = filedialog.askdirectory(title="Selecciona carpeta FiveM")
        root.destroy()
        if not carpeta:
            messagebox.showerror("Error", "No se seleccionó carpeta de FiveM. El programa se cerrará.")
            sys.exit(1)
        save_fivem_app_path(carpeta)

def mostrar_login():
    root = ctk.CTk()
    root.title("Login")
    root.geometry("350x300")

    def intentar_login():
        username = entry_user.get()
        password = entry_pass.get()
        if login_user(username, password):
            root.destroy()
        else:
            messagebox.showerror("Error", "Inicio de sesión fallido.")

    def intentar_registro():
        username = entry_user.get()
        password = entry_pass.get()
        license = entry_license.get()
        success, message = register_user(username, password, license)
        if success:
            messagebox.showinfo("Éxito", message)
        else:
            messagebox.showerror("Error", f"Registro fallido: {message}")

    ctk.CTkLabel(root, text="Usuario:", font=ctk.CTkFont(weight="bold")).pack(pady=(20, 0))
    entry_user = ctk.CTkEntry(root)
    entry_user.pack()

    ctk.CTkLabel(root, text="Contraseña:", font=ctk.CTkFont(weight="bold")).pack(pady=(10, 0))
    entry_pass = ctk.CTkEntry(root, show="*")
    entry_pass.pack()

    ctk.CTkLabel(root, text="Licencia (solo registro):", font=ctk.CTkFont(weight="bold")).pack(pady=(10, 0))
    entry_license = ctk.CTkEntry(root)
    entry_license.pack()

    ctk.CTkButton(root, text="Iniciar Sesión", command=intentar_login).pack(pady=(15, 5))
    ctk.CTkButton(root, text="Registrarse", command=intentar_registro).pack()

    root.mainloop()

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    init_keyauth()

    if not is_authenticated():
        mostrar_login()

    seleccionar_ruta_fivem()

    app = ProfileManagerGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
