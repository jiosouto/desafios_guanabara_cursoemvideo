print(f'{"="*30}')
print(f"{'BOLETIM':^30}")
print(f'{"="*30}')
dados = [[] , [], [], []]
id = 0
while True:
    nome = str(input("NOME: ")).strip()
    n1 = int(input("NOTA 1: "))
    n2 = int(input("NOTA 2: "))
    media = (n1 + n2) / 2
    dados[0].append(id)
    dados[1].append(nome)
    dados[2].append(n1)
    dados[2].append(n2)
    dados[3].append(media)
    resp = input("QUER CONTINUAR [S/N]: ").strip().upper()[0]
    while resp not in "SN":
        resp = input("[ERROR] QUER CONTINUAR [S/N]: ").strip().upper()[0]
    if resp == "N":
        break
    id += 1
    print()
print("="*50)
print("ID", end=" - ")
print(f'{"NOME"}', end="- ")
print(f'{"MEDIA"}',)
for c in range(0, len(dados[0])):
    print(f"{dados[0][c]:<} - {dados[1][c]} - {dados[3][c]}")
print("="*50)
show = 0
while show != 999:
    show = int(input("Mostrar notas de qual aluno [ID] (999 STOP): "))
    while show not in dados[0] and show != 999:
        show = int(input("[TENTE NOVAMENTE] Mostrar notas de qual aluno [ID] (999 STOP): "))
    if show == 999:
        break
    if show == 0:
        print(f'DADOS - {dados[1][show]}')
        print(f"NOTA 1: {dados[2][show]} - NOTA 2: {dados[2][show+1]}")
        print()
    else: 
        print(f'DADOS - {dados[1][show]}')
        print(f"NOTA 1: {dados[2][show*2]} - NOTA 2: {dados[2][show*2+1]}")
        print()
print("="*50)
print('OBRIGADO POR USAR MEU BOLETIM EM PYTHON !!!')
print('VOLTE SEMPRE !')