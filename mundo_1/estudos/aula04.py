# Aula 004: Primeiros comandos em Python3:

# Exemplos de primeiros comandos:

print('Hello, World!') # Exibe a mensagem Hello, World! Na tela.

print(5+2) # Exibe o resultado desta soma (7)

input('Digite algo: ') # Dá espaço para o usuário digitar ago, entretanto ainda não é guardado nem utilizado depois nesse código.

# Teoria 001: Crie um programa que leia o nome do usuário e mande uma mensagem de boas vindas.

nome = input('Qual é o seu nome? ') # Irá permitir o usuário digitar o seu nome, e o guarda na variável nome.
print(f'Seja muito bem vindo, {nome}!') # Dá uma mensagem de boas vindas com base em seu nome.

# Teoria 002: Crie um programa que leia o dia, mês e ano que uma pessoa nasceu e exiba tudo isso junto.

dia = input('Em que dia você nasceu? ') # Permite o usuário digitar o dia de seu nascimento, e guarda na variável dia.
mes = input('Em qual mês você nasceu? ') # Permite o usuário digitar o mês de seu nascimento, e o guarda na variável mes.
ano = input('Em que ano você nasceu? ') # Permite o usuário digitar o ano de seu nascimento, e o guarda na variável ano;

print(f'Você nasceu no dia {dia} de {mes} em {ano}.') # Exibe o dia, mês e ano de nascimento do usuário.
