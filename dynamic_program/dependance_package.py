def find_depend(dependance, idep):
	index = []
	for ind, idata in enumerate(dependance):
		if idata == idep:
			index.append(ind)
	return index

# separate object into groups
def separate_group(worth, importance, dependance, obj_num):
    group_sets = []
    for idep in range(obj_num):
        group_set = []
        index = find_depend(dependance, idep+1)
        if len(index) > 0:
            for iobj in index:
                group_set.append([worth[iobj], importance[iobj]])
        else:
            order_dep = idep + 1
            print('no object depends on %d' % order_dep)
        if dependance[idep] == 0:
            # the domenent object
            group_set.append([worth[idep], importance[idep]])
        if len(group_set) > 0:
            group_sets.append(group_set)
    return group_sets


def zero_one_package(f, bagsize, cost, worth):
    for isize in range(bagsize, cost-1, -1):
        value_in_item = f[isize-cost] + worth
        if value_in_item > f[isize]:
            f[isize] = value_in_item


# zero one package in a dependance set
def group_worth(data_in, bagsize):
    base_obj = data_in[-1]
    num_val = len(data_in)
    if num_val < 1:
        return []
    cost = []
    worth = []
    for idata in data_in[:-1]:
        cost.append(idata[0])
        worth.append(idata[0] * idata[1])
    bagsize = bagsize - base_obj[0]
    f = [0] * (bagsize + 1)
    # f[1] =
    for iobj in range(num_val-1):
        zero_one_package(f, bagsize, cost[iobj], worth[iobj])
    worth_base = base_obj[0] * base_obj[1]
    for i in range(bagsize + 1):
        f[i] += worth_base
    f.insert(0, 0)
    print(f)




    # print('length data: ', len(price), len(importance))
    # print(num_val-1)
    # value = [0] * num_val
    # value[1] = base_obj[0] * base_obj[1]
    # for iobj in range(num_val-1, 0, -1):
    #     if iobj >= price[iobj]:
    #         value_in_item = value[iobj-price[iobj]+1] + price[iobj] * importance[iobj]
    #         if value_in_item > value[iobj]:
    #             value[iobj] = value_in_item
    # return value



budget = 1000
obj_num = 5
worth = [800, 100, 200, 400, 500]
importance = [2, 5, 6, 3, 2]
dependance = [0, 1, 1, 0, 0]

groups_data = separate_group(worth, importance, dependance, obj_num)
print(groups_data)
group_worth(groups_data[0], budget)

