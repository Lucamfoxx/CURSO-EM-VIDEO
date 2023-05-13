def fatorial(n, show=False):
    '''calcula o fatorial de um numero .
    :param n: O numero a ser calculado.
    :param show: (opcional) mostra a a conta.
    :return: o valor do factorial de um numero 'n' 
    '''
    f = 1
    for c in range(n , 0, -1):
        if show:
            print(c, end=" ")
            if c > 1:   
                print('X', end=" ")
            else:
                print('=',end=" ")
        f *= c 
    return f

print(fatorial(14, True))
help(fatorial)