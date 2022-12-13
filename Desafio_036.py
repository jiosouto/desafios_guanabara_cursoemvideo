valor = float(input('Qual o valor da casa: R$' ))
salário = float(input('Qual o seu salário: R$' ))
anos = int(input('Em quantos anos você vai pagar a casa: '))
prestacao = valor / (anos * 12)
excedente = salário * 30/100

print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}!'.format(valor,anos,prestacao))
if prestacao >= excedente:
    print('Seu empréstimo foi NEGADO!')
else:
    print('Seu empréstimo foi concedido!')