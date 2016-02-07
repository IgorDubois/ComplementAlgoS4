import Graphe
import Sommet
import random


g = Graphe.Graphe()

node_1 = 1
node_2 = 2
node_3 = 3
node_4 = 4

nodes = [node_1 , node_2 , node_3 , node_4]
for node in nodes:
    g.add_node(node)

g.add_edge(node_1 , node_2 , 4)
g.add_edge(node_2 , node_4 , 6)
g.add_edge(node_3 , node_2 , 2)
g.add_edge(node_1 , node_4 , 7)


g = Graphe.Graphe()

print g.dijsktra(node_1)

