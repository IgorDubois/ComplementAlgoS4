parent = dict()
rank = dict()

def make_set(node):
    parent[node] = node
    rank[node] = 0

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for node in graph.nodes():
        make_set(node)

    minimum_spanning_tree = []
    edges = graph.edges(data=True)
    edges.sort()
    for edge in edges:
        (u,v,d) = edge
        weight = d['weight']
        if find(u) != find(v):
            union(u, v)
            minimum_spanning_tree.append(edge)
    return minimum_spanning_tree

