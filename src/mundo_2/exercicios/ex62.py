# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

num = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

i = 0
termos_totais = 10
termos_extras = 0

while i < termos_totais:
    if i < termos_totais - 1: print(f'{num}', end=' -> ')
    else: print(f'{num}', end='')

    num += razao

    i += 1

    if i == termos_totais:
        termos_extras = int(input('\nQuantos termos extras você quer ver? '))
        termos_totais += termos_extras

print('FIM')