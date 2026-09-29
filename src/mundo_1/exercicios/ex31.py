# Desafio #031: Crie um programa que pergunte a distância em km de uma viagem e cobre 0.50 reais cada km se ela for até 200km, e 0.45 reais se for mais do que isso.

dis = int(input('Qual a distância em quilômetros da sua viagem? ')) # Guarda o valor da distancia da viagem

preco_1 = 0.50 # Preço 1 (se a viagem for até 200km)
preco_2 = 0.45 # Preço 2 (se for mais do que 200km)

if dis <=200: # Se a viagem for até 200km
    print(f'Sua viagem de {dis}km custará: R$ {dis * preco_1:.2f}'.replace('.', ',')) # Mostra o valor da viagem em reais, após multiplicar o preço 1 por km da viagem de até 200km

else: # Se tiver mais de 200km
    print(f'Sua viagem de {dis}km custará: R$ {dis * preco_2:.2f}'.replace('.', ',')) # Mostra o valor da viagem em reais, após multiplicar o preço 2 por km da viagem de mais de 200km
