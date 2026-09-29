# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.  Depois vai ler a quantidade
# de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Partidas: '))

total_gols = 0

for partida in range(jogador['partidas']):
    gols = int(input(f'Quantidade de gols feitos na partida {partida + 1}: '))

    jogador[f'gols_partida_{partida + 1}'] = gols
    total_gols += gols

jogador['total_gols'] = total_gols

print(jogador)