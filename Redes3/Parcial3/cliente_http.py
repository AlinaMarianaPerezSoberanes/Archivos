import urllib.request
import time
from getSNMP import consultaSNMP
from timeit import default_timer as timer

import requests
from pip._vendor.distlib.compat import raw_input

def tiempo_respuesta(url):
    tiempo_inicial = timer()
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page = response.getheaders()
        status = int(response.status)
    tiempo_final = timer()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    if(status == 200):
        print("Metadatos de la pagina: " + str(the_page))
        print("\n\nEl tiempo de ejecucion fue: "+str(tiempo_ejecucion))
    else:
        print("Status del url: " + str(status))

def transferencia(url):
    r = requests.get(url)
    print("\n\nTransferencia de bytes: "+str(r.headers['Content-Length']))


def ancho_banda(host,comunidad,puerto):
    A_ifInOctects = consultaSNMP(comunidad,host,"1.3.6.1.2.1.31.1.1.1.6.1",puerto)
    A_ifOutOctecs = consultaSNMP(comunidad,host,"1.3.6.1.2.1.31.1.1.1.10.1",puerto)
    time.sleep(10)
    B_ifInOctects = consultaSNMP(comunidad,host,"1.3.6.1.2.1.31.1.1.1.6.1",puerto)
    B_ifOutOctecs = consultaSNMP(comunidad,host,"1.3.6.1.2.1.31.1.1.1.10.1",puerto)

    E_bps = int(B_ifInOctects) - int(A_ifInOctects)
    S_bps = int(B_ifOutOctecs) - int(A_ifOutOctecs)

    entrada_bps = (E_bps*8)/10
    salida_bps = (S_bps*8)/10

    print("\n\nAncho de banda entrada: "+str(entrada_bps)+" bps")
    print("Ancho de banda salida: " +str(salida_bps)+" bps")


def obtener_Cliente_HTTP(url,host,comunidad,puerto):
    print("CLIENTE_HTTP: "+str(url))
    print("\n-----------------------------------------------")
    tiempo_respuesta(url)
    transferencia(url)
    ancho_banda(host,comunidad,puerto)
    print("-----------------------------------------------")


    def main():

    url = "http://10.100.75.174"
    host = "10.100.65.104"
    comunidad = "comunidadSNMPady"
    puerto = "161"

    obtener_Cliente_HTTP(url,host,comunidad,puerto)


if __name__ == '__main__':
    main()
