from random import randint
num = []
jogos = int(input('qual o numero de jogos que voce quer? '))
for c in range(0, jogos):
    for n in range(0, 6):
        num.append(randint(1, 60))
for i in range(0, len(num), 6):
    print(*num[i:i+6])
    print('-='*30)