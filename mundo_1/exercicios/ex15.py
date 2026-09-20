#Desafio 015:  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia_v = 60 # Valor do aluguel do carro por dia
km_v = 0.15 # Valor adicional por km rodado

dias_alugados = int(input('Quantos dias o carro foi alugado? ')) # Guarda a quantidade de dias que o carro foi guardado
km_rodados = int(input('Quantos KM foram rodados? ')) # Guarda a quantidade de kms rodados com o carro

# Calcula o preço do aluguel do carro com base nos dias e km rodados.
preco = (dias_alugados * dia_v) + (km_rodados * km_v)

# Mostra o valor do aluguel do carro.
print(f'Com o carro alugado durante {dias_alugados} dias e {km_rodados} km andados, o aluguel ficará: R$ {preco:.2f}.'.replace('.',','))
