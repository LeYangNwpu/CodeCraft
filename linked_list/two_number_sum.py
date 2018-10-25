'''
Two big number sum
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def print_list(self):
        node = self.head_node
        while node.next:
            print('%d ->' % node.data, end='')
            node = node.next
        print('%d' % node.data)

    def append_node(self, node):
        # for an empty list
        if self.head_node is None:
            self.head_node = node
            self.tail_node = node
        else:
            self.tail_node.next = node
            self.tail_node = node


def sum_lists(list1, list2):
    # for empty list
    if list1.head_node is None:
        return list2
    elif list2.head_node is None:
        return list1

    list_s = SLinkedList()
    node1 = list1.head_node
    node2 = list2.head_node

    adding = 0
    while node1 and node2:
        # the initial node
        value = node1.data + node2.data + adding
        if value > 9:
            value -= 10
            adding = 1
        else:
            adding = 0

        list_s.append_node(Node(value))

        # move to next node
        node1 = node1.next
        node2 = node2.next

    # if list2 is shorter than list1
    while node1:
        value = node1.data + adding
        if value > 9:
            value -= 10
            adding = 1
        else:
            adding = 0

            list_s.append_node(Node(value))

        node1 = node1.next

    # if list1 is shorter than list2
    while node2:
        value = node2.data + adding
        if value > 9:
            value -= 10
            adding = 1
        else:
            adding = 0

            list_s.append_node(Node(value))

        node2 = node2.next

    return list_s

list1 = SLinkedList()
list1.append_node(Node(7))
list1.append_node(Node(1))
list1.append_node(Node(6))
list1.append_node(Node(5))
list1.print_list()

list2 = SLinkedList()
list2.append_node(Node(5))
list2.append_node(Node(9))
list2.append_node(Node(2))
list2.print_list()

list_s = sum_lists(list1, list2)
list_s.print_list()


