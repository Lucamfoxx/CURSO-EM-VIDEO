salario = float(input('Qual é o seu salario:'))

if salario > 1250:
    print('o salario com aumento ficará: R${:.2f} '.format(salario + (salario * 10)/100))
else:
    print('o salario com o aumeneto ficará R${:.2f} '.format(salario + (salario * 15)/100))