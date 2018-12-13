'''
For small dataset, k=1, only consume one cup everyday
For large dataset,
  we can first count the expired cpu number with a forward computation
  then, we backward to count the maximum consume number
  Notice, we can consume the yogurt ahead of time
'''


def day_pass(values):
    values_new = list()
    for data in values:
        data -= 1
        if data > 0:
            values_new.append(data)
    return values_new


def dy_pass(values):
    values = [i - 1 for i in values]
    ind = 0
    while ind < len(values) and values[ind] <= 0:
        ind += 1
    values = values[ind:]
    return values


def max_yogurt(values, k):
    values.sort()
    count = 0

    while len(values) > 0:
        num_cons = min(k, len(values))
        count += num_cons
        values = values[num_cons:]
        # values = day_pass(values)
        values = dy_pass(values)

    return count


def max_yogurt_eff(values, k):
    num = len(values)

    # count the expire number each day
    day_expi = [0] * num
    for data in values:
        if data < num:
            day_expi[data - 1] += 1
        else:
            day_expi[num - 1] += 1

    # print(day_expi[::-1])

    # maximum count
    count = 0
    day_expi = day_expi[::-1]
    for order, data in enumerate(day_expi):
        if data >= k:
            count += k
            if order < num-1:
                day_expi[order + 1] += (data - k)
        else:
            count += data

    return count


in_data_file = 'A-large-practice.in'
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

    # result = max_yogurt(value_N, K)
    result = max_yogurt_eff(value_N, K)
    print('result', result)
    order = itest + 1
    fid_out.write('Case #{}: {}\n'.format(order, result))

