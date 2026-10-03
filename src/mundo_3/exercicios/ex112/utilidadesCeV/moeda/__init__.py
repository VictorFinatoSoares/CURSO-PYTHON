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

def resumo(valor, formatar=False):
    print('======== RESUMO ========')

    print(f'Aumentando R$ 100: {aumentar(valor, 100, formatar=formatar)}')
    print(f'Diminuindo R$ 100: {diminuir(valor, 100, formatar=formatar)}')
    print(f'O dobro: {dobro(valor, formatar=formatar)}')
    print(f'A metade: {metade(valor, formatar=formatar)}')
