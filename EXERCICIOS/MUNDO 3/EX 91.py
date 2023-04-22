from random import randint
from time import sleep
from operator import itemgetter
sorteados = {}
for c in range(1, 5):
    sorteados[c] = randint(1, 10)
    print(f'o jogador {c} tirou {sorteados[c]}')
    sleep(0.7)
for c, k in sorted(sorteados.items(), key=itemgetter(1) , reverse=True):
    print(f'{c} jogador tem {k} pontos')