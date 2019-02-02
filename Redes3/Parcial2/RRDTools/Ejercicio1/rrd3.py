import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 86400
tiempo_inicial = tiempo_final -25920000

while 1:
    ret = rrdtool.graph( "net.png",
                     "--start",'1539964560',
 #                    "--end","N",
                     "--vertical-label=Bytes/s",
                     "DEF:inoctets=net3.rrd:inoctets:AVERAGE",
                     "AREA:inoctets#00FF00:use CPU"
                     )

    time.sleep(30)
