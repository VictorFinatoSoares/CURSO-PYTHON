# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’)

# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(txt):
    tamanho_linha = len(txt) + 5
    print('=' * tamanho_linha)
    print(txt.center(tamanho_linha))
    print('=' * tamanho_linha)

escreva('Olá, Mundo!')
