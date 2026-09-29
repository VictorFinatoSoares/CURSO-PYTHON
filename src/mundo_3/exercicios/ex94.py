# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = []

soma_idade = 0

while True:
    pessoa = {'nome': str(input('Nome: ')), 'sexo': str(input('Sexo: ')), 'idade': int(input('Idade: '))}

    soma_idade += pessoa['idade']

    pessoas.append(pessoa)

    if str(input('Quer continuar (S/N)? ')).upper() == 'N':
        break

print(f'{len(pessoas)} pessoas cadastradas.\nA média de idade foi {soma_idade / len(pessoas):.2f} anos.')

print('Mulheres cadastradas:')

for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'])

print('Pessoas com idade acima da média:')

for pessoa in pessoas:
    if pessoa['idade'] > soma_idade / len(pessoas):
        print(f'{pessoa['nome']} ({pessoa['idade']})')



