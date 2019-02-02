import sys
import rrdtool
import time
from Notify import *

#extrae la informacion del ultimo dato en net3.rrd
ultima_lectura = int(rrdtool.last("net3.rrd"))
tiempo_final = ultima_lectura                                       #Obtiene el tiempo final en net3.rrd
tiempo_inicial = tiempo_final - 3600                                #Obtiene el inicial final en net3.rrd
val_max=80                                                           #Valor maximo a monitorear

while 1:

    ret = rrdtool.graphv( "Lbase.png",
                        "--start",str(tiempo_inicial),
                        "--end",str(tiempo_final),
                        "--vertical-label=Bytes/s",
                        "--lower-limit", "0",                       #Valor menor a graficar
                        "--upper-limit", "100",                     #Valor maximo a graficar
                        "DEF:inoctets=net3.rrd:inoctets:AVERAGE",   #Promedio de inoctets
                        "DEF:outoctets=net3.rrd:outoctets:AVERAGE", #Promedio de outoctets
                        "CDEF:entrada=inoctets,0.008,*",            #Escalar valores a graficar de inoctets
                        "CDEF:salida=outoctets,0.008,*",            #Escalar valores a graficar de inoctets
                        "CDEF:entrada5=entrada,"+str(val_max)+",GT,0,entrada,IF", #Definimos el valor maximo
                        "VDEF:entradaMAX=entrada,MAXIMUM",          #Obtiene el val maximo de entrada
                        "VDEF:entradaMIN=entrada,MINIMUM",          #Obtiene el val minimo de entrada
                        "VDEF:entradaSTDEV=entrada,STDEV",          #Obtiene el val stdev de entrada
                        "VDEF:entradaLAST=entrada,LAST",            #Obtiene el val last de entrada
                        "AREA:entrada#00FF00:Trafico de entrada",   #Etiqueta entrada
                        "AREA:entrada5#FF9F00:Trafico de entrada menor que"+str(val_max),#Etiqueta val menor
                        "LINE2:salida#0000FF:Trafico de salida",    #Etiqueta salida
                        "HRULE:5#FF0000:Umbral 1",                  #Etiqueta umbral
                        "GPRINT:entradaMAX:%6.2lf %SMAX",           #Etiqueta val max
                        "GPRINT:entradaMIN:%6.2lf %SMIN",           #Etiqueta val min
                        "GPRINT:entradaSTDEV:%6.2lf %SSTDEV",       #Etiqueta stdev
                        "GPRINT:entradaLAST:%6.2lf %SLAST" )        #Etiqueta last
    
    #print(ret.keys())
    #print(ret.items())
    min=ret.items()[4]                                              #Obtenemos el valor del MIN en ret
    max=str(ret.items()[10])                                        #Obtenemos el valor del MAX en ret
    print(max)
    
    if max.find("4.")>=0:                                           #Comparamos si sobre pasa el val_max
        #print ("Si hay",max)
        send_alert_attached("Valor Maximo superior a 4")            #Envio de correo
    time.sleep(50)