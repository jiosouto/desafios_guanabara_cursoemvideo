cont = 0
x = int(input('Digite um número inteiro: '))
print('O numero {} é divisivel pelos numeros:' .format(x))
for c in range(1, x + 1):
    if x % c == 0:
        cont += 1
        print(' ',c,end=' ')
print('\nO numero {} foi divido {} vezes'.format(x, cont))
if cont == 2:
    print('É um número primo')
else:
    print('Não é número primo')