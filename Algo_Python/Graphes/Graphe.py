import Sommet
import Arete

class Graphe:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []
        print self.nodes

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance

    def dijsktra(self, initial):
        visited = {initial: 0}
        path = {}

        nodes = set(self.nodes)
        print self.nodes
        while nodes:
            min_node = None
            for node in nodes:
              if node in visited:
                if min_node is None:
                  min_node = node
                elif visited[node] < visited[min_node]:
                  min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.edges[min_node]:
              weight = current_weight + self.distances[(min_node, edge)]
              if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

        return visited, path