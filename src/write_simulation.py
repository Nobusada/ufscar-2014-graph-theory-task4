__author__ = 'Thales'
import datetime

def write_simulation(data):
    # Gera relatorio para grafo UK12
    uk12_data = \
        "Grafo UK12:\n" \
        "\n\ta) Sementes utilizadas: " + str(data['uk12']['a']['seeds'])+ "\n" \
        "\t\tLambda:\n"
    for v, w in data['uk12']['a']['lambda'].items():
        uk12_data += "\t\t\t" + str(v) + "\t\t" + str(data['uk12']['lbl'][v])
        if (len(data['uk12']['lbl'][v]) >= 8):
            uk12_data += "\t\t" + str(w) + "\n"
        else:
            uk12_data += "\t\t\t" + str(w) + "\n"
    uk12_data += "\t\tPi:\n"
    for v, w in data['uk12']['a']['pi'].items():
        uk12_data += "\t\t\t" + str(v) + "\t\t" + str(data['uk12']['lbl'][v])
        if (len(data['uk12']['lbl'][v]) >= 8):
            uk12_data += "\t\t" + str(w) + "\n"
        else:
            uk12_data += "\t\t\t" + str(w) + "\n"
    uk12_data +="\n\tb) Sementes utilizadas: " + str(data['uk12']['b']['seeds'])+ "\n"\
        "\t\tLambda:\n"
    for v, w in data['uk12']['b']['lambda'].items():
        uk12_data += "\t\t\t" + str(v) + "\t\t" + str(data['uk12']['lbl'][v])
        if (len(data['uk12']['lbl'][v]) >= 8):
            uk12_data += "\t\t" + str(w) + "\n"
        else:
            uk12_data += "\t\t\t" + str(w) + "\n"
    uk12_data += "\t\tPi:\n"
    for v, w in data['uk12']['b']['pi'].items():
        uk12_data += "\t\t\t" + str(v) + "\t\t" + str(data['uk12']['lbl'][v])
        if (len(data['uk12']['lbl'][v]) >= 8):
            uk12_data += "\t\t" + str(w) + "\n"
        else:
            uk12_data += "\t\t\t" + str(w) + "\n"

    # Gera relatorio para grafo WG59
    wg59_data = \
        "\nGrafo WG59:\n" \
        "\n\ta) Sementes utilizadas: " + str(data['wg59']['a']['seeds'])+ "\n" \
        "\t\tLambda:\n"
    for v, w in data['wg59']['a']['lambda'].items():
        wg59_data += "\t\t\t" + str(v) + "\t\t" + str(data['wg59']['lbl'][v])
        if (len(data['wg59']['lbl'][v]) >= 12):
            wg59_data += "\t" + str(w) + "\n"
        elif (len(data['wg59']['lbl'][v]) >= 8):
            wg59_data += "\t\t" + str(w) + "\n"
        elif (len(data['wg59']['lbl'][v]) >= 4):
            wg59_data += "\t\t\t" + str(w) + "\n"
        else:
            wg59_data += "\t\t\t\t" + str(w) + "\n"
    wg59_data += "\t\tPi:\n"
    for v, w in data['wg59']['a']['pi'].items():
        wg59_data += "\t\t\t" + str(v) + "\t\t" + str(data['wg59']['lbl'][v])
        if (len(data['wg59']['lbl'][v]) >= 12):
            wg59_data += "\t" + str(w) + "\n"
        elif (len(data['wg59']['lbl'][v]) >= 8):
            wg59_data += "\t\t" + str(w) + "\n"
        elif (len(data['wg59']['lbl'][v]) >= 4):
            wg59_data += "\t\t\t" + str(w) + "\n"
        else:
            wg59_data += "\t\t\t\t" + str(w) + "\n"
    wg59_data +="\n\tb) Sementes utilizadas: " + str(data['wg59']['b']['seeds'])+ "\n"\
        "\t\tLambda:\n"
    for v, w in data['wg59']['b']['lambda'].items():
        wg59_data += "\t\t\t" + str(v) + "\t\t" + str(data['wg59']['lbl'][v])
        if (len(data['wg59']['lbl'][v]) >= 12):
            wg59_data += "\t" + str(w) + "\n"
        elif (len(data['wg59']['lbl'][v]) >= 8):
            wg59_data += "\t\t" + str(w) + "\n"
        elif (len(data['wg59']['lbl'][v]) >= 4):
            wg59_data += "\t\t\t" + str(w) + "\n"
        else:
            wg59_data += "\t\t\t\t" + str(w) + "\n"
    wg59_data += "\t\tPi:\n"
    for v, w in data['wg59']['b']['pi'].items():
        wg59_data += "\t\t\t" + str(v) + "\t\t" + str(data['wg59']['lbl'][v])
        if (len(data['wg59']['lbl'][v]) >= 12):
            wg59_data += "\t" + str(w) + "\n"
        elif (len(data['wg59']['lbl'][v]) >= 8):
            wg59_data += "\t\t" + str(w) + "\n"
        elif (len(data['wg59']['lbl'][v]) >= 4):
            wg59_data += "\t\t\t" + str(w) + "\n"
        else:
            wg59_data += "\t\t\t\t" + str(w) + "\n"

# Gera relatorio para grafo USAir97
    usair97_data = \
        "\nGrafo USAir97:\n" \
        "\n\ta) Sementes utilizadas: " + str(data['usair97']['a']['seeds'])+ "\n" \
        "\t\tLambda:\n"
    for v, w in data['usair97']['a']['lambda'].items():
        usair97_data += "\t\t\t" + str(v) + "\t\t" + str(data['usair97']['lbl'][v])
        if (len(data['usair97']['lbl'][v]) >= 12):
            usair97_data += "\t" + str(w) + "\n"
        elif (len(data['usair97']['lbl'][v]) >= 8):
            usair97_data += "\t\t" + str(w) + "\n"
        elif (len(data['usair97']['lbl'][v]) >= 4):
            usair97_data += "\t\t\t" + str(w) + "\n"
        else:
            usair97_data += "\t\t\t\t" + str(w) + "\n"
    usair97_data += "\t\tPi:\n"
    for v, w in data['usair97']['a']['pi'].items():
        usair97_data += "\t\t\t" + str(v) + "\t\t" + str(data['usair97']['lbl'][v])
        if (len(data['usair97']['lbl'][v]) >= 12):
            usair97_data += "\t" + str(w) + "\n"
        elif (len(data['usair97']['lbl'][v]) >= 8):
            usair97_data += "\t\t" + str(w) + "\n"
        elif (len(data['usair97']['lbl'][v]) >= 4):
            usair97_data += "\t\t\t" + str(w) + "\n"
        else:
            usair97_data += "\t\t\t\t" + str(w) + "\n"
    usair97_data +="\n\tb) Sementes utilizadas: " + str(data['usair97']['b']['seeds'])+ "\n"\
        "\t\tLambda:\n"
    for v, w in data['usair97']['b']['lambda'].items():
        usair97_data += "\t\t\t" + str(v) + "\t\t" + str(data['usair97']['lbl'][v])
        if (len(data['usair97']['lbl'][v]) >= 12):
            usair97_data += "\t" + str(w) + "\n"
        elif (len(data['usair97']['lbl'][v]) >= 8):
            usair97_data += "\t\t" + str(w) + "\n"
        elif (len(data['usair97']['lbl'][v]) >= 4):
            usair97_data += "\t\t\t" + str(w) + "\n"
        else:
            usair97_data += "\t\t\t\t" + str(w) + "\n"
    usair97_data += "\t\tPi:\n"
    for v, w in data['usair97']['b']['pi'].items():
        usair97_data += "\t\t\t" + str(v) + "\t\t" + str(data['usair97']['lbl'][v])
        if (len(data['usair97']['lbl'][v]) >= 12):
            usair97_data += "\t" + str(w) + "\n"
        elif (len(data['usair97']['lbl'][v]) >= 8):
            usair97_data += "\t\t" + str(w) + "\n"
        elif (len(data['usair97']['lbl'][v]) >= 4):
            usair97_data += "\t\t\t" + str(w) + "\n"
        else:
            usair97_data += "\t\t\t\t" + str(w) + "\n"

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