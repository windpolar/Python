from random import shuffle
p1 = input ('Primeiro músculo: ')
p2 = input ('Segundo músculo: ')
p3 = input ('Terceiro músculo: ')
p4 = input ('Quarto músculo: ')
lista = [p1, p2, p3, p4]
escolhido = shuffle (lista)
print (f'A ordem de músculos para treinar será: ')
print (lista)