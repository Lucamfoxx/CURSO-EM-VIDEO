from random import randint
n = int(input('Tente acertar um numero de 0 a 100: '))
n1 = randint(0, 100)
if n==n1:  
    print("-==-"*10)
    print('VENCEU')
    print("-==-"*10)
else:
    print("-==-"*10)
    print('Perdeu o numero era {}'.format(n1))
    print("-==-"*10)

