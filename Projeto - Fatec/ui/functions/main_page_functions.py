import tkinter as tk
from tkinter import messagebox
from estoque.estoque import carregar_estoque
from export.export_estoque import exportar_estoque_para_xls
from data.products import PRODUCTS


def abrir_modal_estoque(parent):
    modal = tk.Toplevel(parent)
    modal.title("Estoque Atual")
    modal.geometry("400x400")
    modal.resizable(False, False)

    estoque_text = tk.Text(modal, width=50, height=15)
    estoque_text.pack(pady=10, padx=10)

    try:
        estoque = carregar_estoque()

        if not estoque:
            estoque_text.insert(tk.END, "Estoque vazio.\n")
        else:
            estoque_text.insert(tk.END, f"{'Código':<10}{'Nome':<25}{'Categoria':<15}{'Qtd':>10}\n")
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

    estoque_text.config(state=tk.DISABLED)

    btn_export = tk.Button(
        modal, 
        text="Exportar Estoque para XLS", 
        command=lambda: exportar_estoque(modal)
    )
    btn_export.pack(pady=10)


def exportar_estoque(parent):
    try:
        exportar_estoque_para_xls()
        messagebox.showinfo("Sucesso", "Estoque exportado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao exportar estoque: {e}")
