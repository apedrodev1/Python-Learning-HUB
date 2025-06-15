import json
from tkinter import messagebox
import main_page

USERS_PATH = "data/users.json"

def carregar_usuarios():
    try:
        with open(USERS_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def login(entry_user, entry_pass, root):
    username = entry_user.get().strip()
    password = entry_pass.get().strip()

    if not username or not password:
        messagebox.showwarning("Campos obrigatórios", "Preencha usuário e senha.")
        return

    users = carregar_usuarios()

    if username not in users:
        messagebox.showerror("Usuário inválido", "Usuário não encontrado.")
        entry_user.delete(0, 'end')
        entry_pass.delete(0, 'end')
        return

    if users[username] != password:
        messagebox.showerror("Senha incorreta", "A senha está errada.")
        entry_pass.delete(0, 'end')
        return

    messagebox.showinfo("Login bem-sucedido", f"Bem-vindo, {username}!")
    root.destroy()
    main_page.set_logged_user(username)
