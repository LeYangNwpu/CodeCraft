# Yogurt
def day_pass(value_in):
    value_out = []
    for data in value_in:
        data -= 1
        if data > 0:
            value_out.append(data)
    return value_out


def max_yogurt(n, k, value_n):
    cons_num = 0
    while len(value_n) > 0:
        num_temp = min(k, len(value_n))
        cons_num += num_temp
        # remove drink yogurt
        value_n = value_n[num_temp:]
        # decrease time
        value_n = day_pass(value_n)
    return cons_num

in_data_file = 'A-large.in'
out_data_file = 'A-large-practice.out'

fid_in = open(in_data_file, 'r')
fid_out = open(out_data_file, 'w')

num_all = int(fid_in.readline())
print('total test samples %d' % num_all)

for itest in range(num_all):
    N_K_line = fid_in.readline()
    N, K = [int(s) for s in N_K_line.split(" ")]
    Ai_line = fid_in.readline()
    value_N = [int(s) for s in Ai_line.split(" ")]
    value_N.sort()
    result = max_yogurt(N, K, value_N)
    print('result', result)
    order = itest + 1
    fid_out.write('Case #{}: {}\n'.format(order, result))


