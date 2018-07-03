'''
compare the adjacent two values, if not in order, swap these two values
'''

def swap_data(data, m, n):
	temp = data[m]
	data[m] = data[n]
	data[n] = temp

def bubble_sort(data):
	num = len(data)
	for i in range(num-1, 1, -1):
		for j in range(1,i):
			if data[j] > data[j+1]:
				swap_data(data, j, j+1)

data = [1,3,8,5,6,7,4,9,2]
print('before bubble sort')
for i in data:
	print i,
bubble_sort(data)
print('after bubble sort')
for i in data:
	print i,
