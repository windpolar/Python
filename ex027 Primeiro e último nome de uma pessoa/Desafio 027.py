#Perguntando o nome completo
nome = str (input ('Digite o seu nome completo: ')).strip()

print ('Prazer em te conhecer! Seja bem-vindo ao meu programa')

#Variável pra split
n = nome.split()

print (f'O seu primeiro nome é {n[0]} \n E seu último nome é {n[-1]}')