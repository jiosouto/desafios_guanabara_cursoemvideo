nome = str(input("Qual o seu nome completo? ")).strip()
print("Seu nome é :", nome.upper())
print("Seu nome é:", nome.lower())
nomedividido = nome.split()
print("Seu nome tem", len("".join(nomedividido)), "letras ao todo.")
print("O seu primeiro nome é {} e ele tem {} letras.".format(nomedividido[0],len(nomedividido[0])))

"""Outra forma de fazer:
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))"""