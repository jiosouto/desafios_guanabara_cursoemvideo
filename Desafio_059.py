a = float(input('Diga o 1° número: '))
b = float(input('Diga o 2° número: '))
o = False
p = [1,2,3,4,5]
while o != True:
    b = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair'))
    if b == 1:
        print('{} + {} = {}'.format(a,b,a+b))
    elif b == 2:
        print('{} x {} = {}'.format(a,b,a*b))
    elif b == 3:
        if a > b:
            print('O maior é {}'.format(a))
        else:
            print('O maior é {}'.format(b))
    elif b == 4:
        a = float(input('Diga o 1° número: '))
        b = float(input('Diga o 2° número: '))
    elif b == 5:
        o = True
    elif not b in p:
        print('Você digitou a opção errada. Tente novamente.')