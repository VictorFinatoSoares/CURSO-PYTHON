# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import datetime

def voto(ano_nasc):
    idade = datetime.now().year - ano_nasc

    if idade < 16:
        return "NEGADO"
    elif idade < 18:
        return "OPCIONAL"
    elif idade <= 69:
        return "OBRIGATÓRIO"
    else:
        return "OPCIONAL"

ano_nasc = int(input('Informe o ano de seu nascimento: '))
print(f'Você possui {datetime.now().year - ano_nasc} anos, portanto seu voto é {voto(ano_nasc)}.')
