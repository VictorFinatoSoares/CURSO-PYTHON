# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N
# primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('Quantos elementos de Fibonacci você quer ver? '))

num_ante_anterior = 0
num_anterior = 0
num_atual = 1
i = 0

print(0, end=' - ')

while i < n - 1:
    if i < n - 2:
        print(num_atual, end=' - ')
    else:
        print(num_atual, end='')

    num_ante_anterior = num_anterior
    num_anterior = num_atual
    num_atual = num_anterior + num_ante_anterior

    i += 1
