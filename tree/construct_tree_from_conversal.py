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


def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.value)


def search(arr, start, end, value):
	for i in range(start, end+1):
		if arr[i] == value:
			return i

def buildTree(inOrder, preOrder, start, end):
	if start > end:
		return None
	temp_node = Node(preOrder[buildTree.preIndex])
	buildTree.preIndex += 1
	if start == end:
		return temp_node
	index = search(inOrder, start, end, temp_node.value)
	temp_node.left = buildTree(inOrder, preOrder, start, index-1)
	temp_node.right = buildTree(inOrder, preOrder, index+1, end)
	return temp_node

inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
# Static variable preIndex
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)
printPostorder(root)

