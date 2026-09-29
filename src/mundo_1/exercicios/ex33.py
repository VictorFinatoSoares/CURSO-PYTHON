# Desafio 033: faça um programa que leia três números e diga qual o maior e menor.

n1 = int(input('Escreva o primeiro número: ')) # Guarda o primeiro
n2 = int(input('Escreva o segundo número: ')) # Guarda o segundo
n3 = int(input('Escreva o terceiro número: ')) # Guarda o terceiro

maior = max(n1,n2,n3) # Vê qual desses é o maior
menor = min(n1,n2,n3)  # Vê qual desses é o menor

print(f'O menor número é o {menor} e o maior número é o {maior}!') # Informa o usuário
