# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input('Digite sua expressão: ') # Obtém a expressão ex: (4*2(9+1))

# Lista responsável por armazenar e gerenciar a lógica para cada par de parênteses
pares = []

# Verificará cada caractere na expressão
for simb in expressao:
    if simb == '(': # Se for um parêntese aberto
        pares.append('(') # Adiciona à lista
    elif simb == ')': # Caso seja um fechado
        if len(pares) > 0: # Se já houver um elemento (que na lógica definida será sempre um parêntese aberto)
            pares.pop() # Remove esse elemento, pois se já havia um aberto e agora tem um fechado, o par foi concluído e pode ser limpo.
        else: # Se não tinha nenhum elemento porém foi encontrado um fechado, significa que está na ordem errada (fechando sem ter aberto)
            pares.append(')')  # Adiciona o elemento à lista
            break # Encerra o loop

if len(pares) == 0: # Se todos os pares fecharam
    print('A expressão é válida.')
else: # Senão
    print('A expressão é inválida!')