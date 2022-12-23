li = []
di = dict()
while True:
    di["nome"] = input("digite o seu nome:")
    while True:
        di["sexo"] = input("sexo [M/F]: ").upper().strip()[0]
        if di["sexo"] == "M" or di["sexo"] == "F":
            break
        else:
            print("ERRO, porfavor responda só M ou F")
    di["idade"] = int(input("digite sua idade: "))
    li.append(di.copy())
    while True:
        r = input("quer continuar? [S/N]: ").lower().strip()[0]
        if r == "s" or r == "n":
            break
        else:
            print("ERRO, responda apenas com S ou N")
    if r == "n":
        break
print(f"A) ao todo temos {len(li)} pessoas cadastradas")
soma = 0
mu = []
for i in li:
    soma += i["idade"]
    if i["sexo"] == "F":
        mu.append(i["nome"])
media = soma / len(li)
print(f"B) a média de idade é de {media:.1f} anos")
print(f"C) as mulheres cadastradas foram {mu}")
print(f"lista de pessoas que estão acima da média")
c = 0
for i in li:
    for k, v in i.items():
        if i["idade"] > media:
            print(f"{k} = {v};", end=" ")
            c += 1
            if c % 3 == 0:
                print()
print("FIM")