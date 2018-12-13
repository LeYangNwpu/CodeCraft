import numpy as np


def idea_option(pref_list, num_opt, num_per):
    pref_hist = np.zeros(num_opt)
    # count person number to add this option
    for data in pref_list:
        pref_hist += data

    ideal_choice = np.zeros(num_opt)
    num_comp = np.zeros(num_opt)
    num_half = num_per / 2.0
    for i in range(len(pref_hist)):
        data = pref_hist[i]
        if data > num_half:
            ideal_choice[i] = 1
            num_comp[i] = num_per - data
        else:
            num_comp[i] = data
    return ideal_choice, num_comp


def choice_comp(choice_cur, choice_idea, comp_idea, num_per):
    count = 0

    num_opt = len(choice_cur)
    for i in range(num_opt):
        data_cur = choice_cur[i]
        data_idea = choice_idea[i]
        if data_cur == data_idea:
            # print('reach idea')
            count += comp_idea[i]
        else:
            count += (num_per - comp_idea[i])

    return count


def gene_possi_choices(num_opt, seq):
    seq_temp = seq.copy()
    if num_opt > 0:
        seq_temp.append(0)
        gene_possi_choices(num_opt - 1, seq_temp)
        seq.append(1)
        gene_possi_choices(num_opt - 1, seq)
    else:
        # print(seq)
        if seq not in forbidden:
            possi_choices.append(seq)


in_data_file = 'B-small-practice2.in'
out_data_file = 'B-small-practice2.out'

fid_in = open(in_data_file, 'r')
fid_out = open(out_data_file, 'w')

num_all = int(fid_in.readline())
print('total test samples %d' % num_all)

for itest in range(num_all):
    sline = fid_in.readline()
    [num_per, num_forb, num_opt] = [int(s) for s in sline.split(" ")]

    preference = list()

    for iline in range(num_per):
        sline = fid_in.readline()
        data = [int(i) for i in sline[:-1]]
        data_np = np.asarray(data)
        preference.append(data_np)

    ideal_choice, ideal_comp = idea_option(preference, num_opt, num_per)
    print('ideal_choice')
    print(ideal_choice)
    print('ideal_comp')
    print(ideal_comp)

    # forbidden sequences
    global forbidden
    forbidden = list()
    for iline in range(num_forb):
        sline = fid_in.readline()
        data = [int(i) for i in sline[:-1]]
        forbidden.append(data)

    global possi_choices
    possi_choices = list()
    gene_possi_choices(num_opt, seq=list())

    num_choice = len(possi_choices)
    comps = np.ones(num_choice) * float('inf')
    for i in range(num_choice):
        comps[i] = choice_comp(possi_choices[i], ideal_choice, ideal_comp, num_per)
    result = int(comps.min())
    print('comps')
    print(comps.shape)
    print('comps.min():', comps.min())

    order = itest + 1
    fid_out.write('Case #{}: {}\n'.format(order, result))

