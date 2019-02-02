import sys
import rrdtool
import time
#from Notify import *
start=1539657633
end=1539671533
umbral=90
if 1:
    ret = rrdtool.graphv( "trend.png",
                     "--start",str(start),
                     "--end",str(end),
                     "--vertical-label=Carga CPU",
                     "--title=Uso de CPU",
                     "--color", "ARROW#009900",
                     '--vertical-label', "Uso de CPU (%)",
                     '--lower-limit', '0',
                     '--upper-limit', '100',
                     "DEF:carga=trend.rrd:CPUload:AVERAGE",
                     "AREA:carga#00FF00:CPU load",
                     "LINE1:30",
                     "AREA:5#ff000022:stack",
                     "VDEF:CPUlast=carga,LAST",
                     "VDEF:CPUmin=carga,MINIMUM",
                     "VDEF:CPUavg=carga,AVERAGE",
                     "VDEF:CPUmax=carga,MAXIMUM",
                     "HRULE:"+str(umbral)+"#FF0000:Umbral 1", 

                     "COMMENT:               Now          Min             Avg             Max//n",
                     "GPRINT:CPUlast:%12.0lf%s",
                     "GPRINT:CPUmin:%10.0lf%s",
                     "GPRINT:CPUavg:%13.0lf%s",
                     "GPRINT:CPUmax:%13.0lf%s",
                     "VDEF:a=carga,LSLSLOPE",
                     "VDEF:b=carga,LSLINT",
                     'CDEF:avg2=carga,POP,a,COUNT,*,b,+',
                     'CDEF:resultado=avg2,'+str(umbral)+',GE,avg2,0,IF',
                     'VDEF:punto=resultado,MAXIMUM',
                     'COMMENT: Fecha de prediccion',
                     'GPRINT:punto:%c:strftime',
                     'PRINT:punto:%6.2lf %SUmbral',
                     "LINE2:avg2#FFBB00" )
    print(ret)
    print(ret.items()[22])
    max=str(ret.items()[22])
    print(ret.items()[3])
    min=str(ret.items()[3])
    linea=str(ret.items()[11])
    print(linea)
    #comparar si el valor maximo del cpu rebasa el val_def a monitorear
    if linea.find(str(umbral))>=0:                                           #Comparamos si sobre pasa el val_max
        print ("El valor sobrepasa",linea)
        #Envio de correo
        #send_alert_attached("Los valores del CPU sobreapasan al umbral "+str(umbral))
   
    time.sleep(15)
