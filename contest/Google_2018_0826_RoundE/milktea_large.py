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


def gen_comp(sel, comps, num):
    if len(sel) == num:
        gen_results.append(sel)
    else:
        for order, ic in enumerate(comps):
            sel_temp = sel.copy()
            sel_temp.append(ic)
            gen_comp(sel_temp, comps[order+1:], num)


def generate_complains(comps, num):
    comp_list = []
    global gen_results
    gen_results = list()
    gen_comp(comp_list, comps, num)
    complains = gen_results

    gen_results = list()
    ord_list = []
    ords = range(len(comps))
    gen_comp(ord_list, ords, num)
    orders = gen_results

    return complains, orders


def sort_comps(comps):
    indexs = np.argsort(comps)
    return indexs


def inv_data(data):
    if data == 1:
        return 0
    elif data == 0:
        return 1


def check_suitable(orders, forbidden, comp_indexs, ideal_choice):
    ideal_choice = list(ideal_choice)
    for order in orders:
        choice = ideal_choice.copy()
        for ind in order:
            index = comp_indexs[ind]
            choice[index] = inv_data(choice[index])
        if choice not in forbidden:
            return order
    # all the cases are unsuitable
    return None


def cal_comp_num(order, comp_indexs, ideal_comp, num_per):
    print('ideal_comp:', ideal_comp)
    print('comp_indexs:', comp_indexs)
    comp = ideal_comp.copy()
    for ind in order:
        index = comp_indexs[ind]

        comp[index] = num_per - comp[index]
    print('real comp', comp)
    return comp.sum()


def factorial(num):
    res = 1
    while num > 1:
        res *= num
        num -= 1
    return res


def cal_selection_num(who_num, sel_num):
    return factorial(who_num) / (factorial(sel_num) * factorial(who_num - sel_num))


def cal_min_num(num_forb, num_choice):
    for inum in range(1, num_choice+1):
        num_selection = cal_selection_num(num_choice, inum)
        if num_selection > num_forb:
            break
    return inum

in_data_file = 'B-test.in'
out_data_file = 'B-test.out'

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

    # check whether idea choice suitable
    ideal_choice_list = list(ideal_choice)
    if ideal_choice_list not in forbidden:
        num_comp = ideal_comp.sum()
        print('minimum complaint number:', num_comp)
        # continue
    else:
        print('idea choice in forbid')
        # comps = [1, 1, 2, 3, 5, 5, 6]
        # make mistake here, we should use comps_change to sort and calculate the index
        comps_change = num_per - ideal_comp
        comps = list(comps_change)
        comps.sort()
        comp_indexs = sort_comps(comps)
        print('comps:', comps)
        potential_min = list()
        num_min = cal_min_num(num_forb, num_opt)
        print('num_min:', num_min)
        for num in range(1, num_min+9):
            print('generate comps, iter: ', num)
            complains, orders = generate_complains(comps, num)
            print('complains:', complains)
            print('orders:', orders)
            suit_order = check_suitable(orders, forbidden, comp_indexs, ideal_choice)
            if suit_order is not None:
                # suit_order = orders[suit_ord]
                num_comp_temp = cal_comp_num(suit_order, comp_indexs, ideal_comp, num_per)
                potential_min.append(num_comp_temp)
                # print('minimum complaint number:', num_comp)
                # break
        potential_min_np = np.asarray(potential_min)
        print('potential_min_np')
        print(potential_min_np)
        num_comp = potential_min_np.min()


    order = itest + 1
    fid_out.write('Case #{}: {}\n'.format(order, int(num_comp)))






