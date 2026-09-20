# Aula 008: Usando módulos (bibliotecas do python)

# Teoria 1: 
from math import sqrt # Da biblioteca math (matemática), importe a função sqrt (raiz quadrada).
num = int(input('Digite um número: ')) # Número recebe o resultado de um input que será convertido em inteiro (int).
raiz = sqrt(num) # Raiz recebe o resultado da raiz quadrada de num.

print(f'A raiz quadrada de {num} é {raiz:.2f}.') # Exibe a raiz quadrada do número escolhido pelo usuário.

# Teoria 2:

import random # importa a biblioteca random
num = random.randint(1, 10) # sorteia número de 1 a 10
print(num) # exibe o número sortead

# Teoria 3:
 
import emoji # importa a biblioteca emoji

print(emoji.emojize("Olá, mundo! :earth_americas:", language= 'alias')) # exibe mensagem com emoji da terra
