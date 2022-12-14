res = cont = tot = 0
while res != 999:
    comando = int(input('Digite 999 para finalizar: '))
    cont += 1
    if comando != 999:
        tot += comando
    if comando == 999:
        res = 999
print('Você digitou {} numeros, e a soma entre eles é {}'.format(cont - 1, tot))