'''
Problem:
    geeksforgeeks write a function that takes in an array of integers
    and return an array of length 2 representing the largest range of numbers
    contained in that array
Way:
    Sort the array, find the largest consist sets
    We should carefully dispose the special cases, such as:
        (1) only one element array
        (2) repeated numbers in the array
        (3) the last set is the largest (when the code will not enter)
Ref:
    https://www.algoexpert.io/questions/Largest%20Range
'''

def largest_range(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    arr.sort()

    max_length = 0
    max_sets = None

    data_f = arr[0]
    length_c = 1
    sets_c = [arr[0]]
    for data in arr[1:]:
        # for repeated number
        if data - data_f == 0:
            continue
        if data - data_f == 1:
            length_c += 1
            sets_c.append(data)
        else:
            if length_c > max_length:
                max_sets = sets_c
                max_length = length_c
            length_c = 1
            sets_c = [data]
        data_f = data
    # for a increasing array or the last sets is the longest sets
    if (max_sets is None) or (length_c > max_length):
        max_sets = sets_c
    return max_sets[0], max_sets[-1]


arr = [19,-1,18,17,2,10,3,12,5,16,4,11,8,7,6,15,12,12,2,1,6,13,14]
data_min, data_max = largest_range(arr)
print(data_min, data_max)


