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

arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
n = len(arr)

print(lis(arr))
