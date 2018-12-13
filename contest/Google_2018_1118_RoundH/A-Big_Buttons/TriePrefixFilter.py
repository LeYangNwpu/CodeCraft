'''
Purpose:
    When filter forbidden strings, considering two strings,
    if the shorter one is the prefix of the longer one,
    then the longer one is redundant, we should only keep the shorter one
Way:
    (1) A naive solution:
    We can use trie to store all the strings,
    then display the trie
    Error Attempts:
      When store the strings and create trie,
      we should check whether current string has been prefixed by an existing string
    Error:
      when 'aa' appears before 'a', both 'aa' and 'a' will be inserted into the trie
      function insert_optim(key) is correct, however, this idea is not good
'''


class Trie_Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = Trie_Node()

    def cha2ind(self, cha):
        return ord(cha) - ord('A')

    def insert(self, word):
        node = self.root
        for cha in word:
            index = self.cha2ind(cha)
            if not node.children[index]:
                node.children[index] = Trie_Node()
            node = node.children[index]
        node.is_end_of_word = True

    # def insert_optim(self, word):
    #     node = self.root
    #     for cha in word:
    #         index = self.cha2ind(cha)
    #         node_temp = node.children[index]
    #         if node_temp is not None and node_temp.is_end_of_word:
    #             print('reach end flag')
    #             return
    #         if not node_temp:
    #             node.children[index] = Trie_Node()
    #         node = node.children[index]
    #     node.is_end_of_word = True

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
                str_temp += chr(order + ord('A'))
                if child.is_end_of_word:
                    pass
                    # print(str_temp)
                self.display(child, str_temp)

    def filter(self, node, str_prex):
        # strs_forb_real = list()

        for order, child in enumerate(node.children):
            # notice here, ensure every child obtain equal str_prex
            str_temp = str_prex
            if child is not None:
                str_temp += chr(order + ord('A'))
                if child.is_end_of_word:
                    strs_forb_real.append(str_temp)
                else:
                    self.filter(child, str_temp)


def filter_forb_prex(keys):
    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    global strs_forb_real
    strs_forb_real = list()
    t.filter(t.root, str_prex='')

    return strs_forb_real


def main():
    # keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    # keys = ['a', "abd", 'ac', 'abcd', 'abbbbb', 'abbabb', 'acaaaaa', "geeks", "for", "geeks", "portal", "to", "learn", "can", "be", "computer", "science", "zoom", "yup", "fire", "in", "data"]
    keys = ['BBB', 'RB']
    seqs = filter_forb_prex(keys)
    print(seqs)


# def main():
#     # keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
#     keys = ['a', "abd", 'ac', 'abcd', 'abbbbb', 'abbabb', 'acaaaaa', "geeks", "for", "geeks", "portal", "to", "learn", "can", "be", "computer", "science", "zoom", "yup", "fire", "in", "data"]
#     output = ["Not present in trie", "Present in tire"]
#
#     # Trie object
#     t = Trie()
#
#     # Construct trie
#     for key in keys:
#         t.insert(key)
#         # t.insert_optim(key)
#
#     # show first level
#
#
#     ## Search for different keys
#     # print("{} ---- {}".format("the", output[t.search("the")]))
#     # print("{} ---- {}".format("these", output[t.search("these")]))
#     # print("{} ---- {}".format("their", output[t.search("their")]))
#     # print("{} ---- {}".format("thaw", output[t.search("thaw")]))
#
#     # display the tire
#     t.display(node=t.root, str_prex='')


# if __name__ == '__main__':
#     main()


