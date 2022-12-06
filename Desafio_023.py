num = int(input("Digite um número entre 0 e 9999: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("A unidade de milhar é: {}".format(m))
print("A centena é: {}".format(c))
print("A dezena é: {}".format(d))
print("A unidade é: {}".format(u))