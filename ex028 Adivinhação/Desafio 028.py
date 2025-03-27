from random import randint
from time import sleep

#Número aleatório do programa
numero_escolhido = randint (0, 5)

#Linha de customização
print ('-=-' *20)

#Usuário tenta adivinhar
pergunta = int (input('Pensarei em um número de 0 a 5, tente adivinhar...: '))

#Linha de customização
print ('-=-' * 20)

#Linha de carregamento com tempo
print ('CARREGANDO...')
sleep (2)

if pergunta == numero_escolhido:
    print ('Parabéns, você acertou!')

else:
    print ('Errou! Muito burro')

print (f'O número que eu escolhi foi {numero_escolhido}')