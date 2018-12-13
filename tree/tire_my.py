'''
Problem:
    Implement a trie, supporting insert and search operation
Ways:
    1. Tire is an efficient way for search (or) rank strings
    We use list to simulate the dictionary, apply space for all possible characters in time
    each character itself can indicate the index
    the function cha2ind is a good idea
    2. For display the trie, use recursive manner
    when display the trie, we naturally show the string in dictionary order

Ref:
    https://www.geeksforgeeks.org/trie-insert-and-search/
    https://www.geeksforgeeks.org/trie-display-content/
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

    def display(self, node, str_prex):
        for order, child in enumerate(node.children):
            # notice here, ensure every child obtain equal str_prex
            str_temp = str_prex
            if child is not None:
                str_temp += chr(order + ord('a'))
                if child.is_end_of_word:
                    print(str_temp)
                self.display(child, str_temp)


def main():
    # keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    keys = ["abd", 'ac', 'abcd', 'abbbbb', 'abbabb', 'acaaaaa', "geeks", "for", "geeks", "a", "portal", "to", "learn", "can", "be", "computer", "science", "zoom", "yup", "fire", "in", "data"]
    output = ["Not present in trie", "Present in tire"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # show first level


    ## Search for different keys
    # print("{} ---- {}".format("the", output[t.search("the")]))
    # print("{} ---- {}".format("these", output[t.search("these")]))
    # print("{} ---- {}".format("their", output[t.search("their")]))
    # print("{} ---- {}".format("thaw", output[t.search("thaw")]))

    # display the tire
    t.display(node=t.root, str_prex='')


if __name__ == '__main__':
    main()
