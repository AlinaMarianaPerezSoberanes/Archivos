import time
import rrdtool
from getSNMP import consultaSNMP

total_input_traffic = 0
total_output_traffic = 0


while 1:
    total_input_traffic = int(
        consultaSNMP('ComunidadASR','localhost',
                     '1.3.6.1.2.1.25.3.3.1.2.196608'))           #Procesador
    valor = "N:" + str(total_input_traffic)
    print valor
    rrdtool.update('netPr.rrd', valor)
    rrdtool.dump('netPr.rrd','netPr.xml')
    time.sleep(1)

if ret:
    print rrdtool.error()
    time.sleep(300)
