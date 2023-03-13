while True:
    print('-'*30)
    n = int(input('DIGITE UM NUMERO: '))
    if n >= 0:
        for c in range(1, 11):
            print(f'{n} X {c} = {n*c}')
    else:
        print('FIM DO PROGRAMA')
print('-'*30)