def Merge(data, left, medium, right):
    num_left = medium - left + 1
    num_right = right - medium

    # copy data
    arr_left = [0] * num_left
    for i in range(num_left):
        arr_left[i] = data[left + i]
    arr_right = [0] * num_right
    for i in range(num_right):
        # error here
        arr_right[i] = data[medium + 1 + i]

    # merge
    i = 0
    j = 0
    k = left
    # error here
    while i < num_left and j < num_right:
        if arr_left[i] < arr_right[j]:
        # if arr_left[i] > arr_right[j]:
            data[k] = arr_left[i]
            i += 1
        else:
            data[k] = arr_right[j]
            j += 1
        k += 1

    # dispose remain data
    while i < num_left:
        data[k] = arr_left[i]
        i += 1
        k += 1
    while j < num_right:
        data[k] = arr_right[j]
        j += 1
        k += 1


def MSort(data, left, right):
    # error here
    if left < right:
        medium = (left + right) / 2
        MSort(data, left, medium)
        # error here
        MSort(data, medium + 1, right)
        Merge(data, left, medium, right)

def MergePass(data, stride, arr_num):
    i = 0
    while i <= arr_num - 2*stride:
        Merge(data, i, i+stride-1, i+2 * stride-1)
        i = i + 2 * stride
    if i < arr_num - stride + 1:
        Merge(data, i, i+stride-1, arr_num-1)

def MSortNoRec(data):
    arr_num = len(data)
    stride = 1
    while stride < arr_num:
        MergePass(data, stride, arr_num)
        stride *= 2


# data = [30,20,50,40,70,60,90,80,10]
data = range(1200, -1, -1)
print('data before merge sort')
for i in range(len(data)):
    print('%d' % data[i]),
MSort(data, 0, len(data)-1)
# MSortNoRec(data)
print('\ndata after merge sort')
for i in range(len(data)):
    print('%d' % data[i]),




