# Aula 01, sobre condições aninhadas

caminho = input('Qual caminho seguir? ')

print('Começo do percurso')

# Estrutura de condições COMPOSTA (não aninhada): (sim, o Guanabara citou um exemplo semelhante que nem é realmente aninhadokkkkkkk)

if caminho == 'esq':
    print('O carro deverá: seguir em frente, virar à direita, seguir em frente, virar à direita, virar à esquerda, seguir em frente, virar à direita, seguir em frente')
elif caminho == 'dir':
    print('O carro deverá: seguir em frente, virar à esquerda, seguir em frente, virar à esquerda, seguir em frente')
else:
    print('O carro deverá: seguir em frente')

print('Fim do percurso')

