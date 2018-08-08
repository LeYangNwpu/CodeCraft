'''
Problem:
    0 1 package problem.
    Giben n objects with weights {w1, w2, ..., wn} and values {v1, v2, ..., vn},
    Suppose we have a package which can hold the weight N at most,
    Which objects should be put into the package, so as to obtain the most total value?
Ways:
    dynamic program
    construct the object-volume table from bottom to top, from left to right
    formulation: f[i,j] = max{f[i-1,j], f[i+1,j-weights[i]]+values[i]}
Requires:

Ref:
    https://blog.csdn.net/mu399/article/details/7722810
'''

import numpy as np


# bulid the table from left to right, from upper to lower
def get_01_package(weight, value, bag_size):
    num_obj = len(weight)
    arr_val = np.zeros((num_obj, bag_size))
    # loop each size
    for jcol in range(bag_size):
        # loop each object
        for irow in range(num_obj):
            if weight[irow] > jcol+1:
                # package irow can not hold item
                if irow == 0:
                    arr_val[irow, jcol] = 0
                else:
                    arr_val[irow, jcol] = arr_val[irow-1, jcol]
            else:
                # package irow can hold item
                if irow == 0:
                    arr_val[irow, jcol] = value[irow]
                else:
                    value_in_item = value[irow] + arr_val[irow-1, jcol-weight[irow]]
                    arr_val[irow, jcol] = value_in_item if value_in_item > arr_val[irow-1, jcol] else arr_val[irow-1, jcol]
    return arr_val

# # bulid the table from left to right, from lower to upper
# def get_01_package(weight, value, bag_size):
#     num_obj = len(weight)
#     arr_val = np.zeros((num_obj, bag_size))
#     # loop each size
#     for jcol in range(bag_size):
#         # loop each object
#         for irow in range(num_obj-1,-1, -1):
#             if weight[irow] > jcol+1:
#                 # package irow can not hold item
#                 if irow == num_obj-1:
#                     arr_val[irow, jcol] = 0
#                 else:
#                     arr_val[irow, jcol] = arr_val[irow+1, jcol]
#             else:
#                 # package irow can hold item
#                 if irow == num_obj - 1:
#                     arr_val[irow, jcol] = value[irow]
#                 else:
#                     value_in_item = value[irow] + arr_val[irow+1, jcol-weight[irow]]
#                     arr_val[irow, jcol] = value_in_item if value_in_item > arr_val[irow+1, jcol] else arr_val[irow+1, jcol]
#     return arr_val

bag_size = 12
weight = [2, 2, 6, 5, 4]
value = [6, 3, 5, 4, 6]
print(get_01_package(weight, value, bag_size))
