preço = float(input("Preço de um produto: R$ "))
desc = preço - (preço * 5 / 100)
print("Esse produto de R$ {:.2f} agora está com 5% de desconto, sendo assim ele agora vale R${:.2f}.".format(preço,desc))