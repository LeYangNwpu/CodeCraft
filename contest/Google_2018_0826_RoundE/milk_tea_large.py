'''
Questions:
    There are N persons, each needs a cup of milktea
    For milktea, there are P binary options
    In addition, there are M forbidden choices that will not be offered
    Shakti want to buy the same kind of milktea for all the N persons
    Calculate the minimum complaint number
    Small dataset: 1 ≤ N ≤ 10. 1 ≤ M ≤ min(10, 2P - 1). 1 ≤ P ≤ 10.
    Large dataset: 1 ≤ N ≤ 100. 1 ≤ M ≤ min(100, 2P - 1). 1 ≤ P ≤ 100.

Analyse:
    As for small dataset, we can recursively enumerate all potential choices
      calculate the complaint number for each choice, then select the minimum number
    As for large dataset,
      (1) we should notice M ≤ 100, indicating that if we generate 101 choices,
      there must be at least one legal choice
      (2) For the length k, if we find out the minimum 101 choice T_k
      for the length k+1, each element in the minimum choice set should start with on choice in T_k
      Consequently, we can generate 101 minimum choices, add 0 or 1 after each choice,
      find out the new 101 minimum choices. In a iterative manner, we can find the potential 101 choices.
      Finally, we select one with minimum complaint

Ref:
    https://code.google.com/codejam/contest/4394486/dashboard#s=p1&a=1
'''

import numpy as np

'''
We calculate the ideal option, along with the ideal complaint number
This will facilite the calculation.
'''
def idea_option(pref_list, num_option, num_person):
    pref_hist = np.zeros(num_option)
    # count person number to add this option
    for data in pref_list:
        pref_hist += data

    ideal_choice = np.zeros(num_option)
    num_comp = np.zeros(num_option)
    num_half = num_person / 2.0
    for i in range(len(pref_hist)):
        data = pref_hist[i]
        if data > num_half:
            ideal_choice[i] = 1
            num_comp[i] = num_person - data
        else:
            num_comp[i] = data
    return ideal_choice, num_comp


'''
Recursive method is a good manner
Use global variable possi_choices is a not bad manner, is there a better one?
'''
def gene_possi_choices(num_opt, seq):
    seq_temp = seq.copy()
    if num_opt > 0:
        seq_temp.append(0)
        gene_possi_choices(num_opt - 1, seq_temp)
        seq.append(1)
        gene_possi_choices(num_opt - 1, seq)
    else:
        if seq not in forbidden:
            possi_choices.append(seq)


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


'''
Select 101 minimum choices 
'''
def cal_min_choices(possi_choices, sort_order):
    choices = list()
    for iord in sort_order:
        choices.append(possi_choices[iord])
    return choices


'''
for potential choices, select the minimun 101 choices
np.argsort() is a useful method
'''
def select_min_comps(possi_choices, ideal_choice, ideal_comp, num_person):
    num_choice = len(possi_choices)
    comps = np.ones(num_choice) * float('inf')
    for i in range(num_choice):
        comps[i] = choice_comp(possi_choices[i], ideal_choice, ideal_comp, num_person)

    min_comp = comps.min()
    # for large data
    sort_order = np.argsort(comps)

    sort_order = list(sort_order)
    min_101_choices = cal_min_choices(possi_choices, sort_order[:101])

    return min_101_choices, min_comp


def add_option(choices):
    res = list()
    for cho in choices:
        data_temp = cho.copy()
        data_temp.append(0)
        res.append(data_temp)
        data_temp = cho.copy()
        data_temp.append(1)
        res.append(data_temp)

    return res


def filter_forbid(min_101_choices, forbidden):
    res = list()
    for cho in min_101_choices:
        if cho not in forbidden:
            res.append(cho)
    return res


in_data_file = 'B-large-practice.in'
out_data_file = 'B-large-practice.out'

fid_in = open(in_data_file, 'r')
fid_out = open(out_data_file, 'w')

num_all = int(fid_in.readline())
print('total test samples %d' % num_all)

for itest in range(num_all):
    sline = fid_in.readline()
    [num_person, num_forb, num_option] = [int(s) for s in sline.split(" ")]

    preference = list()

    for iline in range(num_person):
        sline = fid_in.readline()
        data = [int(i) for i in sline[:-1]]
        data_np = np.asarray(data)
        preference.append(data_np)

    ideal_choice, ideal_comp = idea_option(preference, num_option, num_person)

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
        result = ideal_comp.sum()
    else:
        # 'idea choice in forbid'
        if num_option > 7:
            num_opt = 7
        else:
            num_opt = num_option

        global possi_choices
        possi_choices = list()
        gene_possi_choices(num_opt, seq=list())

        min_101_choices, min_comp = select_min_comps(possi_choices, ideal_choice, ideal_comp, num_person)
        # for small data
        if num_option <= 7:
            result = min_comp
        else:
            for iopt in range(8, num_option+1):
                pote_202_choices = add_option(min_101_choices)
                min_101_choices, min_comp = select_min_comps(pote_202_choices, ideal_choice, ideal_comp, num_person)
                # print(iopt, 'min_comp: ', min_comp)
            # filter forbidden options
            min_real_choices = filter_forbid(min_101_choices, forbidden)
            # this should be abstracted as a function
            # cal minimum number
            num_choice = len(min_real_choices)
            comps_res = np.ones(num_choice) * float('inf')
            for i in range(num_choice):
                comps_res[i] = choice_comp(min_real_choices[i], ideal_choice, ideal_comp, num_person)

            result = comps_res.min()

    result = int(result)
    print(result)
    order = itest + 1
    fid_out.write('Case #{}: {}\n'.format(order, result))


'''
Here we record one unsuccessful but interesting attempts
Idea:
    We first calculate the ideal choice and the fewest complaints
    Then we sort the complaint and corresponding complaint
    We inverse the choice one by one, attempt to find the best choice not in forbidden
    Precisely, 
      we first try to inverse one choice, check whether each choice in forbidden
      then, we try to inverse two choices, check whether each choice in forbidden
      ONCE we find out one choice that is not forbidden, we think this is the best choice
    In fact, this method suppose "inverse one choice must better than inverse two choices", which is not tenable
'''

# def gen_comp(sel, comps, num):
#     if len(sel) == num:
#         gen_results.append(sel)
#     else:
#         for order, ic in enumerate(comps):
#             sel_temp = sel.copy()
#             sel_temp.append(ic)
#             gen_comp(sel_temp, comps[order+1:], num)
#
#
# def generate_complains(comps, num):
#     comp_list = []
#     global gen_results
#     gen_results = list()
#     gen_comp(comp_list, comps, num)
#     complains = gen_results
#
#     gen_results = list()
#     ord_list = []
#     ords = range(len(comps))
#     gen_comp(ord_list, ords, num)
#     orders = gen_results
#
#     return complains, orders
#
#
# def sort_comps(comps):
#     indexs = np.argsort(comps)
#     return indexs
#
#
# def inv_data(data):
#     if data == 1:
#         return 0
#     elif data == 0:
#         return 1
#
#
# def check_suitable(orders, forbidden, comp_indexs, ideal_choice):
#     ideal_choice = list(ideal_choice)
#     for order in orders:
#         choice = ideal_choice.copy()
#         for ind in order:
#             index = comp_indexs[ind]
#             choice[index] = inv_data(choice[index])
#         if choice not in forbidden:
#             return order
#     # all the cases are unsuitable
#     return None
#
#
# def cal_comp_num(order, comp_indexs, ideal_comp, num_per):
#     print('ideal_comp:', ideal_comp)
#     print('comp_indexs:', comp_indexs)
#     comp = ideal_comp.copy()
#     for ind in order:
#         index = comp_indexs[ind]
#
#         comp[index] = num_per - comp[index]
#     print('real comp', comp)
#     return comp.sum()
#
#
# def factorial(num):
#     res = 1
#     while num > 1:
#         res *= num
#         num -= 1
#     return res
#
#
# def cal_selection_num(who_num, sel_num):
#     return factorial(who_num) / (factorial(sel_num) * factorial(who_num - sel_num))
#
#
# def cal_min_num(num_forb, num_choice):
#     for inum in range(1, num_choice+1):
#         num_selection = cal_selection_num(num_choice, inum)
#         if num_selection > num_forb:
#             break
#     return inum
#
# in_data_file = 'B-test.in'
# out_data_file = 'B-test.out'
#
# fid_in = open(in_data_file, 'r')
# fid_out = open(out_data_file, 'w')
#
# num_all = int(fid_in.readline())
# print('total test samples %d' % num_all)
#
# for itest in range(num_all):
#     sline = fid_in.readline()
#     [num_per, num_forb, num_opt] = [int(s) for s in sline.split(" ")]
#
#     preference = list()
#
#     for iline in range(num_per):
#         sline = fid_in.readline()
#         data = [int(i) for i in sline[:-1]]
#         data_np = np.asarray(data)
#         preference.append(data_np)
#
#     ideal_choice, ideal_comp = idea_option(preference, num_opt, num_per)
#
#     print('ideal_choice')
#     print(ideal_choice)
#     print('ideal_comp')
#     print(ideal_comp)
#
#     # forbidden sequences
#     global forbidden
#     forbidden = list()
#     for iline in range(num_forb):
#         sline = fid_in.readline()
#         data = [int(i) for i in sline[:-1]]
#         forbidden.append(data)
#
#     # check whether idea choice suitable
#     ideal_choice_list = list(ideal_choice)
#     if ideal_choice_list not in forbidden:
#         num_comp = ideal_comp.sum()
#         print('minimum complaint number:', num_comp)
#         # continue
#     else:
#         print('idea choice in forbid')
#         # comps = [1, 1, 2, 3, 5, 5, 6]
#         # make mistake here, we should use comps_change to sort and calculate the index
#         comps_change = num_per - ideal_comp
#         comps = list(comps_change)
#         comps.sort()
#         comp_indexs = sort_comps(comps)
#         print('comps:', comps)
#         potential_min = list()
#         num_min = cal_min_num(num_forb, num_opt)
#         print('num_min:', num_min)
#         for num in range(1, num_min+9):
#             print('generate comps, iter: ', num)
#             complains, orders = generate_complains(comps, num)
#             print('complains:', complains)
#             print('orders:', orders)
#             suit_order = check_suitable(orders, forbidden, comp_indexs, ideal_choice)
#             if suit_order is not None:
#                 # suit_order = orders[suit_ord]
#                 num_comp_temp = cal_comp_num(suit_order, comp_indexs, ideal_comp, num_per)
#                 potential_min.append(num_comp_temp)
#                 # print('minimum complaint number:', num_comp)
#                 # break
#         potential_min_np = np.asarray(potential_min)
#         print('potential_min_np')
#         print(potential_min_np)
#         num_comp = potential_min_np.min()
#
#
#     order = itest + 1
#     fid_out.write('Case #{}: {}\n'.format(order, int(num_comp)))


