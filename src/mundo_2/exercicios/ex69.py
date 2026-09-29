# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

quant_maior_idade = 0
quant_homens = 0
quant_mulheres_menos_20_anos = 0

while True:
    idade = int(input('Diga sua idade: '))
    sexo = input('Diga seu sexo (M/F): ').upper()

    if idade >= 18:
        quant_maior_idade += 1
    if sexo == 'M':
        quant_homens += 1
    if sexo == 'F' and idade < 20:
        quant_mulheres_menos_20_anos += 1

    res = input('Quer continuar? [S/N] ').upper()

    if res == 'N':
        break

print(f'Pessoas maior de idade: {quant_maior_idade}\nHomens registrados: {quant_homens}\nMulheres com menos de 20 anos: {quant_mulheres_menos_20_anos}')