from datetime import date
hoje = date.today().year
maior_idade = 0
menor_idade = 0
for contar in range (1, 8):
    nascimentos = int(input('Diga o ano de nascimento da {}° pessoa: '.format(contar)))
    if (hoje - nascimentos) >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print('Há {} pessoas maiores de idade e {} pessoas menores de idade.'.format(maior_idade,menor_idade))