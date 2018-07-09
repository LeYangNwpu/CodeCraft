'''
some strange problem occurs
'''

import numpy as np

n = 5
data = range(n*n)
matrix = np.asarray(data)
matrix = matrix.reshape((n, n))
print(matrix)

for i in range(int(n/2)):
    last = n - 1 - i
    for j in range(i, last):
        offset = j - i
        temp = matrix[i, j]
        print(temp)
        # left to top
        matrix[i,j] = matrix[last-offset, i]
        # bottom to left
        matrix[last-offset, i] = matrix[last, last - offset]
        # right to bottom
        matrix[last, last - offset] = matrix[i, last]
        # set right value
        matrix[i, last] = temp
        print(matrix)
        print('set one value')
print(matrix)

