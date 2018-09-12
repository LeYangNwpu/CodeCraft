'''
Problem:
    Find a triplet that sum to a given value
Way:
    based on two number sum, step futher
Ref:
    https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
'''

def two_number_sum(arr, sumtwo):
    # the arr should be sorted
    arr.sort()
    num = len(arr)
    i = 0
    j = num - 1
    numbers = []
    while (i < j):
        sum_temp = arr[i] + arr[j]
        if sum_temp == sumtwo:
            numbers.append([arr[i], arr[j]])
            i += 1
        elif sum_temp < sumtwo:
            i += 1
        else:
            j -= 1
    return numbers


def three_number_sum(arr, sumthree):
    # the arr should be sorted
    arr.sort()
    num = len(arr)
    three_num_set = []
    for i in range(num - 2):
        data = arr[i]
        numbers = two_number_sum(arr[i + 1:], sumthree-data)
        # collect these data together
        for two_numbers in numbers:
            three_num_set.append([data, two_numbers[0], two_numbers[1]])
    return three_num_set


arr = [1, 4, 45, 6, 10, 8]
sumthree = 22
three_num_set = three_number_sum(arr, sumthree)
print(three_num_set)
