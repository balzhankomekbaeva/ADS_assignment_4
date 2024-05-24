from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)

    def depth_first_search(self, source):
        visited = set()
        self.dfs_util(source, visited)

    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def breadth_first_search(self, source):
        visited = set()
        queue = deque()
        queue.append(source)
        visited.add(source)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Create a graph instance
graph = Graph()

# Add vertices and edges to the graph
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_vertex('G')

graph.add_edge('A', 'C')
graph.add_edge('A', 'B')
graph.add_edge('A', 'D')
graph.add_edge('B', 'C')
graph.add_edge('B', 'E')
graph.add_edge('B', 'G')
graph.add_edge('C', 'D')
graph.add_edge('E', 'G')
graph.add_edge('E', 'F')
graph.add_edge('F', 'G')

# Perform Depth First Search (DFS)
print("DFS:", end=" ")
graph.depth_first_search('A')
print()

# Perform Breadth First Search (BFS)
print("BFS:", end=" ")
graph.breadth_first_search('A')
