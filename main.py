class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            v = queue.pop(0)
            if v not in visited:
                print(v, end=' ')
                visited.add(v)
                for neighbor in self.graph.get(v, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

# Task 1 Graph
graph = Graph()
graph.add_edge('A', 'C')
graph.add_edge('A', 'B')
graph.add_edge('A', 'D')
graph.add_edge('B', 'C')
graph.add_edge('B', 'E')
graph.add_edge('B', 'G')
graph.add_edge('C', 'D')
graph.add_edge('D', 'C')
graph.add_edge('D', 'A')
graph.add_edge('E', 'G')
graph.add_edge('E', 'F')
graph.add_edge('E', 'B')
graph.add_edge('F', 'G')
graph.add_edge('F', 'E')
graph.add_edge('G', 'F')
graph.add_edge('G', 'B')

print("DFS traversal:")
graph.dfs('A')
print("\nBFS traversal:")
graph.bfs('A')
