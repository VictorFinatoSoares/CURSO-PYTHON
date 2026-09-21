# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

# Desafio 028: Faça um programa que faça o computador pensar em um número de 0 a 5, e que o usuario precisa acertar,
# se ele acertar exiba um mensagem, ou se ele perder

from random import randint  # Importa a função randint da biblioteca random

num = randint(0, 10)  # Usa o randint pra escolher um número aleatório entre 0 a 10 e armazena numa variavel

print('-=' * 40)
print('Jogo de ADIVINHAÇÃO: Eu pensei em um número entre 0 e 10, tente adivinhar qual é!')
print('=-' * 40)

quant_palpites = 0
acertou = False

while not acertou:
    num_escolhido = int(input('Seu palpite: '))  # Irá guardar o número escolhido pelo usuário

    if num_escolhido > num:
        print('Desculpe, o número é menor que esse, tente novamente.')
    elif num_escolhido < num:
        print('Desculpe, o número é maior que esse, tente novamente.')
    else:
        acertou = True

    quant_palpites += 1

print(f'Você acertou em {quant_palpites} palpites! O número que pensei era: {num}.')  # Avisa que acertou
