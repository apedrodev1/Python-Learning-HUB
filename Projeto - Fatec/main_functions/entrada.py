from datetime import datetime
from data.products import PRODUCTS
from classes.produto import Produto
from utils.utils_json import carregar_json, salvar_json
from estoque.estoque import atualizar_estoque

INPUT_DB_PATH = "data/db_input.json"


def registrar_entrada(codigo, quantidade):
    produto_data = PRODUCTS.get(codigo)
    if not produto_data:
        raise ValueError("Produto não encontrado.")

    if quantidade <= 0:
        raise ValueError("Quantidade inválida. Informe um número positivo.")

    produto = Produto(
        codigo=codigo,
        nome=produto_data["nome"],
        preco=produto_data["preco"],
        validade=produto_data["validade"],
        categoria=produto_data["categoria"]
    )

    registro = {
        "tipo": "entrada",
        "produto": produto.to_dict(),
        "quantidade": quantidade,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    dados = carregar_json(INPUT_DB_PATH) or []
    dados.append(registro)
    salvar_json(INPUT_DB_PATH, dados)

    atualizar_estoque(codigo, quantidade)
