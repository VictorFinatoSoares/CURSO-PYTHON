# Aula 20 sobre funções (parte 1)

# Funcionalidades personalizadas:
def mostra_cabecalho(msg):
    print('=' * 30)
    print(msg.center(30))
    print('=' * 30)

# Parâmetros com * permitem receber vários valores ao mesmo tempo
def somar(*nums):
    soma = 0

    for num in nums:
        soma += num

    return soma

def dobrar_lista(lista):
    pos = 0

    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

    return lista

# Programa principal
mostra_cabecalho('Início do Programa Principal')

print(somar(1, 2, 3, 4, 5))

lista = [1, 2, 3, 4, 5]
print(dobrar_lista(lista))

mostra_cabecalho('Fim do Programa Principal')