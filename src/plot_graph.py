__author__ = 'Thales Menato'
__author__ = 'Daniel Nobusada'

import networkx as nx
import matplotlib.pyplot as plt
import datetime

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
                        seeds=None,
                        markerscale = 0.5):

    inicio = datetime.datetime.now()

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

    nodelist = {}
    # Caso o grafo tenha sido obtido a partir do Dijkstra
    if(seeds is not None):
        # Obter a lista de vertices ligados a cada semente utilizada
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
        lbl = [labels[i].split(" ")[0]+" [" + str(len(nodelist[i])) + "]" for i in seeds]
        if writeNodeLabel is False:
            plt.legend(tuple(seeds),tuple(lbl) , title="Sementes", scatterpoints = 1, markerscale = markerscale)
        else:
            plt.legend((tuple(lbl)), title="Sementes", scatterpoints = 1, markerscale = markerscale,
                       fontsize='small', framealpha=0.5)

    plt.savefig('../generated-data/'+img_name+".png", bbox_inches = 'tight', pad_inches=0.2)
    plt.close()
    return pos, (datetime.datetime.now() - inicio), nodelist


def write_images(data, uk12=True, wg59=True,usair97=True):
    print "Tempo geracao das imagens: "

    # Imagens para o grafo UK12
    if uk12 is True:
        pos, tempo, data['uk12']['nodelist'] = \
            plot_weighted_graph(data['uk12']['grafo'],
                                title="Grafo uk12 - Original",
                                img_name="uk12__original",
                                writeEdgeLabel=True,
                                writeNodeLabel=True,
                                node_size=4000,
                                iterations=1,
                                width=2)

        print "Grafo uk12 - Original\t\t" + str(tempo)


        h = data['uk12']['a']['h']
        pi = data['uk12']['a']['pi']
        pos, tempo, data['uk12']['a']['nodelist'] = \
            plot_weighted_graph(h, pos=pos,
                                title="Grafo uk12 - a",
                                img_name="uk12_a",
                                writeEdgeLabel=True,
                                writeNodeLabel=True,
                                seeds=data['uk12']['a']['seeds'],
                                pi=pi,
                                node_size=4000,
                                iterations=1,
                                width=2,
                                markerscale=0.2)

        print "Grafo uk12 - a\t\t\t\t" + str(tempo)

        h = data['uk12']['b']['h']
        pi = data['uk12']['b']['pi']
        pos, tempo, data['uk12']['b']['nodelist'] = \
            plot_weighted_graph(h, pos=pos,
                                title="Grafo uk12 - b",
                                img_name="uk12_b",
                                writeEdgeLabel=True,
                                writeNodeLabel=True,
                                seeds=data['uk12']['b']['seeds'],
                                pi=pi,
                                node_size=4000,
                                iterations=1,
                                width=2,
                                markerscale=0.2)

        print "Grafo uk12 - b\t\t\t\t" + str(tempo)

    # Imagens para o grafo WG59
    if wg59 is True:
        pos, tempo, data['wg59']['nodelist'] = \
            plot_weighted_graph(data['wg59']['grafo'],
                                title="Grafo wg59 - Original",
                                img_name="uk59__original",
                                writeNodeLabel=True,
                                node_size= 1200,
                                iterations=10,
                                width=0.3)

        print "Grafo wg59 - Original\t\t" + str(tempo)

        h = data['wg59']['a']['h']
        pi = data['wg59']['a']['pi']
        pos, tempo, data['wg59']['a']['nodelist'] = \
            plot_weighted_graph(h, pos=pos,
                                title="Grafo wg59 - a",
                                img_name="uk59_a",
                                writeNodeLabel=True,
                                writeEdgeLabel=True,
                                seeds=data['wg59']['a']['seeds'],
                                pi=pi,
                                iterations=10,
                                node_size= 1200,
                                width=0.3,
                                markerscale=0.3)

        print "Grafo wg59 - a\t\t\t\t" + str(tempo)

        h = data['wg59']['b']['h']
        pi = data['wg59']['b']['pi']
        pos, tempo, data['wg59']['b']['nodelist'] = \
            plot_weighted_graph(h, pos=pos,
                                title="Grafo wg59 - b",
                                img_name="uk59_b",
                                writeEdgeLabel=True,
                                writeNodeLabel=True,
                                seeds=data['wg59']['b']['seeds'],
                                pi=pi,
                                iterations=10,
                                node_size= 1200,
                                width=0.3,
                                markerscale=0.3)

        print "Grafo wg59 - b\t\t\t\t" + str(tempo)

    # Imagens para o grafo USAir97
    if usair97 is True:
        pos, tempo, data['usair97']['nodelist']= \
            plot_weighted_graph(data['usair97']['grafo'],
                                title="Grafo USAir97 - Original",
                                img_name="usair97__original",
                                font_size=5,
                                node_size= 200,
                                iterations=1,
                                width=0.1,
                                figsize=(20,10))

        print "Grafo USAir97 - Original\t" + str(tempo)

        h = data['usair97']['a']['h']
        pi = data['usair97']['a']['pi']
        pos, tempo, data['usair97']['a']['nodelist'] = \
            plot_weighted_graph(h, pos=pos,
                                title="Grafo USAir97 - a",
                                img_name="usair97_a",
                                writeEdgeLabel=True,
                                writeNodeLabel=True,
                                seeds=data['usair97']['a']['seeds'],
                                pi=pi,
                                iterations=1,
                                font_size=5,
                                node_size=200,
                                width=0.1,
                                figsize=(20,10))

        print "Grafo USAir97 - a\t\t\t" + str(tempo)

        h = data['usair97']['b']['h']
        pi = data['usair97']['b']['pi']
        pos, tempo, data['usair97']['b']['nodelist'] = \
            plot_weighted_graph(h, pos=pos,
                                title="Grafo USAir97 - b",
                                img_name="usair97_b",
                                writeEdgeLabel=True,
                                writeNodeLabel=True,
                                seeds=data['usair97']['b']['seeds'],
                                pi=pi,
                                iterations=1,
                                font_size=5,
                                node_size=200,
                                width=0.1,
                                figsize=(20,10))

        print "Grafo USAir97 - b\t\t\t" + str(tempo)
