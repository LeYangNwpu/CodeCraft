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
    (3)we suppose each value in the binary search tree is unique
'''

'''
difficulty: delete node from the BST, maybe need to record parent node
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

    def look_up(self, value, node):
        if node.data == value:
            print('find value %d' % value, )
            return
        elif value < node.data:
            if node.left_child is not None:
                node = node.left_child
                self.look_up(value, node)
            else:
                print('not found %d' % value)
                return
        else:
            if node.right_child is not None:
                node = node.right_child
                self.look_up(value, node)
            else:
                print('not found %d' % value)
                return

    def min_value_node(self, node):
        while node.left_child is not None:
            node = node.left_child
        return node
        # why the recursive code is wrong?
        # if node.left_child is not None:
        #     node = node.left_child
        #     self.min_value_node(node)
        # else:
        #     return node

    def insert_node(self, value):
        node = self.root
        while True:
            if node.data < value:
                if node.right_child is not None:
                    node = node.right_child
                else:
                    break
            else:
                if node.left_child is not None:
                    node = node.left_child
                else:
                    break
        node_insert = Node(value)
        if node.right_child is None:
            node.right_child = node_insert
        else:
            node.left_child = node_insert

    def delete_node(self, node, value):
        if value < node.data:
            self.delete_node(node.left_child, value)
        elif value > node.data:
            self.delete_node(node.right_child, value)
        else:
            # leaf node
            if (node.left_child is None) and (node.right_child is None):
                print('delete leaf node %d' % node.data)
                node = None
                return
            elif node.left_child is None:
                print('replace node with right child %d' % node.data)
                node = node.right_child
                return
            # only left child
            elif node.right_child is None:
                print('replace node with left child %d' % node.data)
                node = node.left_child
                return
            else:
                print('node has two child %d' % node.data)
                node_successor = self.min_value_node(node.right_child)
                node.data = node_successor.data
                node_successor = None
                return
        return








tree = BST()
arr = [8,10,14,13,3,1,6,4,7,]
for i in arr:
	tree.create_BST(i)
# print('previous order')
# tree.pre_order(tree.root)
print('in order')
tree.in_order(tree.root)

# print('min value')
# min_val_node = tree.min_value_node(tree.root)
# print(min_val_node.data)
# look up
# tree.look_up(5, tree.root)

# insert
# tree.insert_node(7)
# print('after insert previous order')
# tree.in_order(tree.root)

tree.delete_node(tree.root, 4)
print('after delete in order')
tree.in_order(tree.root)
