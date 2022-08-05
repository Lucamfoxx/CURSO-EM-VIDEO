n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))


if n1 > n2:
    print('{} é maior que {} '.format(n1, n2))
elif n2 == n1:
    print('os dois numeros sao iguais')
else:
    print('{} maior que {}'.format(n2,n1))
