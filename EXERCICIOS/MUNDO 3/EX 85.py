par = []
impar =[]
for n in range(1, 8):
    num = int(input(f'{n}º DIGITE UM VALOR : '))
    if num == 0:
        break
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'lista de imaperes digitados : {impar}')
print(f'lista de pares digitados : {par}')
