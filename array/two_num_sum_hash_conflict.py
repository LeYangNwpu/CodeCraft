'''
Problem:
	two number sum problem
Requires:
    use hash table, dispose conflict
'''

MOD = 11
NULLVALUE = -32768


class Node:
    def __init__(self, data_value=None):
        self.data_value = data_value
        self.next_ptr = None

# hash function: mod
def hash(value):
    return value % MOD


def insert_hash(hash_table, value):
    add = hash(value)
    node_exit = hash_table[add]
    # distinguish this location is a first node or a series of linked node
    Flag_Found = False
    while node_exit.data_value != NULLVALUE:
        Flag_Found = True
        if node_exit.next_ptr is not None:
            node_exit = node_exit.next_ptr
        else:
            break
    # linked node
    if Flag_Found:
        node_exit.next_ptr = Node(value)
    # first node
    else:
        hash_table[add] = Node(value)


# data = np.array([3, -1, -6, 5, 2, -4, 8, 11, 13])
data = [13, 5, 12, 1, 8, 11, 9, 6, 4, 16]
sum = 17

# initialize hash table with Node object
node_init = Node(NULLVALUE)
pos_hash_table = [node_init] * 11

proper_pairs = []
for idata in data:
    factor_another = sum - idata
    add = hash(factor_another)
    node_add = pos_hash_table[add]
    # empty node
    if node_add.data_value == NULLVALUE:
        insert_hash(pos_hash_table, idata)
    # a series of linked node
    else:
        Flag_Found = False
        while node_add.data_value != NULLVALUE:
            if node_add.data_value == factor_another:
                proper_pairs.append([idata, factor_another])
                Flag_Found = True
                break
            else:
                if node_add.next_ptr is not None:
                    node_add = node_add.next_ptr
                else:
                    break
        # record current data
        if not Flag_Found:
            insert_hash(pos_hash_table, idata)

print(proper_pairs)

# # show the created hash table
# print('the created hash table is:\r\n')
# for inode, node in enumerate(pos_hash_table):
#     print('the %d node' % inode)
#     while True:
#         print(node.data_value)
#         if node.next_ptr is not None:
#             node = node.next_ptr
#         else:
#             break
