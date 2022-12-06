num = int(input("Digite um número: "))
r = num % 2
if r == 0:
    print("O número {} é par!".format(num))
else:
    print("O número {} é ímpar!".format(num))