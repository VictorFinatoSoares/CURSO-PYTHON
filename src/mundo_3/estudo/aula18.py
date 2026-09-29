# Aula 18 sobre listas (parte 2):

# Se não usar [:], ele liga o mesmo endereço de memória para duas variáveis, [:] faz que copie de um, porém separe o endereço

# teste = []
#
# teste.append('Victor')
# teste.append(15)
#
# galera = []
#
# galera.append(teste[:])
#
# print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for pessoa in galera:
    print(f'Nome: {pessoa[0]}\nIdade: {pessoa[1]}')
