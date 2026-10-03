# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilidadesCeV.moeda  import *
from utilidadesCeV.dado import *

saldo = leiaDinheiro('Digite o seu saldo: R$ ')
resumo(saldo, formatar=True)