'''
Problem:
    Find all possible words in a board of characters
    Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.
Way:
    In each cell, do depth-first-search, obtain the legal word
    We should use recursion properly
Ref:
    https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
'''

class Graph:
    def __init__(self, data, word):
        self.data = data
        self.word = word
        self.num_col = len(data[0])
        self.num_row = len(data)
        self.num_char = len(word)
        self.visited = list()
        self.nei_hei = [-1, -1, -1, 0, 0, 1, 1, 1]
        self.nei_wid = [-1, 0, 1, -1, 1, -1, 0, 1]


    def is_safe(self, i, j, visited):
        return 0 <= i < self.num_row and 0 <= j < self.num_col and not visited[i][j]

    # this function shows the soul of recursion
    def obtain_word(self, i, j, visited, word):
        visited[i][j] = True
        word.append(self.data[i][j])
        if word == self.word:
            print('match pattern', word)
        # add this condition to constrain that:
        # only if the front part matches, we step to explore
        if (word == self.word[:len(word)]) and (len(word) < self.num_char):
            for k in range(8):
                if self.is_safe(i + self.nei_hei[k], j + self.nei_wid[k], visited):
                    self.obtain_word(i + self.nei_hei[k], j + self.nei_wid[k], visited, word)
        # after all explorations starting from a cell, erase this cell, mark it as unvisited
        word.pop()
        visited[i][j] = False


    def boggle(self):
        for i in range(self.num_row):
            for j in range(self.num_col):
                word = list()
                # for each cell, we should re-initialize visited
                visited = [[False] * self.num_col for _ in range(self.num_row)]
                self.obtain_word(i, j, visited, word)


data = list()
data.append(list('GIZ'))
data.append(list('UEK'))
data.append(list('QSE'))
word = list('GEEKS')
graph = Graph(data, word)
graph.boggle()
