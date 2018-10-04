'''
Problem:
    Find the number of islands
Way:
    1. we should traverse the graph with DFS or BFS
    2. according to the definition of island,
    for each vertex, we should consider its 8 neighbours
    3. document the visited vertex to avoid repeated traverse
Ref:
    https://www.geeksforgeeks.org/find-number-of-islands/
Questions:
    try BFS
'''

class Graph:
    def __init__(self, graph):
        self.row = len(graph)
        self.col = len(graph[0])
        self.graph = graph

    def is_safe(self, i, j, visited):
        return 0 <= i < self.row and 0 <= j < self.col and not visited[i][j] and self.graph[i][j]

    def DFS(self, i, j, visited):
        # this combined with is_safe check is beautiful
        nei_row = [-1, -1, -1, 0, 0, 1, 1, 1]
        nei_col = [-1, 0, 1, -1, 1, -1, 0, 1]

        visited[i][j] = True

        for k in range(8):
            if self.is_safe(i + nei_row[k], j + nei_col[k], visited):
                self.DFS(i + nei_row[k], j + nei_col[k], visited)

    def count_islands(self):
        # notice we should use list to create a 5x5 matrix
        visited = [[False] * self.col for _ in range(self.row)]
        # visited = [[False * self.col] for _ in range(self.row)]
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                ## notice we should avoid traverse a vertex more than once
                if not visited[i][j] and self.graph[i][j]:
                ## if self.graph[i][j]:
                    count += 1
                    self.DFS(i, j, visited)
        return count


graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

g = Graph(graph)
print(g.count_islands())

