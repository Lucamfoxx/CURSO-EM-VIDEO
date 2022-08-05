import math 
angulo = float(input("digite um angulo:"))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print("o angulo de {} tem o SENO  de {:.2f}".format(angulo, seno))
print("o angulo de {} tem o cos de {:.2f}".format(angulo, cos))
print("o angulo de {} tem a tangente de {:.2f}".format(angulo, tang))
