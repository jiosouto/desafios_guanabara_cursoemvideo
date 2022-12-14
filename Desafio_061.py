pt = int(input("Qual é o primeiro termo: "))
rz = int(input("Qual é a razão: "))
pa = int(input("Quantos termos: "))
cont=0
while cont < pa:
  print(pt, end='->')
  pt += rz
  cont += 1
print("Fim")