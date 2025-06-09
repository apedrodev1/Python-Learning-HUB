import tkinter as tk
from functions.loguin import login

# Janela principal
root = tk.Tk()
root.title("Login RFID Manager")
root.geometry("300x180")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Usuário:").pack(pady=(15, 5))
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Senha:").pack(pady=(10, 5))
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

# Passa os widgets como parâmetros para login()
tk.Button(root, text="Login", command=lambda: login(entry_user, entry_pass, root)).pack(pady=15)

root.mainloop()