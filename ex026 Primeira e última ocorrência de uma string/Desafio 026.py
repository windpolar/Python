#Pede para digitar uma frase
frase = str(input ('Digite uma frase: ')).upper().strip()

print (f'A letra A aparece {frase.count('A')}')

print (f'A primeira letra A apareceu na {frase.find('A')+1} posição')

print (f'A última letra A apareceu na {frase.rfind('A')+1}')