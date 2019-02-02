import rrdtool


def graficaOIDget(PATHIMAGE,type,FILErrd):

    ret = rrdtool.graph(PATHIMAGE+type+".png",
                            "--start", '1537473600',
                            #                    "--end","N",
                            "--vertical-label=Bytes/s",
                            "DEF:inoctets="+FILErrd+":inoctets:AVERAGE",
                            "DEF:outoctets="+FILErrd+":outoctets:AVERAGE",
                            "AREA:inoctets#00FF00:In traffic",
                            "LINE1:outoctets#0000FF:Out traffic\r")
