 
r1 = int(input('Digite o primeiro segmento: '))
r2 = int(input('Digite o segundo segmento: '))
r3 = int(input('Digite o terceiro segmento: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print("-==-"*10)
    print('Os segmentos formam um triangulo')
    print("-==-"*10)
else:
    print("-==-"*10)
    print("Os segmentos\033[1;31m não\033[m formam um triangulo")
    print("-==-"*10)

 