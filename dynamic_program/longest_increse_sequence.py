'''
Problem:
    Given a sequence, find the length of the longest subsequence of it,
    such that all elements of the subsequence are sorted in increasing order.
    The subsequence need not to be adjacent
Ways:
    The LIS problem satisfies the optimal substructure property of DP task
    Solve the problem recursively
Ref:
    https://www.geeksforgeeks.org/longest-increasing-subsequence/
'''

def _lis(arr, n):
    global maximum
    if n == 1:
        return 1

    # the max length of LIS ending with arr[n-1]
    max_end_here = 1

    # recrsion
    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i - 1] < arr[n - 1] and res + 1 > max_end_here:
            max_end_here = res + 1

    maximum = max(maximum, max_end_here)
    return max_end_here

def lis(arr):
    global maximum
    maximum = 1
    n = len(arr)
    _lis(arr, n)
    return maximum


def lis_optim(arr):
    n = len(arr)
    # lis_doc[i] means for a sub-sequence ended with element arr[i],
    # the longest length
    lis_doc = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and (lis_doc[j]+1 > lis_doc[i]):
                lis_doc[i] = lis_doc[j] + 1
    print(lis_doc)
    maximum = 1
    for i in range(n):
        maximum = max(lis_doc[i], maximum)
    return maximum


arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
# arr = [10 , 22 , 9]
n = len(arr)

print(lis_optim(arr))
