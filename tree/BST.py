'''
Problem:
    Binary search tree
Ways:
    validate BST
    (1)for each node, we should check that
      the maximum value in the left sub-tree is smaller than node value,
      while the minimal value in the right sub-tree is bigger than node value
    (2)we can do in-order traverse, if the output is in ascend order,
      then the tree is a BST
      Notice: the function is_bst can return True, if it check all node and not found False
          otherwise, it will return False once one node violate the BST rule
Ref:
1. https://gist.github.com/thinkphp/1450738
2. check BST: https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
Problem:
    Try Morris traversal https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BST():
    def __init__(self):
        self.root = None
        self.former_value = - float('inf')
        self.value_cloest = float('inf')

    def create_BST(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.data:
                    if current.left_child is not None:
                        current = current.left_child
                    else:
                        current.left_child = Node(value)
                        break
                elif value > current.data:
                    if current.right_child is not None:
                        current = current.right_child
                    else:
                        current.right_child = Node(value)
                        break
                else:
                    break

    def insert_node(self, value):
        node = self.root
        node_insert = Node(value)
        while True:
            if value < node.data:
                if node.left_child is not None:
                    node = node.left_child
                else:
                    node.left_child = node_insert
                    break
            else:
                if node.right_child is not None:
                    node = node.right_child
                else:
                    node.right_child = node_insert
                    break

    def look_up(self, value, node):
        if node.data == value:
            print('find')
            return
        # while True:
        elif value < node.data:
            if node.left_child is not None:
                node = node.left_child
                self.look_up(value, node)
            else:
                print('not found')
                return
        else:
            if node.right_child is not None:
                node = node.right_child
                self.look_up(value, node)
            else:
                print('not found')
                return

    def min_value_node(self, node):
        while node.left_child is not None:
            node = node.left_child
        return node

    def delete_node(self, node, value):
        if value < node.data:
            self.delete_node(node.left_child, value)
        elif value > node.data:
            self.delete_node(node.right_child, value)
        else:
            # leaf node
            if (node.left_child is None) and (node.right_child is None):
                node.data = None
                return
            # only left node
            elif node.right_child is None:
                node = node.left_child
                return
            # only right node
            elif node.left_child is None:
                node = node.right_child
                return
            # two child leaves
            else:
                successor = self.min_value_node(node)
                node.data = successor.data
                successor = None
                return

    # this code is beautiful
    def is_bst(self, node):
        if node is None:
            return True
        else:
            # left tree
            if not self.is_bst(node.left_child):
                return False
            # current
            if self.former_value > node.data:
                return False
            # update former value
            self.former_value = node.data
            return self.is_bst(node.right_child)
            ## optional, the above line is more concise
            # if not self.is_bst(node.right_child):
            #     return False
            # else:
            #     return True

    # # simple but wrong
    # def validate_BST(self, node):
    #     # empty node
    #     if node is None:
    #         return True
    #     # check left node
    #     if (node.left_child is not None) and (node.left_child.data > node.data):
    #         return False
    #     # check right node
    #     if (node.right_child is not None) and (node.data > node.right_child.data):
    #         return False
    #     # recursive check left tree and right tree
    #     if (not self.validate_BST(node.left_child)) or (not self.validate_BST(node.right_child)):
    #         return False
    #     # for the leaf node
    #     return True

    # this code is beautiful
    def in_order(self, current):
        if current is not None:
            self.in_order(current.left_child)
            print(current.data)
            self.in_order(current.right_child)

    def cloest_value(self, current):
        if current is not None:
            self.cloest_value(current.left_child)
            # dispose
            diff_value = current.data - self.former_value
            if diff_value < self.value_cloest:
                self.value_cloest = diff_value
            self.former_value = current.data
            self.cloest_value(current.right_child)


tree = BST()
arr = [8,10,14,13,3,1,6,4,5]
# arr = [3, 2, 5, 1, 4]
for i in arr:
	tree.create_BST(i)

print('in order')
tree.in_order(tree.root)
tree.cloest_value(tree.root)
print(tree.value_cloest)

# root = Node(9)
# root.left_child = Node(6)
# root.right_child = Node(3)
# root.left_child.left_child = Node(5)
# root.left_child.right_child = Node(7)
# root.left_child.right_child.left_child = Node(15)
# root.left_child.right_child.right_child = Node(1)
# root.right_child.left_child = Node(2)
# result = tree.validate_BST(tree.root)
# result = tree.is_bst(root)
# print(result)

# print('min value')
# min_val_node = tree.min_value_node(tree.root)
# print(min_val_node.data)
# look up
# tree.look_up(5, tree.root)

# insert
# tree.insert_node(7)
# print('after insert previous order')
# tree.in_order(tree.root)

# tree.delete_node(tree.root, 4)
# print('after delete in order')
# tree.in_order(tree.root)




