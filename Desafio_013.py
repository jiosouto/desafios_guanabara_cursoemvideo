sa = float(input("Qual o salário de um funcionário? R$ "))
aum = float(input("Qual o aumento em % desse salário? "))
novo = sa - (sa * aum / 100)
print("O novo salário deste funcionário que era de R${:.2f}, agora com {:.0f}% de aumento é R${:.2f}.".format(sa,aum,novo))