class Node:
    def __init__(self, data):
        self.data = data
        self.adding = 0
        self.next = None

    


def sum_lists(node1, node2):
    # the initial node
    value = node1.data + node2.data
    node_whole = Node(value)

    adding = 0
    while (node1.next) and (node2.next):
        # move to next node
        node1 = node1.next
        node2 = node2.next

        value = node1.data + node2.data + adding
        if value > 9:
            value -= 9
            adding = 1
        else:
            adding = 0

        node = Node(value)
        node.adding = adding

        node_whole.next = node
        node_whole = node_whole.next

    # if list2 is shorter than list1
    while node1.next:
        value = node1.data + adding
        if value > 9:
            value -= 9
            adding = 1
        else:
            adding = 0

        node = Node(value)
        node.adding = adding

        node_whole.next = node
        node_whole = node_whole.next
        node1 = node1.next

    # if list1 is shorter than list2
    while node2.next:
        value = node2.data + adding
        if value > 9:
            value -= 9
            adding = 1
        else:
            adding = 0

        node = Node(value)
        node.adding = adding

        node_whole.next = node
        node_whole = node_whole.next
        node2 = node2.next

    return node_whole


def print_list(node):
    while node.next:
        print('%d ->' % node.data, end='')
        node = node.next
    # print the last number
    print('%d' % node.data)


node1 = Node(7)
node1.next = Node(1)
node1.next.next = Node(6)

node2 = Node(5)
node2.next = Node(9)
node2.next.next = Node(2)
print_list(node2)

node_whole = sum_lists(node1, node2)

