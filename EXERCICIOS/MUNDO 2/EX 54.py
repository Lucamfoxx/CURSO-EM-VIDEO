from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Digite o ano que voce nasceu {}: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior+= 1
    else:
        totmenor+= 1
print('{} PESSOAS SAO MAIORES DE IDADE!'.format(totmaior))
print('{} PESSOAS SAO MENORES DE IDADE!'.format(totmenor))
