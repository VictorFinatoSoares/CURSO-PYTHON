#Desafio 013: Faça um programa que leia o salário de um funcionário, e mostre o valor novo com 15% de aumento

salario = float(input('Digite o valor do salário de seu funcionário: ')) # Armazena o salário
aumento = float((salario/20) * 3) # Vê o valor que será acrescentado

# Mostra o valor do novo salário com aumento de 15% já incluso.
print(f'Com um aumento de 15%, o salário dele será de R$ {salario+aumento:.2f}!'.replace('.',','))
