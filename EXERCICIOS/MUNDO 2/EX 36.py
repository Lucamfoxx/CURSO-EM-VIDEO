casa = float(input('Qual o valor da casa R$ '))
salario = float(input('Qual o valor do seu salario mensal R$ '))
anos = float(input('vai pagar em quantos anos? '))

if (salario * 30)/100 > casa/(anos * 12):
    print('A prestação vale R${:.2f}'.format((casa/anos)/12))
else:
    print('o valor da prestação é superior a 30% do seu salario') 