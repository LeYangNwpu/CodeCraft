'''
Problem:
    Given array representation of min Heap, convert it to max Heap in O(n) time.
Solution:
    recursive solution
Ref:
    https://www.geeksforgeeks.org/convert-min-heap-to-max-heap/
'''

def heapify(arr, s, n):
    largest = s
    left = 2 * s + 1
    right = 2 * s + 2
    if left <= n and arr[largest] < arr[left]:
        largest = left
    if right <= n and arr[largest] < arr[right]:
        largest = right
    if largest != s:
        arr[largest], arr[s] = arr[s], arr[largest]
        heapify(arr, largest, n)

def convert_min_max(arr, s, n):
    minal = s
    left = 2 * s + 1
    right = 2 * s + 2
    # leaf node
    if left > n:
        return
    # only left node
    elif (left <= n) and (right > n):
        minal = left
    # both left and right node
    elif left <= n and right <= n:
        if arr[left] > arr[right]:
            minal = right
        else:
            minal = left
    arr[minal], arr[s] = arr[s], arr[minal]
    convert_min_max(arr, minal, n)


def convert_heap_max2min(arr):
    num = len(arr)
    # begin_point = int(num / 2) - 1
    # # construct the max heap
    # for i in range(begin_point, -1, -1):
    #     heapify(arr, i, num - 1)
    print('max heap:', arr)
    for i in range(num-1, -1, -1):
        convert_min_max(arr, i ,num-1)
    print('min heap:', arr)


arr = [20, 18, 10, 12, 9, 9, 3, 5, 6, 8]
convert_heap_max2min(arr)

