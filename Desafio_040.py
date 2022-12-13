nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota + nota2) / 2
print('Sua média foi de {:.1f} pontos.'.format(média))

if média < 5.0:
    print('Você foi REPROVADO!')
elif 6.9 >= média >= 5.0:
    print('Você está de RECUPERAÇÃO!')
elif média >= 7:
    print('Você foi APROVADO!')