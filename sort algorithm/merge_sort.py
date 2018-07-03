'''
Given two in-order sun-arraies, we can merge it to one larger array.
Dispose the problem in recursive manner in two steps: msort and merge
Partition the array when entering recursive, merge arrays when exiting recursive
'''

def merge(data, left, middle, right):
    num_left = middle - left + 1
    data_left = [0] * num_left
    for i in range(num_left):
        data_left[i] = data[left + i]

    num_right = right - middle
    data_right = [0] * num_right
    for i in range(num_right):
        data_right[i] = data[middle + 1 + i]

    k = left
    m = 0
    n = 0
    while m < num_left and n < num_right:
        if data_left[m] < data_right[n]:
            data[k] = data_left[m]
            m += 1
        else:
            data[k] = data_right[n]
            n += 1
        k += 1
    while m < num_left:
        data[k] = data_left[m]
        k += 1
        m += 1
    while n < num_right:
        data[k] = data_right[n]
        k += 1
        n += 1

def msort(data, left, right):
    if left < right:
        middle = (left + right) / 2
        msort(data, left, middle)
        msort(data, middle+1, right)
        merge(data, left, middle, right)


def merge_sort(data):
    msort(data, 0, len(data) - 1)


data = [1, 3, 8, 5, 6, 7, 4, 9, 2]
print('\nbefore merge sort')
for i in data:
    print i,
merge_sort(data)
print('\nafter merge sort')
for i in data:
    print i,
