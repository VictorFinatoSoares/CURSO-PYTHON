# Desafio 028: Faça um programa que faça o computador pensar em um número de 0 a 5, e que o usuario precisa acertar, se ele acertar exiba um mensagem, ou se ele perder 

from random import randint # Importa a função randint da biblioteca random
from time import sleep # Importa a função sleep da biblioteca time

num = randint(0,5)  # Usa o randint pra escolher um número aleatório entre 0 a 5 e armazena numa variavel

num_escolhido = int(input('Eu pensei em um número de 0 a 5, tente adivinhar qual é! ')) # Irá guardar o número escolhido pelo usuário

print('PROCESSANDO...') # "Processa"

sleep(3) # Intervalo de 3 segundos

if num_escolhido >5 or num_escolhido <0: # Testa pra ver se o usuario digitou algo fora de 0 a 5
    print('Você escolheu um número fora do limite! Encerrando...') # Mensagem Encerrando..

else: # Se tá dentro do limite
    if num_escolhido == num: # Verifica se acertou
        print(f'Você acertou! O número que pensei era: {num}!') # Avisa que acertou

    else: # Se errou 
        print(f'Você errou! O número que eu pensei era: {num}!') # Avisa que errou
        