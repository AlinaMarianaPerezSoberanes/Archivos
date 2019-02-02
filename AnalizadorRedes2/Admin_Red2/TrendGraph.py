
import rrdtool



def trendgraphCPU(pathrrd,pathimage):
    pathimage=pathimage+'cpu.png'
    ret = rrdtool.graph(pathimage,
                     "--start",'1539734400',
                     "--vertical-label=Carga CPU",
                     "--title=Uso de CPU",
                     "--color", "ARROW#009900",
                     '--vertical-label', "Uso de CPU (%)",
                     '--lower-limit', '0',
                     '--upper-limit', '100',
                     "DEF:carga="+pathrrd+":CPUload:AVERAGE",
                     "AREA:carga#00FF00:CPU load",


                     "LINE1:30",
                     "AREA:5#ff000022:stack",
                     "VDEF:CPUlast=carga,LAST",
                     "VDEF:CPUmin=carga,MINIMUM",
                     "VDEF:CPUavg=carga,AVERAGE",
                     "VDEF:CPUmax=carga,MAXIMUM",

                     "COMMENT:               Now          Min             Avg             Max//n",
                     "GPRINT:CPUlast:%12.0lf%s",
                     "GPRINT:CPUmin:%10.0lf%s",
                     "GPRINT:CPUavg:%13.0lf%s",
                     "GPRINT:CPUmax:%13.0lf%s",
                     "VDEF:a=carga,LSLSLOPE",
                     "VDEF:b=carga,LSLINT",
                     'CDEF:avg2=carga,POP,a,COUNT,*,b,+',
                     "LINE2:avg2#FFBB00" )


def trendgraphRAM(pathrrd,pathimage):
    pathimage = pathimage + 'ram.png'
    ret = rrdtool.graph(pathimage,
                        "--start", '1539784800',
                        "--vertical-label=RAM",
                        "--title=Uso de RAM",
                        "--color", "ARROW#009900",
                        '--vertical-label', "Uso de la RAM (%)",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                        "DEF:carga="+pathrrd+":RAM:AVERAGE",
                        "AREA:carga#00FF00:RAM load",

                        "LINE1:30",
                        "AREA:5#ff000022:stack",
                        "VDEF:CPUlast=carga,LAST",
                        "VDEF:CPUmin=carga,MINIMUM",
                        "VDEF:CPUavg=carga,AVERAGE",
                        "VDEF:CPUmax=carga,MAXIMUM",

                        "COMMENT:               Now          Min             Avg             Max//n",
                        "GPRINT:CPUlast:%12.0lf%s",
                        "GPRINT:CPUmin:%10.0lf%s",
                        "GPRINT:CPUavg:%13.0lf%s",
                        "GPRINT:CPUmax:%13.0lf%s",
                        "VDEF:a=carga,LSLSLOPE",
                        "VDEF:b=carga,LSLINT",
                        'CDEF:avg2=carga,POP,a,COUNT,*,b,+',
                        "LINE2:avg2#FFBB00")

