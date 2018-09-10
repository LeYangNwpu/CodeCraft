class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.value = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.value)
        printInorder(root.right)

def printPreorder(root):
    if root:
        print(root.value)
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.value)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printPostorder(root)

