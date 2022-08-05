num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidades {}'.format(u)) 
print('dezenas {}'.format(d))
print('centena {}'.format(c))
print('milhares {}'.format(m))


