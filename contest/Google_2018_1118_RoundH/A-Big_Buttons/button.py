'''
This code is implemented during the contest
Although, I correctly solve this problem, this solution is tedious
In precise:
(1) For the small dataset problem, a naive solution is acceptable
    '
    generate all possible sequences recursively, O(2^n)
    check whether each sequence is legal, remove illegal ones O(P*N)
    total complexity: O(2^n * P * N)
    '
    result is the most important for small dataset
(2) For the large dataset, I got the core idea
    '
    we should count for the illegal sequences,
    then subtract it from the total number
    '
    However, my implementation is tedious
      I first sort the forbidden sequences according to their length,
        with a modification of bubble sort, this is not hard
        find myself is not much familiar with basic algorithm
      then, I check and remove forbidden sequences which can be represented by a shorter sequences
        I what to check all strings in the forbidden_string_set, so I use 'for i in range(len(s_set)-1)'
        however, I delete illegal string when I detect them, which means the forbidden_string_set varies
        so this code is unstable
        Alternatively, I could use .copy() to create a stable sequences
        Besides, as check strings is not computation consumption, a simple implementation is enough

'''

in_data_file = 'A-large.in'
out_data_file = 'A-large.out'

fid_in = open(in_data_file, 'r')
fid_out = open(out_data_file, 'w')

num_all = int(fid_in.readline())
print('total test samples %d' % num_all)

def bubble_sort_str(data, s_set):
    num = len(data)
    for i in range(num-1, 1, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                s_set[j], s_set[j+1] = s_set[j+1], s_set[j]


def check_redu(temp_set, s_short, stop_ind):
    for j in range(len(temp_set)-1, stop_ind, -1):
        s_long = temp_set[j]
        s_cmp = s_long[:len(s_short)]
        if s_cmp == s_short:
            return s_long
    return None

def remove_redu(s_set):
    for i in range(len(s_set)-1):
        if i >= len(s_set):
            break
        string = s_set[i]
        while True:
            temp_set = s_set.copy()
            str_redu = check_redu(temp_set, string,i)
            if str_redu is not None:
                s_set.remove(str_redu)
            else:
                break
    return s_set


for itest in range(num_all):
    sline = fid_in.readline()
    num_press, num_forb = [int(s) for s in sline.split(" ")]
    seq = []
    for _ in range(num_forb):
        string = fid_in.readline()
        seq.append(string[:-1])

    # sort the squence
    s_len = [len(s) for s in seq]
    bubble_sort_str(s_len, seq)

    # remove repeated
    seq = remove_redu(seq)

    # count
    count_forb = 0
    for s in seq:
        count_forb += 2 ** (num_press - len(s))
    num_result = 2 ** num_press - count_forb

    order = itest + 1
    fid_out.write('Case #{}: {}\n'.format(order, num_result))
