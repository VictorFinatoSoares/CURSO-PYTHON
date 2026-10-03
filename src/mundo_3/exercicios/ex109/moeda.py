def aumentar(valor, aumento, formatar=False):
    resultado = valor + aumento
    return moeda(resultado) if formatar else resultado


def diminuir(valor, reducao, formatar=False):
    resultado = valor - reducao
    return moeda(resultado) if formatar else resultado


def dobro(valor, formatar=False):
    resultado = valor * 2
    return moeda(resultado) if formatar else resultado


def metade(valor, formatar=False):
    resultado = valor / 2
    return moeda(resultado) if formatar else resultado


def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')