# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from utilidadesCeV.moeda  import *

saldo = float(input('Digite seu saldo: '))
resumo(saldo, formatar=True)