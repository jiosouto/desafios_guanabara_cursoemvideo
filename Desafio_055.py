l = []
for i in range(1,6):
    n = float(input('Peso da {}º pessoa: '.format(i)))
    l.append(n)

print('O maior peso lido foi de {} quilogramas'.format(max(l)))
print('O menor peso lido foi de {} quilogramas'.format(min(l)))