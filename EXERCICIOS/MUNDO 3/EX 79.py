lista = []
cont = 0
while True:
    num = int(input('DIGITE UM VALOR PARA A LISTA:'))
    if num == 0:
        break
    if num in lista:
        print('ja foi adcionado anteriomente')
        continue
    lista.append(num)
    cont += 1
    
    
print(f'A LISTA EM ORDEM FICA {sorted(lista)}')