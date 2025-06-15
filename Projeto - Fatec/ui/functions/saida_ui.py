import tkinter as tk
from tkinter import messagebox
from estoque.estoque import carregar_estoque, salvar_estoque


def abrir_tela_saida():
    saida_window = tk.Toplevel()
    saida_window.title("Registrar Saída")
    saida_window.geometry("400x200")

    tk.Label(saida_window, text="Código do Produto:").pack(pady=5)
    entry_codigo = tk.Entry(saida_window)
    entry_codigo.pack(pady=5)

    tk.Label(saida_window, text="Quantidade:").pack(pady=5)
    entry_quantidade = tk.Entry(saida_window)
    entry_quantidade.pack(pady=5)

    def registrar_saida():
        codigo = entry_codigo.get().strip()
        quantidade = entry_quantidade.get().strip()

        if not codigo or not quantidade.isdigit():
            messagebox.showerror("Erro", "Dados inválidos.")
            return

        estoque = carregar_estoque()
        quantidade = int(quantidade)

        if codigo in estoque:
            if estoque[codigo]["quantidade"] >= quantidade:
                estoque[codigo]["quantidade"] -= quantidade
                salvar_estoque(estoque)
                messagebox.showinfo("Sucesso", "Saída registrada com sucesso.")
                saida_window.destroy()
            else:
                messagebox.showerror("Erro", "Quantidade insuficiente no estoque.")
        else:
            messagebox.showerror("Erro", "Produto não encontrado no estoque.")

    tk.Button(saida_window, text="Registrar", command=registrar_saida).pack(pady=10)
