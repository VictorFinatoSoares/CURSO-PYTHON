# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de
# uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print("====== EXERCÍCIO 36 - EMPRÉSTIMO BANCÁRIO ======\n")

valor_casa = int(input("Qual é o valor da casa? "))
salario = int(input("Qual é o seu salário? "))
anos = int(input("Em quantos anos deseja pagar? "))

prestacoes_mensais = anos * 12
valor_prestacao = valor_casa / prestacoes_mensais
limite_valor = salario * 0.3

if valor_prestacao <= limite_valor:
    print(f'EMPRÉSTIMO ACEITO! Você pagará R$ {valor_prestacao:.2f} por prestação MENSAL!')
else:
    print(f'EMPRÉSTIMO NEGADO! O valor da prestação mensal seria R$ {valor_prestacao:.2f}, o que ultrapassa 30% do seu salário! (R$ {limite_valor:.2f})')
