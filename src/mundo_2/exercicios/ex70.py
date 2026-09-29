# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total_gasto = 0
quant_maiores_mil_reais = 0

primeiro_produto = True

preco_do_mais_barato = 0
nome_do_mais_barato = ''

while True:
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input('Digite o valor do produto: '))

    if primeiro_produto:
        preco_do_mais_barato = preco_produto
        nome_do_mais_barato = nome_produto
        primeiro_produto = False

    if preco_produto < preco_do_mais_barato:
        preco_do_mais_barato = preco_produto
        nome_do_mais_barato = nome_produto

    if preco_produto > 1000:
        quant_maiores_mil_reais += 1

    total_gasto += preco_produto

    res = input('Deseja continuar? [S/N] ').upper()

    if res == 'N':
        break

print(f'Total gasto na compra: R$ {total_gasto:.2f}\nProdutos que custam mais de R$ 1000,00: {quant_maiores_mil_reais}\nNome do mais barato: {nome_do_mais_barato}')
