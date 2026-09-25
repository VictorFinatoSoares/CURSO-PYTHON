# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

nums = []

while True:
    nums.append(int(input('Digite um valor: ')))

    res = input('Quer continuar (S/N)? ').upper()

    if res == 'N':
        break

pares = []
impares = []

for num in nums:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'A lista geral: {nums}\nA lista de pares: {pares}\nA lista de ímpares: {impares}')