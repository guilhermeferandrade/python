import math
catop = float(input('Digite o cateto oposto do triangulo retangulo: '))
catadj = float(input('Digite o cateto adjacente do triangulo retangulo: '))
hip = math.hypot(catop, catadj)
print(f'A hipotenusa desse triangulo eh igual a {hip:.2f}')