import json

ESTOQUE_PATH = "data/estoque.json"

def carregar_estoque():
    try:
        with open(ESTOQUE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def atualizar_estoque(codigo, delta):
    estoque = carregar_estoque()
    codigo_str = str(codigo)
    estoque[codigo_str] = estoque.get(codigo_str, 0) + delta

    with open(ESTOQUE_PATH, "w") as file:
        json.dump(estoque, file, indent=4)
