n = (input ('Digite algo: '))
print ('Segue abaixo as informações: ')
print ('O tipo primitivo desse valor é',(type (n)))
print ('É numérico?: ', (n.isnumeric()))
print ('É alfabético?: ', (n.isalpha()))
print ('É alfanumérico?: ', (n.isalnum()))
print ('É maiúsculo?: ', (n.isupper()))
print ('É minúsculo?: ', (n.islower()))
print ('Está capitalizado?: ', (n.istitle()))
print ('Tem espaços?: ', (n.isspace()))