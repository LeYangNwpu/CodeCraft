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
    median = left + (right - left) / 2
    if data[right] < data[left]:
        swap(data, right, left)
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
