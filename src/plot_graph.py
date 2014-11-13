import networkx as nx
import matplotlib.pyplot as plt

def plot_weighted_graph(G):

    plt.figure()
    pos = nx.spring_layout(G, k = 2, iterations = 100)

    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)

    weights = { (u, v): data['weight'] for u, v, data in G.edges(data=True) }

    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=weights, font_size=12, font_family='sans-serif')

    plt.show()
    plt.close()
