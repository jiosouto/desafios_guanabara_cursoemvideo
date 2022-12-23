def escreva(txt):
    txt2 = (f'{" ":>2}{txt}')
    num = len(txt2)+2
    print('~'*num)
    print(txt2)
    print('~' * num)


escreva('Olá, mundo')
escreva('CACHORRO GRANDÃO')