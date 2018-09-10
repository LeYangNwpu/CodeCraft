'''
Problem:
    Given an unsorted array arr[0..n-1] of size n,
    find the minimum length subarray arr[s..e] such that sorting this subarray makes the whole array sorted.
Way:
    1) Find the candidate unsorted subarray
        a) Scan from left to right and find the first element which is greater than the next element
        b) Scan from right to left and find the first element which is smaller than the next element
    2) Check whether sorting the candidate unsorted subarray makes the complete array sorted or not.
       If not, then include more elements in the subarray
       a) Find the minimum and maximum values in arr[s..e].
       b) Find the first element (if there is any) in arr[0..s-1] which is greater than min,
       change s to index of this element
       c) Find the last element (if there is any) in arr[e+1..n-1] which is smaller than max,
       change e to index of this element
Ref:
    https://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/
'''

def array_min_max(arr):
    data_min = float('inf')
    data_max = -float('inf')
    for data in arr:
        data_min = min(data_min, data)
        data_max = max(data_max, data)
    return data_min, data_max


def min_unsorted_subarray(arr):
    if len(arr) == 1:
        print('only one element')
        return
    data = arr[0]
    # fore
    order = 0
    for idata in arr[1:]:
        if idata > data:
            data = idata
            order += 1
            continue
        else:
            break
    pre_order = order
    if pre_order == len(arr)-1:
        print('this array is sorted')
        return
    # back
    data = arr[-1]
    order = len(arr) - 1
    for idata in arr[-2::-1]:
        if idata < data:
            data = idata
            order -= 1
            continue
        else:
            break
    back_order = order

    # improve
    data_min, data_max = array_min_max(arr[pre_order:back_order + 1])
    # suppose the array does not contain repeated number
    # fore
    while (data_min < arr[pre_order]) and (pre_order > 0):
        pre_order -= 1
    pre_order += 1
    while (data_max > arr[back_order]) and (back_order < len(arr)):
        back_order += 1
    back_order -= 1
    return pre_order, back_order


arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
left, right = min_unsorted_subarray(arr)
print(left, right)


