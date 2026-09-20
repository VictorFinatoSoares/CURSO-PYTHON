# Desafio 010: Escreva um programa que lê quanto dinheiro uma pessoa tem na carteira e veja quantos dólares ela pode comprar (Considere 1,00 Dólar = R$ 3,27)

dinheiro = float(input('Quantos reais você tem na carteira? ')) # Guarda o valor de reais
dolar = dinheiro/3.27 # Converte 

print('\nConsiderando que $1,00 dólar = R$ 3,27...') # Mensagem adicional..
print(f'Com R$ {dinheiro:.2f} você pode comprar ${dolar:.2f} dólares!\n'.replace('.',',')) # Exibe o valor convertido do dinheiro em reais para dólar.
