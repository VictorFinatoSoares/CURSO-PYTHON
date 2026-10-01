# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente.

def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'

    if gols.isnumeric(): # Verifica se a entrada recebida é um número (se não é vazia nem outro tipo)
        gols = int(gols)
    else:
        gols = 0

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome_jogador = str(input('Digite o nome do jogador: '))
gols = str(input('Digite a quantidade de gols: '))

ficha(nome_jogador, gols)
