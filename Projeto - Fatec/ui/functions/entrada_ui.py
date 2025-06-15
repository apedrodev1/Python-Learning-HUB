import tkinter as tk
from tkinter import messagebox
from estoque.estoque import carregar_estoque, salvar_estoque


def abrir_tela_entrada():
    entrada_window = tk.Toplevel()
    entrada_window.title("Registrar Entrada")
    entrada_window.geometry("400x200")

    tk.Label(entrada_window, text="Código do Produto:").pack(pady=5)
    entry_codigo = tk.Entry(entrada_window)
    entry_codigo.pack(pady=5)

    tk.Label(entrada_window, text="Quantidade:").pack(pady=5)
    entry_quantidade = tk.Entry(entrada_window)
    entry_quantidade.pack(pady=5)

    def registrar_entrada():
        codigo = entry_codigo.get().strip()
        quantidade = entry_quantidade.get().strip()

        if not codigo or not quantidade.isdigit():
            messagebox.showerror("Erro", "Dados inválidos.")
            return

        estoque = carregar_estoque()
        quantidade = int(quantidade)

        if codigo in estoque:
            estoque[codigo]["quantidade"] += quantidade
        else:
            nome = "Produto Desconhecido"
            categoria = "N/A"
            estoque[codigo] = {
                "nome": nome,
                "categoria": categoria,
                "quantidade": quantidade
            }

        salvar_estoque(estoque)
        messagebox.showinfo("Sucesso", "Entrada registrada com sucesso.")
        entrada_window.destroy()

    tk.Button(entrada_window, text="Registrar", command=registrar_entrada).pack(pady=10)
