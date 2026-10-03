# Aula 22: Módulos e pacotes (PROGRAMA PRINCIPAL)

from utils import  numeros

num = int(input('Digite um número: '))
fat = numeros.fatorial(num)

print(f'O dobro de {num} é {numeros.dobro(num)}.')
print(f'O triplo de {num} é {numeros.triplo(num)}.')
print(f'O fatorial de {num} é {fat}.')
