# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

# Desafio 035: Faça um programa que leia 3 retas e diga se elas podem ou não formar um triângulo

r1 = float(input('Escreva o comprimento da primeira reta: ')) # Guarda a primeira reta
r2 = float(input('Escreva o comprimento da segunda reta: ')) # Guarda a segunda reta
r3 = float(input('Escreva o comprimento da terceira reta: ')) # Guarda a terceira reta

verif = (r1+r2) > r3 and  (r2+r3) > r1 and  (r1+r3) > r2 # Testa todas as combinações possíveis pra ver se duas retas quaisquer somadas é maior que o terceiro lado, se todas as 3 for verdade, então pode ser formado um triangulo com elas

if verif: # se pode
    print('Essas três retas formam um triângulo!')

    # Verifica se é equilátero:
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else: # se não pode
    print('Essas três retas não formam um triângulo!')