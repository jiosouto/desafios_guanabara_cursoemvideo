import Desafio_109_00

print()
preço = float(input('Digite o preço R$: '))
print()
print(f'A metade de {Desafio_109_00.Desafio_109_00(preço)} é {Desafio_109_00.metade(preço,Desafio_109_00=True)}')
print(f'O dobro de {Desafio_109_00.Desafio_109_00(preço)} é {Desafio_109_00.dobro(preço,Desafio_109_00=True)}')
print(f'Aumentando 10%, temos \33[31m{Desafio_109_00.aumentar(preço,porcento=10, Desafio_109_00=False)}\33[m')
print(f'Reduzindo 13%, temos {Desafio_109_00.dininuir(preço,porcento=13, Desafio_109_00=True)}')