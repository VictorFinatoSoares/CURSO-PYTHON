#Desafio 014: Faça um programa que leia o valor de uma temperatura em graus celsius e converta em fahrenheit

gc = float(input('Digite o valor da temperatura em celsius: ')) # Armazena a temperatura em celsius
gf = (gc * 9/5) + 32# Converte em fahreinheit

# Mostra o valor da temperatura já convertida.
print(f'Convertendo a temperatura em fahrenheit, {gc} graus celsius são {gf:.2f} graus fahrenheit!')
