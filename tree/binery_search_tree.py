'''
reference: https://gist.github.com/thinkphp/1450738
Problem:
    construct binary search tree and traverse it
    binary search tree is a rooted binary tree,
    for which, the in-order traverse result is in non-decrease order
Requires:

Ways:
    (1)create a node class to present data,
    which consists of data, left_child, right_child
    (2)considering that the input data may out-of-order, for each value,
    we should find it proper location in a while loop
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.left_child = None
		self.right_child = None

class BST:
    def __init__(self):
        self.root = None

    def create_BST(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.data:
                    if current.left_child:
                        current = current.left_child
                    else:
                        current.left_child = Node(value)
                        break
                elif value > current.data:
                    if current.right_child:
                        current = current.right_child
                    else:
                        current.right_child = Node(value)
                        break
                else:
                    break

    def pre_order(self, current):
        if current is not None:
            print(current.data)
            self.pre_order(current.left_child)
            self.pre_order(current.right_child)

    def in_order(self, current):
        if current is not None:
            self.in_order(current.left_child)
            print(current.data)
            self.in_order(current.right_child)


tree = BST()
arr = [8,10,14,13,3,1,6,4,7,]
for i in arr:
	tree.create_BST(i)
print('previous order')
tree.pre_order(tree.root)
print('in order')
tree.in_order(tree.root)



