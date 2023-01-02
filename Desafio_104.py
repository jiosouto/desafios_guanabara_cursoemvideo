def leiaInt(txt):
    x = ''
    while not x.isnumeric():
        x = str(input(txt))
        if not x.isnumeric():
            print('\033[31mERRO! Digite um numero inteiro valido\033[m')
    return x


n = leiaInt("Digite um numero: ")
print(f'Você acabu de digitar um numero {n}')