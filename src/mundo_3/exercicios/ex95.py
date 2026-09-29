# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = []

while True:
    jogador = {}

    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input('Partidas: '))

    jogador['gols'] = []

    for partida in range(jogador['partidas']):
        gols = int(input(f'Quantidade de gols feitos na partida {partida + 1}: '))
        jogador['gols'].append(gols)

    jogador['total_gols'] = sum(jogador['gols'])
    time.append(jogador)

    res = input('Quer continuar cadastrando? [S/N] ').strip().upper()

    if res == 'N':
        break

print('\n' + '=' * 55)
print(f'{"ÍNDICE":<8}{"NOME":<25}{"PARTIDAS":<12}{"TOTAL DE GOLS":>12}')
print('-' * 55)

for indice, jogador in enumerate(time):
    print(
        f'{indice:<8}{jogador["nome"]:<25}'
        f'{jogador["partidas"]:<12}{jogador["total_gols"]:>12}'
    )

print('=' * 55)

while True:
    indice = int(input('\nMostrar dados de qual jogador? (999 interrompe): '))

    if indice == 999:
        break

    jogador = time[indice]

    print(f'\nNome: {jogador["nome"]}')
    print(f'Partidas: {jogador["partidas"]}')
    print(f'Total de gols: {jogador["total_gols"]}')
    print('Gols por partida:')

    for partida, gols in enumerate(jogador['gols'], start=1):
        print(f'  Partida {partida}: {gols} gol(s)')