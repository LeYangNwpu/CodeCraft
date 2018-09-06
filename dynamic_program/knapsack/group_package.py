import numpy as np

def zero_one_package(cost, worth, bagsize, f):
    for isize in range(bagsize, cost-1, -1):
        worth_in_item = f[isize - cost] + worth
        if worth_in_item > f[isize]:
            f[isize] = worth_in_item

def complete_package(cost, worth, bagsize, f):
    for isize in range(cost, bagsize+1):
        worth_in_item = f[isize - cost] + worth
        if worth_in_item > f[isize]:
            f[isize] = worth_in_item

def complete_package_2d(worth, cost_u, cost_v, bagsize_u, bagsize_v, f):
    for usize in range(cost_u, bagsize_u+1):
        for vsize in range(cost_v, bagsize_v+1):
            worth_in_item = f[usize-cost_u, vsize-cost_v] + worth
            if worth_in_item > f[usize, vsize]:
                f[usize, vsize] = worth_in_item

def multiple_package(cost, worth, amount, bagsize, f):
    if cost * amount >= bagsize:
        complete_package(cost, worth, bagsize, f)
    else:
        k = 1
        while k < amount:
            zero_one_package(cost*k, worth*k, bagsize, f)
            amount -= k
            k *= 2
        zero_one_package(cost*amount, worth*amount, bagsize, f)

# notice, first loop the bagsize, then loop the object in group
def group_package(worth, cost, bagsize, f):
    num_obj = len(worth)
    for isize in range(bagsize, -1, -1):
        for iobj in range(num_obj):
            if isize >= cost[iobj]:
                value_in_item = f[isize-cost[iobj]] + worth[iobj]
                if value_in_item > f[isize]:
                    f[isize] = value_in_item


bagsize = 10
cost = [2, 2, 6, 5, 4]
worth = [6, 3, 5, 4, 6]
obj_num = len(cost)


worth1 = [3, 4, 6, 5, 2]
cost1 = [1, 3, 2, 4, 4]
worth2 = [4, 3, 5, 2]
cost2 = [3, 2, 4, 4]
worth3 = [6, 2, 5, 4, 3]
cost3 = [4, 4, 2, 1, 3]
bagsize = 10
print('group object')
f = [0] * (bagsize + 1)
worth_cost = ((worth1, cost1), (worth2, cost2), (worth3, cost3))
for igroup in range(len(worth_cost)):
    data_temp = worth_cost[igroup]
    worth = data_temp[0]
    cost = data_temp[1]
    group_package(worth, cost, bagsize, f)
print(f[1:])

