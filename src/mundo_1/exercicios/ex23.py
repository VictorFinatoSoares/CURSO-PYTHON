# Desafio 023: Faça um programa que separe um número de 0 a 9999 e responda com cada casa, ex: 1234 milhar = 1, centena = 2, dezena = 3 e unidade = 4

num = input('Escreva um número de 0 a 9999: ') # Guardará o número de 0 a 9999 em string.
s = '000' + num  # "s" serve para que se digitar um número menor de 4 algarismos como o 1, adiciona três 000 na frente, ficando 0001, e aí o programa irá exibir todas as casas corretamente.

print(f'Número escolhido: {num}.') # Mostra o número
print(f'Milhar: {s[-4]}') # Milhar
print(f'Centena: {s[-3]}') # Centena
print(f'Dezena: {s[-2]}') # Dezena
print(f'Unidade: {s[-1]}') # Unidade
