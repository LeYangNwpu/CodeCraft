'''
Problem:
    Given a singly linked list and a position
    delete a linked list node at the given position.
Way:
    1. create the list, traverse it, obtain length of the linked list, and delete the required node
    2. for deleting the nth node from end, an efficient way is to maintain two pointers,
    move the first pointer n steps, then move these both two pointers until the first pointer reach the end,
    at this time, the second pointer indicates the node to be deleted
    3. traverse the list, maintain a queue to record te nearest k+1 nodes
    when reach list end, we can locate the kth_node from end
Ref:
    https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/
    https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
    find loop
    https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
Questions:
    if the linked_list contain same numbers, it will be judged as contain loop
    how to improve?
    
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    # insert data at the list head
    def push(self, data):
        node = Node(data)
        node.next_node = self.head
        self.head = node

    # create linked list
    # insert from the head is easy to implement
    def create_llist(self, datas):
        for data in datas:
            self.push(data)

    # print linked list
    def print_llist(self):
        print('print linked list')
        temp = self.head
        while temp:
            print(temp.data, )
            temp = temp.next_node

    # delete node at given position
    def delete_pos_node(self, posit):
        if posit == 0:
            self.head = self.head.next_node
        else:
            node_former = self.head
            for i in range(1, posit):
                if node_former.next_node is not None:
                    node_former = node_former.next_node
                # position is out the range of the linked list
                else:
                    print('the position to be deleted is out of range, do nothing')
                    break
            if node_former.next_node is not None:
                node_current = node_former.next_node
                # remove current node
                node_former.next_node = node_current.next_node

    # delete nth node from the end
    def delete_end_nth_node(self, nth):
        ptr_1st = self.head
        for _ in range(nth):
            ptr_1st = ptr_1st.next_node

        ptrf_2nd = self.head
        # dispose out of range
        if ptr_1st is not None:
            # move the first pointer one step
            ptr_1st = ptr_1st.next_node
            # dispose out of range
            if ptr_1st is not None:
                while ptr_1st.next_node is not None:
                    ptr_1st = ptr_1st.next_node
                    ptrf_2nd = ptrf_2nd.next_node

                # remove end nth node
                ptrf_2nd.next_node = ptrf_2nd.next_node.next_node


    def find_loop_sets(self):
        s = []
        temp = self.head
        while temp.next_node:
            data = temp.data
            if data in s:
                return True
            else:
                s.append(data)
            temp = temp.next_node
        return False

    def find_loop_floyd(self):
        slow_p = self.head
        fast_p = self.head
        while slow_p and fast_p and fast_p.next_node:
            slow_p = slow_p.next_node
            fast_p = fast_p.next_node.next_node
            if slow_p.data == fast_p.data:
                return True
        return False


llist = LinkedList()
# llist.create_llist([7, 1, 3, 2, 8])
llist.print_llist()
# llist.delete_pos_node(posit=4)
# llist.delete_end_nth_node(4)
# llist.print_llist()
print(llist.find_loop_floyd())


