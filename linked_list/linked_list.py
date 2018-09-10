class Node:
	def __init__(self, data_value=None):
		self.data_value = data_value
		self.next_node = None

# class SLinkedList:
# 	def __init__(self):
# 		self.head_value = None
# 	def list_print(self):
# 		printval = self.head_value
# 		while printval is not None:
# 			print(printval.data_value)
# 			printval = printval.next_node


class SLinkedList:
    def __init__(self):
        self.head_value = None

    def list_print(self):
        printval = self.head_value
        while printval is not None:
            print(printval.data_value)
            printval = printval.next_node

    def list_length(self):
        count = 1
        printval = self.head_value
        while printval is not None:
            count += 1
            printval = printval.next_node
        return count

    def insert(self, value, location):
        element_num = self.list_length()
        if (location < 1) or (location > element_num + 1):
            print('invalide location')
            return
        n_insert = Node(value)
        # visit location-1 node
        count = 1
        node_cur = self.head_value
        while (count < location - 1) and (node_cur is not None):
            node_cur = node_cur.next_node
        p = node_cur.next_node
        node_cur.next_node = n_insert
        n_insert.next_node = p


list1 = SLinkedList()
list1.head_value = Node('Monday')
n2 = Node('Tuesday')
n3 = Node('Wednesday')
list1.head_value.next_node = n2
n2.next_node = n3

list1.insert('Thursday', 2)
list1.list_print()

