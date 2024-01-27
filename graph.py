from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def iterative_dfs_paths(self, start, end):
        stack = [(start, [start])]
        paths = []

        while stack:
            current_node, path = stack.pop()
            for neighbor in self.graph[current_node]:
                if neighbor == end:
                    paths.append(path + [neighbor])
                elif neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))

        return paths


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)


paths = g.iterative_dfs_paths(0, 4)
print("Paths from 0 to 4:", paths)
