lista = list()
for index in range(1, 8):
    lista.append(int(input(f"Digite o {index}º número: ")))
lista.sort()
print("Os valores pares são", end=" ")
for c in lista:
    if c % 2 == 0:
        print(f"→ {c}", end=" ")
print("\nOs valores impares são ", end=" ")
for x in lista:
    if x % 2 > 0:
        print(f"→ {x}", end=" ")