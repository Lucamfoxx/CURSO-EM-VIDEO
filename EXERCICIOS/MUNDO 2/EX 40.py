n1 = float(input("digite a primeira nota: "))
n2 = float(input('digite a segunda nota: '))

if (n1 + n2)/2 >=7:
    print('\033[0;32m APROVADO\033[m')
elif (n1 + n2)/2 <5:
    print('\033[0;31m REPROVADO \033[m')
else:
    print("\033[7mRECUPERAÇÃO\033[m")