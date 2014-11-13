import networkx as nx
import matplotlib.pyplot as plt

def plot_weighted_graph(G):

    plt.figure()
    pos = nx.spring_layout(G, k = 2, iterations = 100)
    pos_label = pos
    nx.draw_networkx_nodes(G, pos, node_size= 4000,node_color='fuchsia', node_shape='o')
    # funciona o d, h, o, p
    nx.draw_networkx_edges(G, pos)

    weights = { (u, v): data['weight'] for u, v, data in G.edges(data=True) }
    labels = { (u): data['name'] for u, data in G.nodes(data=True) }

    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=weights, font_size=9, font_family='sans-serif')



    #for i in range(0, len(pos_label)):
    #    pos_label[i][1] += 0.04

    nx.draw_networkx_labels(G, pos, labels, font_size= 50, font_weight=10)

    plt.show()
    plt.close()
