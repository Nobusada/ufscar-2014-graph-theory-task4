from plot_graph import plot_weighted_graph
from load_graph import load_graph

data_path = '../data/'
data_name = [[  data_path + 'uk12distB.txt',    data_path + 'uk12_name.txt'],
             [  data_path + 'wg59distB.txt',    data_path + 'wg59_name.txt'],
             [  data_path + 'USAir97.txt',      data_path + 'USAir_names.txt']]

if __name__ == '__main__':
    g = load_graph(data_name[0][0],data_name[0][1])
    plot_weighted_graph(g, writeNodeLabel=True)
