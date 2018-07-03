'''
Problem:
    given an array A[] of n numbers and another number x,
    determines whether or not there exist two elements in S whose sum is exactly x.
Requires:
    Time complexity should be O(n)
    Naive twice loop requires the O(n^2) time complexity.
Ways:
    (1) Resort to inline data structures and functions in python, such as, set(), list, array
    (2) Hash Table (implement with dictionary)
'''

def two_num_sum(data, sum):
	result = []
	s = set()
	for data_cur in data:
		data_require = sum - data_cur
		if data_require in s:
			result.append([data_cur, data_require])
		s.add(data_cur)
	return result

data = [3, 5, 2, -4, 8, 11]
sum = 7
result_pairs = two_num_sum(data, sum)
for pairs in result_pairs:
	print(pairs),

