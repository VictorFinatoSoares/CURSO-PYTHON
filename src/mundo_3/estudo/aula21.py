# Aula 21: Funções (parte 2)

def fatorial(num=1):
    fatorial = 1

    for i in range(num, 0, -1):
        fatorial *= i

    return fatorial

def par(num):
    return num % 2 == 0

num = int(input('Informe um número: '))

print(f'O fatorial de {num} é {fatorial(num)}.')
print(f'O número {num} é PAR.' if par(num) else f'O número {num} é ÍMPAR.')
