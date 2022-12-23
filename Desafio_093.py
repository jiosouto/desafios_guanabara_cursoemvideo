di = {"jogador": input("nome do jogador: ")}
part = int(input(f"quantas partidas {di['jogador']} jogou? "))
total = 0
di['gols'] = []
for i in range(1, part + 1):
    di["gols"].append(int(input(f"quantos gols na {i}° partida? ")))
    total += di["gols"][-1]
di["total"] = total
print("~~"*20)
print(di)
print("~~"*20)
for k, v in di.items():
    print(f"o campo {k} tem o valor {v}")
print("~~" * 20)
print(f"o jogador {di['jogador']} jogou {part} partidas")
for j in range(1, part + 1):
    print(f"na partida {j}, fez {di['gols'][j-1]}")