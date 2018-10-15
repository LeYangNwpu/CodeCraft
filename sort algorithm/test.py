def merge(arr, left, middle, right):
    num_left = middle - left + 1
    arr_left = [0] * num_left
    for i in range(num_left):
        arr_left[i] = arr[left + i]

    num_right = right - middle
    arr_right = [0] * num_right
    for i in range(num_right):
        arr_right[i] = arr[middle + 1 + i]

    i = 0
    j = 0
    k = left
    while (i < num_left) and (j < num_right):
        if arr_left[i] < arr_right[j]:
            arr[k] = arr_left[i]
            i += 1
        else:
            arr[k] = arr_right[j]
            j += 1
        k += 1

    while i < num_left:
        arr[k] = arr_left[i]
        k += 1
        i += 1

    while j < num_right:
        arr[k] = arr_right[j]
        k += 1
        j += 1

def msort(arr, arr_s, left, right):
    if left < right:
        middle = int((left + right) / 2)
        msort(arr, arr_s, left, middle)
        msort(arr, arr_s, middle + 1, right)
        merge(arr, left, middle, right)


def merge_sort(arr):
    msort(arr, arr, 0, len(arr) - 1)

data = [1, 3, 8, 5, 6, 7, 4, 9, 2]
merge_sort(data)
print(data)

