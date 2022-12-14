num = int(input('Quer ver a tabuada de qual valor? '))
print('-' * 20)
while num >= 0:
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(num, c, num*c))
        if c >=12:
            break
    print('-' * 20)
    num = int(input('Quer ver a tabuada de qual valor? '))
print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')