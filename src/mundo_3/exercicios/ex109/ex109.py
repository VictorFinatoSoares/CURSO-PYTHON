# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from moeda import *

def mostrar_menu():
    print(
'''
======== MENU ========

[1] AUMENTAR
[2] DIMINUIR
[3] DOBRO
[4] METADE
[5] SAIR
''')

saldo = float(input('Digite seu saldo: '))

while True:
    mostrar_menu()
    opcao = int(input('Qual opção você deseja? '))

    if opcao == 1:
        aumento = float(input('Digite o valor do aumento: '))
        print(f'Aumento: {aumentar(saldo, aumento, formatar=True)}')
        saldo = aumentar(saldo, aumento)
    elif opcao == 2:
        reducao = float(input('Digite o valor de redução: '))
        print(f'Redução: {diminuir(saldo, reducao, formatar=True)}')
        saldo = diminuir(saldo, reducao)
    elif opcao == 3:
        print(f'Dobro: {dobro(saldo, formatar=True)}')
        saldo = dobro(saldo)
    elif opcao == 4:
        print(f'Metade: {metade(saldo, formatar=True)}')
        saldo = metade(saldo)
    elif opcao == 5:
        print('Saindo do programa...')
        break
    else:
        print('OPÇÃO INEXISTENTE!')
