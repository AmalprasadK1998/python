class Graph:

    def __init__(self, edges):
        # adjacency list representation of graph
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = []
        visited.append(start)
        print(start)
        for next_vertex in self.graph_dict[start]:
            if next_vertex not in visited:
                self.dfs(next_vertex, visited)

    def bfs(self, start):
        visited = []
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                print(vertex)
                queue.extend([v for v in self.graph_dict[vertex] if v not in visited])


# Define a graph as a list of edges
edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]

# Create a new Graph object
graph = Graph(edges)

# Traverse the graph using DFS, starting from vertex 2
print("DFS traversal:")
graph.dfs(2)

# Traverse the graph using BFS, starting from vertex 2
print("BFS traversal:")
graph.bfs(2)


# In the DFS traversal, we start from vertex 2 and recursively explore its neighbors until we have visited all vertices in the graph.
# We print out the vertices in the order they are visited, which gives us the DFS traversal of the graph

# In the BFS traversal, we start from vertex 2 and explore its neighbors one level at a time,
# using a queue data structure to keep track of the vertices to visit next.
# We print out the vertices in the order they are visited, which gives us the BFS traversal of the graph.
