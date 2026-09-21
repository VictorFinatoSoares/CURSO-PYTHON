# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano_nascimento = int(input("Informe o ano do seu nascimento: "))

idade = 2026 - ano_nascimento

if idade < 18:
    print(f'Você ainda irá se alistar! Faltam apenas {18 - idade} anos.')
elif idade == 18:
    print('Já é a hora exata de se alistar!')
else:
    print(f'Já passou da hora de se alistar! Passaram {idade - 18} anos do prazo.')