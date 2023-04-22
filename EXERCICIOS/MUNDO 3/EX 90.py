aluno = {}
aluno['Nome'] = str(input('Nome do aluno : '))
aluno['Media'] = float(input(f'Media do {aluno["Nome"].strip().title()} = '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 5 < aluno['Media'] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
print('-='* 30)
for c, k in aluno.items():
    print(f'{c} = {k}')