__author__ = 'Thales Menato'
__author__ = 'Daniel Nobusada'

from plot_graph import plot_weighted_graph
from load_graph import load_graph
from dijkstra import *
import datetime
import networkx as nx
import numpy as np

data_path = '../data/'
data = {
    'uk12':{'dist':data_path + 'uk12distB.txt','name':data_path + 'uk12_name.txt'},
    'wg59':{'dist':data_path + 'wg59distB.txt','name':data_path + 'wg59_name.txt'},
    'usair97':{'dist':data_path + 'USAir97.txt','name':data_path + 'USAir_names.txt'}
    }

if __name__ == '__main__':

    data['uk12']['a'] = {}
    data['uk12']['b'] = {}

    # Simulacao do grafo UK12, com k = 2
    g = load_graph(data['uk12']['dist'],data['uk12']['name'])

    # Usaremos a periferia para obter duas sementes espalhadas
    data['uk12']['a']['seeds'] = nx.periphery(g)

    # Usaremos um vertice aleatorio e um de seus vizinhos como sementes proximas uma da outra
    random_v = np.random.randint(0, len(g.nodes()))

    data['uk12']['b']['seeds'] = ([random_v,
                 g.neighbors(random_v)[np.random.randint(0, len(g.neighbors(random_v)))]])

    # Executando o Dijkstra nas sementes
    data['uk12']['a']['lambda'], \
    data['uk12']['a']['pi'],\
    data['uk12']['a']['h'] = dijkstra(g, data['uk12']['a']['seeds'])

    data['uk12']['b']['lambda'], \
    data['uk12']['b']['pi'], \
    data['uk12']['b']['h'] = dijkstra(g, data['uk12']['b']['seeds'])

    # Gera imagens das comunidades encontradas
    plot_weighted_graph(g, img_name="Grafo uk12 - Original",
                        writeEdgeLabel=True, writeNodeLabel=True)

    h = data['uk12']['a']['h']
    plot_weighted_graph(h, img_name="Grafo uk12 - a",
                        seeds=data['uk12']['a']['seeds'], writeEdgeLabel=True, writeNodeLabel=True)

    h = data['uk12']['b']['h']
    plot_weighted_graph(h, img_name="Grafo uk12 - b",
                        seeds=data['uk12']['b']['seeds'], writeEdgeLabel=True, writeNodeLabel=True)

    # Gera relatorio para grafo UK12
    uk12_data = \
        "Grafo UK12:\n" \
        "\n\ta) Sementes utilizadas: " + str(data['uk12']['a']['seeds'])+ "\n" \
        "\t\tLambda:\n"
    for v, w in data['uk12']['a']['lambda'].items():
        uk12_data += "\t\t\t" + str(v) + " : " + str(w) + "\n"
    uk12_data += "\t\tPi:\n"
    for v, w in data['uk12']['a']['pi'].items():
        uk12_data += "\t\t\t" + str(v) + " : " + str(w) + "\n"
    uk12_data +="\n\tb) Sementes utilizadas: " + str(data['uk12']['b']['seeds'])+ "\n"\
        "\t\tLambda:\n"
    for v, w in data['uk12']['b']['lambda'].items():
        uk12_data += "\t\t\t" + str(v) + " : " + str(w) + "\n"
    uk12_data += "\t\tPi:\n"
    for v, w in data['uk12']['b']['pi'].items():
        uk12_data += "\t\t\t" + str(v) + " : " + str(w) + "\n"

    # Escreve todos os relatorio no arquivo '/generated-data/simulation-results.txt'
    try:
        f = open('../generated-data/simulation-results.txt', "w")
        f.write("Simulacao gerada em "+ str(datetime.datetime.today()) + "\n\n")
        f.write(uk12_data)
        f.close()
    except IOError:
        print "Erro na escrita do arquivo de simulacao"
