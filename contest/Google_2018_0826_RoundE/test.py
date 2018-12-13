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





### complains
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
# comps = [1,2,3,4,5,6]
# num = 3
# complains, orders = generate_complains(comps, num)
# print('complains')
# print(complains)
# print('orders')
# print(orders)

