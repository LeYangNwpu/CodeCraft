'''
Problem:
    Matrix Chain Multiplication
Way:
    for an arr, m[i,j] means the calculation number of A[i]A[i+1]...A[j]
    for i < k < j, we search for the best k, minimize:
        m[i,k] + m[k+1,j] + arr[i-1]*arr[k]*arr[j]
    when cannot found out the best, consider loop
    Notice:
      If input arr contains 5 numbers, there are 4 matrixs
      matrix A[i] has dimension arr[i-1] x arr[i] for i = 1..n
      To simplify the problem, we construct a matrix of nxn
      the first row and the first column are not used
Reference:
    https://www.geeksforgeeks.org/?p=15553
'''

def matrix_chain_mul(arr):
    n = len(arr)
    inf = float('inf')
    num_mat = [[inf] * n for _ in range(n)]
    for i in range(n):
        num_mat[i][i] = 0

    # chain length
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            for k in range(i, j):
                num_temp = num_mat[i][k] + num_mat[k + 1][j] + arr[i-1] * arr[k] * arr[j]
                num_mat[i][j] = min(num_mat[i][j], num_temp)
    print(num_mat)
    return num_mat[1][n - 1]


arr = [40, 20, 30, 10, 30]
number = matrix_chain_mul(arr)
print(number)

