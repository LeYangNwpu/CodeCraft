'''
Problem:
    selection sort
Way:
    1. scan the array from left to right, for each time, the comparision number is n-i(i=1,2,...,n-1)
       document the minimal number location, after scan, swap the minimal number to the forehead
       time complexity n(n-1)/2 + n-1
    2. when scan, document both the minimal number and the maximal number, swap two numbers after each scan
       time complexity  n^2/4 + n-1
'''

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	return arr

def selection_sort_optim(arr):
    num = len(arr)
    i_range = int(num/2)
    for i in range(i_range):
        # dispose the first and last two numbers
        min_loc = i
        max_loc = num - i - 1
        min_value = arr[i]
        max_value = arr[num-i-1]
        if min_value > max_value:
            swap(arr, min_loc, max_loc)
            min_value = arr[i]
            max_value = arr[num - i - 1]
        for j in range(i+1, num-i-1):
            if arr[j] < min_value:
                min_loc = j
                min_value = arr[j]
            if arr[j] > max_value:
                max_loc = j
                max_value = arr[j]

        if i != min_loc:
            swap(arr, i, min_loc)
        if (num-i-1) != max_loc:
            swap(arr, num-i-1, max_loc)
        print(arr)
    return arr

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_loc = i
        min_value = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min_value:
                min_loc = j
                min_value = arr[j]
        if i != min_loc:
            swap(arr, i, min_loc)
    return arr


arr = [9,1,5,8,3,7,4,6,2]
print(selection_sort_optim(arr))
