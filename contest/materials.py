'''
Effect:
    sort a set of sequences according to their length
Indication:
    data: a list, length of each sequence
    s_set: sequence set
Usage:
    s_len = [len(s) for s in seq]
    bubble_sort_str(s_len, seq)
'''

def bubble_sort_str(data, s_set):
    num = len(data)
    for i in range(num-1, 1, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                s_set[j], s_set[j+1] = s_set[j+1], s_set[j]


