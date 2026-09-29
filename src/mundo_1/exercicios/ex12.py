# Desafio 012: Faça um programa que leia o preço de um produto e mostre o seu preço com desconto de 5%

preco = float(input('Escreva um valor para o preço de um produto hipotético: ')) # Guardará o valor do produto
desconto = preco/20 # Fará o cálculo de quanto é 5% do valor do produto

# Mostra o desconto de 5% do produto
print(f'O preço do produto com 5% de desconto seria R$ {preco-desconto:.2f}!'.replace('.',','))
