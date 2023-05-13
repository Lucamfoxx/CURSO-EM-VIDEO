from datetime import date 
def voto(*idade):
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos. Não vota'
    elif idade > 65 or 16 < idade <18:
        return f'Com {idade} anos. Voto opcional'
    else: 
        return f'Com {idade} anos. Vota'
ano = int(input('ANO DE NASCIMENTO: '))
print(voto(ano))