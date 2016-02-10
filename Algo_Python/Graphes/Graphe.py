import time

class Graphe:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

    def dijsktra(self, initial):
        visited = {initial: 0}
        path = {}
        total_time = 0
        n = set(self.nodes)

        while n:
            min_node = None
            for node in n:
              if node in visited:
                if min_node is None:
                  min_node = node
                elif visited[node] < visited[min_node]:
                  min_node = node

            if min_node is None:
                break

            n.remove(min_node)
            current_weight = visited[min_node]

            start_time = time.time()

            for edge in self.edges[min_node]:
              weight = current_weight + self.distances[(min_node, edge)]
              if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

            total_time += time.time() - start_time
        print total_time
        return visited, path

    def bellman_ford(self,initial):
        visited = {initial: 0}
        path = {}

        n = set(self.nodes)
        finished = False
        start_time = time.time()
        while not finished:
            finished = True
            to_visit = dict(visited)
            for node in to_visit:
                current_weight = visited[node]
                for edge in self.edges[node]:
                  weight = current_weight + self.distances[(node, edge)]
                  if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = node
                    finished = False
        print time.time() - start_time
        return visited, path



        return 0

