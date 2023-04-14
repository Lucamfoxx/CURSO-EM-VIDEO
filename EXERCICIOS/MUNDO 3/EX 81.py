lista = []
cont = 0
while True:
    num = int(input('Digite um valor para a lista(Digite 0 para terminar):'))
    if num == 0:
        break
    else:
        lista.append(num)
        cont +=1
if 5 in lista:
    print('O numero 5 foi ultilizado.')
else:
    print('O 5 não foi ultilizado.')
lista.sort()
lista.reverse()
print(f'A lista decrescente é {lista}.')