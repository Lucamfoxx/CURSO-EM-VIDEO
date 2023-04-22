lista1 = []
temp = []
mai = men = 0
while True:
    temp.append(str(input('NOME: ')))
    temp.append(int(input('PESO: ')))
    if len(lista1) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    lista1.append(temp[:])
    temp.clear()
    resp = input('Continuar? [S/N]: ').strip().lower()
    if resp == "n":
        break
print(f'DADOS: {lista1}')
print(f'O NÚMERO DE PESSOAS CADASTRADAS É: {len(lista1)}')
print(f'O maior peso foi : {mai}')
print(f'O menor peso foi : {men}')
for p in lista1:
    if p[1] == mai:
        print(f'A pessoa com maior peso : {p[0]}')
print(f'')
for p in lista1:
    if p[1] == men:
        print(f'A pessoa com menor peso : {p[0]}')