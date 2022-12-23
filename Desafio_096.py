lista = []
def linha(txt):
    print('-' * 30)
    print(f'\033[31m{txt:^28}\033[m')
    print('-'*30)


linha('CONTROLE DE TERRENOS')

def conta(a,b):
    s = a * b
    print(f'A area do terreno {a}x{b} é de {s}m². ')

largura = float(input('Largura (m): '))
lista.append(largura)
comprimento = float(input('Comrpimento (m): '))
lista.append(comprimento)
conta(lista[0], lista[1])

linha('FIM')