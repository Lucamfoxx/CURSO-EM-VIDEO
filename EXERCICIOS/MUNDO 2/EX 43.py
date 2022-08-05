h = float(input('ALTURA (m): '))
p = float(input('PESO (kg): '))
imc = p/(h**2)
if imc < 18.5:
    print('abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('peso ideal')
elif imc > 25 and imc < 30:
    print('sobre peso')
elif imc > 30 and imc < 40:
    print('obesidade')
else:
    print('obesidade morbida')