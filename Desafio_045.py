import random
l = ('Pedra','Papel','Tesoura')
n = random.randint(0, 2)
print('''Escolhas\n[0]Pedra\n[1]Papel\n[2]Tesoura''')
esc = int(input('Qual é sua escolha ? '))

if esc == n:
    print('Empate, voce escolheu {}, e eu escolhi {}'.format(l[esc],l[n]))
elif esc == 0 and n == 1:
    print('Voce perdeu! Voce escolheu {}, e eu escolhi {}'.format(l[esc],l[n]))
elif esc == 0 and n == 2:
    print('Voce ganhou! Voce escolheu {}, e eu escolhi {}'.format(l[esc],l[n]))
elif esc == 1 and n == 2:
    print('Voce perdeu! Voce escolheu {}, e eu escolhi {}'.format(l[esc],l[n]))
elif esc == 1 and n == 0:
    print('Voce ganhou! Voce escolheu {}, e eu escolhi {}'.format(l[esc],l[n]))
elif esc == 2 and n == 0:
    print('Voce perdeu! Voce escolheu {}, e eu escolhi {}'.format(l[esc],l[n]))
elif esc == 2 and n == 1:
    print('Voce ganhou! Voce escolheu {}, e eu escolhi {}'.format(l[esc],l[n]))
else:
    print('Jogada invalida!')