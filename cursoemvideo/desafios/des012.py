nome = input('Digite o nome do produto: ')
val = float(input('Digite o valor do produto: '))
print(f'O produto {nome} com desconto de 5% no valor dele ficara com o preco de R${val - val * 5 / 100:.2f}')