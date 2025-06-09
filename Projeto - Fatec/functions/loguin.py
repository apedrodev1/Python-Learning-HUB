from tkinter import messagebox

# Usuários fictícios para simulação
USERS = {
    "admin": "1234",
    "usuario": "senha"
}

def login(entry_user, entry_pass, root):
    username = entry_user.get().strip()
    password = entry_pass.get().strip()

    if not username or not password:
        messagebox.showwarning("Campos obrigatórios", "Preencha usuário e senha.")
        return

    if username not in USERS:
        messagebox.showerror("Usuário inválido", "Usuário não encontrado.")
        entry_user.delete(0, 'end')
        entry_pass.delete(0, 'end')
        return

    if USERS[username] != password:
        messagebox.showerror("Senha incorreta", "A senha está errada.")
        entry_pass.delete(0, 'end')
        return

    # Login bem-sucedido
    messagebox.showinfo("Login bem-sucedido", f"Bem-vindo, {username}!")
    root.destroy()

    # Armazena nome do usuário se quiser usá-lo em main_page
    import main_page
    main_page.set_logged_user(username)
