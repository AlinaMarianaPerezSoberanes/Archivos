#!/usr/bin/env python

import rrdtool
ret = rrdtool.create("netP.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:inoctets:COUNTER:600:U:U",
                     "DS:outoctets:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:2016",
                     "RRA:HWPREDICT:50:0.1:0.0035:10:3", #Predecir
                     #RRA:HWPREDICT:rows:alpha:beta:seasonal
                     "RRA:SEASONAL:10:0.1:2", #El 2 para HWPREDICT
                     #RRA:SEASONAL:seasonal period:gamma:rra-num[:smoothing-window=fraction]
                     #Para predecir fallas o errores
                     "RRA:DEVSEASONAL:10:0.1:2",
                     #RRA:DEVSEASONAL:seasonal period:gamma:rra-num[:smoothing-window=fraction]
                     "RRA:DEVPREDICT:50:4",
                     #RRA:DEVPREDICT:rows:rra-num
                     "RRA:FAILURES:50:7:9:4")
                     #RRA:FAILURES:rows:threshold:window length:rra-num guarda 1 si hay falla

if ret:
    print (rrdtool.error())

#LOS INDEX QUE NECESITAN PARA RELACIONARSE :#
#HWPREDICT rra-num is the index of the SEASONAL RRA.
#SEASONAL rra-num is the index of the HWPREDICT RRA.
#DEVPREDICT rra-num is the index of the DEVSEASONAL RRA.
#DEVSEASONAL rra-num is the index of the HWPREDICT RRA.
#FAILURES rra-num is the index of the DEVSEASONAL RRA

