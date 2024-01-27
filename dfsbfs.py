from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, node, visited):
        visited.add(node)
        print(node, end=" ")

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                print(current_node, end=" ")
                visited.add(current_node)
                stack.extend(neighbor for neighbor in self.graph[current_node] if neighbor not in visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            current_node = queue.popleft()
            if current_node not in visited:
                print(current_node, end=" ")
                visited.add(current_node)
                queue.extend(neighbor for neighbor in self.graph[current_node] if neighbor not in visited)

def find_connected_components(graph):
    visited = set()
    components = []
    for node in graph.graph:
        if node not in visited:
            component = []
            graph.dfs_recursive(node, visited, component)
            components.append(component)
    return components

# Identify Cycles
def has_cycle(graph):
    visited = set()
    for node in graph.graph:
        if node not in visited and dfs_detect_cycle(graph, node, visited, parent=None):
            return True
    return False

def dfs_detect_cycle(graph, node, visited, parent):
    visited.add(node)

    for neighbor in graph.graph[node]:
        if neighbor not in visited:
            if dfs_detect_cycle(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True

    return False

# Determine if a Graph is Bipartite
def is_bipartite(graph):
    color = {}
    for node in graph.graph:
        if node not in color:
            if not dfs_color(graph, node, color):
                return False
    return True

def dfs_color(graph, node, color):
    stack = [(node, 0)]

    while stack:
        current_node, current_color = stack.pop()
        if current_node in color:
            if color[current_node] != current_color:
                return False
            continue

        color[current_node] = current_color

        for neighbor in graph.graph[current_node]:
            stack.append((neighbor, 1 - current_color))

    return True


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

print("DFS (Recursive):")
g.dfs_recursive(0, set())
print()

print("DFS (Iterative):")
g.dfs_iterative(0)
print()

print("BFS:")
g.bfs(0)
print()


components = find_connected_components(g)
print("Connected Components:", components)


has_cycle = has_cycle(g)
print("Does the graph have a cycle?", has_cycle)

is_bipartite = is_bipartite(g)
print("Is the graph bipartite?", is_bipartite)
