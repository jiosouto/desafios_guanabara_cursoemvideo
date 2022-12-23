import math

def fatorial(n,show):
    """
    -> Calcular o Fatorial de um numero
    :param n: O numero a ser calculado
    :param show: (opcional) Mostrar oou não a conta
    :return: o valor do fatorial de um numero n.
    """
    if show == True:
        for c in range(n,0,-1):
            print(c,end=' x ' if c > 1 else ' = ')
    fat = math.factorial(n)
    return fat

num = int(input('Digite um numero: '))
resp = str(input('Quer ver a conta do resultado: [S/N] ')).upper()[0]
if resp in "SN":
    if resp == "S":
        print(fatorial(num,show=True))
    elif resp == "N":
        print(fatorial(num, show=False))
print('-'*40)
help(fatorial)