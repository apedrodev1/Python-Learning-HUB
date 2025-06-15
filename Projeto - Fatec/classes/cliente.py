class Cliente:
    def __init__(self, id_cliente, nome, email):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email
        self.compras = []  # Lista de produtos comprados

    def adicionar_compra(self, produto):
        self.compras.append(produto)

    def total_gasto(self):
        return sum(produto.preco for produto in self.compras)

    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nome": self.nome,
            "email": self.email,
            "compras": [p.to_dict() for p in self.compras],
            "total_gasto": self.total_gasto()
        }
