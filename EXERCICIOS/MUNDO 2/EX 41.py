from datetime import date
from tkinter import E
ano = int(input('Digite o ano de nascimento:'))
atual = date.today().year

if atual - ano <= 9:
    print('\033[0;31mMIRIM\033[m')
elif atual - ano > 9 and atual - ano <=14:
    print('\033[0;32mINFANTIL\033[m')
elif atual - ano > 14 and atual - ano <=19:
    print('\033[0;33mJUNIOR\033[m')
elif atual - ano > 19 and atual - ano <=20:
    print('\033[0;34mSÊNIOR\033[m')
else:
    print('\033[7mMASTER\033[m') 