num = int(input('Digite umn numero : '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[31m', end=' ')
        tot+= 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')    
print('\033[m \n O {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print("-==-"*10)
    print('\033[032mNUMERO PRIMO!\033[m ')
    print("-==-"*10)
else:
    print("-==-"*10)
    print('\033[031mNÃO É PRIMO!\033[m')
    print("-==-"*10)
