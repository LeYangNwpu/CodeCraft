'''
Problem:
    A binary tree topology is defined as any configuration of the tree,
    given a number of nodes, that is agnostic of node labels.
    Write an algorithmic function that tells me how many binary tree topologies are possible,
    given n nodes in the tree.
Requires:
    (1) achieve the algorithm in recursion style (not efficient)
    (2) efficient with extra space, record the topology number for each node number
'''

### solution 1 ###
# def binary_tree_topo(n):
#     if n == 0:
#         return 1
#     else:
#         number = 0
#         for i in range(n):
#             number += binary_tree_topo(i) * binary_tree_topo(n-1-i)
#         return number
#
# node_num = 5
# tree_topo_num =  binary_tree_topo(node_num)
# print('tree topology number is %d' % tree_topo_num)


### solution 2 ###

topo_doc = [1, 1]

def binary_tree_topo(n):
    if n == 0 or n == 1:
        number = topo_doc[n]
        return number
    else:
        # notice here, for node n, the value is topo_doc[n]
        for j in range(2, n+1):
            node_add = 0
            for i in range(j):
                node_add += topo_doc[i] * topo_doc[j-1-i]
            topo_doc.append(node_add)
        return topo_doc[n]

number = binary_tree_topo(5)
print(number)

