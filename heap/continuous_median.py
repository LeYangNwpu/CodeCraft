'''
Problem:
    Given that integers are being read from a data stream.
    Find median of all the elements read so far starting from the first integer till the last integer
Ways:
    1. Maintain two heaps, min heap and max heap
    The max heap stores the smaller half of the data, while the min heap stores the bigger half of the data
    For a new data, the heap with less element should be insert one element
    2. Alternatively, we can use Augmented self balanced binary search tree
Ref:
    https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
'''

# construct min heap to store large half
def heapify_min(arr, s, n):
    minimal = s
    left = 2 * s + 1
    right = 2 * s + 2
    if (left <= n) and (arr[minimal] > arr[left]):
        minimal = left
    if (right <= n) and (arr[minimal] > arr[right]):
        minimal = right
    if minimal != s:
        arr[s], arr[minimal] = arr[minimal], arr[s]
        heapify_min(arr, minimal, n)


# construct max heap to store small half
def heapify_max(arr, s, n):
    maximal = s
    left = 2 * s + 1
    right = 2 * s + 2
    if (left <= n) and (arr[maximal] < arr[left]):
        maximal = left
    if (right <= n) and (arr[maximal] < arr[right]):
        maximal = right
    if maximal != s:
        arr[s], arr[maximal] = arr[maximal], arr[s]
        heapify_max(arr, maximal, n)

# def heapify_max(arr, s, n):
#     largest = s
#     left = 2 * s + 1
#     right = 2 * s + 2
#     if left <= n and arr[largest] < arr[left]:
#         largest = left
#     if right <= n and arr[largest] < arr[right]:
#         largest = right
#     if largest != s:
#         arr[largest], arr[s] = arr[s], arr[largest]
#         heapify_max(arr, largest, n)
#
#
# def heapify_min(arr, s, n):
#     minal = s
#     left = 2 * s + 1
#     right = 2 * s + 2
#     if left <= n and arr[minal] > arr[left]:
#         minal = left
#     if right <= n and arr[minal] > arr[right]:
#         minal = right
#     if minal != s:
#         arr[minal], arr[s] = arr[s], arr[minal]
#         heapify_min(arr, minal, n)


def continuous_median(arr):
    min_heap = []
    max_heap = []
    median = 0
    for data in arr:
        # min_heap should add a data
        if len(min_heap) < len(max_heap):
            if data > median:
                min_heap.insert(0, data)
                heapify_min(min_heap, 0, len(min_heap) - 1)
            else:
                temp = max_heap[0]
                max_heap[0] = data
                min_heap.insert(0, temp)
                heapify_min(min_heap, 0, len(min_heap) - 1)
                heapify_max(max_heap, 0, len(max_heap) - 1)
            median = (min_heap[0] + max_heap[0]) / 2
        # max_heap should add a data
        elif len(min_heap) > len(max_heap):
            if data < median:
                max_heap.insert(0, data)
                heapify_max(max_heap, 0, len(max_heap) - 1)
            else:
                temp = min_heap[0]
                min_heap[0] = data
                max_heap.insert(0, temp)
                heapify_min(min_heap, 0, len(min_heap) - 1)
                heapify_max(max_heap, 0, len(max_heap) - 1)
            median = (min_heap[0] + max_heap[0]) / 2
        #
        else:
            if data < median:
                max_heap.insert(0, data)
                heapify_max(max_heap, 0, len(max_heap) - 1)
            else:
                min_heap.insert(0, data)
                heapify_min(min_heap, 0, len(min_heap) - 1)
            if len(min_heap) > len(max_heap):
                median = min_heap[0]
            else:
                median = max_heap[0]
        print('heap_max:', max_heap)
        print('heap_min:', min_heap)
        print('median data:', median)

arr = [5, 15, 10, 20, 3]
continuous_median(arr)
