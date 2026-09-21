# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a
# soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma_pares = 0

for i in range(6):
    n = int(input('Informe um número: '))

    if n % 2 == 0:
        soma_pares += n

print(f'A soma de todos os números pares que você informou é: {soma_pares}')