dis = float(input("Qual a distância da sua viagem? "))
# print("A sua passagem é para uma viagem de {} Km.".format(dis))
if dis <= 200:
    # preço = dis * 0.50
    print("A sua passagem tem uma distância de {} Km.\nO preço dela será de R$ {:.2f}.".format(dis,dis*0.50))
else:
    # preço = dis * 0.45
    print("A sua passagem tem uma distãncia de {} Km.\nO preço dela será de R$ {:.2f}.".format(dis,dis*0.45))
print("Tenha uma boa viagem!")

# Forma Simplificada
"""dis = float(input("Qual a distância da sua viagem? "))
print("A sua passagem é para uma viagem de {} Km.".format(dis))
preço = dis * 0.50 if dis <= 200 else dis * 0.45
print("O preço dela será de R${:.2f}".format(preço))"""