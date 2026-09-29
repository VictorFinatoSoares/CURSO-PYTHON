# Aula 16 sobre tuplas em Python

# TUPLAS SÃO IMUTÁVEIS!!!

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# Utiliza o contador como um índice na coleção, usando o tamanho da tupla como limite.
for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]}')

for item in lanche:
    print(f'Eu vou comer {item}')

for pos, item in enumerate(lanche):
    print(f'Eu vou comer {item} na posição {pos}')

print('Comi pra caramba')