import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from plot_graph import plot_weighted_graph

a = np.loadtxt('../data/uk12distB.txt')
labels = np.loadtxt('../data/uk12_name.txt', dtype=basestring, delimiter='\n')

# Obtem as coordenadas em que o peso eh nao-nulo
rows, cols = np.where(a > 0)

# Obtem o peso de cada uma das arestas
weight = [a[rows[i], cols[i]] for i in range(0, len(rows))]

# Cria lista de arestas com peso
edges_with_weight = zip(rows.tolist(), cols.tolist(), weight)

# Cria um grafo vazio usando NetworkX
g = nx.Graph()

# Insere primeiro os vertices nomeados
set_edges = set(rows.tolist())
for i in range(0, len(set_edges)):
    g.add_node(i, name=labels.tolist()[i])

# Insere as arestas
g.add_weighted_edges_from(edges_with_weight)

plot_weighted_graph(g)

#if __name__ == '__main__':
#    pass