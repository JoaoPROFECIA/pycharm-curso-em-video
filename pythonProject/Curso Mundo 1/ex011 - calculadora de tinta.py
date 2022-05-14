print('CALCULADORA DE TINTA\n')
Largura = float(input('Largura da parede (metros): '))
Altura = float(input('Altura da parede (metros): '))
Área = Largura * Altura
tinta = Área / 2
print(f'Sua parede tem a dimensão de {Largura}m por {Altura}m e sua área é de {Área :.2f}m². \n'
      f'Para pintar a parede você precisará de {tinta :.2f}L de tinta.')
