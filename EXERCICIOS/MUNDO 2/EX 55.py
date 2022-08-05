soma = 0
media = 0
maior = 0
maiorh = 0
nomevelho = ''
for p in range(1, 5):
    print('----- {}º Pessoa -----'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M / F]: '))
    soma += idade
    if p == 1 and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorh:
        maiorh = idade
        nomevelho = nome        
media += soma/4

print('A MEDIA DE IDADE É {}.'.format(media))
print('O nome do homem mais velho é {} e a idade é {}'.format(nomevelho, maiorh))
DFG
