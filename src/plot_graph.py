__author__ = 'Thales Menato'
__author__ = 'Daniel Nobusada'

import networkx as nx
import matplotlib.pyplot as plt

def plot_weighted_graph(G,
                        writeNodeLabel = False,
                        writeEdgeLabel = False,
                        iterations=100,
                        node_size=1000,
                        node_color='fuchsia',
                        font_size=9,
                        img_name="default",
                        figsize=(16,10),
                        k=1,
                        seeds=None):

    colors = {0: 'red',
              1: 'blue',
              2: 'green',
              3: 'fuchsia',
              4: 'white'}

    plt.figure(figsize=figsize)
    plt.title(img_name)
    plt.margins(0)
    plt.axis('off')

    pos = nx.spring_layout(G, k=k, iterations=iterations)

    if(seeds is not None):
        nodelist = {}
        for s in seeds:
            nodelist[s] = [s]
            for v in G.nodes():
                # se estiver conectado
                if (nx.node_connectivity(G, v, s) is 1):
                    nodelist[s].append(v)

        print nodelist

        for i in range(0, len(seeds)):
            nx.draw_networkx_nodes(G, pos,
                                   node_size=node_size,
                                   node_color=colors[i],
                                   nodelist = nodelist.items()[i][1])
        nx.draw_networkx_edges(G, pos)

    else:
        nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=node_color)
        nx.draw_networkx_edges(G, pos)

    weights = { (u, v): info['weight'] for u, v, info in G.edges(data=True) }
    labels = { (u): info['name'] for u, info in G.nodes(data=True) }

    if(writeEdgeLabel is True):
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=weights, font_size = font_size, font_family='sans-serif')

    if(writeNodeLabel is True):
        nx.draw_networkx_labels(G, pos, labels, font_size = font_size)
    else:
        nx.draw_networkx_labels(G, pos)

    plt.savefig('../generated-data/'+img_name+".png", bbox_inches = 'tight', pad_inches=0.2)
    plt.close()
