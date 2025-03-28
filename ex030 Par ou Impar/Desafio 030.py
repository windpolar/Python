from time import sleep

#Varíavel número
num = int(input ('Digite um número qualquer: '))

print ('EM PROCESSAMENTO...')
sleep(2)

print ('AGUARDE...')
sleep(2)

#Varíavel par ou impar
par_ou_impar = (num % 2)

if par_ou_impar == 0:
    print (f'O número {num} é PAR!')

else:
    print (f'O número {num} é ÍMPAR!')