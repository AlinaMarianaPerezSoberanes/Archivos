import rrdtool
from getSNMP import consultaSNMP

def getUDP(comunidad, IP,FILErrd,FILExml):

    total_input_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.7.1.0'))
    total_output_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.7.4.0'))
    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    rrdtool.update(str(FILErrd), valor)
    rrdtool.dump(str(FILErrd),str(FILExml))

    return




def getTCP(comunidad, IP,FILErrd,FILExml):


    total_input_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.6.10.0 '))
    total_output_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.6.11.0'))
    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    rrdtool.update(str(FILErrd), valor)
    rrdtool.dump(str(FILErrd),str(FILExml))

    return

def getSNMP(comunidad, IP,FILErrd,FILExml):

    total_input_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.11.1.0'))
    total_output_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.11.2.0'))
    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    rrdtool.update(str(FILErrd), valor)
    rrdtool.dump(str(FILErrd),str(FILExml))

    return


def getIP(comunidad, IP,FILErrd,FILExml):

    total_input_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.4.3.0'))
    total_output_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.4.10.0'))
    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    rrdtool.update(str(FILErrd), valor)
    rrdtool.dump(str(FILErrd),str(FILExml))

    return


def getICMP(comunidad, IP,FILErrd,FILExml):

    total_input_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.5.1.0'))
    total_output_traffic = int(
        consultaSNMP(comunidad,IP, '1.3.6.1.2.1.5.14.0'))
    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    rrdtool.update(str(FILErrd), valor)
    rrdtool.dump(str(FILErrd),str(FILExml))

    return

#Nuevas funciones de practica2######

def lineaBase1(comunidad,IP,FILErrd,FILExml):
    total_input_traffic = 0
    total_output_traffic = 0
    total_input_traffic = int(
        consultaSNMP(comunidad,IP,
                     '1.3.6.1.2.1.25.3.3.1.2.196608'))           #Procesador

    valor = "N:" + str(total_input_traffic)
    #print(valor)
    rrdtool.update(str(FILErrd), valor)
    rrdtool.dump(str(FILErrd),str(FILExml))

#uso de procesador
def usocpu(comunidad,IP,FILErrd,FILExml):
    carga_CPU = int(
        consultaSNMP(comunidad,IP,
                     '1.3.6.1.2.1.25.3.3.1.2.196608'))

    valor = "N:" + str(carga_CPU)
    #print (valor)
    rrdtool.update(str(FILErrd), valor)
    rrdtool.dump(str(FILErrd),str(FILExml))

#uso de ram
def usoRAM(comunidad,IP,FILErrd,FILExml):
    ram = int(
        consultaSNMP(comunidad,IP,
                     '1.3.6.1.2.1.25.2.3.1.6.1'))

    valor = "N:" + str(ram)
    #print (valor)
    rrdtool.update(str(FILErrd), valor)
    rrdtool.dump(str(FILErrd),str(FILExml))







