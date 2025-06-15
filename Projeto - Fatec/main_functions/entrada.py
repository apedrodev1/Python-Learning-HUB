import json
from datetime import datetime
from data.products import PRODUCTS
from classes.produto import Produto

INPUT_DB_PATH = "data/db_input.json"
ESTOQUE_PATH = "data/estoque.json"

def registrar_entrada():
    try:
        tag = int(input("Digite o código RFID do produto (inteiro): "))
    except ValueError:
        print("Código inválido. Use apenas números inteiros.")
        return

    produto_data = PRODUCTS.get(tag)
    if not produto_data:
        print("Produto não encontrado para o código informado.")
        return

    try:
        quantidade = int(input("Digite a quantidade a ser adicionada: "))
        if quantidade <= 0:
            raise ValueError
    except ValueError:
        print("Quantidade inválida. Informe um número inteiro positivo.")
        return

    # Confirmação
    print(f"\nConfirmar entrada:")
    print(f"Produto: {produto_data['nome']}")
    print(f"Categoria: {produto_data['categoria']}")
    print(f"Preço unitário: R${produto_data['preco']:.2f}")
    print(f"Quantidade: {quantidade}")
    confirmar = input("Deseja confirmar? (s/n): ").lower()
    if confirmar != 's':
        print("Entrada cancelada.")
        return

    produto = Produto(
        codigo=tag,
        nome=produto_data["nome"],
        preco=produto_data["preco"],
        validade=produto_data["validade"],
        categoria=produto_data["categoria"]
    )

    # Registro da entrada
    registro = {
        "tipo": "entrada",
        "produto": produto.to_dict(),
        "quantidade": quantidade,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    salvar_registro(INPUT_DB_PATH, registro)
    atualizar_estoque(tag, quantidade)

    print(f"\nEntrada registrada com sucesso!\n - Produto: {produto.nome}\n - Quantidade adicionada: {quantidade}")

def salvar_registro(caminho, registro):
    try:
        with open(caminho, "r") as file:
            dados = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = []

    dados.append(registro)

    with open(caminho, "w") as file:
        json.dump(dados, file, indent=4)

def atualizar_estoque(codigo, quantidade):
    try:
        with open(ESTOQUE_PATH, "r") as file:
            estoque = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        estoque = {}

    estoque[str(codigo)] = estoque.get(str(codigo), 0) + quantidade

    with open(ESTOQUE_PATH, "w") as file:
        json.dump(estoque, file, indent=4)
