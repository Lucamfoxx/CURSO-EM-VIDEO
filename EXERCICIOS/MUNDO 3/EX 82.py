lista = []
impar = []
par = []
while True:
    num = int(input('Digite um valor : '))
    if num == 0:
        break
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'{lista}')
print(f'{par}')
print(f'{impar}')

