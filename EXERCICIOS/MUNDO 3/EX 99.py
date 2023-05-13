from time import sleep
from random import randint
def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    for valor in num:
        print(f"{valor}",end=" ")
        cont += 1
        sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor 
    print()   
    print(f'Foram analisados {cont}')
    print(f'O maior valor informado é {maior}')
def ale(*x):
    aleatorio = []
    for rad in x:
        aleatorio.append(randint(1, 10))
    maior(*aleatorio)


ale(*[randint(1, 10) for i in range(randint(1, 10))])

