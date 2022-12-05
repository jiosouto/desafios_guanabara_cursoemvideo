a = float(input("Digite a altura de uma parede: "))
l = float(input("Digite a largura de uma parede: "))
ar = l * a
litro = ar / 2
print("Sabendo que a sua parede tem {}m de altura, e {}m de largura, a área da sua parede é de {}m².".format(a,l,ar))
print("Para poder pintar a parede será necessário {} litros de tinta.".format(litro))