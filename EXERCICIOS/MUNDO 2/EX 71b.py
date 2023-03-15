cont = ('zero','um', 'dois', 'três','quatro' ,'cinco' ,'seis' ,'sete' ,'oito' ,'nove' ,'dez' ,'onze' ,'doze' ,'treze' ,'quatorze' ,'quinze' ,'dezesseis' ,'dezesete' ,'dezoito' ,'dezenove' ,'vinte')
while True:
    num = int(input('digite um numero: '))
    if 0 <= num <= 20:
        break
print(f'Voce Digitou {cont[num]}')