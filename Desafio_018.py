from math import radians, tan, sin, cos

ang = int(input("Digite um ângulo: "))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))
print("O seno de {} é {:.2f}.\nO cosseno de {} é {:.2f}.\nA tangente de {} é {:.2f}.".format(ang,sen,ang,cos,ang,tg))