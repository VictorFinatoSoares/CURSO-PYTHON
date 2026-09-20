# Desafio #029: Faça um programa que leia a velocidade de um carro, se ela ultrapassar 80km por hora, mostra uma mensagem dizendo que o usuario foi multado, e cobrando um valor, que  será de 7 reais por km a mais do limite

vel = int(input('Qual a velocidade em quilômetros do carro? ')) # Guardará a velocidade em que o carro estava.
lim = 80 # Define o limite de velocidade
val = 7 # Define o valor em reais cobrado por km acima do limite

cob = (vel - lim) * val # Calcula o valor a ser cobrado pelo usuário se ele for multado.. (vê a diferença da velocidade e o limite) e multiplica os kms a mais por 7..

if vel > lim: # Se ele estava mais rápido que o limite
    print(f'Você foi multado por ultrapassar o limite de velocidade de {lim}km, o valor da cobrança é de R$ {cob:.2f}!'.replace('.', ',')) # Exibe a mensagem de multa com o valor certinho por km acima.

else: # Caso contrário
    print(f'Hmm, você está dentro do limite de velocidade de {lim}km, mas estamos de olho em você!') # Nada de multas na mensagem
    