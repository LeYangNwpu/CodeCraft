class sum_two:
	def __init__(self, data, i, j):
		self.sum = data[i] + data[j]
		self.ind1= i
		self.ind2 = j

def check_distinct(index1, index2, left, right):
    if (index1[left] != index2[left]) and (index1[left] != index2[right]) and (index1[right] != index2[left]) and (index1[right] != index2[right]):
        return True
    return False

arr = [10, 2, 3, 4, 5, 9, 7, 8]
value_sum = 23
two_data_sum = []
index1_ori = []
index2_ori = []
for idata in range(len(arr)-1):
    for jdata in range(idata, len(arr)):
        two_data_sum.append(arr[idata] + arr[jdata])
        index1_ori.append(idata)
        index2_ori.append(jdata)

# must obtain index before sort
index_sort = [two_data_sum.index(x) for x in sorted(two_data_sum)]
two_data_sum.sort()

index1 = []
index2 = []
# change the index according to sort index
# error occurs when arr contains repeated numbers
for ind in index_sort:
    index1.append(index1_ori[ind])
    index2.append(index2_ori[ind])

left = 0
right = len(two_data_sum)-1
while left < right:
    # print(left, right)
    temp_sum_value = two_data_sum[left] + two_data_sum[right]
    if temp_sum_value == value_sum:
        if check_distinct(index1, index2, left, right):
            # print('show information here')
            # print(temp_sum_value)
            # print(left, right)
            print('proper four number is: %d, %d, %d, %d' % (arr[index1[left]], arr[index1[right]], arr[index2[left]], arr[index2[right]], ))
        left += 1
    elif temp_sum_value < value_sum:
        left += 1
    else:
        right -= 1
