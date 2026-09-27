# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        matriz[i].append(int(input('Digite um número: ')))

for line in range(len(matriz)):
    for column in range(len(matriz[line])):
        print(f'[{matriz[line][column]:^5}]', end=' ')
    print()