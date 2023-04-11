lista = []
cont = 0 
while True:
    num = int(input('digite um numero: '))
    if num == 0:
        break
    cont += 1
    lista.append(num)
print(f'voce digitou {cont} numeros.')
print(f'o maior numero foi {max(lista) }')
print(f'o menor numero foi {min(lista) }')
print(lista)