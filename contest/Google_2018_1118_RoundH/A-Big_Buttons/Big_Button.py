'''
For small dataset
'''

# generate sequences
def buttons(press_str):
    if len(press_str) == num_press:
        seqs_all.append(press_str)
        return
    else:
        buttons(press_str + 'R')
        buttons(press_str + 'B')


def filter_forb(seqs_all, seqs_forb):
    count = 0
    for temps in seqs_all:
        flag = True
        for forbs in seqs_forb:
            seq_cmp = temps[:len(forbs)]
            if seq_cmp == forbs:
                flag = False
                break
        if not flag:
            count += 1
    return len(seqs_all)-count

in_data_file = 'A-small-practice.in'
out_data_file = 'A-small-practice.out'

fid_in = open(in_data_file, 'r')
fid_out = open(out_data_file, 'w')


num_all = int(fid_in.readline())
print('total test samples %d' % num_all)

for itest in range(num_all):
    sline = fid_in.readline()
    num_press, num_forb = [int(s) for s in sline.split(" ")]

    global seqs_all
    seqs_all = list()
    press_str = ''
    buttons(press_str)

    seqs_forb = []
    for _ in range(num_forb):
        string = fid_in.readline()
        seqs_forb.append(string[:-1])

    num_win = filter_forb(seqs_all, seqs_forb)

    order = itest + 1
    fid_out.write('Case #{}: {}\n'.format(order, num_win))





