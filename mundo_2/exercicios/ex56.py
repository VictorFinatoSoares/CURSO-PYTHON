# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

nome_homem_mais_velho = '[VAZIO, NÃO HÁ UM HOMEM NESSE GRUPO]'
idade_homem_mais_velho = 0
soma_idade = 0
quant_mulher_menos_20_anos = 0

for i in range(4):
    nome = input('Digite o seu nome: ')
    sexo = input('Digite o seu sexo [M/F]: ').upper()
    idade = int(input('Digite sua idade: '))

    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    elif sexo == 'F' and idade < 20:
        quant_mulher_menos_20_anos += 1

    soma_idade += idade

print(f'A média de idade do grupo é de {soma_idade / 4:.2f} anos\nO nome do homem mais velho é {nome_homem_mais_velho}\nQuantidade de mulheres com pelo menos 20 anos ou mais: {quant_mulher_menos_20_anos}')
