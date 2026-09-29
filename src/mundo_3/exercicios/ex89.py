# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []

while True:
    aluno = []
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))

    boletim.append(aluno)

    res = str(input('Quer continuar (S/N): ')).upper().strip()

    if res == 'N':
        break

for pos, aluno in enumerate(boletim):
    media = (aluno[1] + aluno[2]) / 2
    print(f'[POS]: {pos}\nNome: {aluno[0]}\nMédia: {media:.2f}\n')

while True:
    aluno = int(input('Qual aluno você quer verificar? '))

    print(f'Aluno: {boletim[aluno][0]}\nNotas: {boletim[aluno][1]}, {boletim[aluno][2]}\n')

    res = str(input('Quer continuar (S/N): ')).upper().strip()

    if res == 'N':
        break