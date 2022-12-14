maior_18 = mulher_20 = homens = 0
pergunta = ''
while True:
    print('-'*20)
    print('{: ^20}'.format('Cadastre uma pessoa'))
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper()[0]
    print('-'*20)
    if sexo == 'M':
        homens += 1
    if idade > 18:
        maior_18 += 1
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if pergunta == 'N':
        break
print("{:=^40}".format('Fim do Programa'))
print('Total de pessoas com mais de 18 anos: {}'.format(maior_18))
print('Ao todo temos {} homens cadastrados'.format(homens))
print('E temos {} mulheres com menos de 20 anos.'.format(mulher_20))
print('='*40)