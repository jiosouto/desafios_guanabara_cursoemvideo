from random import randint
from time import sleep


print('-'*30)
print(f'{"JOGO MEGASENA":^30}')
print('-'*30)

jogo = []

qtd = int(input('Quantos jogos voce quer que eu sorteie? '))
print(f'====== SORTEANDO {qtd} JOGOS ======')

for c in range(0, qtd):
    for v in range(0,6):
        n = randint(1,60)
        if len(jogo) == 0:
            jogo.append(n)
        else:
            while jogo.count(n) >= 1:
                n = randint(1,60)
            jogo.append(n)
    print(f' Jogo {c+1}: {jogo}')
    sleep(1)
    jogo.clear()