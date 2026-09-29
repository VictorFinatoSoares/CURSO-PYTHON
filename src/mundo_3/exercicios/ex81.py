# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

nums = []

while True:
    nums.append(int(input('Digite um valor: ')))

    res = input('Quer continuar (S/N)? ').upper()

    if res == 'N':
        break

print(f'Foram digitados {len(nums)} ao todo.')
print(f'Os valores em ordem decrescente: {sorted(nums, reverse=True)}')

if 5 in nums:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')