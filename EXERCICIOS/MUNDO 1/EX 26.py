nome = str(input('Digite um nome: ')).upper().strip()
print('A letra A aparece {}'.format(nome.count('A')))
print('a primeira letra a aparece na posicao {}'.format(nome.find('A')+1))
print('a ultima letra a aparece na posicao {}'.format(nome.rfind('A')+1))