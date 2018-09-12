'''
Problem:
    Given an array of integers, find all combination of four elements in the array
    whose sum is equal to a given value X.
    For example, if the given array is {10, 2, 3, 4, 5, 9, 7, 8} and X = 23,
    then your function should print “3 5 7 8” (3 + 5 + 7 + 8 = 23).
Requires:
    time complexity should be O(n^2logn)
Ways:
    calculate the sum of all possible two-element combination, then sort
    in a sorted list, we can found out two elements that sum to a given value within time complexity O(n)
    adopt a new data structure, implement a modified sort function
Reference:
    https://www.geeksforgeeks.org/find-four-elements-that-sum-to-a-given-value-set-2/
'''

class sum_two:
	def __init__(self, data, i, j):
		self.sum = data[i] + data[j]
		self.ind1= i
		self.ind2 = j


def check_distinct(data_left, data_right):
	if (data_left.ind1 != data_right.ind1) and (data_left.ind1 != data_right.ind2) \
            and(data_left.ind2 != data_right.ind1) and(data_left.ind2 != data_right.ind2):
		return True
	return False


# rewrite insert sort
def sort_sum_data(data_sum):
    data_num = len(data_sum)
    for i in range(1, data_num):
        if data_sum[i-1].sum > data_sum[i].sum:
            temp_node = data_sum[i]
            j = i - 1
            # notice the constrain condition j >= 0
            while data_sum[j].sum > temp_node.sum and j >= 0:
                data_sum[j+1] = data_sum[j]
                j -= 1
            data_sum[j+1] = temp_node

arr = [10, 2, 3, 4, 5, 9, 7, 8]
value_sum = 23
two_data_sum = []
for idata in range(len(arr)-1):
	for jdata in range(idata+1, len(arr)):
		two_data_sum.append(sum_two(arr, idata, jdata))

sort_sum_data(two_data_sum)
# for itemp in two_data_sum:
#     print(itemp.sum, itemp.ind1, itemp.ind2),

left = 0
right = len(two_data_sum)-1
while left < right:
    data_left = two_data_sum[left]
    data_right = two_data_sum[right]
    temp_sum_value = data_left.sum + data_right.sum
    if temp_sum_value == value_sum:
        if check_distinct(data_left, data_right):
            print('proper four number is: %d, %d, %d, %d' % (arr[data_left.ind1], arr[data_left.ind2],
                                                             arr[data_right.ind1], arr[data_right.ind2]))
        left += 1
    elif temp_sum_value < value_sum:
        left += 1
    else:
        right -= 1

