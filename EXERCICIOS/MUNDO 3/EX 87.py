matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0 
max = []
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'DIGITE UM VALOR PARA A MATRIZ {[l], [c]} : '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        
    print()
max.append([matriz[p][1] for p in range(3)])
sorted(max)
maxx = max[-1]
print(f'a soma dos pares é : {par}')
print(f'{sum([matriz[i][2] for i in range(3)])}')
print(f'{maxx}')
