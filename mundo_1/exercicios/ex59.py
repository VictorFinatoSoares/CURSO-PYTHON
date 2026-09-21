# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 0

while opcao != 5:
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))

    print('''
    ====== MENU DE OPÇÕES ======
    
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] DIGITAR NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')

    opcao = int(input('Escolha (1-5): '))

    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}.')
    elif opcao == 3:
        print(f'O maior número entre {n1} e {n2} é {max(n1, n2)}')
    elif opcao == 4:
        print('NOVA ENTRADA:')
    elif opcao == 5:
        print('Encerrando...')
    else:
        print('Essa opção não existe!')