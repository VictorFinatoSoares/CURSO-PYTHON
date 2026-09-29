# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media_aritmetica = (nota1 + nota2) / 2

print(f'Sua média foi {media_aritmetica}, portanto...')

if media_aritmetica >= 7:
    print('Aprovado')
elif media_aritmetica >= 5:
    print('Recuperação')
else:
    print('Reprovado')