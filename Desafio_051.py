p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
for c in range(1, 11):
     print(p + (c - 1) * r, end=' ')
print()
print('O primeiro termo dessa P.A é {}'.format(p))
print('A razão dessa P.A é {}'.format(r))