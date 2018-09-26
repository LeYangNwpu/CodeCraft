'''
Problem:
    Breadth First Search for a graph
Way:
    Use queue
      for each vertex, store all its possible vertexs in a queue
      everytime, pop vertex from the head of the queue, and dispose
    In python, queue can be implemented as list
      append at the tail, pop at the head
    Notice:
      we use a directed graph
Ref:
    https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
'''

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def breadth_first_search(self, v):
        # visited = [False] * len(self.graph)
        visited = [False] * (len(self.graph) + 1)
        queue = []
        visited[v] = True
        queue.append(v)

        while queue:
            temp = queue.pop(0)
            print(temp)

            for iver in self.graph[temp]:
                if not visited[iver]:
                    visited[iver] = True
                    queue.append(iver)


# Create a graph given in
# the above diagram
# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)

# for graph with vertexs not starting from 0
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(5, 6)
g.add_edge(6, 5)

print("Following is Breadth First Traversal")
g.breadth_first_search(1)

