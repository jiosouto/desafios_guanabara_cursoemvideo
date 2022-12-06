# Exemplo de condição simples
velo = float(input("Qual a velocidade do carro: "))
if velo > 80:
    print("Você levou uma multa por passar dos 80Km/h!")
    multa = (velo-80) * 7
    print("A sua multa por estar a {} Km/h é de R$ {:.2f}.".format(velo,multa))
print("Sua velocidade é muito baixa!")