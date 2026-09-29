# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5
# números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista):
    for i in range(5):
        lista.append(randint(1, 10))

def soma_pares(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]

    print(f'Valores da lista: {lista}\nA soma dos pares: {soma}')

numeros = []

sorteia(numeros)
soma_pares(numeros)
