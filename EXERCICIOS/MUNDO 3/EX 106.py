def notas(*n, sit=False):
    '''
    Função para avaliar notas de alunos:
    
    :param n: uma ou varias notas:
    :param sit: se TRUE exibe a condiçao do aluno (ruim, razoavel ou boa).
    :return: um dicionairo com o valores e informaçoes da turma

    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situaçao'] = 'BOA'
        elif r['media'] >= 5:
            r['situaçao'] = 'RAZOAVEL'
        else:
            r['situaçao'] = 'Ruim'
    return r    


resp = notas(9, 5, 10, 3)
print(resp)