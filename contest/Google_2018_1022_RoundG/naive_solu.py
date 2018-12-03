def gen_data(data, N):
    x1, x2, a1, b1, c1, m1 = data

    x_set = [x1, x2]
    if N < 2:
        return x_set[:N]
    for i in range(2, N):
        data = (a1*x_set[i-1] + b1*x_set[i-2] + c1) % m1
        x_set.append(data)
    return x_set

def col_high_score(class_set, class_max_ind):
    scores = -1 * float('inf')
    for i, ind in enumerate(class_max_ind):
        if ind >= 0:
            class_temp = class_set[i]
            data = class_temp[ind]
            # print('data', data)
            scores = max(data, scores)
    return scores

def del_high_scores(high_scores, class_set, class_max_ind):
    for i, cla in enumerate(class_set):
        if cla[-1] == high_scores:
            cla_new = cla[:-1]
            class_set[i] = cla_new
            class_max_ind[i] = len(cla_new)-1
            break

def cal_scores(x_set, y_set, z_set):
    left = list()
    right = list()

    for xi, yi in zip(x_set, y_set):
        left.append(min(xi, yi) + 1)
        right.append(max(xi, yi) + 1)
    k = [zi + 1 for zi in z_set]
    num_require = k[0]

    # whether exceed range
    num_data = 0
    for li, ri in zip(left, right):
        num_data += (ri-li+1)
    if num_require > num_data:
        return 0

    # find disered data
    class_set = list()
    class_max_ind = list()
    for li, ri in zip(left, right):
        class_set.append(list(range(li, ri+1)))
        class_max_ind.append(ri-li)
    # print(class_set)

    while num_require > 1:
        high_scores = col_high_score(class_set, class_max_ind)
        print('high_scores:', high_scores)
        num_require -= 1
        del_high_scores(high_scores, class_set, class_max_ind)

    high_scores = col_high_score(class_set, class_max_ind)
    return high_scores


in_data_file = 'B-small-attempt0.in'
out_data_file = 'B-small-attempt0.out'

fid_in = open(in_data_file, 'r')
fid_out = open(out_data_file, 'w')


num_all = int(fid_in.readline())
# print('total test samples %d' % num_all)

for itest in range(1, num_all+1):
    sline = fid_in.readline()
    N, Q = [int(s) for s in sline.split(" ")]
    # print('N, Q:', N, Q)
    # x_set
    sline = fid_in.readline()
    data_x = [int(s) for s in sline.split(" ")]
    x_set = gen_data(data_x, N)
    # print(x_set)
    # y_set
    sline = fid_in.readline()
    data_y = [int(s) for s in sline.split(" ")]
    y_set = gen_data(data_y, N)
    # print(y_set)
    # z_set
    sline = fid_in.readline()
    data_z = [int(s) for s in sline.split(" ")]
    z_set = gen_data(data_z, Q)
    # print(z_set)

    result = cal_scores(x_set, y_set, z_set)
    print(result)
    fid_out.write('Case #{}: {}\n'.format(itest, result))















