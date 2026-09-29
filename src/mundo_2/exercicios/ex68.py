# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint

print('''
============================================
PAR OU ÍMPAR, O COMPUTADOR IRÁ JOGAR DE 0
A 10 , VOCÊ DEVE ESCOLHER SE QUER PAR
OU ÍMPAR E DEFINIR O NÚMERO QUE JOGARÁ
O JOGO ACABA QUANDO VOCÊ PERDE, E EXIBE
A QUANTIDADE DE VITÓRIAS CONSECUTIVAS
===========================================
''')

quant_vitorias_consecutivas = 0

while True:
    num_computador = randint(0, 5)
    opcao = input('Digite a opção que quer (PAR/IMPAR): ').upper()
    num = int(input('Digite o valor: '))

    total = num + num_computador

    print(f'O computador escolheu: {num_computador}')

    if opcao == 'PAR' and total % 2 == 0 or opcao == 'IMPAR' and total % 2 != 0:
        print('Você VENCEU!')
        quant_vitorias_consecutivas += 1
    else:
        print('Você PERDEU!')
        break

print(f'Vitórias consecutivas: {quant_vitorias_consecutivas}')