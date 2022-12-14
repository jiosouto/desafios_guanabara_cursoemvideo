import random, time
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
nrandom = int(random.randint(0, 10))
c = t = 0
while c == 0:
    n = int(input('Digite um número: '))
    print('Processando...')
    time.sleep(1)
    if nrandom == n:
        print('Parabéns! Você conseguiu adivinhar com {} tentativas!'.format(t + 1))
        exit()
    else:
        print('Você não acertou o número!\nTenta de novo! ')
        c = 0
        t += 1

'''''
from random import randint
chute = int(input('Pensei em um número de 0 a 10, tente adivinhar: '))
aleatorio = randint(0,10)
contador = 0
while chute != aleatorio:
    contador += 2
    if chute < aleatorio:
        chute = int(input('Chutou para baixo!\nTente novamente: '))
    if chute > aleatorio:
        chute = int(input('Chutou para cima!\nTente novamente: '))
if contador == 0:
    print('\33[31mParabens! Você acertou na {}° tentativa!'.format(contador+1))
else:
    print('\33[31mParabens! Você acertou na {}° tentativa!'.format(contador))'''''