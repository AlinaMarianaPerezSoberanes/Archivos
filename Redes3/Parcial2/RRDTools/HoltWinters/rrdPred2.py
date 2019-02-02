import time
import rrdtool
from getSNMP import consultaSNMP

total_input_traffic = 0
total_output_traffic = 0

#Se adquiere la informacon y se grafica
while 1:
    total_input_traffic = int(consultaSNMP('ComunidadASR','localhost','1.3.6.1.2.1.2.2.1.10.1'))
    total_output_traffic = int(consultaSNMP('ComunidadASR','localhost','1.3.6.1.2.1.2.2.1.16.1'))
    #Acelearar el tiepo del grafico
    valor = str(rrdtool.last("netP.rrd")+60 )+":" + str(total_input_traffic) + ':' + str(total_output_traffic)
    print ("Valor en P2",valor)
    ret = rrdtool.update('netP.rrd', valor)
    rrdtool.dump('netP.rrd','netP.xml')

    ret = rrdtool.graph("netP.png",
                        "--start", str(rrdtool.last('netP.rrd')-3600),
                        "--end",str(rrdtool.last('netP.rrd')),
                        "--vertical-label=Bytes/s",
                        "DEF:obs=netP.rrd:inoctets:AVERAGE",            #Predicion de in octets
                        "DEF:outoctets=netP.rrd:outoctets:AVERAGE",
                        "DEF:pred=netP.rrd:inoctets:HWPREDICT",
                        "DEF:dev=netP.rrd:inoctets:DEVPREDICT",
                        "DEF:fail=netP.rrd:inoctets:FAILURES",          #Archivo de fallas
                        "CDEF:scaledobs=obs,8,*",                       #Escalar octetos
                        "CDEF:upper=pred,dev,2,*,+",                    #Dev *2 + pred limite superior
                        "CDEF:lower=pred,dev,2,*,-",                    #Dev *2 - pred limite inferior
                        "CDEF:scaledupper=upper,8,*",                   #Escalar valores anteriores
                        "CDEF:scaledlower=lower,8,*",
                        "CDEF:scaledpred=pred,8,*",                     #Escalar la prediccion
                        "LINE1:scaledobs#00FF00:In traffic",
                        "LINE1:outoctets#0000FF:Out traffic",
                        "LINE1:scaledupper#F0F000:Upper Bound Average bits out",
                        "LINE1:scaledlower#FF0000:Lower Bound Average bits out",
                        "TICK:fail#00FFFF:1.0:- Fallas",                  #Graficar fallas
                        "LINE1:scaledpred#FF00FF:Prediccion")
    

    time.sleep(1)

if ret:
    print (rrdtool.error())
    
    time.sleep(300)
#Notificar las fallas con Notify en el archivo de fallas fail