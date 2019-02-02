import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 86400
tiempo_inicial = tiempo_final -25920000

while 1:
    ret = rrdtool.graph( "trafico1.png",
                     "--start",'1536942360',
 #                    "--end","N",
                     "--vertical-label=Bytes/s",
                     "DEF:inoctets=trafico1.rrd:inoctets:AVERAGE",
                     "DEF:outoctets=trafico1.rrd:outoctets:AVERAGE",
                     "AREA:inoctets#00FF00:In traffic",
                     "LINE1:outoctets#0000FF:Out traffic\r")

    time.sleep(10)
