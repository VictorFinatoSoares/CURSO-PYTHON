# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

quant_numeros = 0
soma_numeros = 0

res = 'S'

menor = 0
maior = 0

primeiro_numero = True

while res != 'N':
    n = int(input('Digite um número inteiro: '))

    if primeiro_numero:
        menor = n
        maior = n
        primeiro_numero = False

    if n < menor:
        menor = n
    else:
        maior = n

    quant_numeros += 1
    soma_numeros += n

    res = input('Quer continuar? [S/N] ').upper()

print(f'Média aritmética dos valores digitados foi: {soma_numeros / quant_numeros:.2f}.')
print(f'O menor valor foi {menor} e o maior foi {maior}.')