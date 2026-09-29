#Desafio #026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Escreva uma frase: ') # Guarda a frase

frase = frase.upper() # Transforma tudo em maiusculo
frase = frase.strip() # Remove possíveis espaços inuteis

num_a = frase.count('A') # Procura quantos A's maiusculos tem na frase.

print(f'Sua frase tem {num_a} letras "A".') # Fala quantos tem
print(f"O primeiro 'A' está no {frase.find('A') + 1} caractere.") # Mostra quando aparece o primeiro A
print(f"O último 'A' está no {frase.rfind('A') + 1} caractere.") # Mostra quando aparece o segundo A
