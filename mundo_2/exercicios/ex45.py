# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

escolha_computador = randint(0, 2)

escolhas = ('PEDRA', 'PAPEL', 'TESOURA')

print('-=' * 16)
print('''
Vamos jogar JOKENPÔ, você deve escolher entre essas opções: 

[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
print('-=' * 16)

escolha = int(input('Qual é a sua jogada? '))

print('JO')
sleep(0.5)

print('KEN')
sleep(0.5)

print('PÔ')
sleep(0.5)

print(f'''
Computador escolheu: {escolhas[escolha_computador]}
Jogador escolheu: {escolhas[escolha]}
''')

if escolha == 0 and escolha_computador == 0 or escolha == 1 and escolha_computador == 1 or escolha == 2 and escolha_computador == 2:
    print('Resultado: EMPATE!')
elif escolha == 0 and escolha_computador == 2 or escolha == 1 and escolha_computador == 0 or escolha == 2 and escolha_computador == 1:
    print('Resultado: JOGADOR VENCE!')
else:
    print('Resultado: COMPUTADOR VENCE!')