conta = input('digite uma conta com parenteses para checar: ')

lista = []

for letra in conta:
    if letra == '(':
        lista.append(letra)
    elif letra ==')':
        if len(lista) > 0:
            lista.pop()
        else:
            print('falta parenteses abrindo!')
            break
if len(lista) == 0:
    print('A CONTA ESTA CORRETA!')
else:
    print('falta fechar parenteses')