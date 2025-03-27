from math import sqrt
co = float (input ('\n Digite o cateto oposto do triângulo retângulo: '))
ca = float (input ('\n Digite o cateto adjascente do triângulo retângulo: '))
h = (co**2) + (ca**2)
print (f'\n O comprimento da hipotenusa {(sqrt(h)):.2f}')