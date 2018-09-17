'''
Problem:
    heap sort
Ways:
    maybe, simple recursive is a good solution
Reference:
    https://www.geeksforgeeks.org/heap-sort/
'''

# To heapify subtree rooted at index i.
# n is size of heap
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


def heapify_no_rec(arr, s, n):
    temp = arr[s]
    # left child index
    j = 2 * s + 1
    while j < n:
        if (j <= n-1) and (arr[j] < arr[j+1]):
            j += 1
        if temp > arr[j]:
            break
        arr[s] = arr[j]
        s = j
        j  = j * 2 + 1
    arr[s] = temp

def heap_sort(arr):
    num = len(arr)
    begin_point = int(num / 2) - 1
    # construct max heap
    for i in range(begin_point, -1, -1):
        # heapify_no_rec(arr, i, num-1)
        heapify(arr, i, num-1)
    # heap sort
    # notice that i = num-1, num-2, ..., 2, we cannot reach i=1
    # for i in range(num-1, 1, -1):
    for i in range(num-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        # heapify_no_rec(arr, 0, i-1)
        heapify(arr, 0, i-1)

arr = [50, 10, 90, 30, 70, 40, 80, 60, 20]
heap_sort(arr)
print(arr)
