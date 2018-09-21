'''
Problem:
    Inorder Tree Traversal without Recursion
Way:
    Use stack
Ref:
    https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# # problem
# def iterative_post_order_traverse(root):
#     s = []
#     while True:
#         while root is not None:
#             if (root is not None) and (root.right is not None):
#                 s.append(root)
#             if (root is not None) and (root.left is not None):
#                 s.append(root)
#             root = root.left
#         if (root is None) and (len(s) > 0):
#             root = s.pop()
#             print(root.value)
#             root = root.right
#
#         if (root is None) and (len(s) == 0):
#             break

def iterative_pre_order_traverse(root):
    s = []
    while True:
        while root is not None:
            print(root.value)
            if (root is not None) and (root.right is not None):
                s.append(root)
            root = root.left
        if (root is None) and (len(s) > 0):
            root = s.pop()
            root = root.right
        if (root is None) and (len(s) == 0):
            break

def iterative_in_order_traverse(root):
    s = []
    while True:
        while root is not None:
            s.append(root)
            root = root.left
        if (root is None) and (len(s) > 0):
            root = s.pop()
            print(root.value)
            root = root.right
        if (root is None) and (len(s) == 0):
            break

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# iterative_in_order_traverse(root)
# iterative_pre_order_traverse(root)
iterative_post_order_traverse(root)
