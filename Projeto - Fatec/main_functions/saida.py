import json
from datetime import datetime
from data.products import PRODUCTS
from classes.produto import Produto

OUTPUT_DB_PATH = "data/db_output.json"
ESTOQUE_PATH = "data/estoque.json"

def registrar_saida():
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
        quantidade = int(input("Digite a quantidade a ser retirada: "))
        if quantidade <= 0:
            raise ValueError
    except ValueError:
        print("Quantidade inválida. Informe um número inteiro positivo.")
        return

    estoque = carregar_estoque()

    estoque_atual = estoque.get(str(tag), 0)
    if quantidade > estoque_atual:
        print(f"Estoque insuficiente. Disponível: {estoque_atual}")
        return

    # Confirmação
    print(f"\nConfirmar saída:")
    print(f"Produto: {produto_data['nome']}")
    print(f"Categoria: {produto_data['categoria']}")
    print(f"Preço unitário: R${produto_data['preco']:.2f}")
    print(f"Quantidade: {quantidade}")
    confirmar = input("Deseja confirmar? (s/n): ").lower()
    if confirmar != 's':
        print("Saída cancelada.")
        return

    produto = Produto(
        codigo=tag,
        nome=produto_data["nome"],
        preco=produto_data["preco"],
        validade=produto_data["validade"],
        categoria=produto_data["categoria"]
    )

    registro = {
        "tipo": "saida",
        "produto": produto.to_dict(),
        "quantidade": quantidade,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    salvar_registro(OUTPUT_DB_PATH, registro)
    atualizar_estoque(tag, -quantidade)

    print(f"\nSaída registrada com sucesso!\n - Produto: {produto.nome}\n - Quantidade retirada: {quantidade}")

def carregar_estoque():
    try:
        with open(ESTOQUE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def salvar_registro(caminho, registro):
    try:
        with open(caminho, "r") as file:
            dados = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = []

    dados.append(registro)

    with open(caminho, "w") as file:
        json.dump(dados, file, indent=4)

def atualizar_estoque(codigo, quantidade_delta):
    estoque = carregar_estoque()
    codigo_str = str(codigo)
    estoque[codigo_str] = estoque.get(codigo_str, 0) + quantidade_delta

    with open(ESTOQUE_PATH, "w") as file:
        json.dump(estoque, file, indent=4)
