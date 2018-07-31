'''
for package problems, record which object are selected
we should use a 2-D matrix to record, 1-D is insufficient
Conclusion: 1-D vector is insufficient
'''

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

# the effect of 'isize <--cost to bagsize'
# equals the effect of 'isize <--bagsize to cost'
# but the former is what we actually do
def is_select_obj_zo(cost, worth, bagsize, f):
    for isize in range(cost, bagsize+1):
        worth_in_item = f[isize - cost] + worth
        if worth_in_item == f[isize]:
            return True
    return False

bagsize = 15
# cost = [2, 2, 6, 5, 4]
# worth = [6, 3, 5, 4, 6]
cost = [2, 2, 6, 5, 4,3,4]
worth = [6, 3, 5, 4, 6,2,4]
obj_num = len(cost)

print('zero one package')
f = [0] * (bagsize + 1)
for iobj in range(obj_num):
	zero_one_package(cost[iobj], worth[iobj], bagsize, f)
print(f)

obj_record = [0] * obj_num
v = 14
for ind in range(obj_num):
    value_in_item = f[v-cost[ind]] + worth[ind]
    if value_in_item == f[v]:
        obj_record[ind] = 1
print(obj_record)


# for iobj in range(obj_num):
# 	Flag = is_select_obj_zo(cost[iobj], worth[iobj], bagsize, f)
# 	if Flag:
# 		obj_record[iobj] = 1
# print(obj_record)

# print('complete package')
# f = [0] * (bagsize + 1)
# for iobj in range(obj_num):
# 	complete_package(cost[iobj], worth[iobj], bagsize, f)
# print(f)
#
# obj_record = [0] * obj_num
# while f[-1]!=0:
#     for iobj in range(obj_num):
#         Flag = is_select_obj_zo(cost[iobj], worth[iobj], bagsize, f)
#         if Flag:
#             obj_record[iobj] += 1
#             cost_temp = cost[iobj]
#             print(f)
#             for isize, data in enumerate(f):
#                 if data != 0:
#                     f[isize] -= cost_temp
#                 if isize >= 10:
#                     break
# print(obj_record)
