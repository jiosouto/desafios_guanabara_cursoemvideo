def aumentar(preço=float(0), taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=float(0), taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=float(0), formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=float(0), formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=float(0), moeda='R$'):
    return f'{moeda} {preço:>.2f}'.replace('.', ',')


def resumo(preço=float(0), taxa1=0, taxa2=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'Dobro do Preço: \t{dobro(preço,True)}')
    print(f'Metade do Preço: \t{metade(preço,True)}')
    print(f'{taxa1}% de Aumento: \t{aumentar(preço, taxa=taxa1,formato=True)}')
    print(f'{taxa2}% de Redução: \t{diminuir(preço, taxa=taxa2,formato=True)}')
    print('-' * 30)