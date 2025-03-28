from time import sleep

#Variável distancia
distancia = float(input ('Digite a distância da sua viagem: '))

print (f'Você está prestes a começar uma viagem de {distancia}km')

#Carregamento
print ('CALCULANDO PREÇO...')
sleep(1)


if distancia <= 200:
    preço = distancia * 0.50
    print (f'O total da sua passagem será de: R${preço}')

else:
    preço = distancia * 0.45
    print (f'O preço da sua passagem será de: R${preço}')