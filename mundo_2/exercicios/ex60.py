# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número: '))

print(f'{num}! = ', end='')
fatorial = 1

for i in range(num, 0, -1):
    if i > 1: print(f'{i} x', end=' ')
    else: print(f'{i}', end=' ')
    fatorial *= i

print(f'= {fatorial}')