# Desafio 016: Crie um programa que leia um número flutuante pelo usuário e mostre a parte inteira dele (ex: 6.317 -> 6)

# Código usando módulos

from math import trunc # Importa a função trunc da biblioteca math (matemática)

num = float(input('Escreva um número decimal: ')) # Guarda o número decimal que o usuário digitar.
num_int = trunc(num) # Irá retirar a parte decimal do número digitado, deixando apenas a parte inteira.

print(f'A parte inteira do número {num} é {num_int}.') # Exibe ambos os valores.

# Código sem usar módulos

# num = float(input('Escreva um número decimal: ')) # Guarda o número decimal que o usuário digitar
# num_int = int(num) # Irá retirar a parte decimal do número digitando deixando apenas a parte inteira.
# print(f'A parte inteira do número {num} é {num_int}.') # Exibe ambos os valores
