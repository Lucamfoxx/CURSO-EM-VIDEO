
sexo = str(input('Digite o sexo do bb : ')).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input('INVALIDO digite o sexo do bb : ')).strip().upper()[0]
if sexo ==("F"):
    print('O SEXO DO BB É FEMININO')
else :
    print('o sexo do bb é masculino')