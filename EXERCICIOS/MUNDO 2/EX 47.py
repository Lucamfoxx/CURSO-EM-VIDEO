soma = 0
cont = 0
for c in range(2, 501, 2):
    if c % 3 == 0:
        cont+= 1
        soma+= c
        
print('De {} numeros a soma é {}'.format(cont,soma))


