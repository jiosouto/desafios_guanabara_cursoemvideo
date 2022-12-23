from time import sleep

def maiorr(*num):
    print('~' * 40)
    print('Analisando os valores passados...')
    for mm in num:
        if len(num) == 1:
            if mm == 0:
                for a in num:
                    if a == 0:
                        print(f'Foram informados 0 valores ao todo.\nO maior valor informado foi 0')
            if mm > 0:
                maior = 0
                if mm == 0:
                    maior = mm
                else:
                    if mm > maior:
                        maior = mm
                print(f'Foram informados {len(num)} valores ao todo.\nO maior valor informado foi {maior}')
    if len(num) > 1:
        for m in num:
            if m > 0:
                print(m, end=' ')
                maior = 0
                if m == 0:
                    maior = m
                else:
                    if m > maior:
                        maior = m
                sleep(0.5)
        print(f'Foram informados {len(num)} valores ao todo.\nO maior valor informado foi {maior}')


maiorr(1,2,3,4,5)
maiorr(1,2,3,4)
maiorr(4,7,0)
maiorr(6)
maiorr(0)