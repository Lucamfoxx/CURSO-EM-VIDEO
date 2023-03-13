from random import randint

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar : ')).strip().upper()[0]
    print(f'VOCE JOGOU {jogador} E O PC JOGOU {computador} A SOMA É {soma}')
    if soma % 2 == 0:
        tipo2 = 'P'
        print(f'{soma} é Par')
    else:
        tipo2 = 'I'
        print(f'{soma} é Impar')
        
    if tipo == tipo2:
        print('VOCE VENCEU!')
        break
    else:  
        print("VOCE PERDEU!  \nFIM DE JOGO")
