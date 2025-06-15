class Produto:
    def __init__(self, codigo, nome, preco, validade, categoria):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.validade = validade
        self.categoria = categoria

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "preco": self.preco,
            "validade": self.validade,
            "categoria": self.categoria
        }
