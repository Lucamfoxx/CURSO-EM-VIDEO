num = int(input('DIGITE O VALOR A RETIRAR :'))
resto50 = num % 50
resto20 = resto50 % 20
resto10 = resto20 % 10
resto05 = resto10 % 5
resto01 = resto05 % 1
cel50 = 0
cel20 = 0
cel10 = 0
cel05 = 0
cel01 = 0
if num % 50 == 0:
    cel50 = int(num / 50)
else:
    cel50 = int(num / 50)
    cel20 = int(resto50 / 20)
    cel10 = int(resto20 / 10)
    cel05 = int(resto10 / 5)
    cel01 = int(resto05 / 1)
print(f'São {cel01} celulas de 1')
print(f'Sao {cel05} celulas de 5')
print(f'São {cel10} celulas de 10')
print(f'São {cel20} celulas de 20')
print(f'São {cel50} celulas de 50')
print('obrigado')
