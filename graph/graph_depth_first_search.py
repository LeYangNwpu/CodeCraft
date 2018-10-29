'''
Problem:
    Depth First Search for a graph
Way:
    First, properly represent the graph
    Then, search the graph recursively
    Notice: we use a directed graph
Ref:
    https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
???:
    what is defaultdict in collections?
    use the proper graph representation, how to do DFS?
'''

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited):
        # mark this vertex as visited
        visited[v] = True
        print(v)
        for ver in self.graph[v]:
            if not visited[ver]:
                self.dfs(ver, visited)

    def depth_first_search(self, v):
        visited = [False] * len(self.graph)
        self.dfs(v, visited)

    def dfs_iter(self, v):
        visited = [False] * len(self.graph)
        # visited = [False] * (len(self.graph) + 1)
        queue = []
        queue.append(v)

        while queue:
            temp = queue.pop(-1)
            if not visited[temp]:
                print(temp)
                visited[temp] = True
            for iver in self.graph[temp]:
                if not visited[iver]:
                    queue.append(iver)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.depth_first_search(0)
# g.dfs_iter(0)


