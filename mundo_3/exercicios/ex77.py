# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("CANETA", "SAPATO", "LAMPADA", "DESENHO", "LIVRO", "QUADRO", "TETO")
vogais = "AEIOU"

print(f'Palavras registradas: {palavras}')

for palavra in palavras:
    print(f'\nVOGAIS ENCONTRADAS EM "{palavra}"')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')