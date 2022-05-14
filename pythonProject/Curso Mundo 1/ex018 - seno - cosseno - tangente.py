print('SENO - COSSENO - TANGENTE')
#import math
#ângulo = float(input('Digite um número: '))
#print(f'O ângulo de {ângulo} tem: \n'
#      f'o seno de {math.sin(math.radians(ângulo)):.2f}\n'
#      f'cosseno de {math.cos(math.radians(ângulo)):.2f}\n'
#      f'tangente de {math.tan(math.radians(ângulo)):.2f}')

from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {angulo} tem: \n'
      f'seno de {sin(radians(angulo)):.2f}\n'
      f'cosseno de {cos(radians(angulo)):.2f}\n'
      f'tangente de {tan(radians(angulo)):.2f}')
