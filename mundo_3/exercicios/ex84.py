# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
pesadas = []
leves = []

mais_leve = mais_pesado = 0

while True:
    info = [str(input('Nome: ')), float(input('Peso: '))]

    if len(pessoas) == 0:
        mais_leve = info[1]
        mais_pesado = info[1]
    else:
        if info[1] > mais_pesado:
            mais_pesado = info[1]
        if info[1] < mais_leve:
            mais_leve = info[1]

    pessoas.append(info)

    res = str(input('Deseja continuar (S/N)? ')).strip().upper()

    if res == 'N':
        break


for i in range(len(pessoas)):
    if pessoas[i][1] >= mais_pesado:
        pesadas.append(pessoas[i][0])

    if pessoas[i][1] <= mais_leve:
        leves.append(pessoas[i][0])

print(f'{len(pessoas)} pessoas foram cadastradas.')
print(f'O maior peso foi {mais_pesado:.2f} KG, obtido por: {pesadas}')
print(f'O menor peso foi {mais_leve:.2f} KG, obtido por: {leves}')