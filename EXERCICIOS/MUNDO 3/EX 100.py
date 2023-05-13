from time import sleep
from random import randint

def sorteado(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ' )
        sleep(0.2)
    print('fim')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'{lista}\nOs pares somam {soma}')        
numeros = list()
sorteado(numeros)
somapar(numeros)
