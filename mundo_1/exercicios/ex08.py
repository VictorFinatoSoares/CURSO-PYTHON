# Desafio 008: Escreva um programa que converta metros em: quilômetros, centimetros e milimetros:

m = float(input('Escreva quantos metros serão convertidos: ')) # Guarda o valor de metros.
km = m / 1000 # Converte em km
cm = m * 100 # Converte os metros em cm
mm = m * 1000 # Converte os metros em mm

print(f'{float(m)} metros são: {float(km)}km, {float(cm):.0f} cm e {float(mm):.0f} mm.') # Mostra os valores de cada conversão.
