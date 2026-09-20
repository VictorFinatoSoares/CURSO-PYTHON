# Desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

nome = input('Escreva o seu nome completo: ').title() # Guarda o nome completo digitado, e usa title pra deixar cada palavra com a primeira letra maiuscula.

nome_limpo = nome.replace(' ', '') # Remove os espaços entre palavras da variavel nome e guarda numa variavel

print(f'Seu nome é {nome}.') # Mostra o nome original escrito

print(f'Seu nome com todas as letras maiúsculas fica: {nome.upper()}') # Mostra o nome original escrito tudo maiusculo
print(f'Seu nome com todas as letras minúsculas fica: {nome.lower()}') # Mostra o nome original escrito tudo minúsculo

print(f'Seu nome tem {len(nome_limpo)} letras no total.') # Mostra quantas letras tem o nome completo do usuário sem contar os espaços
print(f'Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras.') # Mostra o primeiro nome do usuário e quantas letras ele tem
