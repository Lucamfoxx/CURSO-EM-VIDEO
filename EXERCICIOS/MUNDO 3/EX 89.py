nomes = [[], []]
while True:
    nome = str(input('NOME: '))
    nomes[0].append(nome)
    nota1 = float(input('NOTA 1 : '))
    nota2 = float(input('NOTA 2 : '))
    media = nota1 + nota2 / 2
    nomes[1].append(media)
    resp = str(input('quer continuar: '))
    if resp in 'Nn':
        break
print(f'{nomes}')
for i in range(len(nomes[0])):
    print(f'{nomes[0][i]}=-=-==-=-=-=-=-=-=-=--={nomes[1][i]}')