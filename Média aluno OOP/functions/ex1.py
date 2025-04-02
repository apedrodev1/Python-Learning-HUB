produtos = {}

print('Leitura de dados: ')

cod = input('Digite o codigo do produto: ').strp()
price = float(input(f'Digite o preco do produto {cod}: R$ '))
produto = {'Codigo': cod, 'Valor': price}
produtos = produto
