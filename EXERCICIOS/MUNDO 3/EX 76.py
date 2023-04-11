palavras = ('guilherme', 'joao', 'kelvin', 'pedro','matchones','flavio','augusto')
for p in palavras:
    print(f'\na palavra {p.upper()} tem ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra , end=' ')

