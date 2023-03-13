tot18 = totm = totf = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totm += 1
    if sexo == 'F' and idade <20:
        totf += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('QUER CONTINUAR? ')).strip().upper()[0]
    if resp == 'N':
        break
    
print(f"TOTAL DE HOMENS: {totm} \nTOTAL DE MAIORES DE 18: {tot18}\nTOTAL DE MULHERES COM 20+: {totm}")
print('ACABOU')
