largura = float (input ('Digite a largura da parede: '))
altura = float (input ('Digite a altura da parede: '))
área = largura*altura
print (f'A dimensão da sua parede é de {largura}x{altura}, portanto sua área é de exatamente {área:.3f}m²')
litros = área / 2
print (f'Para pintar sua parede você precisa de {litros:.2f}L de tinta')