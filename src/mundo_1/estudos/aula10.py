# Aula #010: Condições

# Uso de condições:

tempo = int(input('Quantos anos tem o seu carro? ')) # Guarda quantos anos tem o carro na variavel tempo

if tempo <=3: # Se o carro tem 3 ou menos anos: 
    print('Seu carro é novo!') # Mostra que é novo

else: # Senão (4 anos pra cima)
    print('Seu carro é velho!') # Mostra que é velho

# Condição simplificada:

# print('Seu carro é novo!' if tempo <=3 else 'Seu carro é velho!')

# <= É menor ou igual >= É maior ou igual < É menor > é maior == É igual != é diferente

# Se for algo tipo: if isso_rolar: é o mesmo que perguntar se isso_rolar == True: ou se usar if !isso_rolar: é o mesmo que perguntar se isso_rolar == False:

# Exemplo do Guanabara: Estruturas simples e compostas:

# Simples 
nome = str(input('Escreva o seu nome: ')) # Guarda o nome do usuário

if nome.title() == 'Victor': # Se o nome for Victor
    print('Que belo nome você tem!') # Fala que o nome é bonito
# Se tivesse o else seria composta
#else: # Se não
    #print('Seu nome é tão normal!') # Fala que é normal
print(f'Bom dia, {nome}!') # Bom dia que acontece sempre.

# Outro:

n1 = float(input('Digite sua primeira nota: ')) # Guarda a primeira nota
n2 = float(input('Digite sua segunda nota: ')) # Guarda a segunda nota
m = (n1 + n2) / 2 # Faz o cálculo pra saber a média entre as duas

print(f'A sua média foi: {m:.1f}!') # Fala a média que foi

if m >=6.0: # Se a media for 6 ou mais
    print('Sua média foi boa!') # Fala que foi boa

else: # Se não
    print('Sua média foi ruim!') # Fala que foi ruim
    