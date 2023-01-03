def metade(valor=0,Desafio_109_00=False):
    if Desafio_109_00 == True:
        resultado = valor / 2
        p = f'R${resultado:5.2f}'
        p = p.replace('.', ',')
        return p
    else:
        resultado = valor / 2
        return resultado


def dobro(valor=0,Desafio_109_00=False):
    if Desafio_109_00 == True:
        resultado = valor * 2
        p = f'R${resultado:5.2f}'
        p = p.replace('.', ',')
        return p
    else:
        resultado = valor * 2
        return resultado


def aumentar(valor=0, porcento=10, Desafio_109_00=False):
    if Desafio_109_00 == True:
        temp = valor * porcento
        valor += temp / 100
        p = f'R${valor:5.2f}'
        p = p.replace('.',',')
        return p
    else:
        temp = valor * porcento
        valor += temp / 100
        return valor


def dininuir(valor=0, porcento=10, Desafio_109_00=False):
    if Desafio_109_00 == True:
        temp = valor * porcento
        valor -= temp / 100
        p = f'R${valor:5.2f}'
        p = p.replace('.', ',')
        return p
    else:
        temp = valor * porcento
        valor -= temp / 100
        return valor



def Desafio_109_00(p):
    p = f'R${p:5.2f}'
    p = p.replace('.', ',')
    return p
