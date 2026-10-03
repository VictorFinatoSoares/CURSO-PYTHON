def leiaDinheiro(msg):
    while True:
        valor = str(input(msg)).replace(',', '.').strip()

        if valor.isalpha() or valor.isalnum() or valor == '':
            print(f'ERRO: {valor} é um preço inválido!')
            continue

        return float(valor)
