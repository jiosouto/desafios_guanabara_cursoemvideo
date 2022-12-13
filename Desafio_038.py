n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print('O número {} é maior que {}.'.format(n1,n2))
elif n2 > n1:
    print('O número {} é maior que {}.'.format(n2,n1))
else:
    print('Os números {} e {} são iguais.'.format(n1,n2))