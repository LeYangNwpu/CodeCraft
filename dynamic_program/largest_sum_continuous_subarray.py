'''
Problem:
    Largest Sum Contiguous Subarray
    Write an efficient program to find the sum of contiguous subarray
      within a one-dimensional array of numbers which has the largest sum.
Way:
    Use Kadane’s Algorithm
    maintain two variables: max_sum_here and max_so_far
      max_sum_here records the maximal sum for sub_array ending with arr[i], we can suppose max_sum_here >= 0
      max_so_far records the desired result
Ref:
    https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
'''

def largest_sum_con_subarray(arr):
	max_sum_here = 0
	max_so_far = 0
	for data in arr:
		max_sum_here += data
		if max_sum_here < 0:
			max_sum_here = 0
		if max_sum_here > max_so_far:
			max_so_far = max_sum_here
	return max_so_far

# this function can dispose array with all negative numbers
def lscb_optim(arr):
    max_sum_here = arr[0]
    max_so_far = arr[0]
    for data in arr[1:]:
        max_sum_here = max(data, max_sum_here+data)
        if max_sum_here > max_so_far:
            max_so_far = max_sum_here
    return max_so_far

# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# print(largest_sum_con_subarray(arr))
arr = [-1,-2,-3,-4]
print(lscb_optim(arr))



