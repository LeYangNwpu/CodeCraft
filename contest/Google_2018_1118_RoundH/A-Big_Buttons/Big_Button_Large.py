'''
For large dataset
'''

def filter_forb_prex(strs_forb):
    strs_forb_real = list()

    for istr in strs_forb:
        left_set = strs_forb.copy()
        left_set.remove(istr)

        flag = True
        for scmp in left_set:
            if len(istr) >= len(scmp):
                str_cmp = istr[:len(scmp)]
                if str_cmp == scmp:
                    flag = False
                    break
        if flag:
            strs_forb_real.append(istr)

    return strs_forb_real


def cal_win_num(seqs_forb, num_press):
    num_sub = 0
    for seq in seqs_forb:
        num_sub += 2 ** (num_press - len(seq))
    num_win = 2 ** num_press - num_sub

    return num_win


in_data_file = 'A-large-practice.in'
out_data_file = 'A-large-practice.out'

fid_in = open(in_data_file, 'r')
fid_out = open(out_data_file, 'w')


num_all = int(fid_in.readline())
print('total test samples %d' % num_all)

for itest in range(num_all):
    sline = fid_in.readline()
    num_press, num_forb = [int(s) for s in sline.split(" ")]

    seqs_forb = []
    for _ in range(num_forb):
        string = fid_in.readline()
        seqs_forb.append(string[:-1])

    seqs_forb_real = filter_forb_prex(seqs_forb)

    num_win = cal_win_num(seqs_forb_real, num_press)

    order = itest + 1
    fid_out.write('Case #{}: {}\n'.format(order, num_win))
