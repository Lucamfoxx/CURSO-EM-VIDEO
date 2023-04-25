from time import sleep
def contador(i, f, p):
    print()
    print(f'\na contagem de {i} ate {f} contando de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont -= p    


contador(1, 10 , 1)
contador(10, 1 , 1)
print()
i = int(input('digite o inicio: '))
f = int(input('digite o fim: '))
p = int(input('digite o periodo: '))
contador(i, f, p)
