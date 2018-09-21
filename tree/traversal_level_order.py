'''
Problem:
	Level Order Tree Traversal
Way:
	Use two functions
	One is to print all nodes at a given level (print_given_level),
	The other is to print level order traversal of the tree (print_level_order).
Ref:
	https://www.geeksforgeeks.org/level-order-tree-traversal/
'''

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

# measure the tree height
def height(root):
	if root is None:
		return 0
	left_hei = height(root.left)
	right_hei = height(root.right)
	if left_hei >= right_hei:
		return left_hei + 1
	else:
		return right_hei + 1

# for a given level, print all node value
def print_given_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.value)
    elif level > 1:
        print_given_level(root.left, level-1)
        print_given_level(root.right, level-1)

# print all level
def print_level_order(root):
    tree_hei = height(root)
    for i in range(1, tree_hei+1):
        print_given_level(root, i)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_level_order(root)


