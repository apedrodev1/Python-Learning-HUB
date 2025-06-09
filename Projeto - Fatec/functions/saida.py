import json
from datetime import datetime
from data.products import PRODUCTS

DB_PATH = "data/output.json"

def registrar_saida():
    try:
        tag = int(input("Digite o código RFID do produto (inteiro): "))
    except ValueError:
        print("Código inválido. Use apenas números inteiros.")
        return

    produto = PRODUCTS.get(tag)
    if not produto:
        print("Produto não encontrado para o código informado.")
        return

    registro = {
        "tipo": "saida",
        "codigo": tag,
        "produto": produto["nome"],
        "preco": produto["preco"],
        "validade": produto["validade"],
        "categoria": produto["categoria"],
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    salvar_registro(registro)
    print(f"Saída registrada com sucesso:\n - Produto: {produto['nome']}\n - Categoria: {produto['categoria']}\n - Preço: R${produto['preco']:.2f}")

def salvar_registro(registro):
    try:
        with open(DB_PATH, "r") as file:
            dados = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = []

    dados.append(registro)

    with open(DB_PATH, "w") as file:
        json.dump(dados, file, indent=4)
