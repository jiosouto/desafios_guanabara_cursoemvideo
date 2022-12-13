from datetime import date
sexo = str(input('Qual o seu sexo? ')).strip().upper()
if sexo == 'FEMININO':
    print('Você não precisa se alistar obrigatoriamente.')
else:
    atual = date.today().year
    ano = int(input('Em que ano você nasceu? '))
    idade = date.today().year - ano
    print('Você tem {} anos, ou quase. Isso em {}.'.format(idade,atual))
    if idade < 18:
        falta = 18 - idade
        print('Você ainda é novo para se alistar. Faltam {} anos para você se alistar.'.format(falta))
        alistamento = atual + falta
        print('Seu alistamento será em {}.'.format(alistamento))
    elif idade == 18:
        print('Você já pode e deve se alistar este ano!')
    elif idade > 18:
        passou = idade - 18
        foi = atual - passou
        print('Você provavelmente se alistou em {} a {} anos atrás. '.format(foi,passou))