from plot_graph import plot_weighted_graph
from load_graph import load_graph
import networkx as nx

data_path = '../data/'
data_name = [[  data_path + 'uk12distB.txt',    data_path + 'uk12_name.txt'],
             [  data_path + 'wg59distB.txt',    data_path + 'wg59_name.txt'],
             [  data_path + 'USAir97.txt',      data_path + 'USAir_names.txt']]

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


"""

    "The students that, like the wild animal being prepared for its tricks in the circus called 'life',
        expects only training as sketched above,
        will be severely disappointed: by his standards he will learn next to nothing"

                                                                                        - Edsger Dijkstra

xddxxxxxxxxxxxxxxxxxxxxxxxxxkkxkkkkkkkkkkkOOOOOkkOOOOOOOOOOO00OOOOO00000000000KKKK0KKXXXXXXXXNNNNNXXNNNNNXXNNNNNXNXXXXKK
xddxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkkkkkkkkkOOOOOOOOOOOOOOOOOOOO00000000000KKKKKKKXXXXXXXXNNNXXXNNNNNNNNNNNNNXXXXXXXXK
dddxxxxxxxxxxxxxxxxxkkxxxxxkkkkkkkkkkkOOOOkkOOOOOOOOOOOOOOOOOOO00000000000000KKKKKKKXXXXXXXNNNNXXNNNNNNNNNXNNXXXXNXXXXXX
dddxxxxxxxxxxxxxxxxxkxxxxxkkkkkkkkkkkOOOOOOOOkkOOOOOOOOOOOkkkxxkOOO0000000000KKKKKKKXXXXXXXXXNNXXXXNNNNNNXXXXXXXXXXXXKKX
ddddxxxxxxxxxxxxxxxxxkkxkkkkkkkkkkkkkkOOOkkkkxxkOOOOOkxdlc:;;;;:clooooolllldkOO000KKKKKKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXKKX
xdxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkkkkkxdooo:codxkxo:,'''''',,;;:cllllccc::ccllldkO00KKKKKKXXXXXXNXXXXXXXXXXXXXXXXXXXXX
dddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdddddolc;,'',;::;,'''''''''',',;;:::::;;;;;;;;;:clodxxk0KXKXXXXXXXXXXXXXXXXXXXXXXXXXX
dddddddddxxxxxxxxdxxxxxxxxxxxdoooolccoc;,'....''''''',,,,'''..''',,,,,,''''',,,;;;;;;:cloddxOKXXXXXXXXXXXXXXXXXXXXXXKKKK
dddddxxdddxxxddxxddxxxxxxxxdlclc:c:;;,'........''..''''',,,,'''',,,,,''''..'',,;:::;:;:ccloookKXKXXXXXXXXXXXXXXXXXXKKKKK
ddddddddddxxxddddddddddxO0kolcc;,,'.....................''''''''',;;;;,''''''',;:clcccccccooooxk0KKKKKKXXXXXXXXXXXXKKKKK
dodddddddxdxdddddddlc:cokkxdl;,'...........................'''''''',,,,,''',,,,,,,;:::::::colloldxO0KKKKXXXXXXXKXKKKKKKK
dooddooddddddooodddc;;;;;;;c:'.....................'''''''''''''''',,,'''',;;;,,,,;;,,,;;,;clllclodkO00KKKKKKKKKKKKKKKKK
dooddddoddddodxkxoc,'...''',;'.....................''..''''''''',,,'''''',,;;;,,,;,,'''',,,;::::coooddxO00KKKKKKKKKKKKK0
dooooooddddodkkxc;'''....'',,,'.....................''''',,,,,''''''''''',,,,',,'''''''''',,,;;;:lc::clokO0KKKKK00000000
oooooooooododxol:,''''..'''',,,,'...................''''''','''''.'''',,;:cc:::;,''''''''''',,;;;;;;;;:ldkO00000000000OO
oooooooooooodxdl;,''''..''''',,,,'............''''''''',,,'''''''',,,;::clloodl;,'..'''''''',,'',,,;:;;cllx0000000000000
ooooooooddooddl:;,,,''...'''''''''''''.''..'''.''''','''',,,,,,;;;:ccloooldkOko:,'..'.''.'''''',,;:::::llcd0000000000000
oooooooooodddol::;,,''..'''.......'''''.''''......'''''',,;;;::coodddxxkkO0XK0xl;,'''''''''..''';clc:::clokO0000000000OO
oooooooooooooool:;;,,''','........'''''....'......''',,;:lloodxkO0O00KKXXNNNXX0dl;,,,,,',;,''',,:cc::::::lxOOO00000OOOOO
oooooooooooooooo:;;;;;,,,''',,,,,'''''''..'''''',;:llldxkO000KKKXNNNNNNNNNNNXKKOx:;;;;;,;:;'',:;:cc:::::coxOOOO0000OOOOO
ooooooooolooooddlllclc:;,,;cxkxdlc:;;;,,,,,;;clodxkOO00KXXXXXXXNNNNNNNNNNNNNXKK0kc,;,,,,;;:;,;:::c:ccclcoxOOOOOOOOOOOOOO
oooooooooooooooddlllclc;,,c0NWNKOxdoccccccclddxkO000KXXXXXXXNNNNNNNNNNNNNNNNXKKOxc,,,;;;;;::;;:;;:::cloooxkOOOOOOOOOOOOO
ooooolooooooooool;:ccc:;,,xWWMMWNK0OkxddddxkkkO0KKXXXXXXNNNNNNNNNNNNNNNNNNWWNNX0kl:;;;;;;:c:;:::;:cc:cllodkkOOOOOOOOkkkO
oooooooooooooooolclol::,'cKMMMMMWNXK0OOkkkkOO000KKXXXXNNNNNNNNNNNNNNNNNNNWWWWWWNX0xl:::c:clc:cllccclc::::okOOOOOOOOOkOOO
oooooooooooolooollllc;,,;xWMMMMMWNX000OOOOO000KKKKXXXXXNNNNNNNNNNNNNNNNNNWWWWWWWNNKOdlccccllcclll:::::;;:okOOOOOOOOOOkkO
oooooooooooolooooll:;;,,oXMMMMMMWNXK0OOOOOO0000KKXXXXXXXXNNNNNNNNNNNNNNNNNWWWWWWWNX0kdlcllllcllcc:;;::;;cdkkOOOOOkkkkkkk
oooooooolllllooooooc:;,:0WMMMMMMWWNKOOOOOOOOO00KKKXKXKKXXNNNNNNNNNNNNNNNNNNNWWWWWNNKkdolloolllcc:;,;;;;:oxkkkkkkkkkkkkkk
oollllllllllllllloool:;oNMMMMMMMMWNXK0O000OO0000000000KKXNNNNNNNNNNNNNNNNNNNNNWWWWNXOolclllccc:;;:;;;;;cdxkkkkkkkkkkkkkk
olllllllllllllllllloolcxWWMMMMMMMMWNXK0K00000000000000KXXNNNNNNNNNNNNNNNNNNNNWWWWWWNXklccccc::;,,;:;;,,cdxkkkkkkkkkkkkkk
olllllllllllllllllloodlxNWMMMMMMMMWNXXKK00000K0000O00KXXXNNNNNNNNNNNNNNNNNWWWWWWNNNNNXOdcc:::;;;,,,,,,,lxkkkkkkkkkkkkkxk
olllllllllllllllllllooloKWWMMMMMMMWNNXK0000000OOOOO0KXXXNNNNNNNNNNNNNNNNNNWWWWWWWWNNNNN0dl::c:::;,,,,,,lxkkkkkkkkkkxxxxx
llllllllllllllllllllllllONWWMMMMWNNXK0OOOOO00OOOOOO00KXXXNXXXXXXNNXXNNNNNNNWWWWWWWWNNNNKxl::::::,,,,,,;oxkxkkkkkkxxkxxxx
ollllllllllllllllllllllcdXWWMMWWNK00OkkkkkOOOOkOOOOOO0000000KKKK00K0KKKXNNNNWWWNNNXK0Okdc:;,,,,,,;;,;:lkK0Okkkkkkkkkxxxx
lllllllllllllllllllllllcckNWMWWNXK00OxxxxxkkkxxkkxxxxdoocccllllllllooooddddkOOkxdooooc:;,,,,,,;;;;,:xOKOxxOkxkkkkxxxxxxx
lllllllllllllllllllcllllcoXWMWNNK0Oxoolllodddodxdoc:::;,,,,,;;;,,,,,,'',,,,;;::;;;;;;;;:ccc::::clllkKXKdoxOkxxxxxxxxxxxx
llllllllllllcccccccllllc:cKWNKOkdoc;,,,,,;;:cllllc:;,,'''',,,,,,;;:::;'',,'',;;;;:loxO0KKKkol::coxO0KXXkxk0Oxxxxxxxxxxxx
lllllllcllcccccccclc:::;''colc;;,,'''.....'',;;:cc;''',,,,''''''''',,;,''.',;;:ldOXNWWWWWNKdl::cdO0KKXNKkO0kxxxxxxxxxxxx
lllllllccllccccccll:''''',:cc:,,'''..............'..',;;;;,',;;'''',;,,,'',;;cdOXNWWMMMMWWXkocldk0KKXXXNK00xxxxxxxxxxxxx
lcccccccccccccccccc:'''',;:::,'''''.....''....',;:,.':clooc:;:::;;;c::::;,cdkOKNNWWWMMMWWWXOdok00kxdkO0XXX0xxxxxxxxxxxxx
lccccccccccccccccccc:;,,:clll:''',,'..'''''..;oxO0o'',;cdxoc:::cccclllodlcxKXNNNWWWWWMMWWWNKOOXWNOxkkOOKXXOxxxxxxxxxxxxx
ccccc::cccccccccc::ccc:,:cccdkxxoc:;,,,,,''''lxxO0kc,';:dkkdllllllloooxxccOXNNNNWWWWWWWWWNNNNWWWWNXXXKKXNXkddxxxdddddddd
cccccccccccccccc:::::cc;,cc:oKNN0oc:;;;;;,,''lxxO0Oko,;lokkkkkxddoooooxdcdKNXNNNWWWWWWWWNNNNNWWWNNNNXXNNNKxdddxxdddddddd
ccc::ccccccc::::::::::::,,::lKNNOocc::::;;,.'lxO0K00Odc:oxkkkkkkkxxdollloOKXXXXXXNNWWWWWNNNNNNWNNNXXNWWWXOddddddxxxxdddd
c::::::::::::::::::::::::,:llONXOoccccclll;;cxkO0KXXXKOkdccccccccccccclok0KKKKKKKXNNNWWWNNNNNNX0O0KKXNNXkdddddxxxxdddddd
c::::::::::::::::::::::::::odOK0xlcllooccokkO0OO00KXNXK0Okdlc:::ccloodxkO00000000KXXNNNNNNWWNX0kkkO0KXKkddddxxxxxxxxdddx
::::::::::::::::::::::::::coxdolcc::cclox0XXX0kOKK0KXXK00Okkxdddooddxk00000OOOO000KXXNNWWWWNNKkkOOO00Okdodddddxxxxxxxddx
:::::::::::::::::::::::::::oO0kxdoodxkOkxdkKkxxk0OkkkO00KKOkkxxxxkO00000000OOOOOOO0KXNNWWWWNNXK0Oxddoooooodddddxxxxddddd
::::::::::::::::::::::::::::oOOkxxxkkkxlccoxolloddoooooooddxkOOxooxkO00000000OOOO0KKNNNWWWWNWNNNXxdoooooodddddxxxxxxdddd
::::::::::::::::::::::::;:::cxOkxkkkkxoc:;;;:;;:ccc;;::;:clxO000OxddxkO000KKKK0000KXXNNWWWWWNNNNXxoooooooodddddddddddddd
:::::;;::::;::;:::;;;;;;:::::cxOkkOOkdc:;,,;oxo;',,;:lddxkkOOOO00OOkkkkkO0KXXXXKKKXXNNNNWWWNNNNNXxoooooooooodddddddddddd
::;;;;;;::;;;;;;;;;;;;;;::::::lxOO0Odc:;,:oxO0Ol',;;;lxkkOOkOOOOOOOOOOOOOO0KNNNXXXXXXNNNNNNNNNNNXkoooooooooodddddddddddd
:;;;;;;;;;;;;;;;;;;;;;;;;::;:::lkO0koc::cxkkkxdc:clccldxkkkkkkkkkkkkkOO000O0XNNNXXXXNNNNWWNNNNNNNkooooooooodddddddxddddd
:;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::oO0xoccdkkdddoooodxddddxxxxxxdddddddxxkO0000KXNNXXXXNNNNWNNNNNNNNOdooooooooddddddxxxxxdd
:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::okxdllolccclc::::cclcc:::::::;;::cclodxkO00KXXXXXXXXNNNNNNXNNNNN0doooooooddddxxxxxxxxdd
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:lxxocc;,''''''''',,,;;;;::cclodkkxdddxkkO0KKKXXXXXXXNNNNXXXNNNNKxoooooodddxxxxdxxxxddd
;;;;;;;;;;,,;;;;;;;;;;;;;;;;;;;;;;:oxdc:,'''',;:c;;;::ccloodxkkO0000OkkkkkkO000KKKKKKXKKKKKXXNNNWXkooooooddddxxxxxxxxxdd
;;;;;,,,,,,;;;;;,,,,,,;;;;;;;;;;;;;:dxl::;;;:dkxoc:::::clodxkkkO0000OOkkxxxkOO00000K000OOO0KXNNNWNOooooooodddxxxxxxxxxdd
;;;;,,,,,,,,,,,,,,,,,,,,;;;,,;;;;;;;:ol;::::lddl:;;;;;:::clddxkkOOOOkkxxxkkkOO000000OkkOOOO0KXNNWN0oooooodddddxxxxxxdddd
;;;;,,,,,,,,,,,,,,,,,,,,,;;,,,,,;;;;;:lc::cclol:,,;:::ccclodxkOOOOOOOOOkkOOO00000OOOOOOOkOO0KXNNWNOooooooddddddddddddddd
;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;cdolloddollclllloodkkO00K00000000000KKKK0OOkxkO00OOO0KKXNNNW0doooooodddddddddddddd
;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;cdxdxkkOOOOKK0OkkkO0KKXXKKK0KK0KXKKK000OxddxOKXK0OO0KXXNNWWKdooooooddddxxxdddxddd
;;;;;;;,,;,,,,,,,,,,,,,,,,,,,,,,;;;;;;;;:dkk000KXNX0OkkkkOO0KKK000000K0K00OOkxolldkOKNXK000KXNNWWWNOdoooooddddxxxddddddd
;;;;;;;,,,,,,,,,,,,,;;;,,,;;;;,,;;;;;;;;;:okOOOO0OkddddooddkkOOkkOkkOkkxxdolcc:clxO0XNNX00KKXNWWWWWNXOdodddddddddxxxdddx
;;;;,;;;;;;,,,;,,,,,,;;,,;;,,;;;;;;;;;;;;;:cdkxxddlcloolccloodddddddoollc::;;:coxO0KXNNXKKKXXNWWWWWXXWKxodddddddxxxxxxxx
;;;;,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;;;cddlc::::ccc:;::cllcccc:::;;;,;:clxO0KXNNNNNXXXXXNWWWWWX0NW0xdddddxxdddddddd
;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;;cOXkl:,,',,,,,,,,,,,,,,,,,,,,,;:ldkKXNNNNNNNNNNNNWWWMMMKkXMN0Oxdddxxdddddddd
;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;:dXWXOxl;,''''',,,,,,''''''',,;;cloxO0XNNNXXXNNNNNWWWMMW0kNMNOO0kxddddddxxxxd
;;;;;;;;,,,,,,,,,,,,,,,,,,,,,;;,,;;;;;;;;;:lxXWNKko:,'''.''',,;,''''',,,;:ccloxkO0KKXKK0KXNNNWWWWWN0XMMWOdO0kxxxdddddddd
;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;:odoOWWNXxc;,''.''''','''''',,;:clloddxkOKKKK0O0KNNNWWWWNKKWMMMKdx0K00Okkxxdddd
;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;;:lxkxlkWWWNKxoc;,''''''''''',,,;;:clloodxxO0KKK0000KNWWWWN0KWMMMMWOoxOKKKKKKK00OO
;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;ckOOxdcdNWWWXOxolc;,''''''',,,,;::cccloodxxk00XXXK00KNNWWWXNMMMMMMMKodx0XXXKKKKKKK
;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;:cokOOkxd:cOWWWXOxl::;;;,''''',,;::cclllooodxxkO0KXXXKKKNNWWWWMMMMMMMMKodk0KXXKKKKKKK
;;;;,,,,,,,,,,,,,,,,,,,,,,,,,;:ccoxkOOkkkkxdc;cKWNNKkoc:;;;;::cllllccllooddddxxxxkkO0KKXXXNNWWMMMMMMMMMMNKolxO0KKKXKKKXK
;;;;,;,,,,,,,,,,,,,,,,,,,,;:codddxkOOOkkkxxoc;,dWWNX0xolc:clloxkKXXK0kxxxkkkkxxxxxxkOO00KKXNWMMMMMMMMMMWXXxoxk00KXXKKKKX
;;;;,,,,,,,,,,,,,,,,,,,:codoolloxkkkkxxxxxxdl:;cKWNX0kddddxkO0KXNWWWWWNXK0OOkkkxxdxxk000XNWMMMMMMMMMMMMWNNxodk00KXNXKKKK
;;;;,,,,,,,,,,,,,,,:lodxxxocc:ldxdxxxddxxdodlc:,lKWXK0OkOO0XNNWWWWMMMMMMMWWNXKOxdddxk000NWMMMMMMMMMMMMMWWNddxkOOKXXXKKKK
;;;;,,,,,,,,,,,,;cokkkxdoolc::cddodkxdoddoodolc;;kNNNK0O0KXNNWWWWWWMMMMMMWMMMWKxolccclc:co0WMMMMMMMMMMMMWKooxkkO0KXXXXKK
;;;;,,;,;,;;;;:lxOOxddolccc::clddodddoodooooolc;,c0WNXKKXNNWWWWWWMMMMMMMMMMWKxc:;;;;;;::;,:0WMMMMMMMMMMMW0ldkkOO0KXXXXXX
:;;;;;;;;;;;:ok00kddooolc:c::clooooollolloooollc;;:xKNWWWWWWWWWWMMMMMMMMMMWO:;,,,,;;;::::;,:OWMMMMMMMMMMNkldxkk00KKKKKKK
:;;;;;;;;:lxO0OOkxdoolllc:::::ldoololclloollolooc::,:xNWMMWWMMWMMMMMMMMMMNk:,,,,,,,;;;;;:::ldKMMMMMMMMMMXxcldxO00KK0O00K
::;;;;;:ok0KKOkkxollllccc:::::odooolccllooooooddocc::;l0WMMMMMMMMMMMMMMMNx;'''''',,,,,;::lkOkONWMMMMMMMW0o:lxx000KKK0OO0
::::codOKK0K0kxxdllllcccc::::;lxdoolcclloodddddoollcc:,;xNMMMMMMMMMMMMMW0c:,'''''',,,,;:ckNNKkx0NMMMMMMWKxcldxkO0KXK0OOO
dxO0KKKKK00Okxdoolcccc:ccc:::;odxddolllloodddxddodolcc:;,cxXMMMMMMMMMWNKOkxc''''''''',,cONMMWN0kOKNWWMMMMWKOkxxOKXXK0000
KKKKKKK00Okkxoooolcccc:::::cc;oxxdoolllloooddxdoodllcl::;''c0WMMMMMWN0OKNNKd,'''''''',,dWWMMMMMWX0OkxkO00KKKKkxkOKKK000O
000000OOkxxxddoollccccc::::cc;oxdoooccccllododoollllclcc:,'',lONNX0kk0NWWWXx:'''''''',;OWMMMMMMMMWNxc::::lc:ldxkO0K0000O
OOkkkkkkxdxddddolllccc:::::::;oxdodollcccclloooolclolcllc:;'..';:;;o0NMMWWNOc,'''''',,;kNMMMMMMMMMWOocccol;,:ldk0KK0000O
kkkxkxxdxddooooolllcccc:c:::::odoloollllcclllodolllllclllc:,'..'''';l0WMWWWKc,'''';,,,',lkNMMMMMMMMNKOddxc,,:odO0KK00KKO
xkxkkkxdddoooollllccccc:c:c:::ooololccccccccloolcccclllllc:;,''.',:c:ckXWWWKl,''';,,,;,'',lONWMMMMMMWKkdo:,,:lxkOKXK0K0O
kkkxxxxdddooollllcccccc::cc:;:llooolllccccccclllc:c:clllllc::;;,'';lddcdXWWXd;'',;,',,,''',;cOWMMMMMW0xo::;,:okxk0KKKK0O
xxxxdoddooooooooolllccccccc:;:llololllcclccccollc:cccclllccclcc:,'';:dxxXWWXd;'''',,,,,;,,,,;l0WMMWWXOko;;;,:oddO0KKKKK0
xxddddododoooolllllllllccclc;:clloooollllllllllll:cccllllccllllc:;,,,;lo0WWO:,''''''',,;:::::coONWWXkxxo:;;;:odxO0K00KKK
xddoddddoodollllllllllcllccc;:llloolollooollcclol:llclolccllcloccc;,',::xNWk;,,'',''''';:cc::ccl0WW0kxol:::;:odO00000KKK

"""