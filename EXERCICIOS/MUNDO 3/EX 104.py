def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[91mDIGITE UM VALOR INTEIRO VALIDO\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um valor: ')
print(f'Voce digitou o numero {n}.')