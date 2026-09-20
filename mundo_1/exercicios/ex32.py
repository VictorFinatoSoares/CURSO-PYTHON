# Desafio #032: Faça um programa que leia um ano e diga se ele é ou não um ano bissexto

ano = int(input('Digite um ano: ')) # Guardará o ano digitado

# --> Para um ano ser bissexto, ele precisa ser divisivel por 4, sempre, a não ser que ele seja centenário (divisivel por 100), se ele for centenario, aí precisa ser divisivel por 400

if ano % 400 == 0: # Verifica se o ano é divisivel por 400 (se sim, ele é bissexto)
    print(f'O ano {ano} é bissexto!') 

elif ano % 100 == 0: # então verifica se é divisivel por 100, se ele é divisivel por 100 e não foi divisivel por 400, então não é bissexto
    print(f'O ano {ano} não é bissexto!') 

elif ano % 4 == 0: # se ainda assim não for centenario nem divisivel por 400, verifica se é divisivel por 4, se for, ele é bissexto
    print(f'O ano {ano} é bissexto!')

else: # Caso contrário, ele não é divisivel por 4 nem bissexto.
    print(f'O ano {ano} não é bissexto!')
    