import tkinter as tk
from tkinter import messagebox
from estoque.estoque import carregar_estoque
from export.export_estoque import exportar_estoque_para_xls
from ui.functions.entrada_ui import abrir_tela_entrada
from ui.functions.saida_ui import abrir_tela_saida


logged_user = None


def set_logged_user(user):
    global logged_user
    logged_user = user
    abrir_pagina_principal()


def abrir_pagina_principal():
    janela = tk.Tk()
    janela.title(f"Controle de Estoque - Usuário: {logged_user}")
    janela.geometry("500x400")
    janela.resizable(False, False)

    tk.Label(janela, text="Menu Principal", font=("Arial", 18)).pack(pady=20)

    tk.Button(janela, text="Registrar Entrada", width=25, height=2, bg="#4CAF50", fg="white",
              command=abrir_tela_entrada).pack(pady=10)

    tk.Button(janela, text="Registrar Saída", width=25, height=2, bg="#f44336", fg="white",
              command=abrir_tela_saida).pack(pady=10)

    tk.Button(janela, text="Visualizar Estoque", width=25, height=2, bg="#2196F3", fg="white",
              command=abrir_modal_estoque).pack(pady=10)

    tk.Button(janela, text="Sair", width=15, command=janela.destroy).pack(pady=30)

    janela.mainloop()


def abrir_modal_estoque():
    estoque = carregar_estoque()

    modal = tk.Toplevel()
    modal.title("Estoque Atual")
    modal.geometry("400x300")
    modal.resizable(False, False)

    texto = "Estoque Atual:\n\n"
    for produto_cod, dados in estoque.items():
        nome = dados.get("nome", "Sem nome")
        qtd = dados.get("quantidade", 0)
        texto += f"{nome} (Código: {produto_cod}) - Quantidade: {qtd}\n"

    label_estoque = tk.Label(modal, text=texto, justify="left", font=("Arial", 12))
    label_estoque.pack(padx=20, pady=20)

    btn_exportar = tk.Button(modal, text="Exportar Estoque para XLS", command=lambda: exportar_estoque_para_xls(estoque))
    btn_exportar.pack(pady=10)
