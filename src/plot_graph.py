__author__ = 'Thales Menato'
__author__ = 'Daniel Nobusada'

import networkx as nx
import matplotlib.pyplot as plt

def plot_weighted_graph(G,
                        pos=None,
                        pi=None,
                        writeNodeLabel = False,
                        writeEdgeLabel = False,
                        iterations=100,
                        node_size=1000,
                        node_color='fuchsia',
                        font_size=9,
                        width=0.5,
                        img_name="default",
                        title=None,
                        figsize=(16,10),
                        k=1,
                        seeds=None):

    colors = {0: 'red',
              1: 'blue',
              2: 'green',
              3: 'fuchsia',
              4: 'white'}

    plt.figure(figsize=figsize)
    plt.title(title)
    plt.margins(0)
    plt.axis('off')

    # Se nao foi passado as posicoes dos vertices, calcular elas
    if (pos is None):
        pos = nx.spring_layout(G, k=k, iterations=iterations)

    # Caso o grafo tenha sido obtido a partir do Dijkstra
    if(seeds is not None):
        # Obter a lista de vertices ligados a cada semente utilizada
        nodelist = {}
        Q = G.nodes()

        # Inicializacao sementes em suas nodelist e remocao da lista de vertices
        for s in seeds:
            try:
                nodelist[s] = [s]
                del Q[Q.index(s)]
            except IndexError:
                print "Erro na plotagem : imagem " + str(img_name)
                print "Sementes: " + str(seeds)
                print "Nodelist: " + str(nodelist)
                exit(-1)
            except ValueError:
                print "Erro na plotagem : imagem " + str(img_name)
                print "Sementes: " + str(seeds)
                print "Nodelist: " + str(nodelist)
                exit(-1)
        # Enquanto houver vertices
        while Q:
            temp = []
            u = Q[0]
            del Q[Q.index(u)]

            # Lista de vertices a partir de u ate semente
            while u is not None:
                temp.append(u)
                u = pi[u]

            # Para a lista obtida, o ultimo valor eh a semente portanto
            # sera inserido na nodelist[ultimo_valor]
            # todos os vertices obtidos e ja sao removidos de Q (evitar verificacao extra)
            for i in range(0, len(temp) - 1):
                if temp[i] not in nodelist[temp[len(temp) - 1]]:
                    nodelist[temp[len(temp) - 1]].append(temp[i])
                if temp[i] in Q:
                    del Q[Q.index(temp[i])]

        # insere vertice na lista de semente em que esta conectado
        """
        for s in seeds:
            if (nx.node_connectivity(G, s, u) is 1):
                nodelist[s].append(u)
                del Q[Q.index(u)]
                print "Connectivity!"
                print "seed: " + str(s) + " u: " + str(u)
                print "nodelist: " + str(nodelist)
                print "Q : " + str(Q)
        """
        # Usando a nodelist obtida, para cada semente (indice),
        # escrever seus vertices com uma cor pre-definida
        for i in range(0, len(seeds)):
            nx.draw_networkx_nodes(G, pos,
                                   node_size=node_size,
                                   node_color=colors[i],
                                   nodelist = nodelist.items()[i][1])
        # desenha as arestas
        nx.draw_networkx_edges(G, pos, width=width)

    # Nenhuma semente foi passada, portanto grafo original
    else:
        nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=node_color)
        nx.draw_networkx_edges(G, pos, width=width)

    weights = { (u, v): info['weight'] for u, v, info in G.edges(data=True) }
    labels = { (u): info['name'] for u, info in G.nodes(data=True) }

    if(writeEdgeLabel is True):
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=weights, font_size = font_size, font_family='sans-serif')

    if(writeNodeLabel is True):
        nx.draw_networkx_labels(G, pos, labels, font_size = font_size)
    else:
        nx.draw_networkx_labels(G, pos, font_size = font_size)

    if seeds is not None:
        if writeNodeLabel is False:
            plt.legend((tuple(seeds)), title="Sementes", scatterpoints = 1, markerscale = 0.5)
        else:
            lbl = []
            for i in seeds:
                lbl.append(labels[i])
            plt.legend((tuple(lbl)), title="Sementes", scatterpoints = 1, markerscale = 0.5,
                       fontsize='small', framealpha=0.5)

    plt.savefig('../generated-data/'+img_name+".png", bbox_inches = 'tight', pad_inches=0.2)
    plt.close()
    return pos

def write_images(data, uk12=True, wg59=True,usair97=True):

    # Imagens para o grafo UK12
    if uk12 is True:
        pos = plot_weighted_graph(data['uk12']['grafo'], title="Grafo uk12 - Original",
                                  writeEdgeLabel=True, writeNodeLabel=True, img_name="uk12__original")

        h = data['uk12']['a']['h']
        pi = data['uk12']['a']['pi']
        plot_weighted_graph(h, pos=pos, title="Grafo uk12 - a", img_name="uk12_a",
                            seeds=data['uk12']['a']['seeds'], pi=pi,writeEdgeLabel=True, writeNodeLabel=True)

        h = data['uk12']['b']['h']
        pi = data['uk12']['b']['pi']
        plot_weighted_graph(h, pos=pos, title="Grafo uk12 - b", img_name="uk12_b",
                            seeds=data['uk12']['b']['seeds'], pi=pi, writeEdgeLabel=True, writeNodeLabel=True)

    # Imagens para o grafo WG59
    if wg59 is True:
        pos = plot_weighted_graph(data['wg59']['grafo'], title="Grafo wg59 - Original",
                                  node_size= 800, writeNodeLabel=True,iterations=10, img_name="uk59__original")

        h = data['wg59']['a']['h']
        pi = data['wg59']['a']['pi']
        plot_weighted_graph(h, pos=pos, pi=pi, title="Grafo wg59 - a", seeds=data['wg59']['a']['seeds'],
                            writeEdgeLabel=True, writeNodeLabel=True,iterations=10, img_name="uk59_a")

        h = data['wg59']['b']['h']
        pi = data['wg59']['b']['pi']
        plot_weighted_graph(h, pos=pos, pi=pi, title="Grafo wg59 - b", seeds=data['wg59']['b']['seeds'],
                            writeEdgeLabel=True, writeNodeLabel=True,iterations=10, img_name="uk59_b")

    # Imagens para o grafo USAir97
    if usair97 is True:
        pos = plot_weighted_graph(data['usair97']['grafo'], title="Grafo USAir97 - Original",
                                  font_size=5, node_size= 200,iterations=1,
                                  width=0.1, figsize=(20,10), img_name="usair97__original")

        h = data['usair97']['a']['h']
        pi = data['usair97']['a']['pi']
        plot_weighted_graph(h, pos=pos, pi=pi, title="Grafo USAir97 - a", seeds=data['usair97']['a']['seeds'],
                            writeEdgeLabel=True, writeNodeLabel=True,iterations=1,
                            font_size=5, node_size=200, width=0.1, figsize=(20,10), img_name="usair97_a")

        h = data['usair97']['b']['h']
        pi = data['usair97']['b']['pi']
        plot_weighted_graph(h, pos=pos, pi=pi, title="Grafo USAir97 - b", seeds=data['usair97']['b']['seeds'],
                            writeEdgeLabel=True, writeNodeLabel=True,iterations=1,
                            font_size=5, node_size=200, width=0.1, figsize=(20,10), img_name="usair97_b")
