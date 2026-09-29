#Desafio 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"

cidade = input('Escreva o nome de uma cidade: ').title() # Deixa todas as palavras da cidade com a primeira letra maiúscula na hora de guardar ela numa variavel
verificacao = (cidade[:5] == 'Santo') # Vê se as primeiras 5 letras da string tem santo.

# Linha grande pra deixar a mensagem bonitinha :)
print(f'A análise se essa cidade começa com Santo definiu como: {verificacao}'.replace('True', 'Sim, começa com Santo.').replace('False', 'Não, não começa com Santo.'))
