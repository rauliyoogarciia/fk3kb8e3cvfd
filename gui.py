import tkinter as tk
import customtkinter as ctk
from utils.profile_manager import get_profiles, save_profile, load_profile, delete_profile
from tkinter import messagebox

class ProfileManagerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Perfiles")
        self.geometry("500x400")
        self.font_bold = ("Helvetica", 14, "bold")

        container = ctk.CTkFrame(self)
        container.pack(padx=20, pady=20, fill="both", expand=True)

        # Listbox para mostrar perfiles
        self.listbox = tk.Listbox(container, font=self.font_bold, bg="#2b2b2b", fg="white",
                                  selectbackground="#3a3a3a")
        self.listbox.pack(fill="both", expand=True)

        # Entrada para crear perfil nuevo
        self.new_profile_entry = ctk.CTkEntry(container, placeholder_text="Nombre nuevo perfil", font=self.font_bold)
        self.new_profile_entry.pack(pady=10, fill="x")

        # Botón crear perfil
        self.create_btn = ctk.CTkButton(container, text="Crear perfil", font=self.font_bold, command=self.create_profile)
        self.create_btn.pack(pady=5)

        # Frame con botones cargar y eliminar perfil
        btn_frame = ctk.CTkFrame(container)
        btn_frame.pack(pady=10, fill="x")

        self.load_btn = ctk.CTkButton(btn_frame, text="Cargar perfil", font=self.font_bold, command=self.load_profile)
        self.load_btn.pack(side="left", expand=True, padx=5)

        self.delete_btn = ctk.CTkButton(btn_frame, text="Eliminar perfil", font=self.font_bold, command=self.delete_profile)
        self.delete_btn.pack(side="left", expand=True, padx=5)

        self.refresh_profiles()

    def refresh_profiles(self):
        self.listbox.delete(0, tk.END)
        perfiles = get_profiles()
        for perfil in perfiles:
            self.listbox.insert(tk.END, perfil)

    def create_profile(self):
        name = self.new_profile_entry.get().strip()
        if not name:
            messagebox.showwarning("Error", "El nombre del perfil no puede estar vacío.")
            return
        perfiles = get_profiles()
        if name in perfiles:
            messagebox.showwarning("Error", "Ese perfil ya existe.")
            return
        try:
            save_profile(name)
            messagebox.showinfo("Éxito", f"Perfil '{name}' creado.")
            self.new_profile_entry.delete(0, tk.END)
            self.refresh_profiles()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el perfil:\n{e}")

    def load_profile(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Error", "Selecciona un perfil para cargar.")
            return
        perfil = self.listbox.get(selection[0])
        try:
            load_profile(perfil)
            messagebox.showinfo("Éxito", f"Perfil '{perfil}' cargado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el perfil:\n{e}")

    def delete_profile(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Error", "Selecciona un perfil para eliminar.")
            return
        perfil = self.listbox.get(selection[0])
        if messagebox.askyesno("Confirmar", f"¿Eliminar perfil '{perfil}'? Esta acción no se puede deshacer."):
            try:
                delete_profile(perfil)
                messagebox.showinfo("Éxito", f"Perfil '{perfil}' eliminado.")
                self.refresh_profiles()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el perfil:\n{e}")
