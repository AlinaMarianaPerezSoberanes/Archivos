import sys
import rrdtool
import time
from Notify import *

#val_max=entradalb[0]   #Valor de procesamiento maximo del CPU
#val_desv=entradalb[1]  #Valor de la desviacion estandar
#val_def= entradalb[2]   #Valor a monitorear del CPU

def linebase(tiempo_inicial,tiempo_final,val_max,imagepath,pathrrd):
    #extrae la informacion del ultimo dato en net3.rrd
    #ultima_lectura = int(rrdtool.last("netPr.rrd"))
    val_max=100   #Valor de procesamiento maximo del CPU
    val_desv=5.70 #Valor de la desviacion estandar
    val_def= 60  #Valor a monitorear del CPU          
    imagepath=imagepath+"Libase.png"
    ret = rrdtool.graphv(imagepath,
                        "--start",str(tiempo_inicial),
                        "--end",str(tiempo_final),
                        "--vertical-label=Porcentraje uso CPU",
                        "--lower-limit", "0",                       #Valor menor a graficar
                        "--upper-limit", "100",                     #Valor maximo a graficar
                        "DEF:entrada="+str(pathrrd)+":cpu:AVERAGE",   #Promedio de inoctets
                        #"DEF:outoctets=net3.rrd:outoctets:AVERAGE", #Promedio de outoctets
                                   #Escalar valores a graficar de inoctets
                        "CDEF:entrada5=entrada,"+str(val_max)+",GT,0,entrada,IF", #Definimos el valor maximo
                        "VDEF:entradaMAX=entrada,MAXIMUM",          #Obtiene el val maximo de entrada
                        "VDEF:entradaMIN=entrada,MINIMUM",          #Obtiene el val minimo de entrada
                        "VDEF:entradaSTDEV=entrada,STDEV",          #Obtiene el val stdev de entrada
                        "VDEF:entradaLAST=entrada,LAST",            #Obtiene el val last de entrada
                        "AREA:entrada#00FF00:Uso de CPU",   #Etiqueta entrada
                        "HRULE:"+str(val_max)+"#FF0000:Umbral 1",                  #Etiqueta umbral
                        "HRULE:"+str(val_def)+"#0000FF:Umbral 2",
                        "HRULE:"+str(val_desv)+"#0000FF:Umbral 3",
                        "GPRINT:entradaMAX:%6.2lf %SMAX",           #Etiqueta val max
                        "GPRINT:entradaMIN:%6.2lf %SMIN",           #Etiqueta val min
                        "GPRINT:entradaSTDEV:%6.2lf %SSTDEV",       #Etiqueta stdev
                        "GPRINT:entradaLAST:%6.2lf %SLAST" )  
    lista=[]
    lista=list(ret.items())
    max=str(lista[16])
    min=str(lista[18])
    print(max , min)
    if max.find(str(val_def))>=0:                                           #Comparamos si sobre pasa el val_max
        print ("El valor sobrepasa",max)
        #Envio de correo
        send_alert_attached("Los valores del CPU sobreapasan al "+str(val_def)+ " con un valor de : "+max,imagepath)
    #Si el valor minimo es menor que la desviacion estandard
    if min.find(str(val_desv))>=0:
        print("El valor es minimo")
        send_alert_attached("Los valores del CPU son menores a "+str(val_desv)+ " con un valor de : "+min,imagepath)
