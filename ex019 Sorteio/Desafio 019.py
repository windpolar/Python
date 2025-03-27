from random import choice
m1 = input ('Digite o primeiro músculo: ')
m2 = input ('Digite o segundo músculo: ')
m3 = input ('Digite o terceiro músculo: ')
m4 = input ('Digite o quarto músculo: ')
lista = [m1, m2, m3, m4]
escolhido = choice (lista)
print (f'O músculo escolhido foi {escolhido}')