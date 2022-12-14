total = mil = barato = contador = 0
print('='*40)
print('{: ^40}'.format('Loja Super Baratão'))
print('='*40)
while True:
    contador += 1
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    print('-'*40)
    total += preço
    if contador == 1:
        barato = preço
        nome = produto
    if preço < barato:
        barato = preço
        nome = produto
    if preço > 1000:
        mil += 1
    opção = str(input('Quer continuar? [S/N]: ')).upper()[0]
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if opção == 'N':
        break
print('{:-^40}'.format('Fim do Programa'))
print('O total da compra foi R$ {:.2f}'.format(total))
print('Temos {} produtos custando mais de R$1.000,00'.format(mil))
print('O produto mais barato foi {} que custa R$ {:.2f}'.format(nome,barato))