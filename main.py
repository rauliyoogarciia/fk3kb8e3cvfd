def mostrar_login():
    root = ctk.CTk()
    root.title("Login")
    root.geometry("350x260")
    root.resizable(False, False)

    def intentar_login():
        username = entry_user.get().strip()
        password = entry_pass.get().strip()
        if login_user(username, password):
            root.destroy()
        else:
            messagebox.showerror("Error", "Inicio de sesión fallido. Verifica tus datos.")

    def intentar_registro():
        username = entry_user.get().strip()
        password = entry_pass.get().strip()
        license_key = entry_license.get().strip()
        if register_user(username, password, license_key):
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            mostrar_login_form()
        else:
            messagebox.showerror("Error", "Registro fallido. Verifica tu licencia.")

    def mostrar_registro_form():
        btn_login.pack_forget()
        btn_registrarse.pack_forget()

        label_license.pack(pady=(10, 0), padx=20)
        entry_license.pack(pady=(0, 10), padx=20)

        btn_registro_final.pack(pady=(15, 5), padx=20)
        btn_volver.pack(padx=20)

        root.geometry("350x320")

    def mostrar_login_form():
        label_license.pack_forget()
        entry_license.pack_forget()
        btn_registro_final.pack_forget()
        btn_volver.pack_forget()

        btn_login.pack(pady=(15, 5), padx=20)
        btn_registrarse.pack(padx=20)

        root.geometry("350x260")

    def cerrar_app():
        root.destroy()
        sys.exit()

    # Frame para alinear mejor todo
    frame = ctk.CTkFrame(root)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    ctk.CTkLabel(frame, text="Usuario:", font=ctk.CTkFont(weight="bold")).pack(pady=(10, 0), padx=20, anchor="w")
    entry_user = ctk.CTkEntry(frame)
    entry_user.pack(padx=20, fill="x")

    ctk.CTkLabel(frame, text="Contraseña:", font=ctk.CTkFont(weight="bold")).pack(pady=(10, 0), padx=20, anchor="w")
    entry_pass = ctk.CTkEntry(frame, show="*")
    entry_pass.pack(padx=20, fill="x")

    label_license = ctk.CTkLabel(frame, text="Licencia (solo registro):", font=ctk.CTkFont(weight="bold"))
    entry_license = ctk.CTkEntry(frame)

    btn_login = ctk.CTkButton(frame, text="Iniciar Sesión", command=intentar_login)
    btn_registrarse = ctk.CTkButton(frame, text="Registrarse", command=mostrar_registro_form)

    btn_registro_final = ctk.CTkButton(frame, text="Registrar", command=intentar_registro)
    btn_volver = ctk.CTkButton(frame, text="Volver", command=mostrar_login_form)

    btn_login.pack(pady=(15, 5), padx=20, fill="x")
    btn_registrarse.pack(padx=20, fill="x")

    root.protocol("WM_DELETE_WINDOW", cerrar_app)
    root.mainloop()
