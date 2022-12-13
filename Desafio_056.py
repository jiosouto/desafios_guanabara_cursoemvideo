import statistics
lista_nomes = []
lista_idades = []
lista_sexo = []
n = int(input('Digite o número de pessoas a serem cadastradas: '))

for i in range(1,n+1):
    print('------- {}º PESSOA-------'.format(i))
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    gen = str(input('Sexo [M/F]: '))
    lista_nomes.append(name)
    lista_idades.append(age)
    lista_sexo.append(gen.upper()) ## evitar não reconhecer na comparação

print('A média de idade do grupo é de {}'.format(statistics.mean(lista_idades)))
print('O homem mais velho tem {} anos e se chama {}'.format(max(lista_idades),lista_nomes[lista_idades.index(max(lista_idades))]))
cont = 0
for i in range(len(lista_idades)):
    if lista_idades[i] < 20 and lista_sexo[i] == 'F':
        cont += 1
if cont >= 1:
    print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))
else:
    print('Nenhuma mulher com menos de 20 anos')