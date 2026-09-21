# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

menor = 0
maior = 0

for i in range(5):
    peso = float(input(f'Digite o seu peso (KG) [{i + 1}]: '))

    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        else:
            menor = peso


print(f'O menor peso registrado foi {menor}KG e o maior foi {maior}KG')