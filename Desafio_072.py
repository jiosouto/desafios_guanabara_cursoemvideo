letter = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
num = int(input('digite um valor entre 0 e 20'))
while num > 20:
    num = int(input('tente novamente'))
    if num == letter:
        break
print('vc digitou o número {}'.format(letter[num]))