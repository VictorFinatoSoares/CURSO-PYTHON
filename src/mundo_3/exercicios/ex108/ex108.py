# Exercício Python 108: Adapte o código do desafio
# 107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

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
    print(f'Saldo: {moeda(saldo)}')

    mostrar_menu()
    opcao = int(input('Qual opção você deseja? '))

    if opcao == 1:
        aumento = float(input('Digite o valor do aumento: '))
        saldo = aumentar(saldo, aumento)
    elif opcao == 2:
        reducao = float(input('Digite o valor de redução: '))
        saldo = diminuir(saldo, reducao)
    elif opcao == 3:
        saldo = dobro(saldo)
    elif opcao == 4:
        saldo = metade(saldo)
    elif opcao == 5:
        print('Saindo do programa...')
        break
    else:
        print('OPÇÃO INEXISTENTE!')
