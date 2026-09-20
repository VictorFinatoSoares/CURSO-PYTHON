# Desafio 017: Crie um programa que leia o comprimento de dois catetos e exiba o comprimento da hipotenusa

from math import hypot # Importa só a função hypot

co = float(input('Digite o comprimento do cateto adjacente: ')) # Armazena o primeiro cateto
ca = float(input('Digite o comprimento do cateto oposto: ')) # Armazena o segundo cateto

# hip = math.sqrt(co ** 2 + ca ** 2) # Usando o teorema de pitágoras
hip = hypot(ca,co) # Usando o teorema de pitágoras de um jeito mais simples.
print(f'Um triângulo retângulo cujo o cateto adjacente vale {co} e o cateto oposto vale {ca} tem {hip:.2f} como hipotenusa.') # Exibe o resultado