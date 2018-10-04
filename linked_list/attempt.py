class LinkedList:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = {}
        self.head = LinkedList
        self.tail = LinkedList

    def push_front(self, node):
        self.hash[node.key] = self.head
        self.head.next = node
        self.head = node

    def pop_back(self):
        del self.hash[self.tail.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head

    def kick(self, prev):
        node = prev.next
        if node == self.head:
            return
        prev.next = node.next
        if node.next is not None:
            self.hash[node.next.key] = prev
        node.next = None
        self.push_front(node)

    def get(self, key):
        if key not in self.hash:
            return -1
        self.kick(self.hash[key])
        # self.hash[key] is <class '__main__.LinkedList'>
        # self.hash[key].next.value is the value we want
        return self.hash[key].next.value

    def set(self, key, value):
        if key in self.hash:
            self.kick(self.hash[key])
            self.hash[key].next.value = value
        else:
            self.push_front(LinkedList(key, value))
            # if len(self.hash) > self.capacity:
            #     self.pop_back()

lru = LRUCache(capacity=2)
lru.set(1, 1)
lru.set(2, 2)
print(lru.hash)
lru.set(1, 1)
print(lru.get(1))
print(lru.hash)

