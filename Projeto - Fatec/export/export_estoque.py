import json
import xlwt

ESTOQUE_PATH = "data/estoque.json"
EXPORT_PATH = "data/estoque.xls"


def carregar_estoque():
    try:
        with open(ESTOQUE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def exportar_estoque_para_xls(estoque):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Estoque")

    headers = ["Código", "Nome", "Categoria", "Quantidade"]
    for col, title in enumerate(headers):
        sheet.write(0, col, title)

    row = 1
    for codigo, dados in estoque.items():
        nome = dados.get("nome", "Desconhecido")
        categoria = dados.get("categoria", "N/A")
        quantidade = dados.get("quantidade", 0)

        sheet.write(row, 0, codigo)
        sheet.write(row, 1, nome)
        sheet.write(row, 2, categoria)
        sheet.write(row, 3, quantidade)
        row += 1

    workbook.save(EXPORT_PATH)
    print(f"✅ Estoque exportado com sucesso para {EXPORT_PATH}")
