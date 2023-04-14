lista1 = []
while True:
    lista2 = []
    lista2.append(str(input('NOME: ')))
    lista2.append(int(input('PESO: ')))
    lista1.append(lista2[:])
    lista2.clear()
    resp = input('Continuar? [S/N]: ').strip().lower()
    if resp == "n":
        break
print(f'DADOS: {lista1}')
print(f'O NÚMERO DE PESSOAS CADASTRADAS É: {len(lista1)}')
