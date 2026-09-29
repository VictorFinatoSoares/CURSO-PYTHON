# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior.

def maior(*nums):
    print(f'Entre os valores analisados, o maior é: {max(nums)}')

maior(21, 9, 4, 5, 7, 1)