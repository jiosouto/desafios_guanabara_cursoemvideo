from random import randint
from time import sleep


def sorte(li):
    print("sorteado os 5 valores da lista...")
    sleep(0.3)
    for i in range(1, 6):
        a = randint(1, 10)
        print(f"{a}", end=" ")
        li.append(a)
        sleep(0.6)
    print("PRONTO!")


def somapar(li):
    s = 0
    for j in li:
        if j % 2 == 0:
            s += j
    print(f"somando todos os valores pares de {li}, temos {s}")


lis = []
sorte(lis)
somapar(lis)