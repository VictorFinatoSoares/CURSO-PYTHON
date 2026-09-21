# Desafio 38: Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela qual dos dois é maior, ou se são iguais.

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))

if num_1 > num_2:
    print(f'{num_1} é maior que {num_2}')
elif num_1 < num_2:
    print(f'{num_2} é maior que {num_1}')
else:
    print('Ambos os números possuem o mesmo valor.')