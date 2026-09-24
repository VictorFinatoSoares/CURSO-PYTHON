# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ("Pizza", 29.50, "Coca-Cola", 9.50, "Lasanha Congelada", 12.37, "Chinelos Havainas", 44.90)

print('-=' * 30)
print('LISTAGEM DE PREÇOS:'.center(60))
print('=-' * 30)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' ')
    else:
        print(f'R$ {produtos[pos]:.2f}')

