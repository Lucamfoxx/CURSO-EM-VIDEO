
def metade(moeda=0):
    metade = moeda/2
    return metade


def aumento(moeda=0, taxa=0):
    aumento = moeda + (moeda * taxa/100)
    return aumento


def dobro(moeda=0):
    dobro = moeda * 2
    return dobro

def diminuir(moeda=0, taxa=0):
    diminuir = moeda - (moeda * taxa/100)
    return diminuir

def sifrao(moeda,sifrao='R$'):
    return f'{sifrao}{moeda:>.2f}'.replace('.', ',')

def resumo(moeda=0, ):
    print('~'*45)
    print('RESULTADO'.center(45))
    print('~'*45)
    print(f'A metade da moeda vale:\t{sifrao(metade(moeda))}')
    print(f'O dobro da moeda vale:\t{sifrao(dobro(moeda))}')
    print(f'Com o aumento de 10%:\t{sifrao(aumento(moeda, 10))}')
    print(f'Com o desconto de 10%:\t{sifrao(diminuir(moeda, 10 ))}'.center(30))
    print('~'*45)