primeiro=int(input(' infome o primeiro termo: '))
razão=int(input (' informe a razão: '))
termo = primeiro 
cont = 1
c= 10
while cont <=c:
      print ('{}-'.format(termo),end='')
      termo = termo +razão
      cont = cont +1
      if cont == c:
         print('Fim')     
      if cont == c:
         c+= int(input('\nquantos termos a mais você deseja ver?: '))