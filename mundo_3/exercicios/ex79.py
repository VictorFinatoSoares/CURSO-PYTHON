# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

nums = []

while True:
    numero = int(input('Digite um valor: '))

    if numero not in nums:
        nums.append(numero)
    else:
        print(f'O valor que você digitou ({numero}) já estava na lista e NÃO foi adicionado!')

    res = input('Deseja continuar (S/N)? ')

    if res.upper() == 'N':
        break

print(f'Lista em ordem crescente: {sorted(nums)}')
