from math import radians,sin,cos,tan
an = float (input ('Digite o ângulo desejado: '))
seno = sin (radians (an))
print (f'O SENO de {an} é igual a: {seno:.2f}')
cosseno = cos (radians (an))
print (f'O COSSENO de {an} é igual a: {cosseno:.2f}')
tangente = tan (radians (an))
print (f'A TANGENTE de {an} é igual a: {tangente:.2f}')