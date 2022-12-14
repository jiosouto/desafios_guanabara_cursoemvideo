n = int(input('Digite um numero para calcular seu fatorial: '))
print('Calculando {}!= '.format(n), end='')
c = n
f = 1
for c in range (c,0,-1):
    print('{}'.format(c), end='')
    print(' x ' if c >1 else ' =', end='')
    f *= n
    n -= 1

print(' {} '.format(f))