# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal
# – 3x ou mais no cartão: 20% de juros

preco_normal = float(input('Informe o preço normal do produto: '))

print('''
====== MÉTODOS DE PAGAMENTO DISPONÍVEIS: ======

(1) À vista dinheiro/cheque: 10% desconto
(2) À vista no cartão: 5% de desconto
(3) À em até 2x no cartão: preço normal 
(4) À 3x ou mais no cartão: 20% de juros

''')

metodo_pagamento = int(input('Informe o método de pagamento: '))

if metodo_pagamento == 1:
    print(f'Você decidiu pagar à vista em dinheiro/cheque, o valor final da sua compra será R$ {preco_normal * 0.9:.2f}')
elif metodo_pagamento == 2:
    print(f'Você decidiu pagar à vista no cartão, o valor final da sua compra será R$ {preco_normal * 0.95:.2f}')
elif metodo_pagamento == 3:
    print(f'Você decidiu pagar em até 2x no cartão, o valor final da sua compra será R$ {preco_normal:.2f}')
else:
    print(f'Você decidium pagar em 3x ou mais no cartão, o valor final da sua compra será R$ {preco_normal * 1.2:.2f}')