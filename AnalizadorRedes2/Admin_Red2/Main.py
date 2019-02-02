
from Consultas import*
import os
from ConsultasOIDS  import *
from GraficarOIDS  import *
from lineaBase import *
from TrendGraph import *

""""" Contenido de la tabla

create table agente(
ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
HOSTNAME VARCHAR(30),
VERSION INT,
PUERTO INT,
COMUNIDAD VARCHAR(30),
FILEUDPrrd VARCHAR(200),
FILEUDPxml VARCHAR(200),
FILETCPrrd VARCHAR(200),
FILETCPxml VARCHAR(200),
FILESNMPrrd VARCHAR(200),
FILESNMPxml VARCHAR(200),
FILEIPrrd VARCHAR(200),
FILEIPxml VARCHAR(200),
FILEICMPrrd VARCHAR(200),
FILEICMPxml VARCHAR(200),
FILEline1rrd VARCHAR(200),
FILEline1xml VARCHAR(200),
FILEcpurrd VARCHAR(200),
FILEcpuxml VARCHAR(200),
FILEramrrd VARCHAR(200),
FILEramxml VARCHAR(200),
PATHIMAGE VARCHAR(200));
"""""

"""""

#Obtener IDS de los agentes guardados en la base de datos
agentesID=selectidsDB()
#Por cada agente obtener host, puerto, comunidad
for ID in range(len(agentesID)):
  hostame=selectColumDB("HOSTNAME", str(agentesID[ID]))
  puerto = selectColumDB("PUERTO", str(agentesID[ID]))
  comunidad = selectColumDB("COMUNIDAD", str(agentesID[ID]))
  agente=[hostame,puerto,comunidad]
  print(agente)
  print(SysDesc(agente))
  InterfaceDisponible=int(ifNumber(agente))
  interfaces = []
  nom_interfaces = []
  for i in range(1, int( InterfaceDisponible) + 1):
    stat_i = ifAdminStatus(i, agente)
    if stat_i == 1:
      stat_i = "up"
    if stat_i == 2:
      stat_i = "down"
    if stat_i == 3:
      stat_i = "testing"
    nom_i = nombre_interfaz(i, agente)
    interfaces.append(stat_i)
    nom_interfaces.append(str(nom_i))

  print(ver_System(agente))
  print(SysUpTime(agente))
  print(sysLocation(agente))
  print(sysContact(agente))
"""""


#Informacion general por agente
#def infoAgente():






#Por cada agente en la base de datos consulta los 5 objetos de la MIB, guarda los datos en sus respectivos rrd y xml

def startmonitoreo():
  agentesID = selectidsDB()
  for ID in range(len(agentesID)):
    comunidad=selectColumDB("COMUNIDAD", str(agentesID[ID]))
    hostname=selectColumDB("HOSTNAME", str(agentesID[ID]))

    getUDP(comunidad,hostname, selectColumDB("FILEUDPrrd", str(agentesID[ID])), selectColumDB("FILEUDPxml", str(agentesID[ID])))
    getTCP(comunidad,hostname, selectColumDB("FILETCPrrd", str(agentesID[ID])), selectColumDB("FILETCPxml", str(agentesID[ID])))
    getSNMP(comunidad,hostname, selectColumDB("FILESNMPrrd", str(agentesID[ID])),selectColumDB("FILESNMPxml", str(agentesID[ID])))
    getIP(comunidad,hostname, selectColumDB("FILEIPrrd", str(agentesID[ID])), selectColumDB("FILEIPxml", str(agentesID[ID])))
    getICMP(comunidad,hostname, selectColumDB("FILEICMPrrd", str(agentesID[ID])), selectColumDB("FILEICMPxml", str(agentesID[ID])))
    #Aqui se pone la nueva actulizacion practica2
    #linea de base
    filerrdline1=selectColumDB("FILEline1rrd", str(agentesID[ID]))
    lineaBase1(selectColumDB("COMUNIDAD", str(agentesID[ID])), selectColumDB("HOSTNAME", str(agentesID[ID])),filerrdline1, selectColumDB("FILEline1xml", str(agentesID[ID])))
    ultima_lectura = int(rrdtool.last(str(filerrdline1)))
    tiempo_final = ultima_lectura  # Obtiene el tiempo final en net3.rrd
    tiempo_inicial = tiempo_final - 3600  # Obtiene el inicial final en net3.rrd
    val_max = 5  # Valor maximo a monitorear
    linebase(tiempo_inicial, tiempo_final, val_max,selectColumDB("PATHIMAGE", str(agentesID[ID])),filerrdline1)
    #filerrdcpu=selectColumDB("FILEcpurrd", str(agentesID[ID]))
    
    
    
 














#obtiene las graficas del agente
def obtenerGraficas(agente):
  hostname="'"+agente+"'"
  IDagente=selectColumDBwhere("id", "HOSTNAME", hostname)

  PATHIMAGE=selectColumDB("PATHIMAGE",str(IDagente))

  FILETCPrrd=selectColumDB("FILETCPrrd",str(IDagente))
  graficaOIDget(PATHIMAGE, "TCP", FILETCPrrd)

  FILEUDPrrd = selectColumDB("FILEUDPrrd", IDagente)
  graficaOIDget(PATHIMAGE, "UDP", FILEUDPrrd)

  FILESNMPrrd = selectColumDB("FILESNMPrrd", IDagente)
  graficaOIDget(PATHIMAGE, "SNMP", FILESNMPrrd)

  FILEIPrrd = selectColumDB("FILEIPrrd", IDagente)
  graficaOIDget(PATHIMAGE, "IP", FILEIPrrd)

  FILEICMPrrd = selectColumDB("FILEICMPrrd", IDagente)
  graficaOIDget(PATHIMAGE, "ICMP", FILEICMPrrd)

#Registra en la base de datos un nuevo agente y crea los archivos RDD por cada OID
def registrarAgente(hostname,version,puerto,comunidad ):
  f1 = open('/etc/snmp/snmpd.conf', 'a')
  f1.write('\nrwcommunity' + '\t' + comunidad)
  f1.close()

  agentesID = selectidsDB()
  id=str(agentesID[len(agentesID)-1]+1)
  #id=str(1)
  os.mkdir(id)
  FILEUDPrrd = "./"+id+"/UDP.rrd"
  FILEUDPxml = "./"+id+"/UDP.xml"
  crearRDDTOOL(FILEUDPrrd)

  FILETCPrrd = "./"+id+"/TCP.rrd"
  FILETCPxml = "./"+id+"/TCP.xml"
  crearRDDTOOL(FILETCPrrd)

  FILESNMPrrd = "./"+id+"/SNMP.rrd"
  FILESNMPxml = "./"+id+"/SNMP.xml"
  crearRDDTOOL(FILESNMPrrd)

  FILEIPrrd = "./"+id+"/IP.rrd"
  FILEIPxml = "./"+id+"/IP.xml"
  crearRDDTOOL(FILEIPrrd)

  FILEICMPrrd = "./"+id+"/ICMP.rrd"
  FILEICMPxml = "./"+id+"/ICMP.xml"
  crearRDDTOOL(FILEICMPrrd)

  FILElinerrd = "./" + id + "/line1.rrd"
  FILElinexml = "./" + id + "/line1.xml"
  crearRDDTOOL(FILEICMPrrd)

  FILEcpurrd = "./" + id + "/cpuuso.rrd"
  FILEcpuxml = "./" + id + "/cpuuso.xml"
  crearRRDTOOLvaloruno(FILEcpurrd)  # Solo un dato de entrada

  FILEramrrd = "./" + id + "/ram.rrd"
  FILEramxml = "./" + id + "/ram.xml"
  crearRRDTOOLram(FILEramrrd)  # Solo un dato de entrada

  pathimage = "./"+id+"/image/"
  os.mkdir("./"+id+"/image/")
  insertDB(hostname, version, puerto, comunidad, FILEUDPrrd, FILEUDPxml, FILETCPrrd, FILETCPxml,FILElinexml, FILESNMPrrd,
           FILESNMPxml, FILEIPrrd, FILEIPxml, FILEICMPrrd,FILEICMPxml,FILElinerrd,FILElinexml,FILEcpurrd,FILEcpuxml,FILEramrrd,FILEramxml,pathimage)



def eliminarAgente(agente):
  hostname = "'" + agente + "'"
  IDagente = selectColumDBwhere("id", "HOSTNAME", hostname)
  deleterow(IDagente)



