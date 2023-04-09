from random import randint
numeros = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))
print('os numeros foram sorteados : ')
for n in numeros:
    print(f'{n}', end='')
