def binary_search(data, left, right, target):
	middle = (left + right) / 2
	if data[middle] == target:
		return middle
	elif data[middle] < target:
		return binary_search(data, middle+1, right, target)
	else:
		return binary_search(data, left, middle-1, target)

data = [1,2,3,5,7,9,12,23,45,76,700]
print(binary_search(data, 0, len(data)-1, 23))


