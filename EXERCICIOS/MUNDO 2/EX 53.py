frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() 
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('==*'*10)
    print('{}  |  {}'.format(frase, inverso))
    print('PALINDROMO')
    print('==*'*10)

else:
    print('==*'*10)
    print('{}  |  {}'.format(frase, inverso))
    print( 'A frase digitada não é um palindromo! ')
    print('==*'*10)
