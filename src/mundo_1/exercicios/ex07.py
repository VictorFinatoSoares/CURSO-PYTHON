# Desafio 007: Crie um programa que leia duas notas de um aluno e faça a média entre elas.
n1 = float(input('Olá, escreva a primeira nota aqui: ')) # Guarda o valor da primeira nota em n1
n2 = float(input('Escreva sua segunda nota aqui: ')) # Guarda o valor da segunda nota em n2
m = (n1+n2)/2 # Soma as duas notas,divide por 2 pra obter a média e guarda o resultado em uma variavel

print(f'A média entre a primeira nota ({n1}), e a segunda nota ({n2}), é {m:.2f}!') # Mostra a média entre os dois valores.
