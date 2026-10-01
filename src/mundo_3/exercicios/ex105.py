# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*notas, sit=False):
    """
    A função recebe uma quantidade indefinida de notas e retorna um dicionário com informações básicas
    como quantas notas foram recebidas, a maior nota, a menor nota, a média de notas e a situação (opcional, BOA, RAZOÁVEL, RUIM)
    :param notas: vários valores floats como nota
    :param sit:  valor lógico opcional para informar a situação geral da turma
    :return: retorna um dicionário com todas as informações obtidas
    """

    info_notas = {}
    info_notas['total'] = len(notas)
    info_notas['maior'] = max(notas)
    info_notas['menor'] = min(notas)
    info_notas['media'] = round(sum(notas) / len(notas), 2)

    if sit:
        if info_notas['media'] >= 7:
            info_notas['situação'] = 'BOA'
        elif info_notas['media'] >= 5:
            info_notas['situação'] = 'RAZOÁVEL'
        else:
            info_notas['situação'] = 'RUIM'

    return info_notas

print(notas(9, 10, 5.5, 2.5, 8.5, sit=True))

help(notas)
