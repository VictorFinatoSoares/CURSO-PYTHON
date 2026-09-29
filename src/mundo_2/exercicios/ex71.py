# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues. OBS
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor_sacado = int(input('Quanto você irá sacar? '))
valor_necessario = valor_sacado

quant_notas_cinquenta = valor_necessario // 50
valor_necessario = valor_necessario % 50

quant_notas_vinte = valor_necessario // 20
valor_necessario = valor_necessario % 20

quant_notas_dez = valor_necessario // 10
valor_necessario = valor_necessario % 10

quant_notas_um = valor_necessario // 1
valor_necessario = valor_necessario % 1

print('SAQUE REALIZADO:')
print(f'Notas de R$ 50: {quant_notas_cinquenta}\nNotas de R$ 20: {quant_notas_vinte}\nNotas de R$ 10: {quant_notas_dez}\nNotas de R$ 1: {quant_notas_um}')