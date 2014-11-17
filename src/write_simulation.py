__author__ = 'Thales'
import datetime

def write_simulation(data):
    # Gera relatorio para grafo UK12
    uk12_data = \
        "Grafo UK12:\n" \
        "\n\ta) Sementes utilizadas: " + str(data['uk12']['a']['seeds'])+ "\n" \
        "\t\tVertice\t\t\tLabel\t\tPi\t\t\tLambda\n"
    for i in data['uk12']['grafo'].nodes():
        uk12_data += "\t\t\t" + str(i) + "\t\t" +\
              str(data['uk12']['lbl'][i])
        if(len(str(str(data['uk12']['lbl'][i]))) > 7):
            uk12_data += "\t\t"
        else:
            uk12_data += "\t\t\t"
        uk12_data += str(data['uk12']['a']['pi'][i]) + "\t\t\t" +\
              str(data['uk12']['a']['lambda'][i]) + "\n"

    uk12_data +="\n\tb) Sementes utilizadas: " + str(data['uk12']['b']['seeds'])+ "\n"\
        "\t\tVertice\t\t\tLabel\t\tPi\t\t\tLambda\n"
    for i in data['uk12']['grafo'].nodes():
        uk12_data += "\t\t\t" + str(i) + "\t\t" +\
              str(data['uk12']['lbl'][i])
        if(len(str(str(data['uk12']['lbl'][i]))) > 7):
            uk12_data += "\t\t"
        else:
            uk12_data += "\t\t\t"
        uk12_data += str(data['uk12']['b']['pi'][i]) + "\t\t\t" +\
              str(data['uk12']['b']['lambda'][i]) + "\n"

    # Gera relatorio para grafo WG59
    wg59_data = \
        "\nGrafo WG59:\n" \
        "\n\ta) Sementes utilizadas: " + str(data['wg59']['a']['seeds'])+ "\n" \
        "\t\tVertice\t\t\tLabel\t\tPi\t\t\tLambda\n"
    for i in data['wg59']['grafo'].nodes():
        wg59_data += "\t\t\t" + str(i) + "\t\t" +\
              str(data['wg59']['lbl'][i])
        if(len(data['wg59']['lbl'][i]) >= 12):
            wg59_data += "\t"
        elif(len(data['wg59']['lbl'][i]) >= 8):
            wg59_data += "\t\t"
        elif(len(data['wg59']['lbl'][i]) >= 4):
            wg59_data += "\t\t\t"
        else:
            wg59_data += "\t\t\t\t"
        wg59_data += str(data['wg59']['a']['pi'][i]) + "\t\t\t" +\
              str(data['wg59']['a']['lambda'][i]) + "\n"

    wg59_data +="\n\tb) Sementes utilizadas: " + str(data['wg59']['b']['seeds'])+ "\n"\
        "\t\tVertice\t\t\tLabel\t\tPi\t\t\tLambda\n"
    for i in data['wg59']['grafo'].nodes():
        wg59_data += "\t\t\t" + str(i) + "\t\t" +\
              str(data['wg59']['lbl'][i])
        if(len(data['wg59']['lbl'][i]) >= 12):
            wg59_data += "\t"
        elif(len(data['wg59']['lbl'][i]) >= 8):
            wg59_data += "\t\t"
        elif(len(data['wg59']['lbl'][i]) >= 4):
            wg59_data += "\t\t\t"
        else:
            wg59_data += "\t\t\t\t"
        wg59_data += str(data['wg59']['b']['pi'][i]) + "\t\t\t" +\
              str(data['wg59']['b']['lambda'][i]) + "\n"

    # Gera relatorio para grafo USAir97
    usair97_data = \
        "\nGrafo USAir97:\n" \
        "\n\ta) Sementes utilizadas: " + str(data['usair97']['a']['seeds'])+ "\n" \
        "\t\tVertice\t\t\t\t\tLabel\t\t\t\tPi\t\t\tLambda\n"
    for i in data['usair97']['grafo'].nodes():
        usair97_data += "\t\t\t" + str(i) + "\t\t" +\
              str(data['usair97']['lbl'][i])
        if(len(data['usair97']['lbl'][i]) >= 12):
            usair97_data += "\t"
        else:
            usair97_data += "\t\t\t\t\t\t"
        usair97_data += str(data['usair97']['a']['pi'][i]) + "\t\t\t" +\
              str(data['usair97']['a']['lambda'][i]) + "\n"

    usair97_data +="\n\tb) Sementes utilizadas: " + str(data['usair97']['b']['seeds'])+ "\n"\
        "\t\tVertice\t\t\t\t\tLabel\t\t\t\tPi\t\t\tLambda\n"
    for i in data['usair97']['grafo'].nodes():
        usair97_data += "\t\t\t" + str(i) + "\t\t" +\
              str(data['usair97']['lbl'][i])
        if(len(data['usair97']['lbl'][i]) >= 12):
            usair97_data += "\t"
        else:
            usair97_data += "\t\t\t\t\t\t"
        usair97_data += str(data['usair97']['b']['pi'][i]) + "\t\t\t" +\
              str(data['usair97']['b']['lambda'][i]) + "\n"

    # Escreve todos os relatorio no arquivo '/generated-data/simulation-results.txt'
    try:
        f = open('../generated-data/simulation-results.txt', "w")
        f.write("Simulacao gerada em "+ str(datetime.datetime.today()) + "\n\n")
        f.write(uk12_data)
        f.write(wg59_data)
        f.write(usair97_data)
        f.close()
    except IOError:
        print "Erro na escrita do arquivo de simulacao"