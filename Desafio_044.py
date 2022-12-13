preco = float(input('Qual o preco do produto? R$ '))
escolha = str(input("""Formas de Pagamento:
[ 1 ] À vista no dinheiro/cheque.
[ 2 ] À vista no cartão.
[ 3 ] Em até 2x no cartão.
[ 4 ] 3x ou mais no Cartão.\nQual forma você escolhe? """)).strip()

desc10 = preco - (preco * (10 / 100))
desc5 = preco - (preco * (5 / 100))
juros = preco + (preco * (20 / 100))

if escolha == '1':
    print('Você ganhou 10% de desconto, pague R$ {:.2f}!'.format(desc10))
elif escolha == '2':
    print('Você ganhou 5% de desconto, pague R$ {:.2f}!'.format(desc5))
elif escolha == '3':
    print('Sua compra será parcelada em 2x, ou seja R$ {:.2f}!'.format(preco/2))
    print('O preco permanece o mesmo. R$ {:.2f}!'.format(preco))
elif escolha == '4':
    print('Sua compra será de R$ {:.2f}!'.format(juros))
    parcela = int(input('Em quantas parcelas? '))
    preco2 = juros / parcela
    print('Como você parcelou a compra em {} vezes! \nO valor parcelado será de R$ {:.2f}!'.format(parcela,preco2))
else:
    print('Opção inválida. Tente Novamente.')