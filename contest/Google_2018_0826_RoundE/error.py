def gen_comp(sel, ORD, comps, num):
    if len(sel) == num:
        complains.append(sel)
        orders.append(ORD)
    else:
        base_order = len(sel)
        for order, ic in enumerate(comps):
            sel_temp = sel.copy()
            sel_temp.append(ic)
            ORD_temp = ORD.copy()
            ORD_temp.append(order + base_order)
            gen_comp(sel_temp, ORD_temp, comps[order+1:], num)


def generate_complains(comps, num):
    comp_list = []
    order_list = []
    global complains
    complains = list()
    global orders
    orders = list()
    gen_comp(comp_list, order_list, comps, num)

    return complains, orders


# comp_temp = list()
# for i in range(101):
#     num_temp = choice_comp(min_choices[i], ideal_choice, ideal_comp, num_person)
#     comp_temp.append(num_temp)

