from random import randint
c = 0
while True:
    resultado = ''
    vc = randint(1,10)
    print('-='*30)
    print('VAMOS JOGAR PAR OU IMPAR'); print('-='*30)
    p = str(input('Par ou Impar? [P/I] ')).upper()[0]
    v = int(input('Diga um valor: '))
    if (vc + v) % 2 == 0:
        resultado = 'P'
        palavra = 'PAR'
    else:
        resultado = 'I'
        palavra = 'IMPAR'
    if p in resultado:
        print('Você jogou {} e o computador {}. Total deu {} e deu {}'.format(v,vc,vc+v,palavra))
        print('Você VENCEU!')
        c += 1
    elif p not in resultado:
        print('Você jogou {} e o computador {}. Total deu {} e deu {}'.format(v,vc,vc+v,palavra))
        print('Você PERDEU!')
        print('-='*30)
        print('GAME OVER! Você venceu {} vezes.'.format(c))
        break