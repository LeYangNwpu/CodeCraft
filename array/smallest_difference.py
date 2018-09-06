'''
Problem:
    Given two arrays of integers, compute the pair of values (one value in each array)
     with the smallest (non-negative) difference
Ways:
    (1) sort two arrays in increasing order, find difference,
    increase the smaller value (by move) so as to decrease the difference
'''

def smallest_difference(arr1, arr2):
    arr1.sort()
    arr2.sort()

    i = 0
    j = 0
    diff = float('inf')
    while i < len(arr1) and j < len(arr2):
        diff_temp = arr1[i] - arr2[j]
        diff = min(diff, abs(diff_temp))
        if diff_temp <= 0:
            i += 1
        else:
            j += 1
    return diff


arr1 = [1, 2, 11, 5]
arr2 = [4, 12, 19, 23, 127, 235]
min_diff = smallest_difference(arr1, arr2)
print(min_diff)
