# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0

for i in range(3):
    for j in range(3):
        num = int(input('Digite um número: '))

        if num % 2 == 0:
            soma_pares += num

        if j == 2:
            soma_terceira_coluna += num

        if i == 1:
            if j == 0:
                maior_valor_segunda_linha = num
            elif num > maior_valor_segunda_linha:
                maior_valor_segunda_linha = num

        matriz[i].append(num)

for line in range(len(matriz)):
    for column in range(len(matriz[line])):
        print(f'[{matriz[line][column]:^5}]', end=' ')
    print()

print(f'Soma de todos os pares: {soma_pares}.')
print(f'Soma da terceira coluna: {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha: {maior_valor_segunda_linha}.')