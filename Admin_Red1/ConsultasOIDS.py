import rrdtool
from getSNMP import consultaSNMP

def getUDP(comunidad, IP,FILErrd,FILExml):

    total_input_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.2.2.1.11.1'))
    total_output_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.2.2.1.11.1'))
    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    rrdtool.update(FILErrd, valor)
    rrdtool.dump(FILErrd,FILExml)

    return




def getTCP(comunidad, IP,FILErrd,FILExml):


    total_input_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.6.10.0 '))
    total_output_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.6.11.0'))
    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    rrdtool.update(FILErrd, valor)
    rrdtool.dump(FILErrd,FILExml)

    return

def getSNMP(comunidad, IP,FILErrd,FILExml):

    total_input_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.11.1.0'))
    total_output_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.11.2.0'))
    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    rrdtool.update(FILErrd, valor)
    rrdtool.dump(FILErrd,FILExml)

    return


def getIP(comunidad, IP,FILErrd,FILExml):

    total_input_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.4.3.0'))
    total_output_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.4.10.0'))
    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    rrdtool.update(FILErrd, valor)
    rrdtool.dump(FILErrd,FILExml)

    return


def getICMP(comunidad, IP,FILErrd,FILExml):

    total_input_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.5.1.0'))
    total_output_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.5.14.0'))
    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    rrdtool.update(FILErrd, valor)
    rrdtool.dump(FILErrd,FILExml)

    return
