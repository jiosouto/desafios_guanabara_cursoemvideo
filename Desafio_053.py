frs = str(input('Digite uma frase: ')).strip().replace(' ','').upper()
rev = ('')
for l in range(len(frs),0,-1):
    rev += frs[l-1]
print('O inverso de {} e {}'.format(frs, rev))
if frs == rev:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')