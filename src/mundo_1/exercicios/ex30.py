# Desafio #030: Faça um programa que exibe se um número é impar ou par:

num = int(input('Escreva um número: ')) # Guardará o número escrito
ver = num % 2 # Guarda o valor do resto da divisão inteira do número por dois (ex 2/2 = 1, não tem resto porque é par, ou 3/2 = 1, tem resto 1 pq e impar)

if ver == 0: # Se o resto é 0 (par)
    print(f'O número {num} é par!') # avisa que é par

else: # se não (impar)
    print(f'O número {num} é ímpar!') # avisa que é impar
