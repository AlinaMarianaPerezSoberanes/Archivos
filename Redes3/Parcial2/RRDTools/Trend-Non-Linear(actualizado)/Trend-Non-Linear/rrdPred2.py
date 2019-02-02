import time
import rrdtool
from getSNMP import consultaSNMP
#from Notify import check_aberration
total_input_traffic = 0
total_output_traffic = 0

rrdpath="/home/alina/Documentos/Redes3/Parcial2/Trend-Non-Linear(actualizado)/Trend-Non-Linear/"
pngpath="/home/alina/Documentos/Redes3/Parcial2/Trend-Non-Linear(actualizado)/Trend-Non-Linear/"
fname="/RRD/netP.rrd"
pngfname="predict.png"
title="Deteccion de comportamiento anomalo"
# Generate charts for last 24 hours
endDate = rrdtool.last(fname) #ultimo valor del XML
begDate = endDate - 86000

while 1:
    total_input_traffic = int(consultaSNMP('ComunidadASR','localhost','1.3.6.1.2.1.2.2.1.10.1'))
    total_output_traffic = int(consultaSNMP('ComunidadASR','localhost','1.3.6.1.2.1.2.2.1.16.1'))

    valor = str(rrdtool.last(fname)+100)+":" + str(total_input_traffic) + ':' + str(total_output_traffic)
    print valor
    #ret = rrdtool.update(fname, valor)
    rrdtool.dump(fname,'Prueba.xml')
    time.sleep(1)
    #print check_aberration(rrdpath,fname)

if ret:
    print rrdtool.error()
    time.sleep(300)
