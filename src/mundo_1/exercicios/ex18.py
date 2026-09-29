from math import radians, sin, cos, tan # Importa funções da biblioteca math

num = float(input('Digite um ângulo qualquer: ')) # Irá armazenar o ângulo que o usuário deseja
rad = radians(num) # Converte o número para radianos

sen = sin(rad) # Vê qual o seno do número escolhido
cos = cos(rad) # Vê qual o cosseno do número escolhido
tan = tan(rad) # Vê qual a tangente do número escolhido

print(f'{num} graus tem o seno {sen:.2f} e o cosseno {cos:.2f}.') # Mostra o seno e o cosseno
print(f'A tangente é {tan:.2f}.') # Mostra a tangente
