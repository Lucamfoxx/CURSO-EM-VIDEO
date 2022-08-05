from datetime import date

ano = int(input('que ano voce nasceu : '))
atual = date.today().year
idade = atual - ano 


if idade <= 17:
    print("ainda faltam {} ano/s pra voce se alistar".format(17 - idade))
elif idade == 18:
    print('voce deve se aliastar agora')
else:
    print("voce deveria ter se alistado a {} ano/s".format(idade-17))

    