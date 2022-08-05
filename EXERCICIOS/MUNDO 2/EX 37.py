n1 = int(input('digite um numero: '))
print('''escolha as seguintes ordens: 
[ 1 ] binario
[ 2 ] octal 
[ 3 ] hexadecimal''')
opçao =  int(input('qual sua escolha: '))
if opçao == 1:
    print('{} convertidos em binario \033[32m{}\033[m'.format(n1, bin(n1).upper()))
elif opçao == 2:
    print('{} convertidos em octal \033[33m{}\033[m'.format(n1, oct(n1)))
else:
    print('{} convertidos em hexadecimal \033[34m{}\033[m'.format(n1, hex(n1)))
