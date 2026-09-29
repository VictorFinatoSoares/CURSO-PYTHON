# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

quant_numeros = 0
soma = 0

while True:
    num = int(input('Digite um número: '))

    if num == 999:
        break

    quant_numeros += 1
    soma += num

print(f'Foram digitados {quant_numeros} números, a soma total foi: {soma}.')