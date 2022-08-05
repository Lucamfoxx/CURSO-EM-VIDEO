from datetime import date
n1 = int(input('coloque um ano: '))
if n1 == 0:
    n1 = date.today().year
if n1 % 2 == 0 and n1 % 100 != 0 and n1 % 400 == 0:
    print("-==-"*10)
    print('O ano {} é bissexto'.format(n1).upper())
    print("-==-"*10)
else:
    print("-==-"*10)
    print('o ano {} não é bissexto '.format(n1).upper())
    print("-==-"*10)