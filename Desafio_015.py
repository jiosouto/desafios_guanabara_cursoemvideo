dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos quilômetros você rodou com o carro? "))
preço = dias * 60 + km * 0.15
print("Como esse carro foi usado por {} dias, e rodou {} quilômetros, o total a pagar é de R$ {:.2f}.".format(dias,km,preço))