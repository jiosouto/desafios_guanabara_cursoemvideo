lista=[]
dic={}

while True:
    nome=input('Digite o nome: ')
    if nome=='':
        break
    dic['nome:']=nome
    media=float(input('Digite a média: '))
    dic['média:']=media

    if media>=7:
        dic['situação:']='Aprovado'
    if media<4:
        dic['situação:']='Reprovado'
    if 4<=media<7:
        dic['situação:']='Em recuperação'
    lista.append(dic.copy())
print('-='*30)
print('{:^60}'.format('ANÁLISE'))
print('-='*30)
for cont in lista:
    print(f'Nome: {cont["nome:"]} - Média: {cont["média:"]} - Situação: {cont["situação:"]}')