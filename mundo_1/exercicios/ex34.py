# Desafio 034: Faça um programa que leia o salario de um funcionario, se o salario for mais de 1250, o aumento é de 10 porcento, se for igual ou menos de 1250, então é 15 porcento

salario = float(input('Informe o valor do seu salário: ')) # Guarda o valor do salário

a1 = (salario /20) * 2 # Faz o cálculo pra um aumento de 10% (caso o salário seja acima de 1250)
a2 = (salario/20) * 3 # Faz o cálculo pra um aumento de 15% (caso o salário seja abaixo ou igual 1250)

if salario > 1250: # verifica se o salário é maior que 1250 reais
    print(f'O seu salário de R$ {salario:.2f} terá um aumento de 10%, ficando: R$ {salario + a1:.2f}!'.replace('.', ',')) # Mostra o salário do usuário, quantos % de aumento e o valor do seu salário após aumento

else: # Se for menor
    print(f'O seu salário de R$ {salario:.2f} terá um aumento de 15%, ficando R$ {salario + a2:.2f}!'.replace('.', ',')) # Mostra o salário do usuário, quantos % de aumento e o valor do seu salário após o aumento
