# Desafio 019: Crie um programa que leia o nome de 4 alunos, e sorteie um deles para apagar o quadro para o professor

from random import choice # Importa tudo da biblioteca random

# Pergunta o nome dos 4 alunos que serão sorteados
aluno_1 = input('Qual o nome do primeiro aluno? ')
aluno_2 = input('Qual o nome do segundo aluno? ')
aluno_3 = input('Qual o nome do terceiro aluno? ')
aluno_4 = input('Qual o nome do quarto aluno? ')

lista = [aluno_1, aluno_2, aluno_3, aluno_4] # Cria uma lista com todos os alunos que serão sorteados.

escolhido = choice(lista) # Escolherá e guardará o aluno escolhido
 
print(f'O aluno escolhido para apagar o quadro foi: {escolhido}!') # Mostra o resultado do sorteio.
