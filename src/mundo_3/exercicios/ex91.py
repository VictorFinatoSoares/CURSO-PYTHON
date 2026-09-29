# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo
# que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

resultados = {}

for i in range(4):
    resultados[i] = randint(1, 6)

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)

for jogador, valor in resultados.items():
    print(f'O Jogador {jogador +  1} tirou {valor} no dado.')

print('====== RANKING ======')

for c, j in ranking:
    print(f'Jogador {c + 1}: {j}')