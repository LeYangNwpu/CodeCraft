'''
Problem:
    Matrix Chain Multiplication
Way:
    for an arr, m[i,j] means the calculation number of A[i]A[i+1]...A[j]
    for i < k < j, we search for the best k, minimize:
        m[i,k] + m[k+1,j] + arr[i-1]*arr[k]*arr[j]
    when cannot found out the best, consider loop
Reference:
    https://www.geeksforgeeks.org/?p=15553
'''

def matrix_chain_mul(arr):
    n = len(arr)
    inf = float('inf')
    num_mat = [[inf] * n for i in range(n)]
    for i in range(n):
        num_mat[i][i] = 0

    # chain length
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            for k in range(i, j):
                num_temp = num_mat[i][k] + num_mat[k + 1][j] + arr[i-1] * arr[k] * arr[j]
                num_mat[i][j] = min(num_mat[i][j], num_temp)
    return num_mat[1][n - 1]


arr = [1, 2, 3, 4]
number = matrix_chain_mul(arr)
print(number)

