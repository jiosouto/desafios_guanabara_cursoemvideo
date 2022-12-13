from time import sleep
from datetime import date

ano = date.today().year
for c in range(10, -1, -1):
    print('{}'.format(c))
    sleep(0.5)
print('Bum... bum... cabum!!!')
sleep(0.5)
print('Feliz {}!!!'.format(ano))