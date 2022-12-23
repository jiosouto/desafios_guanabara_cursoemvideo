from datetime import date

def voto(txt):
    ano_atutal = date.today().year
    idade = ano_atutal - txt
    resp = ' '
    if idade >= 18 and idade < 65:
        resp = (f'Com {idade} anos: VOTO OBRIGATORIO')
    if idade < 16 :
        resp =(f'Com {idade} anos: NÃO PODE VOTAR AINDA')
    if idade >= 16 and idade < 18 or idade > 65:
        resp =(f'Com {idade} anos: VOTO OPCIONAL')
    return resp


ano = int(input('Em que ano você nasceu? '))
voto(ano)
print(voto(ano))