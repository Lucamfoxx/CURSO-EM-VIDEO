def jogador(nome, gols):
    if nome == '' and gols == '':
        print(f'O jogador desconhecido tem 0 gols no Campeonato')
    elif gols == '':
        print(f'O JOGADOR {nome} fez 0 gols')
    elif nome == '':
        print(f'o jogador desconhecido tem {gols} gols.')
    else:
        print(f'o jogador {nome} fez {gols} gols')
nome = input('NOME DO JOGADOR : ').strip().title()
gols = input('GOLS FEITOS: ')
jogador(nome, gols)
