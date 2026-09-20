# Desafio #027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Escreva o seu nome completo: ').title() # Guarda o nome completo da pessoa

nome = nome.split() # Divide a string em pedaços (cada um com uma palavra)
sb = len(nome) # Determina quantas palavras tem, e já indica o sobrenome guardando na variavel sb

print(f'Seu primeiro nome é {nome[0]}') # Mostra o primeiro nome
print(f'Seu último nome é {nome[sb -1]}') # Mostra o ultimo nome usando sb -1 (já que começa em 0, então se for 4 palavras, -1 = 3, logo mostrará a quarta palavra (0,1,2,3))
