# Aula 14: Aula sobre a estrutura de repetição while

# for i in range (1, 10):
#     print(i)
# print('Fim')

# i = 1
#
# while i < 10:
#     print(i)
#     i += 1
# print('Fim')

n = 1

quant_par = 0
quant_impar = 0

while n != 0:
    n = int(input('Digite um número: '))

    if n != 0:
        if n % 2 == 0:
            quant_par += 1
        else:
            quant_impar += 1

print(f'Você digitou {quant_par} pares e {quant_impar} ímpares.')