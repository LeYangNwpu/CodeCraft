'''
Problem:
    Design and implement a data structure for Least Recently Used (LRU) cache.
    It should support the following operations:
      get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
      put(key, value) - Set or insert the value if the key is not already present.
      When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
Way:
    Use linked list, each node contains three attributes: key, value and next
    For LRUCache, maintain a dictionary, self.hash[key] = value
    For a node in linked list, we only know its next node.
    Thus, the pop operation can only be done at the head of the list.
    We should pop at the front, push at the back, put the most recently node at the tail of the linked list

Ref:
    https://blog.csdn.net/Koala_Tree/article/details/80326015
    https://www.jiuzhang.com/solution/lru-cache/#tag-highlight-lang-python
'''


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

    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head

    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        if node.next is not None:
            self.hash[node.next.key] = prev
        node.next = None
        self.push_back(node)

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
            self.push_back(LinkedList(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()

lru = LRUCache(capacity=2)
lru.set(1, 1)
lru.set(2, 2)
# print(type(lru.hash))
print(lru.get(1))
print(lru.hash)
# lru.set(3, 3)
# print(lru.get(2))
# lru.set(4, 4)
# print(lru.get(1))
# print(lru.get(3))
# print(lru.get(4))
