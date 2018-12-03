def det_zero(data):
    count = 0
    while (count < len(data)) and (data[count] == 0):
        count += 1
    if count == 0:
        return 0, data
    else:
        # 0 * 1
        num_two_zero = count * (count - 1) / 2
        if count > 2:
            num_three_zero = count * (count -1) * (count - 2) / 6
        # 0 * 0
        num_data = len(data[count:])
        zero_whole_num = num_two_zero * num_data + num_three_zero
        # print('num_three_zero', num_three_zero)
        return zero_whole_num, data[count:]


def triplet_num(data):
    data.sort()

    count_zero, data_new = det_zero(data)
    print(data_new)

    count = 0
    if len(data_new) > 0:
        largest_num = data_new[-1]
        num_data = len(data_new)
        for i in range(num_data-2):
            for j in range(i+1, num_data-1):
                print('i,j', i,j)
                mul = data_new[i] * data_new[j]
                for k in range(j+1, num_data):
                    if mul == data_new[k]:
                        count += 1
                # val_set = data_new[j+1:]
                # print('val_set', val_set)
                # if mul in val_set:
                #     count += 1
                # if mul > largest_num:
                #     break

    num_whole = int(count + count_zero)
    return num_whole

# data = [0,0,0,0]
# print(triplet_num(data))

in_data_file = 'A-large.in'
out_data_file = 'A-large.out'

fid_in = open(in_data_file, 'r')
fid_out = open(out_data_file, 'w')

num_all = int(fid_in.readline())
print('total test samples %d' % num_all)

for itest in range(1, num_all+1):
    irow = int(fid_in.readline())
    # print('sample {} contains {} data'.format(itest, irow))
    sline = fid_in.readline()
    data = [int(s) for s in sline.split(" ")]
    print(data)
    count = triplet_num(data)
    fid_out.write('Case #{}: {}\n'.format(itest, count))
