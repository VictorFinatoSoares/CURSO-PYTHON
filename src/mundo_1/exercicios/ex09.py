# Desafio 009: Escreva um programa que leia um número inteiro e mostre sua tabuada (1-10).
n = int(input('De qual número você quer ver a tabuada? ')) # Guarda o valor do número 

print(f'Aqui está a tabuada do {n}!') # Mensagem tipo título

print('=' * 30) # Exibe 30 sinais de igual para montar uma tabela mais bonita.
print(f'{n} x {1:2} = {n*1}.') # Exibe a tabuada multiplicando do 1 ao 10 o número escolhido.
print(f'{n} x {2:2} = {n*2}.') # --
print(f'{n} x {3:2} = {n*3}.') # --
print(f'{n} x {4:2} = {n*4}.') # --
print(f'{n} x {5:2} = {n*5}.') # --
print(f'{n} x {6:2} = {n*6}.') # --
print(f'{n} x {7:2} = {n*7}.') # --
print(f'{n} x {8:2} = {n*8}.') # --
print(f'{n} x {9:2} = {n*9}.') # --
print(f'{n} x {10:2} = {n*10}.') # --
print('=' * 30) # Exibe 30 sinais de igual para montar uma tabela mais bonita
