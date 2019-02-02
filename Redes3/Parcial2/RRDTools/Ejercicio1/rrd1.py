#!/usr/bin/env python

import rrdtool
ret = rrdtool.create("netPr.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:cpu:GAUGE:600:U:U", #Obtener el valor real
                     "RRA:AVERAGE:0.5:6:700",
                     "RRA:AVERAGE:0.5:1:600")

if ret:
    print rrdtool.error()

