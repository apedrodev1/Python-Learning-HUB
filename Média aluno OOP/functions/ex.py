class Product:
    def __init__(self, id_product, price, sell_price):
        self.id_product = id_product
        self.price = price
        self.sell_price = sell_price

    def profit (self):
        gross_margin = ((self.sell_price / self.price) - 1)* 100
        return print(gross_margin)



products = []

while True:
    print ('\nDigite os dados do produto (ou insira 0 em qualquer campo para encerrar)')
    id_product = int(input('Digite o codigo do produto'))
    if id_product == 0:
        print('Encerrando programa...')
        break

    price = float(input('Digite o preco de compra'))
    if price == 0:
        print('Encerrando programa...')
        break

    sell_price = float(input('Digite o preco de venda'))
    if sell_price == 0:
        print('Encerrando programa...')
        break


    product = Product(id_product, price, sell_price)
    product.append(products) 

    print ('\nProdutos cadastrados e margem bruta:')
    for product in products:
         print(
        f"Produto ID: {product.id_product}, "
        f"Preço de Compra: R${product.price:.2f}, "
        f"Preço de Venda: R${product.sell_price:.2f}, "
        f"Margem Bruta: {product.profit():.2f}%"
    )


