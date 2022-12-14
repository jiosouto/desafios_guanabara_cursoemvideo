lista = []
opção = ""
contador = 0
while opção in "Ss":
    numero = float(input("Digite os valores: "))
    lista.append(numero)
    opção = input("Deseja continuar a digitar os valores S/N: ").upper().strip()[0]
    contador +=1
print("Você digitou {} numeros A Media de todos os valores foi {:.2f} ".format(contador , sum(lista)/contador))
print(f"O maior valor lido da lista foi {max(lista):.0f} e o menor foi {min(lista):.0f}")