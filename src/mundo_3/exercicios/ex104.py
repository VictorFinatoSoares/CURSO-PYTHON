# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    while True:
        entrada = str(input(msg))

        if entrada.isnumeric():
            return int(entrada)
        else:
            print('A entrada precisa ser um número inteiro!')

print(f'Número informado: {leiaInt('Digite um número: ')}')