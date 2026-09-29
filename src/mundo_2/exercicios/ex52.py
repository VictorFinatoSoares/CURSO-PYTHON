# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número INTEIRO POSITIVO: '))

quantDivisores = 0

if num > 0:
    for i in range(1, num + 1):
        if (num % i == 0):
            quantDivisores += 1

    if quantDivisores == 2:
        print(f'{num} É PRIMO!')
    else:
        print(f'{num} NÃO É PRIMO!')

else:
    print('O número precisa ser POSITIVO!')

