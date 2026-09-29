# Desafio 004: Crie um programa que leia algo pelo teclado, e  mostre na tela o seu tipo primitivo e outras infos sobre.

dado = input('Digite algo: ') # Armazenando o que for escrito.

print('Lista de Informações:') # Iniciando a lista
print(f'O tipo primitivo disso é: {type(dado)}') # Mostra o tipo primitivo (se é str, float, int, bool etc).
print(f'Só tem espaços? {dado.isspace()}') # Verifica se é espaço vazio
print(f'É um número? {dado.isnumeric()}') # Verifica se é número
print(f'É alfabético? {dado.isalpha()}') # Verifica se só tem letras
print(f'É alfanúmerico? {dado.isalnum()}') # Verifica se tem letras junto de números apenas.
print(f'Está tudo maiúsculo? {dado.isupper()}') # Verifica se a mensagem está totalmente em maísculo
print(f'Está tudo minúsculo? {dado.islower()}') # Verifica se a mensagem está totalmente em maísculo
print(f'Está capitalizada? {dado.istitle()}') # Verifica se a mensagem está totalmente em maísculo
