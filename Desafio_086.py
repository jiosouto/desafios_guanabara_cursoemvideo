mat = []
for row in range(3):
    for col in range(3):
        mat.append(int(input(f'Type a number for [{row}, {col}]: ')))
for count, i in enumerate(mat):
    print(f'[{i:^5}]', end='')
    if count == 2 or count == 5:
        print('')
print('')