# Aula 17: Listas em Python (Primeira parte)

# LISTAS SÃO MUTÁVEIS

lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
lanche[1] = 'Refrigerante'

print(lanche)
lanche.append('Biscoitos') # Append adiciona no final da lista
print(lanche)

lanche.sort() # Sort organiza por ordem crecente (quando são números) e em ordem alfabética quando são letras/palavras
print(lanche)

lanche.insert(0, 'Açúcar') # Insert insere um elemento no índice informado
print(lanche)

print(f'Essa lista possui {len(lanche)} elementos.')
lanche.pop(0) # Pop com parâmetro

print('Lanche sem açúcar:')
print(lanche)

if 'Miojo' in lanche:
    lanche.remove('Miojo')
else:
    print('Miojo não está na lista.')

# Caso haja uma lista a = [1, 2, 3, 4] e uma lista b = a, a lista "b" e a lista "a" são ligadas, e não copiadas uma para a outra
# Isso faz com que a lista "b" que recebe a lista "a" ao ser alterada, também altere o conteúdo da lista "a". Portanto:

a = [1, 2, 3, 4]
b = a.copy()
