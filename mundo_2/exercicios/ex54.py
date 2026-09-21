# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

quant_maior_idade = 0

for i in range(7):
    ano_nascimento = int(input('Informe o ano de nascimento da pessoa: '))
    idade = 2026 - ano_nascimento

    if idade >= 18:
        quant_maior_idade += 1

print(f'Com base nos anos de nascimento das sete pessoas informadas, {quant_maior_idade} são de maior e {7 - quant_maior_idade} não são.')