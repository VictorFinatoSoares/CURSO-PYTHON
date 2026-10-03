# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

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
    print(f'Saldo: {saldo}')

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
