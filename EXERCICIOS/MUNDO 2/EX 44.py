print(' Lojas Magão ')
preço = float(input('Qual do valor da compra R$ '))
escolha = int(input('''
[0] À vista cheque/dinheiro
[1] À vista cartão
[2] 2x no cartão
[3] 3x ou mais no cartão
:--> '''))

if escolha == 3:
    dividido = int(input('quantas vezes ? '))
    parcela = ((preço + (preço*20)/100) / dividido)
    print("=.="*10)
    print('O valor em {}x  tem 20% de juros'.format(dividido))
    print('O valor a parcela ficara R${} e o valor total será R${}'.format(parcela , preço + ((preço * 20)/100)))
    print("=.="*10)
if escolha == 0:
    print('=.='*10)
    print(' O valor a vista tem 10% de desconto!')
    print(' O valor com desconto vale {}'.format(preço - (preço * 10)/100))
    print('=.='*10)
elif escolha == 1:
    print('=.='*10)
    print(' O valor a no cartão tem 5% de desconto!')
    print(' O valor com desconto vale {}'.format(preço - (preço * 5)/100))
    print('=.='*10)
elif escolha == 2:
    print('=.='*10)
    print(' O valor em 2x no cartão R$ {}'.format(preço))
    print('=.='*10)
else:
    print('\033[1;31m Opção errada!\033[m')
