import json
import xlwt
from data.products import PRODUCTS

ESTOQUE_PATH = "data/estoque.json"
EXPORT_PATH = "data/estoque.xls"

def visualizar_estoque():
    try:
        with open(ESTOQUE_PATH, "r") as file:
            estoque = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Estoque vazio ou não encontrado.")
        return

    if not estoque:
        print("Estoque está vazio.")
        return

    print("\nEstoque Atual:")
    print(f"{'Código':<10} {'Nome':<25} {'Categoria':<15} {'Qtd':>5}")
    print("-" * 60)

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Estoque")

    headers = ["Código", "Nome", "Categoria", "Quantidade"]
    for col, title in enumerate(headers):
        sheet.write(0, col, title)

    row = 1
    for codigo_str, qtd in estoque.items():
        codigo = int(codigo_str)
        produto = PRODUCTS.get(codigo)

        nome = produto["nome"] if produto else "Desconhecido"
        categoria = produto["categoria"] if produto else "N/A"

        print(f"{codigo:<10} {nome:<25} {categoria:<15} {qtd:>5}")

        sheet.write(row, 0, codigo)
        sheet.write(row, 1, nome)
        sheet.write(row, 2, categoria)
        sheet.write(row, 3, qtd)
        row += 1

    workbook.save(EXPORT_PATH)
    print(f"\n📁 Estoque exportado com sucesso para: {EXPORT_PATH}")
