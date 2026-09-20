# Aula009: Manipular textos
# Existem varios jeitos de manipular textos:

frase = 'Curso em Vídeo' # Texto dentro de variavel

# Fatiamento:

print(frase[9]) # Retorna a letra V (já que o indice da string acima começa em 0, então 9 = a décima letra dela.)

# É importante lembrar que o python diferencia letras minusculas das maiusculas, não sendo iguais.

print(frase[9:13]) # Retorna "Víde" ele printa do indice 9  até o 13 excetuando o 13, então é do 9 ao 12, para exibir vídeo teria que ser 9:14

print(frase[:5]) # Printa do 0 ao 5 (excetuando o 5), já que antes dos : não tem nada, conta como 0. (o começo da string) retorna: Curso

print(frase[6:]) # Como depois dos : não tem nada, ele começa no 6 e vai até o fim da string. retorna "em Vídeo"

print(frase[9:14:2]) # Começa no 9, vai até o 14 excetuando o 14, pulando de dois em dois: "Vdo"

print(frase[9::3]) # Do 9 ao final das string pulando 3 letras: "Ve"

# Análise:

print(len(frase)) # Printa quantos caracteres (contando os espaços) tem a string no caso, 14.

print(frase.count('o')) # Conta quantos "o" minúsculos tem na string: 2

print(frase.find('deo')) # Procura na string se tem "deo" e vai retornar o número de qual indice começa essa parte, no caso: 11
# Se não tiver, ele retornará -1 (não tem, ja que começa no indice 0)

print('Curso' in frase) # Retorna False se não tiver, ou True se tiver isso na frase.


# Transformação: 

print(frase.replace('Vídeo', 'Foto')) # Troca a parte "Vídeo" por "Foto", mas altera apenas a instancia, não a variavel global, então se pedir pra printar frase, não irá mostrar Curso em Foto, mas se pedir pra printar frase.replace bla bla aí mostra, ou então se falar que frase = frase.replace bla bla

print(frase.upper()) # Vai deixar tudo maiusculo

print(frase.lower()) # Vai deixar tudo minusculo

print(frase.capitalize()) # Vai deixar tudo minusculo e a primeira letra da primeira palavra fica maiuscula

print(frase.title()) # tudo minusculo porem a primeira letra de cada palavra fica maiuscula

frase2 = '   Aprendendo Python  ' # Como podemos ver, essa string tem alguns espaços inuteis...

print(frase2.strip()) # Remove os espaços inuteis tanto da esquerda ou direita.

print(frase2.lstrip()) # Remove apenas os espaços inuteis da esquerda

print(frase.rstrip()) # Remove apenas os espaços inuteis da direita

# Para remover até os espaços não inutéis, dá pra usar o replace pra substuir o " " por ""

# Separação:

print(frase.split()) # Usando split, o python (com base nos espaços entre texto) vai separar por palavras (só na instancia), então se pedir pra printar o [0] em vez de mostrar a primeira letra, ele mostra a primeira palavra, [1] seria a segunda palavra, se usar [0][0] aí é a primeira letra da primeira palavra etc...


# Junção:

print('-'.join(frase.split())) # Vai juntar todas as palavras de volta... e colocar um - entre elas..
