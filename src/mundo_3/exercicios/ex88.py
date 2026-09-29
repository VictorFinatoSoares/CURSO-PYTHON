# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint

quant_jogos = int(input('Quantos jogos você quer sortear? '))
jogos = []

for i in range(quant_jogos):
    sorteados = []
    for j in range(6):
        sorteados.append(randint(1, 60))
    jogos.append(sorteados)

for pos, jogo in enumerate(jogos):
    print(f'[JOGO {pos + 1}]: {jogo}')