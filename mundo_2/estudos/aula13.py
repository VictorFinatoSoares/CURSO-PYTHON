# Aula 13: Sobre o loop for

# Teste de contagem regressiva:
for i in range(10, -1, -1):
    print(i)

# Pular uma linha:
print()

# Imprimir pares de 0 a 100
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

print()

# Início, fim e passo:

inicio = int(input('Informe o início do loop: '))
fim = int(input('Informe o fim do loop: '))
passo = int(input('Informe o passo do loop: '))

for i in range(inicio, fim + 1, passo):
    print(i)