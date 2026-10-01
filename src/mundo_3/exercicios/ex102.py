# Exercício Python 102: Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=False):
    fatorial = 1
    print(f'{num}! = ', end='')

    for i in range(num, 0, -1):
        fatorial *= i

        if show:
            if i > 1:
                print(f'{i} x ', end='')
            else:
                print(f'{i} = ', end='')

    print(f'{fatorial}')

num = int(input('Digite um número: '))
fatorial(num, True)
