from plot_graph import plot_weighted_graph
from load_graph import load_graph
import networkx as nx
import numpy as np

data_path = '../data/'
data_name = [[  data_path + 'uk12distB.txt',    data_path + 'uk12_name.txt'],
             [  data_path + 'wg59distB.txt',    data_path + 'wg59_name.txt'],
             [  data_path + 'USAir97.txt',      data_path + 'USAir_names.txt']]

def Dijkstra(G, seed):
#   Como referencia foi utilizado o pseudocode encontrado em:
#       https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
#   e no codigo fornecido pelo prof. em sala de aula

    # Lambda: weight de cada aresta
    # Pi: predecessor de cada vertice
    Lambda = {}
    Pi = {}

    # Inicializacao
    for v in G.nodes():
        Lambda[v] = np.inf
        Pi[v] = None
    Lambda[seed] = 0
    Q = G.nodes()

    # Loop principal
    while Q:
        # smallest = infinito para comparacao
        # u sempre primeiro valor (garante existencia)
        smallest = np.inf
        u = Q[0]

        # ao final do loop, u contem a menor distancia e smallest o menor valor
        # e recebe os vertices (indice), w os pesos dos vertices (valor)
        for e, w in Lambda.items():
            if (w < smallest) and (e in Q):
                smallest = w
                u = e

        # remover u de Q
        del Q[Q.index(u)]


        for v in G.neighbors(u):
            alt = Lambda[u] + G[u][v]['weight']
            # Verifica se v ainda esta na lista Q e se caminho eh menor
            if (v in Q) and (alt < Lambda[v]):
                Lambda[v] = alt
                Pi[v] = u

    print Lambda
    print Pi


if __name__ == '__main__':
    g = load_graph(data_name[0][0],data_name[0][1])

    path = nx.single_source_dijkstra(g, 0)

    # Pega os caminhos separados
    nos = path[1]
    edges = []

    # Cria uma lista de arestas com os vertices retornados
    for i in range(0, len(nos)):
        temp = []
        for j in range(0, len(nos[i]) - 1 ):
            t = nos[i][j], nos[i][j+1]
            temp.append(t)
        edges.append(temp)

    Dijkstra(g, 0)
    print path
    #plot_weighted_graph(g)
"""

    "The students that, like the wild animal being prepared for its tricks in the circus called 'life',
        expects only training as sketched above,
        will be severely disappointed: by his standards he will learn next to nothing"

                                                                                        - Edsger Dijkstra

;::;;;;;;;;;;;;;;;;;;;;;;;;;,,;,,,,,,,,,,,''''',,'''''''''''..'''''..........................     ..     ..     . ......
;::;;;;;;;;;;;;;;;;;;;;;;;;;,,,,,,,,,,,,,,,,,,''''''''''''''''''''..........................   ...             .........
:::;;;;;;;;;;;;;;;;;,,;;;;;,,,,,,,,,,,'''',,'''''''''''''''''''............................    ..         .  .... ......
:::;;;;;;;;;;;;;;;;;,;;;;;,,,,,,,,,,,'''''''',,''''''''''',,,;;,'''..........................  ....      ...............
::::;;;;;;;;;;;;;;;;;,,;,,,,,,,,,,,,,,''',,,,;;,''''',;:lodxxxxdolcccccllll:,''.........................................
;:;;;;;;;;;;;;;;;;;;;;;;;;,,,,,,,,,,,,,,;:cccdoc:;,;cdkOOOOOOkkxxdolllloooddoolll:,'.............. .....................
:::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::cloxkOOkxddxkOOOOOOOOOOkOkxxdddddxxxxxxxxxdolc:;;,..............................
:::::::::;;;;;;;;:;;;;;;;;;;;:ccccloocoxkO0000OOOOOOOkkkkOOO00OOOkkkkkkOOOOOkkkxxxxxxdolc::;'...........................
:::::;;:::;;;::;;::;;;;;;;;:lolododxxkO00000000OO00OOOOOkkkkOOOOkkkkkOOOO00OOkkxdddxdxdoolccc,..........................
::::::::::;;;::::::::::;'.,clooxkkO000000000000000000000OOOOOOOOOkxxxxkOOOOOOOkxdolooooooocccc;,........................
:c:::::::;:;:::::::lodoc,,;:lxkO000000000000000000000000000OOOOOOOOkkkkkOOOkkkkkkkxdddddddocllcl:;'.....................
:cc::cc::::::ccc:::oxxxxxxxodO000000000000000000000OOOOOOOOOOOOOOOOkkkOOOOkxxxkkkkxxkkkxxkxolllolc:,'...................
:cc::::c::::c:;,;cokO000OOOkxO000000000000000000000OO00OOOOOOOOOkkkOOOOOOkkxxxkkkxkkOOOOkkkxddddoccc::;'................
:cccccc::::c:,,;oxOOO0000OOkkkO000000000000000000000OOOOOkkkkkOOOOOOOOOOOkkkkOkkOOOOOOOOOOkkkxxxdloddolc,'..............
cccccccccc:c:;cldkOOOO00OOOOkkkkO0000000000000000000OOOOOOOkOOOOO0OOOOkkxdoodddxkOOOOOOOOOOOkkxxxxxxxxdl:,'...........''
cccccccccccc:;:lxkOOOO00OOOOOkkkkO000000000000OOOOOOOOOkkkOOOOOOOOkkkxddollcc:lxkO00OOOOOOOOkkOOkkkxdxxoll;.............
cccccccc::cc::ldxkkkOO000OOOOOOOOOOOOO0OO00OOO0OOOOOkOOOOkkkkkkxxxdoolcccl:,',cdkO00O0OO0OOOOOOkkxdddddllo:.............
cccccccccc:::clddxkkOO00OOO0000000OOOOO0OOOO000000OOOOOOkkxxxddocc:::;;,,'....;lxkOOOOOOOOO00OOOxolodddolc,'..........''
cccccccccccccccldxxkkOOOkO00000000OOOOO0000O000000OOOkkxdllcc:;,'.'......   ...:lxkkkkkOkxkOOOkkdooddddddl;'''.....'''''
ccccccccccccccccdxxxxxkkkOOOkkkkkOOOOOOO00OOOOOOkxdlll:;,'.......           ...';dxxxxxkxdxOOkdxdoodddddoc;''''....'''''
ccccccccclcccc::lllolodxkkxo;,;:lodxxxkkkkkxxolc:;,''..........             ....,okxkkkkxxdxkxdddodoooloc;''''''''''''''
ccccccccccccccc::llloloxkko.   .';:coooooool::;,'...........                ...';okkkxxxxxddxxdxxdddolccc;,'''''''''''''
ccccclcccccccccclxdooodxkk;      ..',;::::;,,,'.........                      ..,ldxxxxxxdodxdddxdoodollc:,,'''''''',,,'
cccccccccccccccclolclddkOo.       ...'',,,,''.........                          ..;ldddodolodolloooloddddc,''''''''','''
cccccccccccclccclllloxkkx;        ....'''''............                           .':loooolloollldddddxxdc,'''''''''',,'
cccccccccccclcccclldxxkkc.        ...''''''..............                         ..,:lollllolloodxxddxxo:,,''''',,,,,,,
cccccccclllllccccccodxkd.          .'''''''''............                          .,:cllccllloodxkxxxxdc;,,,,,,,,,,,,,,
cclllllllllllllllcccldxc           ...'...''.............                          .'clolllooodxxdxxxxxo:;,,,,,,,,,,,,,,
cllllllllllllllllllcclo;            .....................                           .,loooooddxkkxdxxkko:;,,,,,,,,,,,,,,
cllllllllllllllllllcc:l;            ..............'......                            .':oodddxxxkkkkkkkl;,,,,,,,,,,,,,;,
clllllllllllllllllllcclc.            .........'''''.....                               .:lddodddxkkkkkkl;,,,,,,,,,,;;;;;
llllllllllllllllllllllll'          ...'''''..''''''...... ......  ..                   .;lddddddkkkkkkxc;,;,,,,,,;;,;;;;
cllllllllllllllllllllllo:.       ...',,,,,'''',''''''...................          ...',:odxkkkkkkxxkxdl,..',,,,,,,,,;;;;
llllllllllllllllllllllloo,      ....';;;;;,,,;;,,;;;;:ccooollllllllcccc::::,'',;:ccccodxkkkkkkxxxxkd;'.';;',;,,,,;;;;;;;
lllllllllllllllllllolllloc.     ..';cclllc:::c:;:codddxkkkkkxxxkkkkkkOOkkkkxxddxxxxxxxxdoooddddolll,...:c;',;;;;;;;;;;;;
llllllllllllooooooollllodo.  .',:coxkkkkkxxdollllodxkkOOOOkkkkkkxxdddxOOkkOOkxxxxdlc;'....,clddoc;'....,;,.';;;;;;;;;;;;
lllllllolloooooooolodddxOOocloxxkkOOO00000OOkxxdooxOOOkkkkOOOOOOOOOkkxkOO0Okxxdl:'.       .:lddo:'.... .,'.,;;;;;;;;;;;;
llllllloolloooooolldOOOOOkdoodkkOOO00000000000000O00OkxxxxkOkxxOOOOkxkkkOOkxxo:'.         .,col:,...... ...;;;;;;;;;;;;;
loooooooooooooooooodOOOOkxdddkOOOOO00000OO0000Okxdk0Odolccodxdddxxxoddddxko:,'.           .':c,..,;:,'.....;;;;;;;;;;;;;
looooooooooooooooooodxkkdollldOOOkkO00OOOOO00xc;'.cOOkxo:;codddoooolllc:lo;..              .''.  ';,,''...';;;;;;;;;;;;;
oooooddooooooooooddooodkdooo:,;;codxkkkkkOOOOl;;'.,okOxd:,,:lllllllccc;;oo'.                      ...... .,::;;;::::::::
oooooooooooooooodddddooxkoodc.  .codxxxxxkkOOl;;'.',ckxlc,,,,,;::ccccc;:o:. .                       ..   .;:::;;::::::::
oooddoooooooddddddddddddkkddl.  'cooddddxxk0Ol;'....':odc;,,,,,,,;;:clllc'.......                 ..    .'::::::;;;;::::
oddddddddddddddddddddddddkdll' .'cooooolllxxo;,'......',:ooooooooooooolc,.........            ..'....  .,:::::;;;;::::::
oddddddddddddddddddddddddddc:'..;lollccooc,,'.''.... ...',:lodddoolcc:;,'...........         ..,,,'....,::::;;;;;;;;:::;
ddddddddddddddddddddddddddoc;:clooddoolc;.....,'.........',,;:::cc::;,.....''''......        .,,'''..',:c:::::;;;;;;;::;
dddddddddddddddddddddddddddc'.,;:cc:;,',;:,.,;;,.',,,'....',,;;;;,'........'''''''...        ...';::cccccc:::::;;;;:::::
ddddddddddddddddddddddddddddc'',;;;,,,;looc;cllc::ccccccc::;,'';cc;,'........''''...            .;:cccccc:::::;;;;;;::::
ddddddddddddddddddddddddxdddo;',;,,,,;codxxxdxxdoooxxddxdol;'...';::;,'..............           .;cccccccc::::::::::::::
dddddxxddddxddxdddxxxxxxdddddo;',,'',:odxkkxc;cxOkkxdl::;,,''''..'',,,,,'...........            .;cccccccccc::::::::::::
ddxxxxxxddxxxxxxxxxxxxxxddddddl;''.':odxkdc;'.'lOkxxxl;,,'',''''''''''''''..   ......           .,cccccccccc::::::::::::
dxxxxxxxxxxxxxxxxxxxxxxxxddxdddl,'.,coddo;,,,;:odolool:;,,,,,,,,,,,,,''...'..   ....             ,ccccccccc:::::::;:::::
dxxxxxxxxxxxxxxxxxxxxxxxxxxxxdddc'.;coo:,,:::cccc:;::::;;;;;;:::::::;;,'......  ....             ':cccccccc::::::;;;;;::
dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxddc,;:llcloooloddddooloodddddddxxddoolc:;,'...........      .     .:ccccccc::::;;;;;;;;::
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdl;;cooxkOOOOOOOOOkkkxxxxddoolc:,,;:::;,,'...........    ...    .;cccccc:::;;;;:;;;;:::
xxxxxxxxxxkkxxxxxxxxxxxxxxxxxxxxxxdc;:odkOOOOkxdoxxxddoolcc:;,,'....',,,,,,'.................    .,cccccc::::;;;;;;;;;::
xxxxxkkkkkkxxxxxkkkkkkxxxxxxxxxxxxxd:;lddxxxd:,;codddddolc:;,,,'....'',,;;;,''.........'''...     'ccccccc:::;;;;;;;;;::
xxxxkkkkkkkkkkkkkkkkkkkkxxxkkxxxxxxxdclxddddl::ldxxxxxdddol::;,,'''',,;;;,,,''......',,''''...    .cccccc:::::;;;;;;::::
xxxxkkkkkkkkkkkkkkkkkkkkkxxkkkkkxxxxxdloddoolcldkkxdddooolc:;,''''''''',,'''.....''''''',''...    'cccccc:::::::::::::::
xxxxxxxkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxo:cllc::cllollllcc:,,'...................'',;,'..'''....    .:cccccc::::::::::::::
xxxxxxkkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxxo:;:;,,''''...',,,'....................';::;'....''....    .:cccccc::::;;;:::;:::
xxxxxxxkkxkkkkkkkkkkkkkkkkkkkkkkxxxxxxxxd:,,..... ..',,,,''...............'',;cll:,'. .......      ':ccccc::::;;;:::::::
xxxxxxxkkkkkkkkkkkkkxxxkkkxxxxkkxxxxxxxxxdc,''''.',::::cc::,,'',,',,',,;;:cloodol;'..  ......       .':c:::::::::;;;:::;
xxxxkxxxxxxkkkxkkkkkkxxkkxxkkxxxxxxxxxxxxxdo:,;;::lolccloolcc:::::::cclloddxxdoc;'...  ......      .. .;c:::::::;;;;;;;;
xxxxkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxxxo::loddddooodxddolloooodddxxxkxdol;'...     .....      ..  .;:::::;;::::::::
xxxxkkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxxo'.,ldkkOkkkkkkkkkkkkkkkkkkkkkxdl:,..                  .,.  .';:::;;::::::::
xxxxxxxkkkkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxd:. .';lxkOOOOOkkkkkkOOOOOOOkkxxolc;'..   ...           .,   ''.,;::::::;;;;:
xxxxxxxxkkkkkkkkkkkkkkkkkkkkkxxkkxxxxxxxxxdl;.  .,cdkOOO0OOOkkxkOOOOOkkkxdoolc;,'.........         ..   ':'.,;;;::::::::
xxxxxxxkkkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxxdc:c'   .;oxkOO0OOOOOkOOOOOOkkxdollc::;,'.....'..        ..    .:;....',,;;::::
xxxxxxxkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxxxdl;,;l,    .;coxkOOOOOOOOOOOkkkxxdollcc:;;'.........      ..      'c;'.........''
xxxxkkkkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxo,'';:o:    .';cloxkOOOOOOOkkkkxddooolcc:;;,.........     .        .c:;...........
xxxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxdoc,'',;:do'   .';lddxxxkOOOOOkkxddoolllccc:;;,'........              .c:,...........
xxxxkkkkkkkkkkkkkkkkkkkkkkkkkxdooc;,'',,,,;:oxo.   .,codxxxxddolllloollcc::::;;;;,,'......               .cl;'..........
xxxxkxkkkkkkkkkkkkkkkkkkkkxdoc:::;,''',,,;;coxk:   ..;clodollc;,.....,;;;,,,,;;;;;;,''.....             ..;c;,..........
xxxxkkkkkkkkkkkkkkkkkkkdoc:ccllc;,,,,;;;;;;:ldxo.  ..,::::;,'...       ...'',,,;;:;;,....                 ;c:,.... .....
xxxxkkkkkkkkkkkkkkkdlc:;;;coodl:;:;;;::;;:c:lodkl. ...',''..                ..';:::;,...                  ::;,''........
xxxxkkkkkkkkkkkkxoc,,,;:ccloddo::c:,;:c::cc:cloxx,   ..'...                   .;clooolodoc.              .cc;,,'........
xxxxkkxkxkxxxxdl;'';::cloooddol::c:::cc:cccccloxko.  ....                   .;odxxxxxxddxkd.             .l:,,''........
dxxxxxxxxxxxdc,..,::ccclododdolcccccllcllcccclloxxd;.                      'dxkkkkxxxddddxkd'            ,l:;,,.........
dxxxxxxxxdl;'.'',;:cclllodddddl:cclclollccllclccoddkd;                    ,dkkkkkkkxxxxxdddl:.          .;ol:;'.....'...
ddxxxxxdc,...',,;cllllooodddddc:cccloollcccccc::cooddxl.                 ;xOOOOOOkkkkkxddl,','          .cdl;;.......''.
ddddoc:'.....,;;:llllooooddddxl;:ccloollcc:::::cclloodkx;               .odkOOOOOOkkkkxdo,  .,;.        .;ol:;,'.....'''
:;'........',;:ccloooodooodddxc:;::cllllcc:::;::c:cloodxko;.           .',;oOOOOOOOOOkko'     .,'.        .',;;'........
.........',,;ccccloooodddddooxc;;:ccllllccc::;:cc:llolddxOOo.        .'.  .:kOOOOOOOOkk:        ..',;,'......,;,'......'
......'',;;;::cclloooooddddooxc;:cccoooollc:c:cclllloloodkOOkl'  ..,,.    .;dOOOOOOOOkx'           ;oddddlodl:;,'......'
'',,,,,,;:;::::clllooodddddddxc;:c:clloooollcccclolclollodxO00Oxdxxc.      'okOOOOOOkkx,           'coooclxkdl:,.......'
,,,;,;;:;::cccccllloooododddddc:clcclllloolllc:clllllolllodkO00OOOOxl.     .okOOOOxkkkOkl,          .'::;okkdc:'.......'
;,;,,,;:::ccccllllooooodododddccclcloooooooolccloooolllllodxkOO0Okdodo,.   .lkOOOxkkkxkOOkl'         .,:cdkkdl;,'......'
,,,;;;;:::cccllllooooooddoodxdllccclllooooooolllododollllloddxxkOOxl::o:.  .:xOOkxkOkkkOOOkxo'       .;cddxkdc,;,......'
;;;;:c::ccccccccclllooooooodxdllclclllooloooocllodoooollloooloodkOOxd:;;.  .:xOOOOkkkkkxkkkkxl.     .',cxxxkdc::'.......
;;::::c:c:ccccllllllllloooloxdollcccclllllllllllldooolllloollllodxkkkxlc.  'dkOOOOOOOkkxdddddoc'   .,;;cdxxxdc:;'.......
;::c::::cc:cllllllllllolloooxdlllcclcllccclloolcldllolcloollolcoooxkOkdd;  ,xkkOOkOOOOOxdooddool.  .,;cldddxdc:'........

"""