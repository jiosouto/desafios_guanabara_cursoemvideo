import math
salário = float(input("Qual o salário do funcionário? R$ "))

if salário <= 1250:
    aumento = salário + (salário * 15/100)
else:
    aumento = salário + (salário * 10/100)
print("O salário que antes era de R$ {:.2f} ganhou um aumento, se tornando R$ {:.2f}!".format(salário,aumento))