import tkinter as tk
from tkinter import messagebox
import json
from ui import main_page  # importando o módulo main_page para chamar set_logged_user

USERS_PATH = "data/users.json"

def verificar_login(usuario, senha):
    try:
        with open(USERS_PATH, "r") as file:
            usuarios = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

    return usuarios.get(usuario) == senha

def login(entry_user, entry_pass, root_login):
    usuario = entry_user.get()
    senha = entry_pass.get()

    if verificar_login(usuario, senha):
        messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
        root_login.destroy()
        main_page.set_logged_user(usuario)  # chama a tela principal
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")
