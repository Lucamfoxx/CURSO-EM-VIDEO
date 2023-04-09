p= ('Lapis   ','R$ 2,50',
    'Borracha','R$ 1,00',
    'Papel a4','R$ 0,50',
    'Lampada','R$ 8,50')
for pos in range(0, len(p)):
    if pos % 2 == 0:
        print(f'{p[pos]:.<30}', end='')
    else:
        print(f'{p[pos]:>7}')