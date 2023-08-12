class Graph:
    def __init__(self):
        self.adjancency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1] = [v for v in self.adjacency_list[vertex1] if v != vertex2]
            self.adjacency_list[vertex2] = [v for v in self.adjacency_list[vertex2] if v != vertex1]
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            return None

        while self.adjacency_list[vertex]:
            temp = self.adjacency_list[vertex].pop()
            self.remove_edge(vertex, temp)

        del self.adjacency_list[vertex]
        return self

graph = Graph()
graph.add_vertex("A")