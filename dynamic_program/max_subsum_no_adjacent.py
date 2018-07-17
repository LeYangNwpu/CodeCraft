'''
Problem:
    Given an array of positive numbers,
    find the maximum sum of a subsequence with the constraint that
    no 2 numbers in the sequence should be adjacent in the array.
Requires:
    the solution should be efficient
Ways:
    loop through the array, record the sum of odd series and even series
Ref:
    https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
'''

def max_sum_no_adjacent(array):
	sum_odd = 0
	sum_even = 0
	for data in array[::2]:
		sum_even += data
	for data in array[1::2]:
		sum_odd += data
	return max(sum_odd, sum_even)

array = [5,  5, 10, 40, 50, 35]
max_subsum = max_sum_no_adjacent(array)
print(max_subsum)

# ### do not understand the following algorithm
# # Function to return max sum such that
# # no two elements are adjacent
# def find_max_sum(arr):
#     incl = 0
#     excl = 0
#
#     for i in arr:
#         # Current max excluding i (No ternary in
#         # Python)
#         new_excl = excl if excl > incl else incl
#
#         # Current max including i
#         incl = excl + i
#         excl = new_excl
#
#     # return max of incl and excl
#     return (excl if excl > incl else incl)
#
#
# # Driver program to test above function
# arr = [5, 5, 10, 100, 10, 5]
# print(find_max_sum(arr))
#
#
# # This code is contributed by Kalai Selvan


