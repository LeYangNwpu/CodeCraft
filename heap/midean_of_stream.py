'''
Problem:
    Given that integers are being read from a data stream.
    Find median of all the elements read so far starting from the first integer till the last integer
Ways:
    Maintain two heaps, min heap and max heap
    The max heap stores the smaller half of the data, while the min heap stores the bigger half of the data
    For a new data, the heap with less element should be insert on element
'''

def heapify_max(arr, s, n):
    largest = s
    left = 2 * s + 1
    right = 2 * s + 2
    if left <= n and arr[largest] < arr[left]:
        largest = left
    if right <= n and arr[largest] < arr[right]:
        largest = right
    if largest != s:
        arr[largest], arr[s] = arr[s], arr[largest]
        heapify_max(arr, largest, n)


def heapify_min(arr, s, n):
    minal = s
    left = 2 * s + 1
    right = 2 * s + 2
    if left <= n and arr[minal] > arr[left]:
        minal = left
    if right <= n and arr[minal] > arr[right]:
        minal = right
    if minal != s:
        arr[minal], arr[s] = arr[s], arr[minal]
        heapify_min(arr, minal, n)


def median_of_stream(arr):
    median = 0
    heap_min = []
    heap_max = []
    for data in arr:
        if len(heap_max) > len(heap_min):
            # heap_min should add one element
            # however this new data should be inserted into heap_max
            # thus, we should first pop the root data in heap_max, insert this new data into heap_max
            # then, we insert the popped data into heap_min
            if data < median:
                temp = heap_max[0]
                heap_max[0] = data
                heap_min.insert(0, temp)
                # after data insert, the heap should be adjusted
                heapify_min(heap_min, 0, len(heap_min) - 1)
                heapify_max(heap_max, 0, len(heap_max) - 1)
            else:
                heap_min.insert(0, data)
                heapify_min(heap_min, 0, len(heap_min) - 1)
            median = (heap_min[0] + heap_max[0]) / 2
        elif len(heap_max) < len(heap_min):
            if data < median:
                heap_max.insert(0, data)
                heapify_max(heap_max, 0, len(heap_max) - 1)
            else:
                temp = heap_min[0]
                heap_min[0] = data
                heap_max.insert(0, temp)
                heapify_min(heap_min, 0, len(heap_min) - 1)
                heapify_max(heap_max, 0, len(heap_max) - 1)
            median = (heap_min[0] + heap_max[0]) / 2
        else:
            if data < median:
                heap_max.insert(0, data)
                heapify_max(heap_max, 0, len(heap_max) - 1)
            else:
                heap_min.insert(0, data)
                heapify_min(heap_min, 0, len(heap_min) - 1)
            if len(heap_min) == 0:
                median = heap_max[0]
            elif len(heap_max) == 0:
                median = heap_min[0]
            else:
                median = (heap_min[0] + heap_max[0]) / 2
        print('heap_max:', heap_max)
        print('heap_min:', heap_min)
        print('median data:', median)


arr = [5, 15, 10, 20, 3]
median_of_stream(arr)

