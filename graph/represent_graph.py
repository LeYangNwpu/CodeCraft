'''
Problem:
    Represent a graph
Way:
    1. use adjacent matrix
      we should maintain three variables:
      vertexs: a dictionary, key is the name of the node, value is the index of the node
      vertexs_list: a list, saving vertex name according to their id
      adjacent_mat: adjacent matrix, with vertex rank as the order in vertexs_list
    2. Adjacent list
      An array of lists is used. Size of the array is equal to the number of vertices.
      Let the array be array[]. An entry array[i] represents the list of vertices adjacent to the ith vertex.
      Notice: adjacent list can also represent weight in graph
Ref:
    https://ide.geeksforgeeks.org/9je5j6jJ13
    https://www.geeksforgeeks.org/graph-and-its-representations/
'''


class Graph:
    def __init__(self, vertex_num):
        self.vertex_num = vertex_num
        self.vertexs = {}
        self.vertexs_list = [None] * vertex_num
        self.adjacent_mat = [[None] * vertex_num for _ in range(vertex_num)]

    def set_vertex(self, ver, id):
        if ver < self.vertex_num:
            self.vertexs[id] = ver
            self.vertexs_list[ver] = id

    def set_edge(self, frm, to, cost):
        frm_num = self.vertexs[frm]
        to_num = self.vertexs[to]
        self.adjacent_mat[frm_num][to_num] = cost
        self.adjacent_mat[to_num][frm_num] = cost

    def get_vertex(self):
        return self.vertexs_list

    def get_matrix(self):
        return self.adjacent_mat

    def get_edges(self):
        edges = []
        for i in range(self.vertex_num):
            for j in range(self.vertex_num):
                if self.adjacent_mat[i][j] is not None:
                    edges.append((self.vertexs_list[i], self.vertexs_list[j], self.adjacent_mat[i][j]))
        return edges

# G = Graph(6)
# G.set_vertex(0, 'a')
# G.set_vertex(1, 'b')
# G.set_vertex(2, 'c')
# G.set_vertex(3, 'd')
# G.set_vertex(4, 'e')
# G.set_vertex(5, 'f')
# G.set_edge('a', 'e', 10)
# G.set_edge('a', 'c', 20)
# G.set_edge('c', 'b', 30)
# G.set_edge('b', 'e', 40)
# G.set_edge('e', 'd', 50)
# G.set_edge('f', 'e', 60)
# print("Vertices of Graph")
# print(G.get_vertex())
# print("Edges of Graph")
# print(G.get_edges())
# print("Adjacency Matrix of Graph")
# print(G.get_matrix())


class adj_vert:
    def __init__(self, ver):
        self.ver = ver
        self.next = None


class Graph_adj:
    def __init__(self, num_vertex):
        self.V = num_vertex
        self.verts = [None] * num_vertex

    def add_edge(self, src, dest):
        # notice here
        # src to dest
        vert_temp = adj_vert(src)
        vert_temp.next = self.verts[dest]
        self.verts[dest] = vert_temp
        # dest to src
        vert_temp = adj_vert(dest)
        vert_temp.next = self.verts[src]
        self.verts[src] = vert_temp

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.verts[i]
            while temp:
                print(" -> {}".format(temp.ver), end="")
                temp = temp.next
            print(" \n")

V = 5
graph = Graph_adj(V)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_graph()

