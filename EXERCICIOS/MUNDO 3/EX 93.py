pessoas = []
cont = 0
while True:
    cadastro = {}
    cadastro['nome'] = str(input('NOME : '))
    cadastro['Idade'] = int(input('IDADE : '))
    cadastro['sexo'] = str(input('SEXO : ')).strip().upper()
    while cadastro['sexo'] not in "FM":
        print('erro use F ou M')
        cadastro['sexo'] = str(input('SEXO : ')).strip().upper()
    pessoas.append(cadastro)
    cont += 1
    resp = str(input('Desejar continuar : ')).strip().upper()
    while resp not in "SN":
        print('erro DIGITE S OU N')
        resp = str(input('Desejar continuar : ')).strip().upper()
    if resp == 'S':
        continue
    else:
        break
media = sum(p["Idade"] for p in pessoas) / len(pessoas)
print(f'ao todo temos {cont} pessoas cadastradas')
print(f'a media de idade {media}')
