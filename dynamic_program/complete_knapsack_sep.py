import copy

def sum_cost(cost):
    cost_sum = copy.deepcopy(cost)
    for iobj in range(len(cost) - 2, -1, -1):
        cost_sum[iobj] += cost_sum[iobj + 1]
    return cost_sum


def complete_knapsack(cost, value, bagsize):
    obj_num = len(value)
    f = [0] * (bagsize + 1)
    cost_sum = sum_cost(cost)
    for iobj in range(obj_num):
        # ensure the volume of bag can hold the object
        bound = max(bagsize-cost_sum[iobj], cost[iobj])
        # jsize changes from bound to bagsize,
        # considering each object can be selected more time
        for jsize in range(bagsize, bound - 1, -1):
            f_in_item = f[jsize-cost[iobj]] + value[iobj]
            if f_in_item > f[jsize]:
                f[jsize] = f_in_item
    return f[1:]

# # version 2
# # expand the cost and worth of each object with factor 2 ** k
# # then, solve the problem with zero-one-package method
# def seperate_obj(cost, worth, bagsize):
#     cost_sep = []
#     worth_sep = []
#     # use zip for iterate two variables
#     for icost, iworth in zip(cost, worth):
#         num = 1
#         cost_ori = icost
#         worth_ori = iworth
#         while cost_ori * num < bagsize:
#             cost_sep.append(cost_ori * num)
#             worth_sep.append(worth_ori * num)
#             num *= 2
#     return cost_sep, worth_sep
# cost_sep, worth_sep = seperate_obj(cost, worth, bag_size)
# f = complete_knapsack(cost_sep, worth_sep, bag_size)


bag_size = 10
cost = [2, 2, 6, 5, 4]
worth = [6, 3, 5, 4, 6]

cost_sep, worth_sep = seperate_obj(cost, worth, bag_size)
print(cost_sep)
print(worth_sep)
f = complete_knapsack(cost_sep, worth_sep, bag_size)
print(f)


