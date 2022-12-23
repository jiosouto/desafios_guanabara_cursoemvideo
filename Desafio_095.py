di = dict()
todos = []
total = 0
while True:
    di["jogador"] = input("nome do jogador: ")
    di['gols'] = []
    part = int(input(f"quantas partidas {di['jogador']} jogou? "))
    for i in range(1, part + 1):
        di["gols"].append(int(input(f"quantos gols na {i}° partida? ")))
        total += di["gols"][-1]
    di["total"] = total
    total = 0
    todos.append(di.copy())
    r = input("quer continuar?[S/N]: ").lower().strip()[0]
    while True:
        if r == "s" or r == "n":
            break
        else:
            print("ERRO! digite somente S ou N")
            r = input("quer continuar?[S/N]: ").lower().strip()[0]
    if r == "n":
        break
print(todos, "lista full")
print("~~"*20)
print(f'''{"COD"!s:<3} {"NOME"!s:<15}{"GOLS"!s:<15}{"TOTAL"!s:<15}''')
print("_"*40)
for p, j in enumerate(todos):
    print(f"{p!s:<3}", end=" ")
    for k, v in j.items():
        print(f"{v!s:<15}", end=" ")
    print()
print("_"*40)
while True:
    es = int(input("quer ver as estatisticas de qual jogador?[999 pra parar]"))
    if es == 999:
        print("finalizando...")
        break
    print(f"LEVANTAMENTO DO JOGADOR {todos[es]['jogador']}")
    for c, l in enumerate(todos[es]['gols']):
        print(f"na partida {c + 1} fez {l} gols")
    print("_"*40)
print("fim do programa")