vel = int(input('Diga a velocidade do carro : '))
if vel > 80:
    print("-==-"*10)
    print("Multado, voce deve pagar {}reais".format((vel - 80)*7))
    print("-==-"*10)
else:
    print("-==-"*10)
    print('Tenha um bom dia. Dirija com cuidado'.upper())
    print("-==-"*10)