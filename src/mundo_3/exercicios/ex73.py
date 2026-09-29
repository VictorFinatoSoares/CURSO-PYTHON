# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = (
    "Flamengo",
    "Palmeiras",
    "Athletico-PR",
    "Fluminense",
    "Bahia",
    "Cruzeiro",
    "Atlético-MG",
    "Santos",
    "Coritiba",
    "Bragantino",
    "São Paulo",
    "Botafogo",
    "Vitória",
    "Corinthians",
    "Mirassol",
    "Vasco",
    "Grêmio",
    "Internacional",
    "Remo",
    "Chapecoense"
)

# 5 Primeiros times
print(times[:5])

# Últimos 4 colocados
print(times[-4:])

# Em ordem alfabética
print(sorted(times))

for i in range(len(times)):
    if times[i] == "Chapecoense":
        print(f'O Chapecoense está na posição {i + 1}')
