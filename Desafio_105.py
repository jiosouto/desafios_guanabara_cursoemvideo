def notas(*n,sit=0):
    """
    -> Função para anlisar notas e situações de varios alunos:
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adcional-lo a situação
    :return: retorna o dicionario preenchido com todas informaçõoes
    """
    dic = dict()
    acum = cont = maior = menor = 0
    for c in n:
        cont += 1
        acum += c
        media = acum/cont
        if cont == 1:
            maior = menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
    dic['Total'] = cont
    dic['Maior'] = maior
    dic['Menor'] = menor
    dic['Media'] = media
    if sit == True:
        if media >= 7:
            dic['Situação'] = 'Boa'
        elif 5 <= media < 7:
            dic['Situação'] = 'Razoavel'
        elif media < 5:
            dic['Situação'] = 'Ruim'
    return dic
resp = notas(5,10,7,4,8,11,sit=True)
print(resp)
help(notas)