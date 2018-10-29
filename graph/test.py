from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def breadth_first_search(self, v):
        visited = [False] * (len(self.graph) + 1)
        queue = list()
        queue.append(v)
        visited[v] = True

        while queue:
            ver = queue.pop(0)
            print(ver)

            for iver in self.graph[ver]:
                if not visited[iver]:
                    queue.append(iver)
                    visited[iver] = True

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
g.breadth_first_search(2)

