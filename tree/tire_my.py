'''
Problem:
    Implement a trie, supporting insert and search operation
Ways:
    Tire is an efficient way for search (or) rank strings
    We use list to simulate the dictionary, apply space for all possible characters in time
    each character itself can indicate the index
    the function cha2ind is a good idea
Ref:
    https://www.geeksforgeeks.org/trie-insert-and-search/
'''


class Trie_Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = Trie_Node()

    def cha2ind(self, cha):
        return ord(cha) - ord('a')

    def insert(self, word):
        node = self.root
        for cha in word:
            index = self.cha2ind(cha)
            if not node.children[index]:
                node.children[index] = Trie_Node()
            node = node.children[index]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for cha in word:
            index = self.cha2ind(cha)
            if not node.children[index]:
                return False
            node = node.children[index]
        return node is not None and node.is_end_of_word


def main():
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    output = ["Not present in trie", "Present in tire"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

        # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()
