from random import randint

itens = ['PEDRA', 'PAPEL', 'TESOURA']
print("="*10 ,'JO KEN PO','='*10)

esc = int(input(""" Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
"""))
pc = randint(0, 2)
print('='*10)
print('voce escolheu {}'.format(itens[esc]))
print('='*10)
print(' o computador escolheu : {}'.format(itens[pc]))
print('='*10)

if pc == 0:
    if esc == 2:
        print('Perdeu')
    elif esc == 1:
        print('Venceu')
    else:
        print('Empate')


elif pc == 1:
    if esc == 2:
        print('Venceu')
    elif esc == 1:
        print('Empate')
    else:
        print('Perdeu')

elif pc == 2:
    if esc == 2:
        print('empata')
    elif esc == 1:
        print('Ganha')
    else:
        print('perde5')

    




