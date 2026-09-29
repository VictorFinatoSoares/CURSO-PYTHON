# Desafio 011: Faça um programa que leia a largura e altura de uma parede

largura = float(input('Escreva a largura da parede: ')) # Armazena a largura da parede em metros
altura = float(input('Escreva a altura da parede: ')) # Armazena a altura  da parede em metros

area = largura * altura # Calcula a área

print(f'A parede possui {area} m²') # Mostra a área da parede

# Mostra quantos litros de tinta precisa para a área total da parede, considerando a quantidade de m² pintados por litro de tinta
print(f'Como a cada 1L de tinta pinta 2m², a sua parede precisará de {area/2} litros de tinta.')
