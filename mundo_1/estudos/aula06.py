# Aula 06: Tipos primitivos e saída de dados

# Teoria rápida e simples:

dado = input('Por favor, escreva algo aqui: ') # Irá armazenar o que o usuário escrever na variável dado.

print(f'O que você é escreveu é do tipo: {type(dado)}.') # Exibe o tipo primitivo do que o usuário escreveu. (Vindo de um input sem conversão para outro tipo primitivo, sempre resultará em str (string))
print(f'Verificação se é um número: {dado.isnumeric()}.') # Verifica se é número e exibe a resposta na tela. (Como o input sempre será str, então isso sempre será do tipo falso, mesmo se digitar 9, o Python considera o 9 do tipo str como texto.)

print('Há diversos tipos de verificações que podem ser feitas no que você escreveu.') # Mensagem de explicação extra.
