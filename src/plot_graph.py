import networkx as nx
import matplotlib.pyplot as plt

def plot_weighted_graph(G,
                        writeNodeLabel = False,
                        writeEdgeLabel = False,
                        k=2,
                        iterations=100,
                        node_size=4000,
                        node_color='fuchsia',
                        font_size=9,
                        nodelist=None,
                        edgelist=None):

    plt.figure()

    pos = nx.spring_layout(G, k=k, iterations=iterations)
    nx.draw_networkx_nodes(G, pos, nodelist=nodelist, node_size=node_size, node_color=node_color)
    nx.draw_networkx_edges(G, pos, edgelist=edgelist)

    weights = { (u, v): data['weight'] for u, v, data in G.edges(data=True) }
    labels = { (u): data['name'] for u, data in G.nodes(data=True) }

    if(writeEdgeLabel):
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=weights, font_size = font_size, font_family='sans-serif')

    if(writeNodeLabel):
        nx.draw_networkx_labels(G, pos, labels, font_size = font_size)

    plt.show()
    plt.close()
