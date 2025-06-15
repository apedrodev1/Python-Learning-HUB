import tkinter as tk
from tkinter import messagebox
from main_functions.entrada import registrar_entrada
from main_functions.saida import registrar_saida
from export.export_estoque import visualizar_estoque, exportar_estoque  # ajuste conforme exportar.py

logged_user = None

def set_logged_user(user):
    global logged_user
    logged_user = user
    abrir_pagina_principal()

def abrir_pagina_principal():
    window = tk.Tk()
    window.title("RFID Manager - Menu Principal")
    window.geometry("350x300")
    window.resizable(False, False)

    saudacao = f"Bem-vindo, {logged_user}!" if logged_user else "Bem-vindo!"
    tk.Label(window, text=saudacao, font=("Arial", 12, "bold")).pack(pady=20)

    tk.Button(window, text="Registrar Entrada", width=20, command=registrar_entrada).pack(pady=5)
    tk.Button(window, text="Registrar Saída", width=20, command=registrar_saida).pack(pady=5)
    tk.Button(window, text="Visualizar Estoque", width=20, command=lambda: abrir_modal_estoque(window)).pack(pady=5)
    tk.Button(window, text="Sair", width=20, command=window.destroy).pack(pady=20)

    window.mainloop()

def abrir_modal_estoque(parent):
    modal = tk.Toplevel(parent)
    modal.title("Estoque Atual")
    modal.geometry("400x400")
    modal.resizable(False, False)

    # Texto do estoque no modal
    estoque_text = tk.Text(modal, width=50, height=15)
    estoque_text.pack(pady=10, padx=10)

    # Carregar e mostrar o estoque no Text widget
    try:
        from estoque.estoque import carregar_estoque
        from data.products import PRODUCTS
        estoque = carregar_estoque()

        if not estoque:
            estoque_text.insert(tk.END, "Estoque vazio.\n")
        else:
            estoque_text.insert(tk.END, f"{'Código':<10}{'Nome':<25}{'Categoria':<15}{'Quantidade':>10}\n")
            estoque_text.insert(tk.END, "-"*60 + "\n")

            for codigo_str, qtd in estoque.items():
                codigo = int(codigo_str)
                produto = PRODUCTS.get(codigo)
                nome = produto["nome"] if produto else "Desconhecido"
                categoria = produto["categoria"] if produto else "N/A"
                linha = f"{codigo:<10}{nome:<25}{categoria:<15}{qtd:>10}\n"
                estoque_text.insert(tk.END, linha)

    except Exception as e:
        estoque_text.insert(tk.END, f"Erro ao carregar estoque: {e}")

    estoque_text.config(state=tk.DISABLED)  # para evitar edição manual

    # Botão para exportar o estoque
    btn_export = tk.Button(modal, text="Exportar Estoque para XLS", command=lambda: exportar_estoque(modal))
    btn_export.pack(pady=10)

def exportar_estoque(parent):
    try:
        from export.export_estoque import exportar_estoque_para_xls
        exportar_estoque_para_xls()
        messagebox.showinfo("Sucesso", "Estoque exportado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao exportar estoque: {e}")
