'''

'''

class Node:
	def __init__(self,data):
		self.data = data
		self.left_child = None
		self.right_child = None

# pre_order_seq = ‘AB#D##C##’
def create_bi_tree(tree):
	char = input('input a char:')
	if char == '#':
		tree = None
	else:
		if not tree:
			return
		tree.data = char
		create_bi_tree(tree.left_child)
		create_bi_tree(tree.right_child)

root_node = Node('A')
create_bi_tree(root_node)
print('finish')

