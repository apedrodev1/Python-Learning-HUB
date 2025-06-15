
import json


def carregar_json(caminho):
    try:
        with open(caminho, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def salvar_json(caminho, dados):
    with open(caminho, "w") as file:
        json.dump(dados, file, indent=4)
