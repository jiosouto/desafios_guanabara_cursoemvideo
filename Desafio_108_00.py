def metade(valor=0):
    resultado = valor / 2
    return resultado

def dobro(valor=0):
    resultado = valor * 2
    return resultado

def aumentar(valor=0, porcento=10):
    temp = valor * porcento
    valor += temp / 100
    return valor

def dininuir(valor=0, porcento=10):
    temp = valor * porcento
    valor -= temp / 100
    return valor


# def Desafio_108_00(p):
#     return f'R${p:5.2f}'

def Desafio_108_00(p):
    p = f'R${p:5.2f}'
    p = p.replace('.',',')
    return p

# #forma guanabara.
# def Desafio_108_00(preço=0, Desafio_108_00='R$'):
#     return f'{Desafio_108_00}{preço:>8.2f}'.replace('.',',')