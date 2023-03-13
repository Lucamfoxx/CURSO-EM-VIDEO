num = quant = soma = 0
while True:
    num = int(input('DIGITE UM NUMERO: [PARA PARAR DIGITE 999 ]'))
    if num == 999:
        break
    quant += 1
    soma += num
print(f'FIM DO PROGRAMA. Voce digitou {quant} numeros e a soma é {soma}')
