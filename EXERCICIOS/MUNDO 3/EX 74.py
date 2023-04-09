num = ((int(input('DIGITE O VALOR : '))),
       (int(input('DIGITE O VALOR : '))),
       (int(input('DIGITE O VALOR : '))),
       (int(input('DIGITE O VALOR : '))),
       (int(input('DIGITE O VALOR : '))))
print(f'VOCE DIGITOU {num}')
print(f'o numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o numero 3 apareceu na colocaçao {num.index(3)+1}')
else:
    print('O numero 3 nao foi listado')
for n in num:
    if n % 2 == 0:
        print(f'os numeros {n} sao pares')
