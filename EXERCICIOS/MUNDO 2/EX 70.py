barato = total = caro = cont = menor = 0
while True:
    produto = str(input('QUAL NO NOME DO PRODUTO: '))
    preco = int(input('QUAL O PREÇO ? '))
    cont += 1
    total += preco
    if preco >1000:
        caro += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in "SN":
        resp = str(input('QUER CONTINUAR ? ')).strip().upper()[0]
    if resp == 'N':
        break    

print(f'TOTAL R$ {total}\nO PRODUTO MAIS BARATO: {barato}\nO VALOR DE R${menor}')
