# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Informe um número: '))

    if num < 0:
        break

    print(f'====== Tabuada do {num} ======')

    for i in range(11):
        print(f'{num} x {i} = {num * i}')

print('FIM')