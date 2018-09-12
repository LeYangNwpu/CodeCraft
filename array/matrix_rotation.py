'''
Problem:
    Given an image of size NxN, write a function to rotate this image by 90 angle
Ways:
    rotate this matrix layer by layer, move from right to up, from bottom to right,
    from right to bottom, from (temp) to right
    use a small matrix as example to build the index connection
Notice:
    the time complexity is O(N^2)
    This is already optimal, as any algorithm needs to visit all element
'''

import numpy as np

def matrix_rotation(matr):
    [N, _] = matr.shape
    res = np.zeros((N, N))
    half_n = int(N / 2)
    for i in range(half_n + 1):
        for j in range(i, N - i):
            temp = matr[i, j]
            # left to up
            res[i, j] = matr[N-j-1, i]
            # bottom to left
            res[N-j-1, i] = matr[N-i-1, N-j-1]
            # right to bottom
            res[N-i-1, N-j-1] = matr[j, N-i-1]
            # temp to right
            res[j, N-i-1] = temp
    return res


data = range(1, 101)
data_np = np.asarray(data)
data_np = data_np.reshape((10, 10))
print(data_np)
res = matrix_rotation(data_np)
print(res)


