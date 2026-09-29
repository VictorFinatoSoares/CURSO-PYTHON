# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

quant_numeros = 0
soma_numeros = 0
n = 0

while n != 999:
    n = int(input('Digite um número inteiro (999 para parar): '))

    if n != 999:
        quant_numeros += 1
        soma_numeros += n

print(f'{quant_numeros} foram digitados, soma total: {soma_numeros}.')
