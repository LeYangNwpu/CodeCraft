'''
Problem:
    Given an array of n positive integers.
    Write a program to find the sum of maximum sum subsequence of the given array
    such that the intgers in the subsequence are sorted in increasing order
Ways:
    This problem is similar with longest increasing subsequence problem
    we should maintain an array msic_doc
    msic_doc[i] indicates the max sum value for an increasing subsequence ended with arr[i]
Notice:
    There are two judge conditions "arr[j] < arr[i]" or "(arr[j] < arr[i]) and (temp_sum > msis_doc[i])"
    Actually, as we initialize msis_doc same with arr, the condition "temp_sum > msis_doc[i]" is always True.
Reference:
    https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/
'''

def max_sum_increasing_sub(arr):
    num = len(arr)
    msis_doc = [arr[i] for i in range(num)]
    for i in range(num):
        for j in range(i):
            temp_sum = msis_doc[j] + arr[i]
            if arr[j] < arr[i]:
                msis_doc[i] = temp_sum
            # if (arr[j] < arr[i]) and (temp_sum > msis_doc[i]):
            #     msis_doc[i] = temp_sum
    print(msis_doc)
    max_sum = 0
    for data in msis_doc:
        max_sum = max(max_sum, data)
    return max_sum

arr = [1, 101, 2, 3, 100, 4, 5]
print(max_sum_increasing_sub(arr))
