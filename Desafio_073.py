times = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Athletico-PR','Atlético-MG','Fortaleza','São Paulo','América-MG','Botafogo','Santos','Goiás','Bragantino','Coritiba','Cuiabá','Ceará','Atlético-GO','Avaí','Juventude')
f = 0
print('{:=^40}'.format('TABELA BRASILEIRÃO'))
for c in times:
    f+=1
    print(f'{f:2}° {c}')
print('='*40)
print('\n')
print('{:=^40}'.format('TOP 5'))
f = 0
for c in range(0, 5):
    f+=1
    print(f'{f:2}° {times[c]}')
print('='*40)
print('\n')
print('{:=^40}'.format('ULTIMOS COLOCADOS'))
f =  16
for c in range(15, len(times)):
    print(f'{f}° {times[c]}')
    f += 1
print('='*40)
print('\n')
print('{:=^40}'.format('COLOCAÇÃO DO CORINTHIANS'))
lugar = times.index('Corinthians')+1
print(f'{lugar}° Corinthians')
print('='*40)
print('\n')
f = 0
print('{:=^40}'.format('TABELA BRASILEIRÃO EM ORDEM ALFABETICA'))
for c in sorted(times):
    f+=1
    print(f'{f:2}° {c}')
print('='*40)