from datetime import datetime
atual = datetime.now().year
cadastro = {}
while True:
    cadastro['nome'] = str(input('Nome : '))
    cadastro['nasc'] = int(input('ano de nascimento : '))
    idade = atual - cadastro['nasc']
    resp = int(input('numero da carteira de trabalho : {0 nao tem. } : '))
    if resp == 0:
        break
    else:
        cadastro['CTPS'] = resp
        cadastro['ano'] = int(input('Ano da contratação : '))
        cadastro['SALARIO'] = int(input('Salario R$ '))
        apos = 35 - (atual - cadastro['ano'])
        print(f'{cadastro["nome"]} tem {idade} anos e vai se aposentar com {idade + apos}')
print(f'{cadastro["nome"].strip().title()} tem {idade} anos e nao tem carteira de trabalho!')