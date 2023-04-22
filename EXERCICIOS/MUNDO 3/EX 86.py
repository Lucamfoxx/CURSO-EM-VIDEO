lista = [[], []]
for n in range(1, 8):
    num = int(input(f'{n}º DIGITE UM VALOR : '))
    if num == 0:
        break
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'lista de imaperes digitados : {lista[1]}')
print(f'lista de pares digitados : {lista[0]}')
