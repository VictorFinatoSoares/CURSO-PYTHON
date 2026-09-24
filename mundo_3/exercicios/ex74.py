# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

# Gera 5 números de 1 a 10 aleatoriamente e guarda na tupla
nums = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

menor = nums[0]
maior = nums[0]

for num in nums:
    if num >= maior:
        maior = num

    if num <= menor:
        menor = num

    print(num)

print(f'O menor elemento é {menor} e o maior elemento é {maior}.')
