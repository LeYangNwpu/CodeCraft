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

    def breadth_first_search(self, v):
        # as the vertex order starts from 1, the length of visited list should be len(self.graph) + 1
        visited = [False] * (len(self.graph) + 1)
        queue = list()
        queue.append(v)
        # every time we append an vertex into queue, we should mark it as visited
        visited[v] = True

        while queue:
            temp_v = queue.pop(0)
            print(temp_v)
            # alternatively, we can mark each vertex as visited after print
            # however, this means we do repeated work
            # visited[temp_v] = True
            for i_u in self.graph[temp_v]:
                if not visited[i_u]:
                    queue.append(i_u)
                    visited[i_u] = True

    def dfs(self, v, visited):
        print(v)
        visited[v] = True
        for iver in self.graph[v]:
            if not visited[iver]:
                self.dfs(iver, visited)

    def depth_first_search(self, v):
        visited = [False] * (len(self.graph) + 1)
        self.dfs(v, visited)

    # for dfd in iteration manner, we should use stack,
    # append and pop operations only occur at the tail
    # for each vertex, we should check all it child-nodes,
    # even though this node has been visited
    # the result of dfs_iter and depth_first_search may be different,
    # because for a given node, there are multiple child-nodes,
    # the recursion solution traverse the first node,
    # while the iteration solution traverse the last node
    def dfs_iter(self, v):
        visited = [False] * (len(self.graph) + 1)
        stack = list()
        stack.append(v)

        while stack:
            temp_ver = stack.pop(-1)
            if not visited[temp_ver]:
                print(temp_ver)
                visited[temp_ver] = True
            for iver in self.graph[temp_ver]:
                if not visited[iver]:
                    stack.append(iver)


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

# print("Following is Breadth First Traversal")
# g.breadth_first_search(1)
print("Following is Depth First Traversal")
# g.depth_first_search(1)
g.dfs_iter(1)



