class Graph:
    def __init__(self, vertex_size):
        self.vertex_size = vertex_size
        self.graph = [[0 for _ in range(vertex_size)] for _ in range(vertex_size)]

    def add_edge(self, v1, v2):
        if v1 < self.vertex_size and v2 < self.vertex_size:
            self.graph[v1][v2] = 1
            self.graph[v2][v1] = 1

    def print_graph(self):
        for row in self.graph:
            print(row)

if __name__=="__main__":
    my_graph = Graph(5)

    # 간선 추가
    my_graph.add_edge(0, 1)
    my_graph.add_edge(0, 4)
    my_graph.add_edge(1, 2)
    my_graph.add_edge(1, 3)
    my_graph.add_edge(1, 4)
    my_graph.add_edge(2, 3)
    my_graph.add_edge(3, 4)

    # 그래프 출력
    my_graph.print_graph()