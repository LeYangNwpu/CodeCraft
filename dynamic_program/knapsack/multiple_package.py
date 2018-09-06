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

bagsize = 10
cost = [2, 2, 6, 5, 4]
worth = [6, 3, 5, 4, 6]
obj_num = len(cost)
amount = [3, 2, 3, 1, 4]
print('multiple package')
f = [0] * (bagsize + 1)
for iobj in range(obj_num):
	multiple_package(cost[iobj], worth[iobj], amount[iobj], bagsize, f)
print(f[1:])
