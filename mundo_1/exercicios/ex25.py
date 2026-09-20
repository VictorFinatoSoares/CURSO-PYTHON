# Desafio #025: Faça um programa que lê um nome e diga se ele tem silva.

nome = input('Escreva seu nome: ').title() # Guarda o nome em uma variavel

ver = 'Silva' in nome # Verifica se tem Silva no nome.

print(f'O nome {nome} tem Silva? {ver}'.replace('True', 'Sim.').replace('False', 'Não.')) # Indica a resposta
