print('GERADOR DE PA')
print('-='* 10)
primeiro = int(input('primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} => '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')