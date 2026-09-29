# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# Desafio 009: Escreva um programa que leia um número inteiro e mostre sua tabuada (1-10).
n = int(input('De qual número você quer ver a tabuada? ')) # Guarda o valor do número

print(f'Aqui está a tabuada do {n}:') # Mensagem tipo título

for i in range(11):
    print(f'{n} x {i} = {n * i}')
