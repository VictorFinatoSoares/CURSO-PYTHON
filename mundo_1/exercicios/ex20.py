# Desafio 020: Escreva um codigo que sorteará a ordem da apresentação de 4 alunos do mesmo professor.

from random import shuffle # Importa a função shuffle da biblioteca random.

# Escolhendo os alunos para sortear
aluno_1 = input('Qual o nome do primeiro aluno? ')
aluno_2 = input('Qual o nome do segundo aluno? ')
aluno_3 = input('Qual o nome do terceiro aluno? ')
aluno_4 = input('Qual o nome do quarto aluno? ')

# Cria uma lista com todos os aunos
lista = [aluno_1, aluno_2, aluno_3, aluno_4]

# Embaralha a ordem dos alunos dentro da lista
shuffle(lista)

# Mostra a lista
print('Aqui está a ordem das apresentações:')
print(lista)