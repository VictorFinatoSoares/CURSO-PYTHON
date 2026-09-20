# Desafio 003: Crie um programa que leia dois números e mostre a soma entre eles:
print('Testando o Desafio 003 (Aula 6): ') # Iniciando teste

n1 = int(input('Digite o primeiro número: ')) # Armazenando o primeiro valor.
n2 = int(input('Digite o segundo número: ')) # Armazenando o segundo valor.
resultado = n1 + n2 # Somando e guardando o resultado.

print(f'O resultado da soma entre {n1} e {n2} é {resultado}.') # Mostrando o resultado

# Desafio 004: Crie um programa que leia algo pelo teclado, e  mostre na tela o seu tipo primitivo e outras infos sobre.
print('Testando o Desafio 004 (Aula 6): ') # Iniciando teste

n3 = input('Digite algo: ') # Armazenando o que for escrito.

print('Lista de Informações:') # Iniciando a lista
print(f'O tipo primitivo disso é: {type(n3)}') # Mostra o tipo primitivo (se é str, float, int, bool etc).
print(f'Só tem espaços? {n3.isspace()}') # Verifica se é espaço vazio
print(f'É um número? {n3.isnumeric()}') # Verifica se é número
print(f'É alfabético? {n3.isalpha()}') # Verifica se só tem letras
print(f'É alfanúmerico? {n3.isalnum()}') # Verifica se tem letras junto de números apenas.
print(f'Está tudo maiúsculo? {n3.isupper()}') # Verifica se a mensagem está totalmente em maísculo
print(f'Está tudo minúsculo? {n3.islower()}') # Verifica se a mensagem está totalmente em maísculo
print(f'Está capitalizada? {n3.istitle()}') # Verifica se a mensagem está totalmente em maísculo
