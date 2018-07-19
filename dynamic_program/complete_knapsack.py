import numpy as np
import copy

def sum_cost(cost):
    cost_sum = copy.deepcopy(cost)
    for iobj in range(len(cost) - 2, -1, -1):
        cost_sum[iobj] += cost_sum[iobj + 1]
    return cost_sum

# version 3
# similar with zero one knapsack, only change the variation jsize
def complete_knapsack(cost, value, bagsize):
    obj_num = len(value)
    f = [0] * (bagsize + 1)
    cost_sum = sum_cost(cost)
    for iobj in range(obj_num):
        # ensure the volume of bag can hold the object
        bound = max(bagsize-cost_sum[iobj], cost[iobj])
        # jsize changes from bound to bagsize,
        # considering each object can be selected more time
        for jsize in range(bound, bagsize+1):
            f_in_item = f[jsize-cost[iobj]] + value[iobj]
            if f_in_item > f[jsize]:
                f[jsize] = f_in_item
    return f[1:]


# version 2
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


# version 1
# a naive implementation with 2-dimension array
# def complete_knapsack(cost, worth, bag_size):
#     num_obj = len(cost)
#     f = np.zeros((num_obj, bag_size+1))
#     for isize in range(bag_size+1):
#         for iobj in range(num_obj-1, -1, -1):
#             max_k = int(isize / cost[iobj])
#             max_worth = 0
#             for k in range(max_k, -1, -1):
#                 if iobj == num_obj-1:
#                     temp_worth = k * worth[iobj]
#                 else:
#                     temp_worth = k * worth[iobj] + f[iobj+1, isize-k*cost[iobj]]
#                 if temp_worth > max_worth:
#                     max_worth = temp_worth
#             f[iobj, isize] = max_worth
#     return f[:,1:]


bag_size = 10
cost = [2, 2, 6, 5, 4]
worth = [6, 3, 5, 4, 6]

f = complete_knapsack(cost, worth, bag_size)
print(f)




