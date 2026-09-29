# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número: '))

print('''
OPÇÕES DE CONVERSÃO:
    
[1] - BINÁRIO
[2] - OCTAL
[3] - HEXADECIMAL
''')

opcao = int(input("Escolha: "))

# O Python já possui métodos PRÓPRIOS para tais conversões, o que faz sentido pois seria uma lógica complexa demais para o Guanabara implementar no nível atual
# do curso, fico indignado...

if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Essa opção de conversão não existe!')

