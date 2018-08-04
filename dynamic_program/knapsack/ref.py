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
        for jsize in range(bound, bagsize+1):
            f_in_item = f[jsize-cost[iobj]] + value[iobj]
            if f_in_item > f[jsize]:
                f[jsize] = f_in_item
    return f[1:]

bag_size = 10
cost = [2, 2, 6, 5, 4]
worth = [6, 3, 5, 4, 6]

f = complete_knapsack(cost, worth, bag_size)
print(f)
