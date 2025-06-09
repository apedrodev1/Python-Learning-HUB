import tkinter as tk

# Armazena o nome do usuário logado (recebido via set_logged_user)
logged_user = None

def set_logged_user(user):
    global logged_user
    logged_user = user
    abrir_pagina_principal()

def abrir_pagina_principal():
    window = tk.Tk()
    window.title("RFID Manager - Menu Principal")
    window.geometry("350x250")
    window.resizable(False, False)

    # Saudação
    saudacao = f"Bem-vindo, {logged_user}!" if logged_user else "Bem-vindo!"
    tk.Label(window, text=saudacao, font=("Arial", 12, "bold")).pack(pady=20)

    # Botões de ação
    tk.Button(window, text="Registrar Entrada", width=20, command=registrar_entrada).pack(pady=5)
    tk.Button(window, text="Registrar Saída", width=20, command=registrar_saida).pack(pady=5)

    # Botão para fechar
    tk.Button(window, text="Sair", width=20, command=window.destroy).pack(pady=20)

    window.mainloop()

# Funções temporárias de ação
def registrar_entrada():
    print(">> Entrada de produto (em breve)")

def registrar_saida():
    print(">> Saída de produto (em breve)")
