print('Aqui está a soma entre todos os números impares múltiplos de 3, de 1 a 500!')

soma = 0
i = 0
for c in range(1,500,2):
    if c%3 == 0:
        i = i+1
        soma = soma + c
print('a soma de todos os {} valores é {}'.format(i,soma))