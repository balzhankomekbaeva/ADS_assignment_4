from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)

    def dfs(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                stack.extend([neighbor for neighbor in self.adjacency_list[vertex] if neighbor not in visited])

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                queue.extend([neighbor for neighbor in self.adjacency_list[vertex] if neighbor not in visited])

# Create graph
graph = Graph()

# Add edges
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

print("DFS:", end=' ')
graph.dfs('A')

print("\nBFS:", end=' ')
graph.bfs('A')
