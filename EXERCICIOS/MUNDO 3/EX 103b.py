def jogador (nome='<DESCONHECIDO>', gols=0):
    print(f'O jogador {nome}, fez {gols} gols')


n = input('NOME DO JOGADOR : ')
g = input('GOLS FEITOS: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if  n.strip() == '':
    jogador(gols=g)
else:
    jogador(n, g)