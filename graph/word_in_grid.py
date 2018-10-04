'''
Problem:
    Search a Word in a 2D Grid of characters
Way:
    loop through each cell in the gird, found matching pattern
Ref:
    https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/
'''

class Graph:
    def __init__(self, data, word):
        self.data = data
        self.word = word
        self.num_col = len(data[0])
        self.num_row = len(data)
        self.num_char = len(word)
        self.visited = [[False] * self.num_col for _ in range(self.num_row)]

    def is_safe(self, i, j):
        return 0 <= i < self.num_row and 0 <= j < self.num_col and not self.visited[i][j]

    def obtain_word(self, i, stepi, j, stepj):
        word = []
        for s in range(self.num_char):
            # optimize to be more efficient
            if self.is_safe(i, j):
                temp_char = self.data[i][j]
                if temp_char == self.word[s]:
                    word.append(temp_char)
                    # Moving in particular direction
                    i += stepi
                    j += stepj
                else:
                    return None
            else:
                return None
        return word

    def record_vis(self, i, stepi, j, stepj):
        for s in range(self.num_char):
            self.visited[i][j] = True
            i += stepi
            j += stepj

    def word_in_grid(self):
        nei_hei = [-1, -1, -1, 0, 0, 1, 1, 1]
        nei_wid = [-1, 0, 1, -1, 1, -1, 0, 1]
        for i in range(self.num_row):
            for j in range(self.num_col):
                # 8 directions
                for k in range(8):
                    word_temp = self.obtain_word(i, nei_hei[k], j, nei_wid[k])
                    if word_temp:
                        if word_temp == self.word:
                            print('match pattern at row %d col %d' % (i, j))
                            # document visited cell
                            self.record_vis(i, nei_hei[k], j, nei_wid[k])

data = list()
data.append(list('GEEKSFORGEEKS'))
data.append(list('GEEKSQUIZGEEK'))
data.append(list('IDEQAPRACTICE'))
word = list('GEEKS')
graph = Graph(data, word)
graph.word_in_grid()

