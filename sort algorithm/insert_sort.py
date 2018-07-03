'''
Suppose the front part of the array is in order, insert current value to proper location.
Then obtain a new array, whose number increases one.
Notice: only insert once, no swap
'''

def insert_sort(data):
    num = len(data)
    for i in range(2, num):
        if data[i] < data[i-1]:
            temp = data[i]
            j = i - 1
            while data[j] > temp and j > 0:
                data[j+1] = data[j]
                j -= 1
            data[j+1] = temp

data = [1,3,8,5,6,7,4,9,2]
print('\nbefore insert sort')
for i in data:
	print i,
insert_sort(data)
print('\nafter insert sort')
for i in data:
	print i,

