# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

num = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

i = 0

while i < 10:
    print(f'{num}', end=' -> ')
    num += razao

    i += 1

print('FIM')