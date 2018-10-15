def heapify_min(arr, s, n):
    minimal = s
    left_child = 2 * s + 1
    right_child = 2 * s + 2
    if (left_child <= n) and (arr[left_child] < arr[minimal]):
        minimal = left_child
    if (right_child <= n) and (arr[right_child] < arr[minimal]):
        minimal = right_child
    if minimal != s:
        arr[s],  arr[minimal] = arr[minimal], arr[s]
        heapify_min(arr, minimal, n)

def construct_min_heap(arr):
	num = len(arr)
	begin_point = int(num / 2) - 1
	for i in range(begin_point, -1, -1):
		heapify_min(arr, i, num-1)


def heap_sort(arr):
    construct_min_heap(arr)

    num = len(arr)
    for i in range(num - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_min(arr, 0, i - 1)

data = [12,5,7,8,4,6,9,10,3,1,2,11]
# data = [50, 10, 90, 30, 70, 40, 80, 60, 20]
# construct_min_heap(data)
# print(data)
heap_sort(data)
print(data)

