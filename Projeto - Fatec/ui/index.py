import tkinter as tk
import main_functions.login as login_module

def iniciar_app():
    root = tk.Tk()
    root.title("Login - Sistema")

    tk.Label(root, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
    entry_user = tk.Entry(root)
    entry_user.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
    entry_pass = tk.Entry(root, show="*")
    entry_pass.grid(row=1, column=1, padx=10, pady=10)

    btn_login = tk.Button(root, text="Entrar", command=lambda: login_module.login(entry_user, entry_pass, root))
    btn_login.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    iniciar_app()
