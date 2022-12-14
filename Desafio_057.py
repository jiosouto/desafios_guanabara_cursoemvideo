n = 1
sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
if sexo == 'M' or sexo == 'F':
    print('Sexo {} registrado com sucesso'.format(sexo))
    exit()
while n != 'M' and n != 'F':
    n = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()
print('Sexo {} registrado com sucesso'.format(n))