#!/usr/bin/python
# coding=utf-8
import Graphe
import time
import random

nb_nodes = 10000
nb_edges = 20000

g = Graphe.Graphe()



node_full = []
for i in range(0,nb_nodes):
    node_full.append(i)
'''
node_1 = 1
node_2 = 2
node_3 = 3
node_4 = 4

nodes = [node_1 , node_2 , node_3 , node_4]
'''
nodes = node_full

for node in nodes:
    g.add_node(node)

for j in range(0,nb_edges):
    g.add_edge(node_full[random.randint(0,nb_nodes-1)] , node_full[random.randint(0,nb_nodes-1)] , random.randint(2 , 20))
'''

g.add_edge(node_1 , node_2 , 1)
g.add_edge(node_2 , node_4 , 6)
g.add_edge(node_3 , node_4 , 1)
g.add_edge(node_3 , node_2 , 2)
g.add_edge(node_1 , node_4 , 7)




chemin = g.dijsktra(node_1)
chemin_ford = g.bellman_ford(node_1)
'''
chemin = g.dijsktra(node_full[0])
chemin_ford = g.bellman_ford(node_full[0])
print "Dijkstra :"
print "Longueur des chemins : " + str(chemin[0])
print "Précédent à un sommet : " + str(chemin[1])
print "Bellman :"
print "Longueur des chemins : " + str(chemin_ford[0])
print "Précédent à un sommet : " + str(chemin_ford[1])

