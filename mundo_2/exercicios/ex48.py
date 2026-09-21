# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que
# são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma_total = 0

for i in range(1, 501):
    if i % 3 == 0:
        soma_total += i

print(f'A soma total dentre todos os números de 1 a 500 e que são múltiplos de 3 é: {soma_total}.')