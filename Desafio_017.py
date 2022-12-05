import math

co = float(input("Qual o cateto oposto: "))
ca = float(input("Qual o cateto adjacente: "))
hi = math.hypot(co, ca)
print("A hipotenusa do triângulo retângulo tem {:.2f} de comprimento.".format(hi))