import networkx as nx
import random
import unittest
import kruskal

'''
for i in range(1,500,1):
    for j in range(i+1,500,1):
        G.add_edge(int(i),int(j),weight=random.randint(1,20))

nx.write_weighted_edgelist(G, "k500.adjlist")
'''
G = nx.read_weighted_edgelist("k500.adjlist" , nodetype=int)
print kruskal.kruskal(G)
print ('coucou')
T = nx.minimum_spanning_tree(G)
print(sorted(T.edges(data=True)))

#print nx.all_pairs_dijkstra_path_length(G)[1]
