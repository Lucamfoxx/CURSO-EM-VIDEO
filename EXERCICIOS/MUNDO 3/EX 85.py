lista1 = []

while True:
    lista1.append(str(input('NOME: ')))
    lista1.append(int(input('PESO: ')))
    resp = str(input('Continuar: '))
    if resp == "Nn":
        break
    print(lista1)