import numpy as np

mat = np.empty([3,3], dtype=int)
even = []
for i in range(3):
    for j in range(3):
        n = int(input(f'Type a number for [{i}, {j}]: '))
        mat[i][j] = n
        if n % 2 == 0:
            even.append(n)
for row in mat:
    print(row)
print(f'Sum of even numbers: {sum(even)}')
print(f'Sum of the 3rd column: {mat[:,-1].sum()}')
print(f'Max value of 2nd row: {mat[1].max()}')