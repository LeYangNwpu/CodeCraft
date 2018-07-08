'''
Problem:
    invert a binary tree. For each node, exchange it left node and right node
Requires:

Ways:
    (1) recursion solve the problem
    (2) non-recursion solution relies on queue, push and pop.
    ref: http://www.cnblogs.com/grandyang/p/4572877.html
'''

class Node:
	def __init__(self, value):
		self.data = value
		self.left_child = None
		self.right_child = None

def invert_binary_tree(node):
	if node is None:
		return
	else:
		# if (node.left_child is None) and (node.right_child is None):
		# 	return
		# else:
			node_temp = node.left_child
			node.left_child = node.right_child
			invert_binary_tree(node.left_child)
			node.right_child = node_temp
			invert_binary_tree(node.right_child)

def inorder(root):
    if root is not None:
        inorder(root.left_child)
        print(root.data,)
        inorder(root.right_child)

root = Node(9)
root.left_child = Node(6)
root.right_child = Node(3)
root.left_child.left_child = Node(5)
root.left_child.right_child = Node(7)
root.left_child.right_child.left_child = Node(15)
root.left_child.right_child.right_child = Node(1)
root.right_child.left_child = Node(2)

print('inorder')
print(inorder(root))
invert_binary_tree(root)
print('inorder after invert')
print(inorder(root))
