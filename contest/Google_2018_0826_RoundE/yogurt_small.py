'''
For small dataset, k=1, only consume one cup everyday
'''


def max_yogurt(a):

    count = 0

    while len(a) > 0:
        # find the miniest data
        day_min = float('inf')
        ord_del = None
        for order, ai in enumerate(a):
            if ai < day_min:
                day_min = ai
                ord_del = order

        count += 1
        del a[ord_del]
        a_new = list()
        for a_temp in a:
            a_temp -= 1
            if a_temp > 0:
                a_new.append(a_temp)
        a = a_new
    return count


in_data_file = 'A-small-attempt0.in'
out_data_file = 'A-small-attempt0-test.out'

fid_in = open(in_data_file, 'r')
fid_out = open(out_data_file, 'w')

num_all = int(fid_in.readline())
print('total test samples %d' % num_all)

for itest in range(num_all):
    N_K_line = fid_in.readline()
    N, K = [int(s) for s in N_K_line.split(" ")]
    Ai_line = fid_in.readline()
    value_N = [int(s) for s in Ai_line.split(" ")]

    result = max_yogurt(value_N)
    print('result', result)
    order = itest + 1
    fid_out.write('Case #{}: {}\n'.format(order, result))

