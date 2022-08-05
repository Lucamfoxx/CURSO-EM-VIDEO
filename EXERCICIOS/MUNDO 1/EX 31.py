km = int(input('Qual a distancia da viagem em km:'))
if km >= 201:
    print("-==-"*10)
    print('A viagem custará R$:{}'.format(km * 9/20))
    print("-==-"*10)
else:
    print("-==-"*10)
    print('A viagem custará R$:{}'.format(km * 1/2))
    print("-==-"*10)