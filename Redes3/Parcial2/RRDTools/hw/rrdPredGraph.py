import time
import rrdtool

fname="netP.rrd"
title="Deteccion de comportamiento anomalo, valor de Alpha 0.1"
endDate = rrdtool.last(fname) #ultimo valor del XML
begDate = endDate - 86000

rrdtool.tune(fname,'--alpha','0.1') #tune permite cambiar el valor de alfa
if 1:
    ret = rrdtool.graphv("netPalphaBajoFallas.png",
                            '--start', str(begDate), '--end', str(endDate), '--title=' + title,
                            "--vertical-label=Bytes/s",
                            '--slope-mode',
                            "DEF:obs="       + fname + ":inoctets:AVERAGE",
                            "DEF:outoctets=" + fname + ":outoctets:AVERAGE",
                            "DEF:pred="      + fname + ":inoctets:HWPREDICT",
                            "DEF:dev="       + fname + ":inoctets:DEVPREDICT",
                            "DEF:fail="      + fname + ":inoctets:FAILURES", #coleccion de fallas rrd failures

                        #"RRA:DEVSEASONAL:1d:0.1:2",
                        #"RRA:DEVPREDICT:5d:5",
                        #"RRA:FAILURES:1d:7:9:5""
                            "CDEF:scaledobs=obs,8,*",
                            "CDEF:upper=pred,dev,2,*,+",
                            "CDEF:lower=pred,dev,2,*,-",
                            "CDEF:scaledupper=upper,8,*",
                            "CDEF:scaledlower=lower,8,*",
                            "CDEF:scaledpred=pred,8,*",
                            "TICK:fail# #FF0000:1.0:Fallas", #Linea vertical amarilla de fallas en grafica
                            "LINE3:scaledobs#00FF00:In traffic",
                            "LINE1:scaledpred#FF00FF:Prediccion\\n",
                            #"LINE1:outoctets#0000FF:Out traffic",
                            "LINE1:scaledupper#ff0000:Upper Bound Average bits in\\n",
                            "LINE1:scaledlower#0000FF:Lower Bound Average bits in")
    print(ret.items())
    #time.sleep(30)