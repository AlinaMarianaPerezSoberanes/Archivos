import time
import rrdtool
import tempfile
import os
from Notify import *


fname="netP.rrd"
rrdpath="/home/alina/Escritorio/Trend-Non-Linear/"
title="Deteccion de comportamiento anomalo, valor de Alpha 0.1"
endDate = rrdtool.last(fname) #ultimo valor del XML
print(endDate)
begDate = endDate - 83000
if 1:
    rrdtool.tune(fname,'--alpha','0.1')
    ret = rrdtool.graphv("netPalphaBajoFallas1.png",
                            '--start', str(begDate), '--end', str(endDate), '--title=' + title,
                            "--vertical-label=Bytes/s",
                            '--slope-mode',
                            "DEF:obs="       + rrdpath+fname + ":inoctets:AVERAGE",
                            #"DEF:outoctets=" + rrdpath+fname + ":outoctets:AVERAGE",
                            "DEF:pred="      + rrdpath+fname + ":inoctets:HWPREDICT",
                            "DEF:dev="       + rrdpath+fname + ":inoctets:DEVPREDICT",
                            "DEF:fail="      + rrdpath+fname + ":inoctets:FAILURES",

                        #"RRA:DEVSEASONAL:1d:0.1:2",
                        #"RRA:DEVPREDICT:5d:5",
                        #"RRA:FAILURES:1d:7:9:5""
                            "CDEF:scaledobs=obs,8,*",
                            "CDEF:upper=pred,dev,2,*,+",
                            "CDEF:lower=pred,dev,2,*,-",
                            "CDEF:scaledupper=upper,8,*",
                            "CDEF:scaledlower=lower,8,*",
                            "CDEF:scaledpred=pred,8,*",
                            "TICK:fail#FDD017:1.0:Fallas",
                            "LINE3:scaledobs#00FF00:In traffic",
                            "LINE1:scaledpred#FF00FF:Prediccion\\n",
                            #"LINE1:outoctets#0000FF:Out traffic",
                            "LINE1:scaledupper#ff0000:Upper Bound Average bits in\\n",
                            "LINE1:scaledlower#0000FF:Lower Bound Average bits in")
    flag=0 #Bandera para correo
    flag2=0                          
    #Deteccion de anomalias
    for i in range(begDate,endDate):
        ab_status = 0
        rrdfilename =fname
        info = rrdtool.info(rrdfilename)
        rrdstep = int(info['step'])
        #print(rrdstep)
        lastupdate = i#info['last_update']
        #print(lastupdate)
        previosupdate = str(begDate)#str(lastupdate - rrdstep - 1)
        graphtmpfile = tempfile.NamedTemporaryFile()
        values = rrdtool.graph(graphtmpfile.name+'F',
                            'DEF:f0=' + rrdfilename + ':inoctets:FAILURES:start=' + previosupdate + ':end=' + str(lastupdate),
                            'PRINT:f0:MIN:%1.0lf',
                            'PRINT:f0:MAX:%1.0lf',
                            'PRINT:f0:LAST:%1.0lf')
        fmin = int(values[2][0])
        fmax = int(values[2][1])
        flast = int(values[2][2])
        #print ("fmin="+str(fmin)+", fmax="+str(fmax)+",flast="+str(flast))  
        i+=300
        
        if(fmax!=fmin):
            if flast==1:
                if flag==0:
                    print("Envia Correo")
                    send_alert_attached("Falla detectada")
                    flag=1
                    flag2=0
                #print("Empieza Falla")
            if flast==0:
                flag=0
                if flag2==0:
                    print("CorreoTermina")
                    send_alert_attached("Falla terminada")
                    flag2=1
                #print("Termina falla")


    time.sleep(10)
