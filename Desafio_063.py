print ('/ Sequencia Fibonacci /')
termos = int(input("Quantos termos você quer mostrar?: "))
num = 1
a = 0
b = 1

while num <= termos:
  print("{}" .format(a), end="")
  total = a + b
  a = b
  b = total

  print(" > " if num < termos else " >> FIM", end="")
  num+=1