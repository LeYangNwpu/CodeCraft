'''
quick sort
Idea:
  1. The partition function is the core of this algorithm, it first selects a key value
    after a loop of operation, values smaller than key site on the left side
    while values bigger than key site on the right
  2. In partition function, we select the key value as the left data, key = arr[left]
    after each swap operation, the left ptr or right ptr point to the key value
  3. Optimization method
    (1) Generate a good pivot key, median of three number
    (2) Quick sort is efficient when the array contains many numbers.
      On the contrary, simple sort algorithm is more efficient
      Combine them together
    (3) use tail recursion to replace the original two recursions
Notice:
  1. In the function qsort, do not forget the condition "if left < right:"
Space time complexity:
  Optimal status:
    the pivot value is proper, which can equally partition the array
    time complexity: O(n log n)
    space complexity: O(long n)
  Worst status:
    the pivot value is the smallest or biggest value, one partition is empty
    time complexity: O(n^2)
    space complexity: O(n)
Inspiration:
  Similar with bubble sort, quick sort belong to exchange sort
  the core idea is to make use of each comparison, site the smaller on one side, the bigger on the other side

'''

def swap(data, idx1, idx2):
	temp = data[idx1]
	data[idx1] = data[idx2]
	data[idx2] = temp

def InsertSort(data):
    for i in range(1, len(data)):
        if data[i] < data[i - 1]:
            temp = data[i]
            j = i - 1
            while data[j] > temp and j >= 0:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = temp

def generate_median(data, left, right):
    median = left + int((right - left) / 2)
    if data[right] < data[median]:
        swap(data, right, median)
    if data[left] < data[median]:
        swap(data, left, median)


def Partition(data, left, right):
    # optimize pivotkey selection
    generate_median(data, left, right)
    pivotkey = data[left]
    while left < right:
        while left < right and data[right] >= pivotkey:
            right -= 1
        swap(data, left, right)
        while left < right and data[left] <= pivotkey:
            left += 1
        swap(data, left, right)
    return left


def PartitionS(data, left, right):
	generate_median(data, left, right)
	pivotkey = data[left]
	while left < right:
		while left < right and data[right] >= pivotkey:
			right -= 1
		data[left] = data[right]
		while left < right and data[left] <= pivotkey:
			left += 1
		data[right] = data[left]
	data[left] = pivotkey
	return left


def QSort(data, left, right):
    if left < right:
        pivot = PartitionS(data, left, right)
        QSort(data, left, pivot-1)
        QSort(data, pivot+1, right)

def QSortS(data, left, right):
    if (right - left) > MAX_LENGTH_INSERT_SORT:
        while left < right:
            pivot = PartitionS(data, left, right)
            QSortS(data, left, pivot-1)
            left = pivot + 1
    else:
        InsertSort(data)

def QuickSort(data):
    QSortS(data, 0, len(data)-1)

global MAX_LENGTH_INSERT_SORT
MAX_LENGTH_INSERT_SORT = 7
data = [50, 10, 90, 30, 70, 40, 80, 60, 20]
print('data before quick sort')
for i in range(len(data)):
    print('%d' % data[i]),
QuickSort(data)
print('\ndata after quick sort')
for i in range(len(data)):
    print('%d' % data[i]),
