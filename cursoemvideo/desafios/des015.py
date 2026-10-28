dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dia * 60) + (km * 0.15)
print(f'Valor a pagar: R${pago:.2f}')