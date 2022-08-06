n1 = int(input('Digite o primeiro valor :'))
n2 = int(input('Digite o segundo valor :'))
opcao = 0
while opcao != 5:
    print('''    [ 1 ]SOMAR
    [ 2 ]MAIOR
    [ 3 ]MULTIPLICAR
    [ 4 ]NOVOS NUMEROS 
    [ 5 ]SAIR DO PROGRAMA''')
    opcao = int(input('>>>>>>>>>> qual sua escolha? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma vale: {} '.format(soma))
    elif opcao == 2:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('o maior entre os dois numeros é {}'.format(maior))
    elif opcao == 3:
        multiplicacao = n1 * n2
        print('A multiplicacao vale {}'.format(multiplicacao))
    elif opcao == 4:
        print('Informe novos numeros!')
        n1 = int(input('Digite o primeiro valor :'))
        n2 = int(input('Digite o segundo valor :'))
    elif opcao == 5:
        print('FINALIZNADO ....')
    else:
        print('opcao invalida')

    
