#!/usr/bin/env python

import rrdtool
ret = rrdtool.create("Prueba.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:inoctets:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:2016",
            #RRA:HWPREDICT:rows:alpha:beta:seasonal period[:rra - num]
                     "RRA:HWPREDICT:1000:0.1:0.0035:288:3",
              #RRA:SEASONAL:seasonal period:gamma:rra-num
                     "RRA:SEASONAL:288:0.1:2",
              #RRA:DEVSEASONAL:seasonal period:gamma:rra-num
                     "RRA:DEVSEASONAL:288:0.1:2",
                #RRA:DEVPREDICT:rows:rra-num
                     "RRA:DEVPREDICT:1000:4",
            #RRA:FAILURES:rows:threshold:window length:rra-num
                     "RRA:FAILURES:288:7:9:4")

#HWPREDICT rra-num is the index of the SEASONAL RRA.
#SEASONAL rra-num is the index of the HWPREDICT RRA.
#DEVPREDICT rra-num is the index of the DEVSEASONAL RRA.
#DEVSEASONAL rra-num is the index of the HWPREDICT RRA.
#FAILURES rra-num is the index of the DEVSEASONAL RRA.

if ret:
    print rrdtool.error()

