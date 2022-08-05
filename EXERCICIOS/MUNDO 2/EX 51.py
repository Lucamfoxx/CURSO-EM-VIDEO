num = int(input('Digite o primeiro termo : '))
num2 = int(input('Digite a razão : '))
deci = num + (10 - 1) * num2
for c in range(num , deci, num2):
    print(c)
