from time import sleep

def função(txt=True):
    while True:
        print('\033[m\033[97;42m~' * 40)
        print('SITEMA DE AJUDA PyHELP')
        print('~' * 40)
        sleep(1)
        resp = str(input('\033[mDigite uma Função ou biblioteca: ')).lower()
        if resp in 'fim':
            sleep(1)
            print('\033[97;41mAté Logo')
            break
        sleep(1)
        print('\033[m\033[97;44m~' * 40)
        print(f'Acessando o manual do comando "{resp}"')
        print('~' * 40)
        sleep(1)
        print('\033[m\033[7m')
        coman = help(resp)

função(txt=True)