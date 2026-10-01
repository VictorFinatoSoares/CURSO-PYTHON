# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’,
# o programa se encerrará. Importante: use cores.

# Respectivamente: SEM COR, VERMELHO, VERDE, AMARELO, AZUL, ROXO E BRANCO.
cores = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7;30m')

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 3)
    print(cores[6], end='')
    help(com)
    print(cores[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4

    print(cores[cor], end='')
    print('=' * tam)
    print(msg.center(tam))
    print('=' * tam)
    print(cores[0], end = '')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 4)

    comando = str(input('Função ou Biblioteca > '))

    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break
    else:
        ajuda(comando)