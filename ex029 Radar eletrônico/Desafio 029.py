from time import sleep

#Customização
print ('-=-' * 20)

#Variável velocidade
velocidade_carro = float (input ('Qual é a velocidade atual do carro em km/h?: '))

#Customização
print ('-=-' * 20)

#Processamento com tempo
print ('PROCESSANDO...')
sleep (2)

if velocidade_carro <= 80:
    print ('Sua velocidade está dentro dos limites estabelecidos pela nossa norma de segurança, continue assim!')

else:
    print (f'Você excedeu o limite de velocidade e foi multado em R${((velocidade_carro - 80) * 7):.2f}')